from django.urls import path
from . import views

app_name='website'

urlpatterns=[
    path('',views.index,name='index'),
    path('<int:pk>/update-view',views.AboutUpdateView.as_view(), name='about'),
    path('create-staff',views.create_staff,name='create_staff'),
]
