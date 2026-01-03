import os

gitignore_content = """
# See https://help.github.com/articles/ignoring-files/ for more about ignoring files.

# dependencies
/node_modules
/.pnp
.pnp.js

# testing
/coverage

# next.js
/.next/
/out/

# production
/build

# misc
.DS_Store
*.pem

# debug
npm-debug.log*
yarn-debug.log*
ts-debug.log*

# local env files
.env*.local
.env

# vercel
.vercel
"""

def setup_git():
    print("🛡️  Creating .gitignore file...")
    with open(".gitignore", "w", encoding="utf-8") as f:
        f.write(gitignore_content.strip())
    print("✅ .gitignore created. You are safe to push.")

if __name__ == "__main__":
    setup_git()
