from django.shortcuts import render
from .forms import contactForm
from django.core.mail import send_mail
from django.conf import settings


# to import the settings we typed in the mail
# Create your views here.
def contact(request):
    title= 'Contact'
    form = contactForm(request.POST or None)
    confirm_message =None
    if form.is_valid():
        name= form.cleaned_data['name']
        comment=form.cleaned_data['comment']
        subject='Message from my shopping website'
        message='%s %s' %(comment, name)
        emailFrom=form.cleaned_data['email']
        emailTO=[settings.EMAIL_HOST_USER]
        send_mail(
            subject,
            message,
            emailFrom,
            emailTO,
            fail_silently=True,
        )
        # send_mail(
        #     'Subject here',
        #     'Here is the message.',
        #     'from@example.com',
        #     ['to@example.com'],
        #     fail_silently=False,
        # )
        # after the form is being submitted
        form=None
        title="Thanks!!"
        confirm_message ="Thanks for your concern, will get back to you"
    context ={'title':title,'form':form, 'confirm_message':confirm_message}
    template = 'contact.html'
    return render(request,template,context)
