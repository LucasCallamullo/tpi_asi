from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from posts.models import MateriaTutor, Subject, Degree, Tutor

def get_subjects(request):
    if request.method == 'GET':
        subjects = Subject.objects.all().values('id', 'name')
        return JsonResponse(list(subjects), safe=False)
    

def registrar_solicitud(request, tutor_id, materia_id):
    try:
        tutor = Tutor.objects.select_related('user').get(id=tutor_id)
        materia = MateriaTutor.objects.get(id=materia_id)
        
        context = {
            'tutor': tutor,
            'tutor_user': tutor.user,  # Datos del usuario
            'materia': materia,  # Datos del usuario
        }
        return render(request, 'posts/registrar_solicitud.html', context)
        
    except Tutor.DoesNotExist:
        return render(request, 'posts/error.html', {'mensaje': 'Tutor no encontrado'})

def materias_lista(request):
    # Obtener parámetros del request
    degree_id = request.GET.get('degree') or request.POST.get('degree')
    subject_id = request.GET.get('subject') or request.POST.get('subject')
    university = request.GET.get('university') or request.POST.get('university')
    modalidad = request.GET.get('modalidad') or request.POST.get('modalidad')
    precio_min = request.GET.get('precio_min') or request.POST.get('precio_min')
    precio_max = request.GET.get('precio_max') or request.POST.get('precio_max')
    
    # Filtrar materias de tutores
    materias_tutores = MateriaTutor.objects.all()
    
    if subject_id and subject_id != '0':
        materias_tutores = materias_tutores.filter(materia_id=subject_id)
    
    if modalidad and modalidad != 'todas':
        materias_tutores = materias_tutores.filter(modalidad=modalidad)
    
    if precio_min:
        materias_tutores = materias_tutores.filter(precio__gte=float(precio_min))
    
    if precio_max:
        materias_tutores = materias_tutores.filter(precio__lte=float(precio_max))
    
    # Si es una petición AJAX, devolver JSON
    
    # Si es petición normal, renderizar template
    context = {
        'materias': materias_tutores,
        'filtros': {
            'degree': degree_id,
            'subject': subject_id,
            'modalidad': modalidad,
            'precio_min': precio_min,
            'precio_max': precio_max,
        }
    }
    return render(request, 'posts/materias_lista.html', context)
    


def search_tutor(request):
    subjects = Subject.objects.all()
    degrees = Degree.objects.all()
    
    
    context = {
        'subjects': subjects,
        'degrees': degrees,
    }
    return render(request, 'posts/search_tutor.html', context)
