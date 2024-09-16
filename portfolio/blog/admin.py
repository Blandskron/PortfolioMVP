from django.contrib import admin
from .models import Post

# Registrar el modelo Post en el panel de administración
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')  # Mostrar estos campos en la lista del admin
    search_fields = ('title', 'content')  # Habilitar búsqueda por título y contenido
    list_filter = ('created_at',)  # Filtro por fecha de creación
    date_hierarchy = 'created_at'  # Navegación jerárquica por fecha
