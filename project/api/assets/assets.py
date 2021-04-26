import requests
url = 'https://staging.replit.com/graphql'
headers = {
    "X-Requested-With": "https://staging.replit.com",
    "Referrer":"https://staging.replit.com/"
}

def getuserbody(username):
    return {
        "query": f'query UserData {{ userByUsername(username:"{username}"){{ karma, bio, posts {{ items {{ title, url, repl {{ language }}, board {{ slug }} }} }}, publicRepls{{ items{{ }}}} }} }}'
    }

def getboardbody(slug):
    return {
        "query": f'query {{  boardBySlug(slug: "{slug}"){{ posts {{ items {{ title, url, voteCount, repl {{ language }}, comments{{ items {{ body, voteCount, timeCreated, user {{ username }}}} }}  }} }} }} }}'
    }



def sendrequser(body):
    x = requests.post(url=url, data=body, headers=headers)
    return x.json()['data']['userByUsername']

def sendreqboard(body):
    x = requests.post(url=url, data=body, headers=headers)
    return x.json()['data']['boardBySlug']['posts']['items']