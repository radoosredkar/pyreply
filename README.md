# pyreply V0.3
Create script to repat last n commits
Using GitPython library

Either use gitreply.py script from the master or use standalone dist/gitreply.sh from the
standalone_lib branch

Usage:
1. set repository path and hash arguments:
   
     -h, --help            show this help message and exit
     -r REPO, --repo REPO  Absolute path to repository
     -x HASH, --hash HASH  First hash that will be in the reply

3. Run: python3 gitreply.py > reply.sh
4. Reset to last_hast
5. Run reply.sh if needed
