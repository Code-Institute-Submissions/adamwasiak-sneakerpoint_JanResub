from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'review',
        'created_on',
    )

    ordering = ('review',)

admin.site.register(Review, ReviewAdmin)