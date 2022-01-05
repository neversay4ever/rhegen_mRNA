from django.contrib import admin

# Register your models here.
from .models import UTR5


class UTR5Admin(admin.ModelAdmin):
    model = UTR5
    list_display = [field.name for field in UTR5._meta.get_fields()
                    if field.name != 'id']


admin.site.register(UTR5, UTR5Admin)
