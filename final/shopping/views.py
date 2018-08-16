from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import data
def home(request):
    context = {
        "datas": data.objects.all()
    }
    template = 'home.html'
    return render(request,template,context)

def about(request):
    context = locals()
    template = 'about.html'
    return render(request,template,context)

@login_required
def UserProfile(request):
    user=request.user
    context = {'user':user}
    template = 'profile.html'
    return render(request,template,context)
