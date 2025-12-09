from django.urls import path
from . import views

app_name = 'analytics'

urlpatterns = [
    path('', views.analytics_dashboard, name='dashboard'),
    path('form/<int:form_id>/results/', views.form_results, name='form_results'),
    path('form/<int:form_id>/export/', views.export_form_results, name='export_results'),
    path('students/export/', views.export_students_list, name='export_students'),
]