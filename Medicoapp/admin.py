from django.contrib import admin
from Medicoapp.models import product
from Medicoapp.models import branch
from Medicoapp.models import contact
from Medicoapp.models import appointment
from Medicoapp.models import members
from Medicoapp.models import Admin

# Register your models here.
admin.site.register(product)
admin.site.register(branch)
admin.site.register(contact)
admin.site.register(appointment)
admin.site.register(members)
admin.site.register(Admin)
