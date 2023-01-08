from . import views
from django.urls import path
from reviews import views as review_views

# urls for reviews app
urlpatterns = [
    path('', review_views.review_view, name='review'),
]
