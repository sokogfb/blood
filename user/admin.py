from django.contrib import admin
from .models import Info

class InfoAdmin(admin.ModelAdmin):
	list_display = ('name', 'age', 'blood_group')
	list_filter = ('age', 'blood_group')
	search_fields = ('name', 'age', 'blood_group')


admin.site.register(Info, InfoAdmin)
