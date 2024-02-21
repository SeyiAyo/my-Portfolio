from django.shortcuts import render
from .models import about, project
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm



def index(request):
    about_me = about.objects.all()
    projects = project.objects.all()
    
    context = {
        'about_me': about_me,
        'projects': projects
    }
    return render(request, 'showcase.html', {'about_me' : about_me, 'projects' : projects})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and email and message:
            email_message = f"From: {name}\nEmail: {email}\nMessage: {message}"
            send_mail(
                subject='Contact Form Submission',
                message=email_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['oluwaseyiayoola97@gmail.com']  # Enter your email address here
            )
            return render(request, 'showcase.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})