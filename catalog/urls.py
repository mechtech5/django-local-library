from django.urls import path
from django.views.generic import RedirectView
from . import view

urlpatterns = [
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
]