from slackclient import SlackClient

slack_token = "xoxb-xxx-xxx-xxx"  # 替换成你的 Bot User OAuth Access Token
slack = SlackClient(slack_token)

def main():
  slack.api_call(
    "chat.postMessage",
    channel="#general",
    username="my_bot",
    icon_url="https://blog.dianqk.org/favicon.png",
    text='Hello World!'
  )

if __name__ == '__main__':
  main()
