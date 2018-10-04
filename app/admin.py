from django.contrib import admin
from .models import scenario, department, bcp_measure

# Register your models here.
admin.site.register(scenario)
admin.site.register(department)
admin.site.register(bcp_measure)
