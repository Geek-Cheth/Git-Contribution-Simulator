import os
import random
from datetime import datetime
import sys
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
from rich.panel import Panel
from rich.text import Text
from rich import print as rprint

console = Console()

def ensure_directory():
    """Ensure we're in a valid directory and create it if necessary."""
    # Get the current script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Change to the script's directory
    os.chdir(script_dir)
    
    # Create a work directory if it doesn't exist
    work_dir = os.path.join(script_dir, 'git_simulator_work')
    if not os.path.exists(work_dir):
        os.makedirs(work_dir)
    os.chdir(work_dir)
    return work_dir

def get_user_input(prompt: str, input_type: type):
    """Get and validate user input."""
    while True:
        try:
            value = console.input(f"[cyan]{prompt}[/cyan]")
            return input_type(value)
        except ValueError:
            console.print("[red]Please enter a valid value.[/red]")
            continue

def create_commit(file_path: str, date_str: str, commit_num: int) -> bool:
    """Create a single commit with the specified date."""
    try:
        # Ensure the file exists
        if not os.path.exists(os.path.dirname(file_path)):
            os.makedirs(os.path.dirname(file_path))
            
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(f'Commit for {date_str}\n')
        
        # Use shell=True for Windows compatibility
        os.system('git add .')
        commit_msg = f'feat: automated commit #{commit_num}'
        result = os.system(f'git commit --date="{date_str}" -m "{commit_msg}" > {"NUL" if os.name == "nt" else "/dev/null"} 2>&1')
        
        return result == 0
    except Exception as e:
        console.print(f"[red]Error creating commit: {e}[/red]")
        return False

def main():
    """Main function to handle the Git contribution simulation."""
    try:
        # Setup working directory
        work_dir = ensure_directory()
        FILE_PATH = os.path.join(work_dir, 'test.txt')
        CURRENT_YEAR = datetime.now().year

        # Display welcome banner
        welcome_text = Text("Git Contribution Simulator", style="bold cyan")
        console.print(Panel(welcome_text, border_style="cyan", padding=(1, 2)))
        console.print()

        # Get user input
        num_commits = get_user_input("Enter the number of commits to create: ", int)
        year = get_user_input(f"Enter the year for the commits (1970-{CURRENT_YEAR}): ", int)

        # Validate year
        if not (1970 <= year <= CURRENT_YEAR):
            console.print(f"[red]Please enter a year between 1970 and {CURRENT_YEAR}[/red]")
            return

        # Initialize repository if needed
        if not os.path.exists('.git'):
            with console.status("[bold green]Initializing Git repository...", spinner="dots"):
                os.system('git init > {"NUL" if os.name == "nt" else "/dev/null"} 2>&1')

        # Create initial commit if file doesn't exist
        if not os.path.exists(FILE_PATH):
            with console.status("[bold green]Creating initial commit...", spinner="dots"):
                with open(FILE_PATH, 'w', encoding='utf-8') as file:
                    file.write('# Git Contribution Simulator\n')
                os.system('git add .')
                os.system(f'git commit -m "init: initial commit" > {"NUL" if os.name == "nt" else "/dev/null"} 2>&1')

        console.print("\n[bold green]Starting commit generation...[/bold green]")
        
        # Create progress bar layout
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(complete_style="green", finished_style="green"),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TimeElapsedColumn(),
            console=console,
        ) as progress:
            main_task = progress.add_task(f"[cyan]Creating commits for {year}", total=num_commits)
            
            successful_commits = 0
            
            for i in range(num_commits):
                month = random.randint(1, 12)
                day = random.randint(1, 28)
                hour = random.randint(9, 17)
                minute = random.randint(0, 59)
                
                date_str = f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:00"
                
                if create_commit(FILE_PATH, date_str, i + 1):
                    successful_commits += 1
                    progress.update(main_task, advance=1)

        # Final push
        console.print("\n[bold green]Pushing commits to remote repository...[/bold green]")
        try:
            with console.status("[bold green]Pushing commits...", spinner="dots"):
                push_result = os.system('git push -u origin main > {"NUL" if os.name == "nt" else "/dev/null"} 2>&1')
            if push_result == 0:
                console.print("[bold green]✓[/bold green] Successfully pushed all commits!")
            else:
                console.print("[yellow]⚠️ Push failed. You may need to push manually or check your remote configuration.[/yellow]")
        except Exception as e:
            console.print(f"[red]Error during push: {e}[/red]")

        # Final summary
        summary = Text()
        summary.append("\n=== Summary ===\n", style="bold cyan")
        summary.append(f"Total commits created: ", style="dim")
        summary.append(f"{successful_commits}/{num_commits}\n", style="bold green")
        summary.append(f"Target year: ", style="dim")
        summary.append(f"{year}\n", style="bold cyan")
        summary.append(f"Working directory: ", style="dim")
        summary.append(f"{work_dir}\n", style="bold white")
        
        console.print(Panel(summary, border_style="cyan", padding=(1, 2)))

    except Exception as e:
        console.print(f"[red]An error occurred: {str(e)}[/red]")
        console.print("[yellow]Please ensure you have appropriate permissions and Git is properly installed.[/yellow]")

if __name__ == "__main__":
    main()
