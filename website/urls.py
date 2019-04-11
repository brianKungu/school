from django.urls import path
from . import views

app_name='website'

urlpatterns=[
    path('',views.index,name='index'),
    path('<int:pk>/update-view',views.AboutUpdateView.as_view(), name='about'),
    path('create-staff',views.create_staff,name='create_staff'),
    path('(?P<staff_id>[0-9]+)/delete-staff', views.staff_delete, name='delete-staff'),
    path('<int:pk>/update-staff',views.StaffUpdateView.as_view(), name='update-staff'),
    path('departments',views.department,name='departments'),
    path('create-department',views.create_department,name='create_department'),
    path('<int:pk>/update-department',views.DepartmentUpdateView.as_view(),name='update-department'),
    path('(?P<department_id>[0-9]+)/delete-department',views.department_delete,name='delete-department'),
    path('clubs',views.club,name='clubs'),
    path('create-club',views.create_club,name='create_club'),
    path('<int:pk>/update-club',views.ClubUpdateView.as_view(),name='update-club'),
    path('(?P<club_id>[0-9]+)/delete-club',views.club_delete,name='delete-club'),
]


