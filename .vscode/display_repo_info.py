import os
import subprocess

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


def main() -> None:
    """Main function to print repository details."""
    repo_name = get_repo_name()
    branch_name = get_branch_name()
    gitpod_user = get_gitpod_user()

    # Display the repository information
    print('╭' + '─' * 40 + '╮')
    print('│     🚀 Gitpod Environment Info 🚀     │')
    print('╰' + '─' * 40 + '╯')
    print(f'🗂️ Repo           {repo_name:>23}')
    print(f'🌿 Branch         {branch_name:>23}')
    print(f'👤 User           {gitpod_user:>23}')


if __name__ == '__main__':
    main()
