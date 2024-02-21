from django.contrib import admin
from .models import about, project, contact, resume

admin.site.site_header = "My Portfolio Admin"
admin.site.site_title = "My Portfolio Admin Portal"
admin.site.index_title = "Welcome to My Portfolio Admin Portal"





admin.site.register(about)
admin.site.register(project)
admin.site.register(contact)
admin.site.register(resume)