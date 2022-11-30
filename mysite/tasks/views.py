from django.shortcuts import HttpResponse
from datetime import datetime

# Create your views here.
def home_view(request):
    print("request: ", request)
    return HttpResponse("Hello from Django")

def welcome_page(request):
    print("request: ", request)
    return HttpResponse(f"<h1 style='text-align:center; background-color:DodgerBlue'> <b>Hello my name is Vahe !!!!! </b> </h1>"
                        f"<br>"
                        f"{datetime.now()}")