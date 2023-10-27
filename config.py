import os

base_url = 'https://canvas.instructure.com'
account_id = 0

try:
    with open(os.path.expanduser('~/.canvas-api-token')) as f:
        access_token = f.read().strip()
except FileNotFoundError:
    print("Canvas API token not found. Please create a file called ~/.canvas-api-token and put your Canvas API token in it.")
    exit(1)