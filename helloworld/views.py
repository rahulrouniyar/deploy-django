from django.http import request, HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello Rahul. Deployment successful.")
