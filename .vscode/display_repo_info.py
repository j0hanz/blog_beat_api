import os
import subprocess
from datetime import UTC, datetime

import fancy_text


def get_repo_name():
    """Returns the name of the current Git repository."""
    try:
        repo_path = (
            subprocess.check_output(['git', 'rev-parse', '--show-toplevel'])
            .strip()
            .decode('utf-8')
        )
        return os.path.basename(repo_path)
    except subprocess.CalledProcessError:
        return 'Unknown Repository'


def get_branch_name():
    """Returns the current Git branch name."""
    try:
        return (
            subprocess.check_output(
                ['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
            )
            .strip()
            .decode('utf-8')
        )
    except subprocess.CalledProcessError:
        return 'Unknown Branch'


def get_gitpod_user():
    """Returns the Gitpod user name from environment variables."""
    return os.getenv('GITPOD_GIT_USER_NAME', 'Unknown User')


def get_latest_commit_date() -> str | None:
    """Returns the latest commit date in a human-readable format."""
    try:
        commit_date_str = (
            subprocess.check_output(['git', 'log', '-1', '--format=%cd'])
            .strip()
            .decode('utf-8')
        )
        commit_date = datetime.strptime(
            commit_date_str,
            '%a %b %d %H:%M:%S %Y %z',
        )
        now = datetime.now(UTC)
        delta = (now - commit_date).days

        if delta == 0:
            return 'today'
        if delta == 1:
            return 'yesterday'
        return f'{delta} d'
    except subprocess.CalledProcessError:
        return 'Unknown'


def main() -> None:
    """Main function to print repository details."""
    repo_name = get_repo_name()
    branch_name = get_branch_name()
    gitpod_user = get_gitpod_user()
    commit_date = get_latest_commit_date()

    # Display the repository information
    print(fancy_text.gitpod_info)
    print(f'{"🔖":<1} {"Repo":<15} {repo_name:>28}')
    print(fancy_text.long_line)
    print(f'{"👤":<1} {"User":<15} {gitpod_user:>28}')
    print(fancy_text.long_line)
    print(f'{"🌿":<1} {"Branch":<15} {branch_name:>28}')
    print(fancy_text.long_line)
    print(f'{"🕒":<1} {"Last Commit":<15} {commit_date:>28}')
    print('')


if __name__ == '__main__':
    main()
