


from django.urls import path

from home import views


urlpatterns = [
    path('', views.home, name="Home"),
    path('about-us', views.about_us, name="About-Us"),
    path('casos-uso', views.casos_uso, name="Casos-Uso"),
    path('alcances', views.alcances, name="Alcances"),
]