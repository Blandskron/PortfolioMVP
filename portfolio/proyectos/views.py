from django.shortcuts import render, redirect, get_object_or_404
from .models import Proyecto
from .forms import ProyectoForm
from django.contrib.auth.decorators import login_required

# Vista para mostrar todos los proyectos de un usuario autenticado
@login_required
def lista_proyectos(request):
    proyectos = Proyecto.objects.filter(usuario=request.user)
    return render(request, 'proyectos/lista_proyectos.html', {'proyectos': proyectos})

# Vista para crear un nuevo proyecto
@login_required
def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.usuario = request.user  # Asignar el usuario logueado
            proyecto.save()
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm()
    return render(request, 'proyectos/crear_proyecto.html', {'form': form})

# Vista para editar un proyecto
@login_required
def editar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm(instance=proyecto)
    return render(request, 'proyectos/editar_proyecto.html', {'form': form, 'proyecto': proyecto})

# Vista para eliminar un proyecto
@login_required
def eliminar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    proyecto.delete()
    return redirect('lista_proyectos')
