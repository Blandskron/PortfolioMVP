# 🛠️ MVP Portafolio Personal en Django

Este proyecto es un **MVP (Producto Mínimo Viable)** de un portafolio desarrollado con **Django**, que incluye tanto el **frontend como el backend en un solo repositorio**.

### 🚀 Características

- Autenticación de usuarios (`accounts`)
- Blog personal (`blog`)
- Página de contacto funcional (`contact`)
- Página de inicio (`home`)
- Proyectos desarrollados (`proyectos`)
- Portafolio visual (`portfolio`)
- Páginas de error personalizadas (`error_pages`)
- Archivos estáticos (`static`) y plantillas (`templates`) organizadas
- Script de carga para posts (`load_posts.py`)

### 🧩 Tecnologías utilizadas

- **Python 3**
- **Django 4+**
- HTML + CSS (con posible integración JS)
- SQLite (puede adaptarse a PostgreSQL fácilmente)

### 📦 Estructura del proyecto

```

.
├── accounts/
├── blog/
├── contact/
├── error\_pages/
├── home/
├── portfolio/
├── proyectos/
├── static/
├── templates/
├── load\_posts.py
└── manage.py

````

### ▶️ Cómo ejecutar

```bash
# Crear entorno virtual
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Migraciones y servidor
python manage.py migrate
python manage.py runserver
````

### 🌐 Resultado esperado

* Navegación fluida entre secciones (Inicio, Blog, Portafolio, Contacto)
* Administración completa desde el panel de Django (`/admin`)
* Diseño responsive y moderno

---

📌 Este MVP es ideal para desarrolladores que quieren tener su **portafolio listo para producción** rápidamente, **sin depender de frameworks externos de frontend**.

---

¿Te sirvió? ⭐ ¡Dale star y sígueme para más proyectos útiles!

