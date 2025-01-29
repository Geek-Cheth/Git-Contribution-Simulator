# Git Contribution Simulator 🎯

An educational Python tool that simulates Git commit history by creating timestamped commits across specified timeframes. Demonstrates Git's timestamp handling and repository history manipulation through automated commit generation.

## ✨ Features

- Interactive CLI with progress visualization
- Customizable number of commits and target year
- Random distribution of commits during business hours
- Automated Git operations
- Cross-platform compatibility

## 🔧 Prerequisites

- Python 3.x
- Git installed and configured
- GitHub account with SSH or token authentication
- pip (Python package manager)

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/geek-cheth/git-contribution-simulator
cd git-contribution-simulator
```

2. Install required packages:
```bash
pip install rich
```

3. Ensure Git is configured:
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## 🚀 Usage

1. Run the script:
```bash
python git.py
```

2. Follow the interactive prompts:
   - Enter the number of commits you want to create
   - Specify the target year for the commits

3. The script will:
   - Create a working directory (`git_simulator_work`)
   - Initialize a Git repository
   - Generate commits with random timestamps
   - Display progress with a visual interface
   - Attempt to push changes to your remote repository

## 📝 Important Notes

- The script creates a new directory called `git_simulator_work` to keep operations isolated
- Commits are distributed randomly across business hours (9 AM - 5 PM)
- Ensure you have proper Git authentication set up for pushing changes
- The tool works on Windows, Linux, and macOS

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## 📜 License

This project is released under the MIT License.

## ⚠️ Disclaimer

This tool is for educational purposes only. Use it responsibly and in accordance with your organization's guidelines.
