from django.contrib import admin
from users.models import GlobalDB, SpamDB, PersonalContact

# Register your models here.
admin.site.register(GlobalDB)
admin.site.register(PersonalContact)
admin.site.register(SpamDB)