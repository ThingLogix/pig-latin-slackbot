# ThingLogix
### AWS Lambda function for serverless Pig Latin Slack bot

## Installation guide
Clone this repository, then zip all of the contents. Upload the zip file to AWS Lambda as a Lambda function with runtime Python 3.6. The handler should be pig_latin_slackbot.lambda_handler. Set an environment variable called "BOT_TOKEN" with the bot token provided by Slack.

Huge thanks to:
* [Rigel Di Scala](https://chatbotslife.com/@zedr) for his [tutorial on writing a serverless Slack bot using AWS](https://chatbotslife.com/write-a-serverless-slack-chat-bot-using-aws-e2d2432c380e)
* [Ken Kapptie](https://gist.github.com/kappter) for his [Python code on implementing Pig Latin to save me the trouble :)](https://gist.github.com/kappter/9936137)
