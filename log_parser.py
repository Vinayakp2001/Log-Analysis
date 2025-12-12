import re
import datetime

APACHE_LOG_PATTERN = re.compile(r'''
    (?P<ip_address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})
    \s-\s-\s
    \[(?P<timestamp>\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}\s[+\-]\d{4})\]
    \s
    \"(?P<method>[A-Z]+)\s(?P<path>.*?)\s(?P<protocol>HTTP/\d\.\d)\"
    \s(?P<status_code>\d{3})
    \s(?P<content_size>\d+|-)
    \s\"(?P<referrer>.*?)\"
    \s\"(?P<user_agent>.*?)\"
''', re.VERBOSE)

def parse_apache_log_entry(log_entry):
    match = APACHE_LOG_PATTERN.match(log_entry)
    if match:
        return match.groupdict()
    return None

def normalize_log_data(parsed_data):
    if not parsed_data: # Ensure parsed_data is not None
        return None

    normalized_data = parsed_data.copy()

    # 1. Standardize timestamps
    # Example: "10/Jun/2024:14:30:05 +0000" to ISO 8601
    try:
        # Remove the brackets first
        ts_str = normalized_data['timestamp'].replace('[', '').replace(']', '')
        # Parse the string with its current format
        dt_object = datetime.datetime.strptime(ts_str, "%d/%b/%Y:%H:%M:%S %z")
        # Convert to ISO 8601
        normalized_data['timestamp'] = dt_object.isoformat()
    except (ValueError, KeyError):
        normalized_data['timestamp'] = None # Or keep original if parsing fails

    # 2. Categorize event types
    status_code = int(normalized_data['status_code']) if normalized_data['status_code'] != '-' else 0
    if 200 <= status_code < 300:
        normalized_data['event_type'] = "successful_request"
    elif 300 <= status_code < 400:
        normalized_data['event_type'] = "redirection"
    elif 400 <= status_code < 500:
        normalized_data['event_type'] = "client_error"
    elif 500 <= status_code < 600:
        normalized_data['event_type'] = "server_error"
    else:
        normalized_data['event_type'] = "other"

    # Convert content_size and status_code to appropriate types
    normalized_data['status_code'] = status_code
    normalized_data['content_size'] = int(normalized_data['content_size']) if normalized_data['content_size'] != '-' else 0
    
    return normalized_data

if __name__ == "__main__":
    # Example log entry from generate_logs.py
    sample_log_entry = '192.168.1.100 - - [10/Jun/2024:14:30:05 +0000] "GET /index.html HTTP/1.1" 200 1234 "http://example.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"'
    
    parsed_data = parse_apache_log_entry(sample_log_entry)
    if parsed_data:
        print("Successfully parsed log entry:")
        for key, value in parsed_data.items():
            print(f"  {key}: {value}")
    else:
        print("Failed to parse log entry.")

    # Test with a generated log entry from our access.log
    try:
        with open("access.log", "r") as f:
            first_log_from_file = f.readline().strip()
            print(f"\nAttempting to parse and normalize log from file: {first_log_from_file[:70]}...")
            parsed_data_from_file = parse_apache_log_entry(first_log_from_file)
            if parsed_data_from_file:
                normalized_data_from_file = normalize_log_data(parsed_data_from_file)
                if normalized_data_from_file:
                    print("Successfully parsed and normalized log entry from file:")
                    for key, value in normalized_data_from_file.items():
                        print(f"  {key}: {value}")
                else:
                    print("Failed to normalize log entry from file.")
            else:
                print("Failed to parse log entry from file.")
    except FileNotFoundError:
        print("Error: access.log not found. Please run generate_logs.py first.")
