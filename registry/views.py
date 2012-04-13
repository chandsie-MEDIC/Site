from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def auth(request):
    response = 'False'
    if request.method == 'POST':
        u = authenticate(username = request.POST['username'], password = request.POST['password'])
        if u is not None: 
            response = 'Dr. ' + u.get_full_name()
          
    return HttpResponse(response)
    
