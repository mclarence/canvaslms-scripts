import os

base_url = 'https://canvas.parra.catholic.edu.au'
account_id = 8

try:
    with open(os.path.expanduser('~/.canvas-api-token')) as f:
        access_token = f.read().strip()
except FileNotFoundError:
    print("Canvas API token not found. Please create a file called ~/.canvas-api-token and put your Canvas API token in it.")
    exit(1)