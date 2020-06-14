from git import Repo

last_hash = "0f77021"
user = "radoosredkar"

repo: Repo = Repo("~/software/GitTeaching/test")
all_commits = list(repo.iter_commits())
all_commits.reverse()
print("git reset")
for commit in all_commits:
    short_hash = repo.git.rev_parse(commit, short=7)
    if short_hash == last_hash:
        break
    else:
        files = commit.stats.files
        for file in files:
            cmd_add = f"git add {file}"
            print(cmd_add)
        cmd_commit = f'git commit -m "{commit.message}"'
        print(cmd_commit)
