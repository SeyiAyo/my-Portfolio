from django.shortcuts import render, get_object_or_404
from .models import about, project, resume
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.http import FileResponse, Http404



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


def download_resume(request):
    # Assuming there's only one resume in the database
    try:
        # Retrieve the first (and presumably only) resume
        resume_obj = resume.objects.first()
        # Open the file associated with the resume and return it as a FileResponse
        return FileResponse(open(resume_obj.file.path, 'rb'), as_attachment=True)
    except (resume.DoesNotExist, FileNotFoundError, AttributeError):
        raise Http404("File does not exist")