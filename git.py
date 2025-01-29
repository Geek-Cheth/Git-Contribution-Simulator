import os
import random
from datetime import datetime
import sys

def get_user_input(prompt: str, input_type: type):
    """Get and validate user input."""
    while True:
        try:
            value = input(prompt)
            return input_type(value)
        except ValueError:
            print(f"Please enter a valid {input_type.__name__}.")
            continue

def create_commit(file_path: str, date_str: str, commit_num: int) -> bool:
    """Create a single commit with the specified date."""
    try:
        # Add new content to file
        with open(file_path, 'a') as file:
            file.write(f'Commit for {date_str}\n')
        
        # Stage and commit changes
        os.system('git add test.txt')
        commit_msg = f'feat: automated commit #{commit_num}'
        result = os.system(f'git commit --date="{date_str}" -m "{commit_msg}"')
        
        return result == 0
    except Exception as e:
        print(f"Error creating commit: {e}")
        return False

def main():
    """Main function to handle the Git contribution simulation."""
    # Configuration
    FILE_PATH = 'test.txt'
    CURRENT_YEAR = datetime.now().year

    # Get user input
    print("\n=== Git Contribution Simulator ===")
    num_commits = get_user_input("Enter the number of commits to create: ", int)
    year = get_user_input(f"Enter the year for the commits (1970-{CURRENT_YEAR}): ", int)

    # Validate year
    if not (1970 <= year <= CURRENT_YEAR):
        print(f"Please enter a year between 1970 and {CURRENT_YEAR}")
        return

    # Initialize repository if needed
    if not os.path.exists('.git'):
        print("Initializing Git repository...")
        os.system('git init')

    # Create initial commit if file doesn't exist
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'w') as file:
            file.write('# Git Contribution Simulator\n')
        os.system('git add test.txt')
        os.system('git commit -m "init: initial commit"')

    # Create commits
    print(f"\nCreating {num_commits} commits for {year}...")
    successful_commits = 0

    for i in range(num_commits):
        # Generate random date components
        month = random.randint(1, 12)
        day = random.randint(1, 28)  # Using 28 to avoid invalid dates
        hour = random.randint(9, 17)  # Business hours
        minute = random.randint(0, 59)
        
        # Create timestamp
        date_str = f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:00"
        
        # Create commit
        if create_commit(FILE_PATH, date_str, i + 1):
            successful_commits += 1
            sys.stdout.write(f"\rProgress: {successful_commits}/{num_commits} commits created")
            sys.stdout.flush()

    print("\n\nAttempting to push commits...")
    try:
        push_result = os.system('git push -u origin main')
        if push_result == 0:
            print("Successfully pushed all commits!")
        else:
            print("Push failed. You may need to push manually or check your remote configuration.")
    except Exception as e:
        print(f"Error during push: {e}")

    print(f"\nCompleted! Successfully created {successful_commits} commits.")

if __name__ == "__main__":
    main()
