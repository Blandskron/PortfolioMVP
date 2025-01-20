from django import template

register = template.Library()

@register.filter
def add_class(value, arg):
    """Agrega una clase CSS a un formulario en el template."""
    return value.as_widget(attrs={'class': arg})
