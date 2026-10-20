from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Servicio
from .forms import ServicioForm
from django.core.paginator import Paginator


def inicio(request):
    info_bd = connection.settings_dict
    contexto = { 
        'motor': info_bd['ENGINE'],
        'host': info_bd['HOST'],
    }
    return render(request, 'core/inicio.html', contexto)


# @login_required: si no hay sesión, manda a LOGIN_URL en lugar de ejecutar la vista
@login_required
# servicios: la vista del listado, ahora con búsqueda y paginación
def servicios(request):
    # filter(propietario=request.user): solo los servicios del usuario actual (Semana 6)
    # order_by('-creado_en', '-id'): del más nuevo al más viejo; '-id' desempata si dos se crearon al mismo tiempo (paginar exige un orden fijo)
    lista_servicios = Servicio.objects.filter(propietario=request.user).order_by('-creado_en', '-id')
    # request.GET.get('q', ''): lee el texto buscado desde ?q=algo; '' si no hay búsqueda · strip() quita espacios sobrantes
    query = request.GET.get('q', '').strip()
    # si el usuario escribió algo en el buscador...
    if query:
        # titulo__icontains=query: WHERE titulo LIKE '%query%', sin distinguir mayúsculas/minúsculas
        lista_servicios = lista_servicios.filter(titulo__icontains=query)
    # Paginator(lista, 5): agrupa los resultados (ya filtrados) en páginas de 5 registros cada una
    paginator = Paginator(lista_servicios, 5)
    # request.GET.get('page'): lee el número de página desde la URL, ej. ?page=2
    numero_pagina = request.GET.get('page')
    # get_page(): devuelve la página pedida; si no es un número da la 1, y si se pasa del total da la última
    pagina = paginator.get_page(numero_pagina)
    # servicios: la página actual (se recorre igual que una lista) · query: para que el buscador recuerde lo escrito
    return render(request, 'core/servicios.html', {'servicios': pagina, 'query': query})

@login_required
def crear_servicio(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            nuevo = form.save(commit=False)
            nuevo.propietario = request.user
            nuevo.save()
            return redirect('servicios')
    else:
        form = ServicioForm()
    return render(request, 'core/servicio_form.html', {'form': form, 'titulo_pagina': 'Nuevo servicio'})


@login_required
def editar_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk, propietario=request.user)
    if request.method == 'POST':
        form = ServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            return redirect('servicios')
    else:
        form = ServicioForm(instance=servicio)
    return render(request, 'core/servicio_form.html', {'form': form, 'titulo_pagina': 'Editar servicio'})


@login_required
def eliminar_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk, propietario=request.user)
    if request.method == 'POST':
        servicio.delete()
        return redirect('servicios')
    return render(request, 'core/servicio_confirm_delete.html', {'servicio': servicio})


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario_nuevo = form.save()
            login(request, usuario_nuevo)
            messages.success(request, f'Cuenta creada. ¡Bienvenido, {usuario_nuevo.username}!')
            return redirect('servicios')
    else:
        form = UserCreationForm()
    return render(request, 'core/registro.html', {'form': form})


def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, 'Sesión iniciada correctamente.')
            return redirect('servicios')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})


def cerrar_sesion(request):
    logout(request)
    messages.info(request, 'Sesión cerrada correctamente.')
    return redirect('login')
