import os
from slackclient import SlackClient
# from app.routes import inbound

# SLACK_TOKEN = os.environ.get('SLACK_TOKEN', None)

# slack_client = SlackClient(SLACK_TOKEN)
# BOT_ID = os.environ.get("BOT_ID")

AT_BOT = "<@" + BOT_ID + ">"


# def list_channels():
#     channels_call = slack_client.api_call("channels.list")
#     if channels_call['ok']:
#         return channels_call['channels']
#     return None
#
#
# def channel_info(channel_id):
#     channel_info = slack_client.api_call("channels.info", channel=channel_id)
#     if channel_info:
#         return channel_info['channel']
#     return None
#
# def send_message(channel_id, message):
#     slack_client.api_call(
#         "chat.postMessage",
#         channel=channel_id,
#         text=message,
#         username='pythonbot',
#         icon_emoji=':robot_face:'
#     )

if __name__ == '__main__':
    print("In app file")

    # channels = list_channels()
    # if channels:
    #     print("Channels: ")
    #     for channel in channels:
    #         print(channel['name'] + " (" + channel['id'] + ")")
    #         detailed_info = channel_info(channel['id'])
    #         if detailed_info:
    #             print('Latest text from ' + channel['name'] + ":")
    #             print(detailed_info['latest']['text'])
    #         if channel['name'] == 'general':
    #             send_message(channel['id'], "Hello " +
    #                          channel['name'] + "! It worked!")
    print('-----')
else:
    print("Unable to authenticate.")
