import os
import urllib.parse
from twilio.rest import Client
from django.conf import settings

def get_voicemail_data():
    return [
        {
            "to_number": settings.EXAMPLE_NUMBER,
            "from_number" : settings.TWILIO_PHONE_NUMBER,
            "content": "Hello, I am an ai assitant of Influence Media. We are leaving you this voicemail as a follow up to our email discussing our promoition. Please call back at 999-999-9999",
            "is_text": True,

        },
    ]

def send_voicemail(to_number, from_number ,voicemail, is_text=True):
    print("sending voicemail function ago")
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    print("client", client)
    encoded_content = urllib.parse.quote(voicemail)
    query_params = f"?is_text={is_text}&content={encoded_content}"
    function_url = 'https://voicemail-5543.twil.io/voicemail' + query_params
    print("Function URL:", function_url)  # Print function URL for debugging
    
    try:
        call = client.calls.create(
            to=to_number,
            from_=from_number,
            url=function_url,
            machine_detection='DetectMessageEnd'
        )
        print(f"Call initiated with SID: {call.sid}")  # Print call SID for debugging
    except Exception as e:
        # Log the exception
        print("An error occurred while sending the voicemail:", e)