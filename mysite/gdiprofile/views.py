from django.shortcuts import render
from .models import Profile

# Create your views here.
def profile(request):
    profile_list = Profile.objects.order_by('name')
    context = {'profile_list': profile_list}
    print('profile')
    return render(request, 'gdiprofile/profile.html', context)

def profileDetail(request,profile_id):
    profile = Profile.objects.get(pk=profile_id)
    return render(request, 'gdiprofile/profileDetail.html', {'profile' : profile})

def DisplayMyPageWithParameter(request, my_parameter):
    parameter = my_parameter
    profile_list = Profile.objects.order_by('name')
    context = {'profile_list': profile_list, 'parameter':parameter}
    return render(request, 'portal/profile.html', context)