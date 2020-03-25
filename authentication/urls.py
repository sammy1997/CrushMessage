from django.urls import path, include
from . import views

app_name = 'authentication'

urlpatterns = [
    path('',views.index, name= 'home'),
    path('CrushMessage/<username>', views.submit_message, name = 'submit_message'),
    # path('submit_message/<username>', views.submit_message, name = 'submit_message'),
]
