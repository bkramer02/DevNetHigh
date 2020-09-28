"""
Using Webex Teams API to create a new webex room called DevNet High, 
post a message to the newly created room.
Includes error detection. 
"""

import requests
import json

myWebexToken = "ZDBlYWNlYzEtZGQyOS00MWMxLTk4M2ItOTk4OGIzMGY4ZmM1ZGFlNmUyYjEtNGQ4_PF84_55609b58-8953-4e48-a3e4-f03e857c3ac6"  # your personal token
WebexRoomID = ""
room_url = "https://webexapis.com/v1/rooms"
message_url = "https://webexapis.com/v1/messages"

room_data = {
    "title": "DevNet High 2020 - Challenge4"
}


header = {
    # api key authorization header
    "Content-Type": "application/json",
    "Authorization": f"Bearer {myWebexToken}"
}


def post_message():
    """
    Post text to newly created room.
    Display a confirmation message on the console with message and room name text
    """
    message_data = {
    "roomId": WebexRoomID,
    "text": "Hello World"
    }
    rsp = requests.post(message_url, headers=header, data=json.dumps(message_data))  ##post to room
    jsonRsp = rsp.json()
    RoomTit= room_data["title"]
    MsgTxt = jsonRsp["text"]
    print(f"{MsgTxt} was succesfully displayed in the {RoomTit} space!")


if __name__ == '__main__':
    """
    Main method which creates the room and calls the post_message() method.
    Error detection prints message if room was not created.
    """
    response = requests.post(room_url, headers=header, data=json.dumps(room_data))  ##create room

    if response.status_code == 200:
        jsonResponse = response.json()
        WebexRoomID = jsonResponse["id"]
        post_message()
    else:
        print('An error occurred')  ##error detection
        print(response.status_code)
