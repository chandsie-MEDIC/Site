from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def auth(request):
    response = 'False'
    if request.method == 'POST':
        u = authenticate(username=request.POST['username'], password=request.POST['password'])
        if u is not None and not u.is_staff: 
            response = 'Dr. ' + u.get_full_name()
          
    return HttpResponse(response)

@login_required
def detail(request):
    if request.user.is_staff:
        return redirect('/MEDIC/admin')
    n = request.user.get_full_name()
    profile = request.user.get_profile()
    u = [profile.specialty, profile.address, profile.phone_number, ]
    return render_to_response('detail.html', {'name' : n, 'user': u, 'url' : profile.url},
                               context_instance=RequestContext(request))
    
    
