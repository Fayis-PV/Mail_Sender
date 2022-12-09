from django.shortcuts import render,redirect
from .models import Recipients
from django.contrib import messages
from .forms import RecipientsForm
from django.conf import settings
from django.core.mail import send_mail,EmailMessage
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

# Create your views here.

def home(req):
    form = RecipientsForm()
    context = {'form':form}
    return render(req,'add_recipient.html',context)

def add(req):
    if req.method == 'POST':
        form = RecipientsForm(req.POST,req.FILES)
        print(req.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            file = form.cleaned_data.get('file')
            
            reciepient = Recipients.objects.create(name=name,email=email,file=file)
            reciepient.save()
            messages.info(req,reciepient.name+' is added as a new recipient')
        else:
            messages.info(req,'wrong')
        return redirect('/')


def view(req):
    recipients = Recipients.objects.all()
    print(recipients)
    context = {'recipients':recipients}
    return render(req,'view_recipient.html',context)

def delete(req,id):
    print(id)
    recipient = Recipients.objects.get(pk=id)
    recipient.delete()
    return redirect('/view')

def mail(req):
    recipient = Recipients.objects.all()
    for reci in recipient:
        subject = 'Seerah Conference Certificate'
        message = 'Hi '+reci.name+', We are very happy to inform you that it was an exhilarating moment that you participated in this Seerah conference. We humbly request you to cooperate in more such programs in coming days, may Allah bless us. Here we provide a certificate of participation in this* National Seerah Conference 2K22.' 
        email_from = settings.EMAIL_HOST_USER
        # recipient_list = ['fayispvchelari@gmail.com','finutyping@gmail.com','mfayispv@gmail.com' ]
        print([reci.email])
        email = EmailMessage( subject, message, email_from, [reci.email] )
        email.content_subtype='html'

        img_path = open(reci.file.path,'rb').read()
        img = MIMEImage(img_path, 'jpg')
        img.add_header("Content-Disposition", "inline", filename='Seerah Conference Certificate') # David Hess recommended this edit

        email.attach(img)
        email.send()
        messages.info(req,'Message Send to '+reci.name)
    return redirect('/')
