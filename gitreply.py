from git import Repo, InvalidGitRepositoryError
import argparse
import os
import itertools


def create_documentation():
    parser = argparse.ArgumentParser(
        description="Create script for replying commits from hash to HEAD"
    )
    parser.add_argument(
        "-r", "--repo", dest="repo", type=str, help="Absolute path to repository"
    )
    parser.add_argument(
        "-x",
        "--hash",
        dest="hash",
        type=str,
        help="First hash that will be in the reply",
    )
    return parser


def read_arguments(container):
    args = parser.parse_args()
    return (args.repo, args.hash)


parser = create_documentation()
git_repo, git_hash = read_arguments(parser)

if git_repo and git_hash:
    path_exists = os.path.exists(os.path.expanduser(git_repo))

if git_repo and git_hash and path_exists:
    try:
        repo: Repo = Repo(git_repo)
        all_commits = list(
            itertools.takewhile(
                lambda x: repo.git.rev_parse(x, short=7) != git_hash,
                repo.iter_commits(),
            )
        )
        all_commits.reverse()
        print("git reset")
        for commit in all_commits:
            files = commit.stats.files
            for file in files:
                cmd_add = f"git add {file}"
                print(cmd_add)
            cmd_commit = f'git commit -m "{commit.message}"'
            print(cmd_commit)
    except InvalidGitRepositoryError as e:
        print(f"Invalid git repository in folder {git_repo}")
else:
    parser.print_help()
