from django.http import HttpResponse

def index(request):

    return HttpResponse(f'Here will be  more text soon\n Request:\b {request.META}')