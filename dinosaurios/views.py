from django.shortcuts import render, redirect
from .models import Periodo, Dinosaurio
from .forms import PeriodoForm, DinoForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

#class NuevoDino(LoginRequiredMixin, CreateView):
class NuevoDino(CreateView):
    model = Dinosaurio
    form_class = DinoForm
    success_url = reverse_lazy('lista_dinos')

#class ListaDino(PermissionRequiredMixin, ListView):
class ListaDino(ListView):
    model = Dinosaurio
    #permission_required = 'dinosaurios.view_dinosaurio'
    
class EliminaDinos(DeleteView):
    model = Dinosaurio
    success_url = reverse_lazy('lista_dinos')


class ActualizaDinos(UpdateView):
    form_class = DinoForm
    model = Dinosaurio
    success_url = reverse_lazy('lista_dinos')
    template_name = 'dinosaurios/dinosaurio_edit.html' 

def eliminar_periodo(request, id):
    try:
        periodo = Periodo.objects.get(pk=id)
        periodo.delete()
        return redirect('lista_periodo')
    except Periodo.DoesNotExist:
        periodos = Periodo.objects.all()
        nombre ="T-REX"
        context={'periodos': periodos,'nombre':nombre,'error':'No se pudo encontrar el periodo'}
        return render(request, 'periodos.html',context)

def editar_periodo(request, id):
    periodo = Periodo.objects.get(pk=id)
    if request.method == 'POST':
        form = PeriodoForm(request.POST, instance=periodo)
        if form.is_valid():
            form.save()
            return redirect('lista_periodo')
    else:
        form = PeriodoForm(instance=periodo)
    return render(request, 'editar.html', {'form':form}) 

def agregar_periodo(request):
    if request.method == 'POST':
        form = PeriodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_periodo')
    else:
        form = PeriodoForm()

    form = PeriodoForm()
    return render(request, 'nuevo.html', {'form':form}) 

def agregar_dino(request):
    context = {'app':'Dinosaurio','nuevo':True}
    if request.method == 'POST':
        form = DinoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_periodo')
    else:
        form = DinoForm()

    form = DinoForm()
    return render(request, 'nuevo.html', {'form':form}) 

def lista_periodo(request):
    periodos = Periodo.objects.all()
    nombre = "T-REX"
    context = {'periodos':periodos, 'nombre':nombre}
    #return render(request, 'periodos.html',{'nombre':nombre})
    return render(request, 'periodos.html',context)
