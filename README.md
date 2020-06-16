# pyreply V0.2
Create script to repat last n commits
Using GitPython library

Usage:
1. set repository path and hash arguments:
   
     -h, --help            show this help message and exit
     -r REPO, --repo REPO  Absolute path to repository
     -x HASH, --hash HASH  First hash that will be in the reply

3. Run: python3 gitreply.py > reply.sh
4. Reset to last_hast
5. Run reply.sh if needed

TODO:
- Add filtering by user
- Add Create standalone lib
- Add Hash and repo poath checking
