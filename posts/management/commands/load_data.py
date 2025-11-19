

import random
from django.conf import settings
from posts.models import *
from django.contrib.auth.hashers import make_password
from users.models import CustomUser

from django.core.management.base import BaseCommand
from django.utils.text import slugify


def init_data():
    
    degrees = {
        'Ciencias básicas': [
            'Analisis Matematico I',
            'Analisis Matematico II',
            'Algebra',
            'Fisica I',
            'Fisica II',
        ],
        'Ingeniería en Sistemas': [
            'Algoritmos y Estructura de Datos', 'Semantica y Sintaxis del Lenguaje', 'Analisis de Sistemas',
        ],
        'Ingeniería Civil': [
            'Estabilidad I', 'Estabilidad II'
        ],
        'Ingeniería Mecánica': [],
        'Ingeniería Química': [
            'Quimica General'
        ],
        'Ingeniería Electrónica': [],
        'Ingeniería Industrial': [],
        'Ingeniería Metalúrgica': [],
        'Ingeniería Eléctrica':[],
    }
    
    for key, value in degrees.items():
        degree, _ = Degree.objects.get_or_create(
            slug = slugify(key),
            name=key,
        )
        print("Name Degree:", degree.name)
        
        for name in value:
            subject, _ = Subject.objects.get_or_create(
                slug = slugify(name),
                name=name,
                degree_program=degree,
            )
            print("Name subject:", subject.name)
    
    
    
    # Crear usuarios de ejemplo
    users = [
        {"email": "admin@gmail.com", "first_name": "Comprador", "last_name": "Anonimo", 'role': 'admin'},
        {"email": "tutor@gmail.com", "first_name": "Lucas", "last_name": "Martinez", 'role': 'teacher'},
        {"email": "user1@gmail.com", "first_name": "Agos", "last_name": "Pereyra", 'role': 'student'},
        {"email": "user2@gmail.com", "first_name": "Sofía", "last_name": "Martinez", 'role': 'student'},
    ]
    
    for user_data in users:
        user, created = CustomUser.objects.get_or_create(
            email=user_data["email"],
            defaults={
                "password": make_password("1234"),
                "first_name": user_data["first_name"],
                "last_name": user_data["last_name"],
                "role": user_data["role"],
                "is_active": True,
            }
        )
        
        if created:
            print(f'El usuario {user.email} Se creo exitosamente')
        else:
            print(f"El usuario {user.email} ya existia")
            
            
    



class Command(BaseCommand):
    help = "Your custom command"
    
    def handle(self, *args, **kwargs):
        
        init_data()
        
        
        # Verificar que existan grados y materias
        if not Degree.objects.exists():
            self.stdout.write(
                self.style.ERROR('No hay grados creados. Primero crea algunos grados.')
            )
            return
        
        if not Subject.objects.exists():
            self.stdout.write(
                self.style.ERROR('No hay materias creadas. Primero crea algunas materias.')
            )
            return

        tutores_creados = 0
        
        for i in range(10, 60):
            try:
                # Crear usuario
                email = f"tutor{i}@ejemplo.com"
                
                # Verificar si el usuario ya existe
                if CustomUser.objects.filter(email=email).exists():
                    continue
                
                # Datos de prueba
                nombres = [
                    'Ana', 'Facundo', 'María', 'Juan', 'Laura', 'Cecilia', 'Sofía', 
                    'Trinidad', 'Nahir', 'Lucas'
                ]
                
                apellidos = ['Gómez', 'López', 'Martínez', 'Rodríguez', 'Pérez', 'García', 'Fernández', 'Díaz']
                cellphone = f"+54 9 351 543-76{i}"
                direccion = f"Av. Siempre Viva 1{i}"
                
                user = CustomUser.objects.create_user(
                    email=email,
                    password='1234',  # Contraseña por defecto
                    first_name=random.choice(nombres),
                    last_name=random.choice(apellidos),
                    cellphone=cellphone,
                    province='Córdoba',
                    address=direccion,
                    role='tutor'
                )
                
                # Crear tutor
                tutor = Tutor.objects.create(user=user)
                
                precios = []
                for i in range(5000, 10001, 500):
                    precios.append(i)
                
                # Asignar 1-3 materias aleatorias al tutor
                materias = Subject.objects.order_by('?')[:random.randint(1, 3)]
                for materia in materias:
                    MateriaTutor.objects.create(
                        tutor=tutor,
                        materia=materia,
                        modalidad=random.choice(['virtual', 'hibrido', 'presencial']),
                        año_promocion=random.randint(2015, 2024),
                        verificado=random.choice([True, False]),
                        precio=float(random.choice(precios))
                    )
                
                tutores_creados += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Tutor creado: {user.email}')
                )
                
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Error creando tutor {i}: {str(e)}')
                )
        
        self.stdout.write(
            self.style.SUCCESS(f'Se crearon {tutores_creados} tutores exitosamente')
        )
        
        
        # Your code command
        
        
        
        
# To run it, use the console -> python manage.py name_command
def stupid_slug():
    degree, _ = Degree.objects.get_or_create(
        name='Ciencias básicas',
    )
    
    degrees = Degree.objects.all()
    subjects = Subject.objects.all()
    for degree in degrees:
        degree.slug = slugify(degree.name)
        degree.save()
        print(degree.slug)
        
    for degree in subjects:
        degree.slug = slugify(degree.name)
        degree.save()
        print(degree.slug)

