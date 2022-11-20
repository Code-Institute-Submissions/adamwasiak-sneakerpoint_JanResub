from . import views
from django.urls import path
from reviews import views as review_views

urlpatterns = [
    path('', review_views.review_view, name='review'),
]
