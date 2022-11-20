from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'subject',
        'review',
    )

    ordering = ('review',)

admin.site.register(Review, ReviewAdmin)