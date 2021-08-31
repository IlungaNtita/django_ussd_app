
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.



@csrf_exempt
def index(request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')

        response = ""

        if text == "":
            response = "CON Welcome to watcheye choose your emergency:\n"
            # response .= "1. My Account \n"
            response += "1. 5 Stars \n"
            response += "2. 4 Stars \n"
            response += "3. 3 Stars \n"
            response += "4. 2 Stars \n"
            response += "5. 1 Star \n"

        elif text == "1":
            response = "END You chose 5 Stars. We will send help to this phone number {0}".format(phone_number)

        elif text == "2":
            response = "END You chose 4 Stars. We will send help to this phone number {0}".format(phone_number)

        elif text == "3":
            response = "END You chose 3 Stars. We will send help to this phone number {0}".format(phone_number)

        elif text == "4":
            response = "END You chose 2 Stars. We will send help to this phone number {0}".format(phone_number)
        
        elif text == "5":
            response = "END You chose 1 Stars. We will send help to this phone number {0}".format(phone_number)


        return HttpResponse(response)
