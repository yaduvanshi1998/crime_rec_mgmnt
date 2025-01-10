from django.contrib import admin

# Register your models here.

from crime_rec_app.models import Login_info, Court_info, Judge_info, Offender_info, Crime_info, Prison_information, Guard_information 

admin.site.register(Login_info)
admin.site.register(Court_info)
admin.site.register(Judge_info)
admin.site.register(Offender_info)
admin.site.register(Crime_info)
admin.site.register(Prison_information)
admin.site.register(Guard_information)