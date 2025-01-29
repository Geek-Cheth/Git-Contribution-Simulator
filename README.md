# Git Contribution Simulator

A Python-based educational tool that demonstrates Git history manipulation by creating timestamped commits across a specified timeframe. This project helps developers understand how Git handles commit timestamps and repository history.

## ⚠️ Educational Purpose

This tool is designed for educational purposes to understand:
- How Git handles commit timestamps
- The mechanics of repository history
- Git's commit dating system
- Basic Git operations using Python

## 🚀 Features

- Create multiple commits with custom timestamps
- Specify target year for commits
- Random distribution of commits across months
- Automated commit message generation
- Simple Python implementation

## 📋 Prerequisites

- Python 3.x
- Git installed and configured
- Active GitHub account
- Local Git configuration with GitHub authentication

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/geek-cheth/git-contribution-simulator
cd git-contribution-simulator

# Ensure you have Git configured
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## 💻 Usage

1. Run the Python script:
```bash
python3 git.py
```

2. When prompted:
   - Enter the number of commits you want to create
   - Specify the target year for the commits

3. The script will:
   - Create a test file
   - Generate the specified number of commits
   - Distribute commits randomly across the chosen year
   - Push changes to your repository

## ⚙️ How It Works

The script operates by:
1. Creating a simple text file to track changes
2. Generating commits with randomized timestamps
3. Using Git's `--date` parameter to set specific commit dates
4. Automating the commit and push process

## 📝 Note

Remember that manipulating repository history should be done responsibly and in accordance with your organization's guidelines. This tool is meant for learning and understanding Git's functionality.

## 🤝 Contributing

Contributions to improve the educational value of this tool are welcome. Please feel free to:
- Submit issues
- Propose new features
- Create pull requests

## 📜 License

This project is released under the MIT License.
