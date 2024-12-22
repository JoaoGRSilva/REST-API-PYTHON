from urllib.request import urlopen
import json
try:
    git_user = input("Digite o usuário: ")
    url = f"https://api.github.com/users/{git_user}/events/public"
    print(url)
    with urlopen(url) as response:
        body = response.read()

    git_activity = json.loads(body)
    print(git_activity)
except Exception as e:
    print(f"Error: {e}")