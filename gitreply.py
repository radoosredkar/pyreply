from git import Repo
import argparse

last_hash = "0f77021"
user = "radoosredkar"


parser = argparse.ArgumentParser(description="Create script for replying commits from hash to HEAD")
parser.add_argument("-r", "--repo", dest="repo", type=str,  help="Absolute path to repository")
parser.add_argument("-x", "--hash", dest="hash", type=str, help="First hash that will be in the reply")
args = parser.parse_args()

if args.repo and args.hash:
    repo: Repo = Repo(args.repo)
    all_commits = list(repo.iter_commits())
    all_commits.reverse()
    print("git reset")
    for commit in all_commits:
        short_hash = repo.git.rev_parse(commit, short=7)
        if short_hash == args.hash:
            break
        else:
            files = commit.stats.files
            for file in files:
                cmd_add = f"git add {file}"
                print(cmd_add)
            cmd_commit = f'git commit -m "{commit.message}"'
            print(cmd_commit)
else:
    parser.print_help()

# TODO: Add hash and repo path checking
