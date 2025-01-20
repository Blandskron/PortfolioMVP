from django.shortcuts import render, redirect
from .forms import ContactoForm

def contacto_view(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exito')
    else:
        form = ContactoForm()
    return render(request, 'contact/contacto.html', {'form': form})

def exito_view(request):
    return render(request, 'contact/exito.html')