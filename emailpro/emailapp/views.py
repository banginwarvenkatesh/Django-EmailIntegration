from email import message
from django.shortcuts import render
from .forms import UserForm
from .models import User
from django.core.mail import send_mail
from django.conf import settings


def saveUser(request):
    form = UserForm()
    template_name = 'emailapp/sendemail.html'
    context={'form':form}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

        obj = request.POST
        uname = obj.get('u')
        pword = obj.get('p')
        em = obj.get('e')
        recipient_list = [em,]
        subject = 'You have registred Succefully!'
        message = f"Hi!, This is a wlecome email from Venkatesh's Django App! Your username is {uname} and password is {pword}!"
        email_from = settings.EMAIL_HOST_USER
        send_mail (subject, message, email_from,recipient_list)
    return render(request, template_name, context)
# Create your views here.
