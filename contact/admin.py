from django.contrib import admin
from .models import Contact

# below will be displayed in admin portal


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'subject',
        'message',
    )

    ordering = ('email',)


admin.site.register(Contact, ContactAdmin)
