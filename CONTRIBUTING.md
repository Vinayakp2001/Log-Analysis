# Contributing to LogGuard

Thank you for your interest in contributing to LogGuard! We welcome contributions from everyone.

## Getting Started

### 1. Fork and Clone
```bash
# Fork the repository on GitHub, then:
git clone https://github.com/YOUR_USERNAME/Log-Analysis.git
cd Log-Analysis
```

### 2. Set Up Development Environment
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Test the setup
cd src
python generate_logs.py
python log_ingestor.py  # In one terminal
python app.py          # In another terminal
```

### 3. Create a Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

## Types of Contributions

### 🐛 Bug Fixes
- Check existing issues first
- Create a bug report if none exists
- Write a test that reproduces the bug
- Fix the bug and ensure tests pass

### ✨ New Features
- Check the [roadmap](README.md#community-roadmap---help-us-decide) first
- Start a discussion for major features
- Implement the feature with tests
- Update documentation

### 📚 Documentation
- Fix typos and improve clarity
- Add examples and use cases
- Translate to other languages
- Create tutorials and guides

### 🧪 Testing
- Add unit tests for existing code
- Test LogGuard in different environments
- Report compatibility issues
- Improve test coverage

## Development Guidelines

### Code Style
- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings for public functions
- Keep functions small and focused

### Testing
- Write tests for new features
- Ensure existing tests still pass
- Test edge cases and error conditions
- Include integration tests where appropriate

### Commits
- Use clear, descriptive commit messages
- Keep commits focused on a single change
- Reference issue numbers when applicable

Example commit messages:
```
Add geolocation detection for IP addresses (#123)
Fix ML model training memory leak
Update README with Docker setup instructions
```

## Pull Request Process

### 1. Before Submitting
- [ ] Code follows the style guidelines
- [ ] Tests are added and passing
- [ ] Documentation is updated
- [ ] No merge conflicts with main branch

### 2. Submit Pull Request
- Use a clear title and description
- Reference related issues
- Explain what changes were made and why
- Include screenshots for UI changes

### 3. Review Process
- Maintainers will review your PR
- Address any feedback or requested changes
- Once approved, your PR will be merged

## Issue Guidelines

### Bug Reports
Use the bug report template and include:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Environment information
- Log files and error messages

### Feature Requests
Use the feature request template and include:
- Clear description of the feature
- Use case and problem it solves
- Implementation ideas (if any)
- Willingness to help implement

### Questions
Use the question template for:
- Setup and configuration help
- Usage questions
- Clarification on features

## Community Guidelines

### Be Respectful
- Use welcoming and inclusive language
- Respect different viewpoints and experiences
- Accept constructive criticism gracefully
- Focus on what's best for the community

### Be Helpful
- Help newcomers get started
- Share your knowledge and experience
- Provide constructive feedback
- Celebrate others' contributions

## Getting Help

### Stuck on Something?
- Check existing issues and discussions
- Ask questions in GitHub Discussions
- Create a question issue with details
- Join community discussions

### Want to Contribute but Don't Know How?
- Look for issues labeled "good first issue"
- Check the roadmap for interesting features
- Improve documentation and examples
- Test LogGuard in your environment and report feedback

## Recognition

Contributors will be recognized in:
- README acknowledgments
- Release notes
- Community showcases
- Contributor hall of fame (coming soon)

## Development Roadmap

See our [community roadmap](README.md#community-roadmap---help-us-decide) for planned features and vote on priorities.

## Questions?

Feel free to ask questions in:
- [GitHub Discussions](https://github.com/Vinayakp2001/Log-Analysis/discussions)
- [GitHub Issues](https://github.com/Vinayakp2001/Log-Analysis/issues) (use the question template)

Thank you for contributing to LogGuard! 🎉