import requests
url = 'https://staging.replit.com/graphql'
headers = {
    "X-Requested-With": "https://staging.replit.com",
    "Referrer":"https://staging.replit.com/"
}

def getuserbody(username):
    return {
        "query": f'query UserData {{ userByUsername(username:"{username}"){{ karma, bio, posts {{ items {{ title, repl {{ language }} }} }} }} }}'
    }

def sendreq(body):
    x = requests.post(url=url, data=body, headers=headers)
    return x