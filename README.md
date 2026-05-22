<!DOCTYPE html>
<html lang="es-AR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README - Help_U - TPI Análisis de Sistemas</title>
</head>
<body>

<h1>Help_U 🙌<small>TPI · Análisis de Sistemas</small></h1>

<p><strong> Facultad · Trabajo práctico integrador · MVP funcional</strong></p>

<p>Plataforma de ayuda entre estudiantes: podés publicar consultas, ofrecer respuestas y calificar. Hecho con Django + DRF + JavaScript vainilla. Estructura real: home, posts, reviews y users.</p>

<hr />

<h2>📁 Estructura real del proyecto (desde tu repo)</h2>

<pre><code>tpi_asi/
├── manage.py
├── db.sqlite3
├── requirements.txt (inferido)
├── home/              # app principal, landing + vistas generales
├── posts/             # lógica de publicaciones (preguntas / ofertas)
├── reviews/           # sistema de valoraciones y comentarios
├── users/             # perfiles, autenticación, registro
├── static/            # CSS, JS vainilla, assets
└── templates/         # SSR con Django Template Language
</code></pre>

<p><strong>Apps incluidas:</strong> home · posts · reviews · users</p>

<p>Tal como figura en tu commit inicial: <strong>help_u, home, posts, reviews, static, users</strong> — ese es el esqueleto real del TP.</p>

<hr />

<h2>Stack técnico (usado en el proyecto)</h2>

<ul>
    <li>Django</li>
    <li>Django REST Framework (DRF)</li>
    <li>SSR + Templates DTL</li>
    <li>JavaScript Vanilla (ES6)</li>
    <li>SQLite (db.sqlite3 incluida)</li>
    <li>CSS + Bootstrap custom</li>
    <li>Autenticación por sesiones</li>
    <li>Fetch API para interacciones dinámicas</li>
</ul>

<p>Según los archivos y la estructura, combina renderizado del lado del servidor (home, posts, users) con pedidos asincrónicos vía DRF + JS vainilla para ciertas acciones (dar likes, enviar reseñas).</p>

<hr />

<h2>Funcionalidades del MVP (por app)</h2>

<ul>
<li><strong>home</strong> → landing page, vista de inicio, posible feed de últimos posts o resumen.</li>
<li><strong>posts</strong> → ABM de publicaciones: los estudiantes pueden crear posts pidiendo ayuda o compartiendo conocimiento, comentarios y reacciones básicas.</li>
<li><strong>reviews</strong> → sistema de valoraciones: después de interactuar, se puede dejar una reseña al usuario (estrella + texto).</li>
<li><strong>users</strong> → registro, login, perfil público, listado de otros estudiantes.</li>
</ul>

<p><strong>Integración:</strong> Los posts pueden tener reseñas asociadas. Los usuarios acumulan reputación según las reviews que reciben en sus publicaciones/respuestas. Es un foro de ayuda académica clásico pero funcional.</p>

<hr />

<h2>Contexto académico</h2>

<p><strong>Materia:</strong> Análisis de Sistemas<br />
<strong>Comisión:</strong> TPI (Trabajo Práctico Integrador)<br />
<strong>Autor:</strong> Lucas Callamullo</p>

<p>Este repositorio es la implementación de un <strong>MVP (Producto Mínimo Viable)</strong> que simula una plataforma colaborativa entre estudiantes. El objetivo principal era demostrar la capacidad de construir una aplicación web con autenticación, lógica de negocio clara (posts + reseñas) y una API básica para operaciones asincrónicas.</p>

<p>Se priorizó el uso de <strong>Django + DRF</strong> para el backend y <strong>JavaScript vainilla</strong> para mejorar la experiencia sin agregar frameworks pesados. Ideal para mostrar en la facultad la separación de capas y la comunicación cliente-servidor.</p>

<hr />

<h2>API endpoints (DRF) incluidos</h2>

<ul>
<li><code>/api/posts/</code> → listado, creación, detalle de publicaciones</li>
<li><code>/api/reviews/</code> → enviar y obtener reseñas de un usuario/post</li>
<li><code>/api/users/</code> → información de perfiles y ranking (según reviews)</li>
</ul>

<p>Por la estructura del TP, se usaron <code>ViewSets</code> o <code>APIViews</code> para consumir desde el fetch de JS vainilla.</p>

<hr />

<h2>Cómo correr el proyecto (local)</h2>

<pre><code>git clone https://github.com/LucasCallamullo/tpi_asi.git
cd tpi_asi
python -m venv venv
source venv/bin/activate   # o venv\Scripts\activate en Windows
pip install django djangorestframework
python manage.py migrate
python manage.py runserver
</code></pre>

<p>→ Abrir <a href="http://127.0.0.1:8000">http://127.0.0.1:8000</a> 🚀</p>

<p><strong>Usuario demo:</strong> Podés crear un superusuario con <code>python manage.py createsuperuser</code> o revisar si hay un fixture precargado en la app <code>users</code>.</p>

<hr />

<h2>Estado del repo (según GitHub)</h2>

<ul>
<li><strong>Lenguajes:</strong> HTML 37%, JavaScript 26.2%, CSS 21.2%, Python 15.6%</li>
<li><strong>Commit inicial:</strong> Nov 19, 2025 (first commit de la materia)</li>
<li><strong>Estructura funcional:</strong> incluye static, templates, y cada app con su lógica.</li>
<li><strong>Estado:</strong> MVP para entrega académica, sin despliegue en producción (se puede hacer en Railway o PythonAnywhere).</li>
</ul>

<p>No tiene releases ni documentación extendida, pero el código está completo para cumplir con el trabajo práctico.</p>

<hr />

<p><strong>README generado en HTML semántico para conversión a Markdown.</strong><br />
🧉 Trabajo práctico integrador · Análisis de Sistemas · Código educativo.</p>

</body>
</html>