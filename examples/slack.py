from slackclient import SlackClient

slack_token = "TOKEN"
sc = SlackClient(slack_token)

r = sc.api_call(
  "chat.postMessage",
  channel="@joy_wang",
  text="Hello from python"
)