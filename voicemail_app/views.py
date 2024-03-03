from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .utils import send_voicemail
from django.conf import settings
import json

from django.shortcuts import render
from django.template import loader
print(loader.get_template('voicemail_app/index.html'))
# New view function to render the index.html template
def index(request):
    return render(request, 'voicemail_app/index.html')

@csrf_exempt  # Consider using CSRF token in AJAX request instead of exempting
def ajax_send_voicemail(request):
    # Simulate fake JSON data for testing
    fake_data = {
        "to_number": settings.EXAMPLE_NUMBER,
        "from_number": settings.TWILIO_PHONE_NUMBER,
        "voicemail": "This is a test voicemail message",
        "is_text": True
    }

    # Use the fake data for testing
    to_number = fake_data.get('to_number')
    from_number = fake_data.get('from_number')
    voicemail = fake_data.get('voicemail')
    is_text = fake_data.get('is_text', True)

    # Example validation (You should implement actual validation logic)
    if not to_number or not voicemail:
        return JsonResponse({"success": False, "message": "Missing to_number or content"}, status=400)

    try:
        # Call the send_voicemail function with the actual data
        send_voicemail(to_number, from_number, voicemail, is_text),

        # Return a fake JSON response indicating success for testing
        return JsonResponse({"success": True, "message": "Simulated voicemail sent successfully."})
    except Exception as e:
        # Log the exception here
        return JsonResponse({"success": False, "message": "An error occurred while sending the voicemail."}, status=500)