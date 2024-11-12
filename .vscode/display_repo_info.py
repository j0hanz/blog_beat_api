import os
import subprocess
from datetime import datetime


def get_repo_name():
    """Returns the name of the current Git repository."""
    try:
        repo_path = subprocess.check_output(['git', 'rev-parse', '--show-toplevel']).strip().decode('utf-8')
        return os.path.basename(repo_path)
    except subprocess.CalledProcessError:
        return 'Unknown Repository'


def get_branch_name():
    """Returns the current Git branch name."""
    try:
        return subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).strip().decode('utf-8')
    except subprocess.CalledProcessError:
        return 'Unknown Branch'


def get_gitpod_user():
    """Returns the Gitpod user name from environment variables."""
    return os.getenv('GITPOD_GIT_USER_NAME', 'Unknown User')


def get_latest_commit_date():
    """Returns the latest commit date in YYYY-MM-DD format."""
    try:
        commit_date = subprocess.check_output(['git', 'log', '-1', '--format=%cd']).strip().decode('utf-8')
        # Parse the commit date and format it to YYYY-MM-DD
        formatted_date = datetime.strptime(commit_date, '%a %b %d %H:%M:%S %Y %z').strftime('%Y-%m-%d')
        return formatted_date
    except subprocess.CalledProcessError:
        return 'Unknown'


def main() -> None:
    """Main function to print repository details."""
    repo_name = get_repo_name()
    branch_name = get_branch_name()
    gitpod_user = get_gitpod_user()
    commit_date = get_latest_commit_date()

    # Display the repository information
    print('─' * 41)
    print('      🚀 ɢɪᴛᴘᴏᴅ ᴇɴᴠɪʀᴏɴᴍᴇɴᴛ ɪɴꜰᴏ 🚀      ')
    print('─' * 41)
    print('-' * 41)
    print(f'Repo           {repo_name:>26}')
    print('-' * 41)
    print(f'Branch         {branch_name:>26}')
    print('-' * 41)
    print(f'User           {gitpod_user:>26}')
    print('-' * 41)
    print(f'Last Updated   {commit_date:>26}')
    print('-' * 41)


if __name__ == '__main__':
    main()
