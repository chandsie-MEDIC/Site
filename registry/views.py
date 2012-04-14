from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
from registry.forms import UserRegistrationForm, UserProfileRegistrationForm

@csrf_exempt
def server_auth(request):
    if request.method == 'POST':
        response = 'Error'
        u = authenticate(username=request.POST['username'], password=request.POST['password'])
        if u is not None and not u.is_staff: 
            response = 'Dr. ' + u.get_full_name()
        return HttpResponse(response)
    raise Http404

@csrf_exempt
def server_detail(request, username):
    if request.method == 'POST':
        response = 'Error'
        auth = authenticate(username=request.POST['username'], password=request.POST['password'])
        if auth is not None and auth.is_staff: 
            user = User.objects.get(username=username)
            if not user.is_staff: 
                profile = user.get_profile()
                response = 'Dr. ' + user.get_full_name() + '$';
                response += profile.specialty + '$'
                response += profile.url + '$'
                response += profile.address + '$'
                response += profile.phone_number + '$'
        return HttpResponse(response)
    raise Http404
    
@login_required
def detail(request, new_user = False):
    if request.user.is_staff:
        return redirect('/MEDIC/admin')
    n = request.user.get_full_name()
    profile = request.user.get_profile()
    u = [profile.specialty, profile.address, profile.phone_number, ]
    return render_to_response('detail.html', {'name' : n, 'user': u, 'url' : profile.url, 'new' : new_user},
                               context_instance=RequestContext(request))
    
def register(request):
    if request.method == 'POST':
        userForm = UserRegistrationForm(request.POST)
        userProfileForm = UserProfileRegistrationForm(request.POST)
        if userForm.is_valid() and userProfileForm.is_valid():
            user = User.objects.create_user(userForm.cleaned_data["username"], userForm.cleaned_data["email"], userForm.cleaned_data["password"])
            user.first_name = userForm.cleaned_data["first_name"]
            user.last_name = userForm.cleaned_data["last_name"]
            user.save()
            userProfile = userProfileForm.save(commit=False)
            userProfile.user = user
            userProfile.save()
            return redirect('/MEDIC/success/')
    else:
        userForm = UserRegistrationForm()
        userProfileForm = UserProfileRegistrationForm()
    return render_to_response('register.html', 
                              {'userForm': userForm, 'userProfileForm' : userProfileForm},
                              context_instance=RequestContext(request))
