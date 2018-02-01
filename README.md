# ThingLogix
### AWS Lambda function for serverless Pig Latin Slack bot


## Installation guide  

You will first need to clone this repository to your device.  You can do this from this git hub page by clicking the green
'clone or download' button found on the right side of the screen and clicking 'download as zip'.<br>

Sign into your AWS account and navigate to the AWS Lambda page, this can be found from the console by clicking the
'Lambda' button under the 'Compute' section.<br>

Click the 'Create Function' button in the upper right.<br>

Under 'Author from scratch', make sure that you have each of the following:
- Name can be anything you want
- Runtime must be 'Python 3.6'
- Role must be 'Choose an existing role'
- In the 'Existing role' drop down menu, select 'lambda_basic_execution'

Go ahead and create your lambda function by clicking the orange button in the bottom right corner

In the lambda configuration screen scroll down to the page the says 'Function Code'
in the 'Code Entry Type' drop down, select 'Upload a .ZIP file'

In the 'Handler' menu, type *pig_latin_slackbot.lambda_handler*

Set an environment variable called "BOT_TOKEN" with the bot token provided by Slack.

The last step is to upload code.  Under the 'Function package' section, click the Upload button and find the .zip that you just downloaded.



Huge thanks to:
* [Rigel Di Scala](https://chatbotslife.com/@zedr) for his [tutorial on writing a serverless Slack bot using AWS](https://chatbotslife.com/write-a-serverless-slack-chat-bot-using-aws-e2d2432c380e)
* [Ken Kapptie](https://gist.github.com/kappter) for his [Python code on implementing Pig Latin to save me the trouble :)](https://gist.github.com/kappter/9936137)
