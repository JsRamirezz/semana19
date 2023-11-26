from django.shortcuts import render,redirect
from .formularios.registerform import NewUserForm
from .formularios.loginform import LoginForm
from .formularios.proveedorform import ProveedorForm
from .formularios.productoform import ProductoForm
from django.http import HttpResponseRedirect
from .models import Productos,Proveedores
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required, user_passes_test

def es_admin(user):
    return user.is_staff

@user_passes_test(es_admin, login_url="acceso_denegado")
def registrar_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registrar_proveedor')  
    else:
        form = ProveedorForm()

    return render(request, 'registrar_proveedor.html', {'form': form})


def mostrar_proveedores(request):
    proveedores = Proveedores.objects.all()
    return render(request, 'mostrar_proveedores.html', {'proveedores': proveedores})

@user_passes_test(es_admin, login_url="acceso_denegado")
def registrar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('error.html')  
        else:
            print(form.errors)  
    else:
        form = ProductoForm()

    return render(request, 'registrar_producto.html', {'form': form})


def mostrar_productos(request):
    productos = Productos.objects.all()
    return render(request, 'mostrar_productos.html', {'productos': productos})


def reg_user(request):
    if request.method == "POST":
        formulario = NewUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        return HttpResponseRedirect("/")
    else:
        formulario = NewUserForm()
        return render(request,"Reg_user.html",{"form":formulario})

@login_required(login_url='login')
def index(request):
    es_estudiante = request.user.groups.filter(name='Estudiante').exists()
    es_admin = request.user.is_staff
    if es_estudiante or es_admin:
        return render(request, 'index.html', {'user':request.user, 'es_estudiante': es_estudiante,'es_admin':es_admin})
    else:
        return render(request, 'index.html')


def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def cerrar_sesion(request):
    logout(request)
    return redirect('login')


def acceso_denegado(request):
    return render(request, 'error.html')

