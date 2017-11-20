import os
import urllib


BOT_TOKEN = os.environ["BOT_TOKEN"]

SLACK_URL = "https://slack.com/api/chat.postMessage"


def piglatin_text(original):
    """
    Thanks to kappter on GitHub for this
    https://gist.github.com/kappter/9936137
    """
    pyg = 'ay'

    if original and original.isalpha():
        word = original.lower()
        first = word[0]
        if first == ('a' or 'e' or 'i' or 'o' or 'u'):
            new_word = word + pyg
            return new_word
        new_word = word[1:] + first + pyg
        return new_word
    return original


def lambda_handler(data, context):
    if "challenge" in data:
        return data["challenge"]
    slack_event = data['event']

    if "bot_id" in slack_event:
        print("Ignore bot")

    else:
        channel_id = slack_event["channel"]
        msg = ''
        for word in slack_event['text'].split():
            msg += piglatin_text(word) + ' ' 

        print(msg)
        data = urllib.parse.urlencode(
            (
                ("token", BOT_TOKEN),
                ("channel", channel_id),
                ("text", msg)
            )
        )
        data = data.encode("ascii")
        
        request = urllib.request.Request(
            SLACK_URL, 
            data=data, 
            method="POST"
        )

        request.add_header(
            "Content-Type", 
            "application/x-www-form-urlencoded"
        )
        
        urllib.request.urlopen(request).read()

    return "200 OK"
