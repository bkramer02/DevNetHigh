from webexteamssdk import WebexTeamsAPI
import requests
import json

#RECOMMENDED MERAKI FIRMWARE VERSIONS
msversion = '12-13'
mrversion = '27-5'
mxversion = '14-42'
mvversion = '4-8'
mtversion = 'X-X'

####GLOBAL VARIABLES FOR MERAKI SECTION
meraki_api_key = 'XXX'
mynetwork = 'XXX'

baseurl = "https://dashboard.meraki.com/api/v0/networks/"
url = baseurl + f"{mynetwork}/devices"

payload = {
}
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": meraki_api_key
} 
meraki_output = []
meraki_string = ""

####GLOBAL VARIABLES FOR WEBEX TEAMS SECTION
WebexRoomID = "XXX"
myWebexToken = "XXX"
message_url = "https://webexapis.com/v1/messages"
webex_header = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {myWebexToken}"
}

def post_message():
    """
    Post text to the DevNet High Team Room
    """
    global meraki_string

    message_data = {
    "roomId": WebexRoomID,
    "text": meraki_string

    }
    rsp = requests.post(message_url, headers=webex_header, data=json.dumps(message_data))
    print(rsp.status_code)

def MerakiFirmwareCompliance():
    """
    Verify if Meraki Devices are running firmware code that is within the defined versions above and print on console screen
    """
    CountMR = 0
    CountMV = 0
    CountMS = 0
    CountMX = 0
    CountMT = 0
    global meraki_string

    response = requests.get(url, headers=headers, data=payload)
    myresponse = response.json()

    meraki_output.append("-- Challenge 5 - Meraki compliance report has completed -- \n")
    meraki_output.append("The Devices in the network that are OUT of firmware compliance are:"+"\n")
    for x in myresponse:
        if x['model'][1]=='R' and x['firmware'].endswith(mrversion):
            CountMR += 1
        elif x['model'][1]=='V' and x['firmware'].endswith(mvversion):
            CountMV += 1
        elif x['model'][1]=='X' and x['firmware'].endswith(mxversion):
                CountMX += 1
        elif x['model'][1]=='S' and x['firmware'].endswith(msversion):
            CountMS += 1
        elif x['model'][1]=='T' and x['firmware'].endswith(mtversion):
            CountMT += 1
        else:
            meraki_output.append(f"\tA {x['model']} with {x['serial']} Serial Number is running this out of compliance firmware: {x['firmware']}"+"\n")

    meraki_output.append("The number of devices in the network that meet the standards are:"+"\n")
    meraki_output.append(f"\t{CountMR} APs"+"\n")
    meraki_output.append(f"\t{CountMS} Switches"+"\n")
    meraki_output.append(f"\t{CountMX} FWs"+"\n")
    meraki_output.append(f"\t{CountMV} Cameras"+"\n")
    meraki_output.append(f"\t{CountMT} Sensors"+"\n")

    for y in meraki_output:
        meraki_string += y
    print (meraki_string)

if __name__ == '__main__':
    MerakiFirmwareCompliance()
    post_message()

