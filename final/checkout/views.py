from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def UserCheckout(request):
    context = {}
    template = 'checkout.html'
    return render(request,template,context)
