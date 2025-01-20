import os
import django
from django.utils import timezone

# Configura el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')  # Reemplaza 'portfolio.settings' por el nombre de tu archivo de configuración (settings.py)
django.setup()

# Ahora puedes importar tus modelos
from blog.models import Post  # Asegúrate de que 'blog' es el nombre correcto de tu aplicación

# Cargar datos de ejemplo
def load_data():
    posts_data = [
        {
            "title": "Introducción a Django",
            "content": "<p>Este es el contenido de un artículo sobre Django. Puedes incluir <strong>HTML</strong> aquí.</p>",
            "created_at": timezone.now(),
            "updated_at": timezone.now()
        },
        {
            "title": "Aprende Python",
            "content": "<p>Python es un lenguaje de programación versátil. ¡Vamos a explorar sus características!</p>",
            "created_at": timezone.now(),
            "updated_at": timezone.now()
        },
        {
            "title": "Machine Learning y AI",
            "content": "<p>El <em>Machine Learning</em> es el futuro de la tecnología. Este artículo te guiará por sus fundamentos.</p>",
            "created_at": timezone.now(),
            "updated_at": timezone.now()
        }
    ]
    
    for post_data in posts_data:
        post = Post.objects.create(
            title=post_data["title"],
            content=post_data["content"],
            created_at=post_data["created_at"],
            updated_at=post_data["updated_at"]
        )
        print(f"Post '{post.title}' creado con éxito.")

if __name__ == "__main__":
    load_data()
