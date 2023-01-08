from django.urls import path
from contact import views as contact_views

# urls for contact app
urlpatterns = [
    path('', contact_views.contact_view, name='contact'),
]