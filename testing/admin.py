from django.contrib import admin

# Register your models here.


from testing.models import Form1
admin.site.register(Form1)

from testing.models import Form3
admin.site.register(Form3)

