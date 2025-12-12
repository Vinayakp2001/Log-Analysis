import datetime
import random

def generate_apache_log_entry():
    ip_address = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
    timestamp = datetime.datetime.now().strftime("[%d/%b/%Y:%H:%M:%S +0000]")
    method = random.choice(["GET", "POST", "PUT", "DELETE"])
    path = random.choice(["/index.html", "/about.html", "/products/view/1", "/api/user", "/admin/dashboard"])
    protocol = "HTTP/1.1"
    status_code = random.choice([200, 200, 200, 200, 404, 500, 301])
    content_size = random.randint(100, 5000)
    referrer = random.choice(["-", "http://example.com/", "http://google.com/"])
    user_agent = random.choice([
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    ])
    return f'{ip_address} - - {timestamp} "{method} {path} {protocol}" {status_code} {content_size} "{referrer}" "{user_agent}"'

def generate_logs(filename="access.log", num_entries=100):
    with open(filename, "w") as f:
        for _ in range(num_entries):
            f.write(generate_apache_log_entry() + "\n")
    print(f"Generated {num_entries} log entries in {filename}")

if __name__ == "__main__":
    generate_logs()
