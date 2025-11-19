

from django.urls import path
from posts import views


urlpatterns = [
    path('get-subjects/', views.get_subjects, name="Subjects"),
    
    path('form-tutor-search/', views.search_tutor, name="tutor_search"),
    
    path('materias/', views.materias_lista, name="materias_lista"),
    
    path('registrar/<int:tutor_id>/<int:materia_id>', views.registrar_solicitud, name='registrar'),
]