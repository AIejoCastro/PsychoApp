from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
import psychoapp.expertSystem as expertSystem
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterForm, UpdateUserForm
from django.contrib.auth.decorators import login_required
from .models import HistorialResultado
from datetime import datetime
from django.contrib.auth.models import User

from .models import user_collection

def index(request):
    doc_index = open("psychoApp/templates/index.html")
    template = Template(doc_index.read())
    doc_index.close()
    context = Context()
    doc = template.render(context)
    return render(request, 'index.html', {'user': request.user})

def about(request):
    doc_index = open("psychoApp/templates/about.html")
    template = Template(doc_index.read())
    doc_index.close()
    context = Context()
    doc = template.render(context)
    return HttpResponse(doc)

def chat(request):
    doc_index = open("psychoApp/templates/chat.html")
    template = Template(doc_index.read())
    doc_index.close()
    context = Context()
    doc = template.render(context)
    return HttpResponse(doc)

@csrf_exempt
def process_symptoms(request):
    if request.method == 'POST':
        selected_buttons = request.POST.get('selected_buttons').split(',')
        symptoms_dict = {
            'hiperventilacion': 1 if '1' in selected_buttons else 0,
            'llanto_incontenible': 1 if '2' in selected_buttons else 0,
            'agresividad': 1 if '3' in selected_buttons else 0,
            'abuso_de_sustancias': 1 if '4' in selected_buttons else 0,
            'distorsion_de_la_realidad': 1 if '5' in selected_buttons else 0,
            'ideas_de_autolesion': 1 if '6' in selected_buttons else 0,
            'temblores': 1 if '7' in selected_buttons else 0,
            'sudoracion': 1 if '8' in selected_buttons else 0,
            'pitido': 1 if '9' in selected_buttons else 0,
            'nubla_de_vision': 1 if '10' in selected_buttons else 0,
            'palpitaciones_rapidas': 1 if '11' in selected_buttons else 0,
            'vomito': 1 if '12' in selected_buttons else 0,
            'abstinencia': 1 if '13' in selected_buttons else 0,
            'agresion_a_otros': 1 if '14' in selected_buttons else 0
        }

        result = expertSystem.start(
            symptoms_dict['hiperventilacion'],
            symptoms_dict['llanto_incontenible'],
            symptoms_dict['agresividad'],
            symptoms_dict['abuso_de_sustancias'],
            symptoms_dict['distorsion_de_la_realidad'],
            symptoms_dict['ideas_de_autolesion'],
            symptoms_dict['temblores'],
            symptoms_dict['sudoracion'],
            symptoms_dict['pitido'],
            symptoms_dict['nubla_de_vision'],
            symptoms_dict['palpitaciones_rapidas'],
            symptoms_dict['vomito'],
            symptoms_dict['abstinencia'],
            symptoms_dict['agresion_a_otros']
        )

        if request.user.is_authenticated:
            historial = HistorialResultado(
                usuario=request.user,
                sintomas=','.join(selected_buttons),
                resultado=result['resultado']
            )
            historial.save()

            mongo_historial = {
                "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "sintomas": selected_buttons,
                "resultado": result['resultado']
            }
            user_collection.update_one(
                {"usuario_id": request.user.id},
                {"$push": {"historial": mongo_historial}}
            )

        return render(request, 'result_page.html', {'selected_buttons': selected_buttons, 'result': result})
    
    return render(request, 'your_template.html')

@login_required
def ver_historial(request):
    historial = HistorialResultado.objects.filter(usuario=request.user).order_by('-fecha')
    return render(request, 'see_history.html', {'historial': historial})

@login_required
def eliminar_historial(request, id):
    if request.method == "POST":
        entry = get_object_or_404(HistorialResultado, id=id)
        entry.delete()
        return redirect('ver_historial')
    return HttpResponse(status=405)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')  
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )

            mongo_user = {
                "usuario_id": user.id,
                "username": user.username,
                "email": user.email,
                "password": user.password,
                "fecha_nacimiento": datetime.combine(
                    form.cleaned_data['fecha_nacimiento'], datetime.min.time()
                ),
                "direccion": form.cleaned_data['direccion'],
                "telefono": form.cleaned_data['telefono'],
                "antecedentes_medicos": form.cleaned_data['antecedentes_medicos'],
                "medicamentos_actuales": form.cleaned_data['medicamentos_actuales'],
                "alergias": form.cleaned_data['alergias'],
                "contacto_emergencia": form.cleaned_data['contacto_emergencia'],
                "telefono_emergencia": form.cleaned_data['telefono_emergencia'],
                "historial": [],
            }
            user_collection.insert_one(mongo_user)

            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def edit_user(request):
    user = request.user  # Usuario actual
    mongo_user = user_collection.find_one({"usuario_id": user.id})  # Datos en MongoDB
    
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=user)
        if form.is_valid():
            # Actualizar información en el modelo User
            form.save()

            # Actualizar información en MongoDB
            user_collection.update_one(
                {"usuario_id": user.id},
                {
                    "$set": {
                        "direccion": form.cleaned_data['direccion'],
                        "telefono": form.cleaned_data['telefono'],
                        "antecedentes_medicos": form.cleaned_data['antecedentes_medicos'],
                        "medicamentos_actuales": form.cleaned_data['medicamentos_actuales'],
                        "alergias": form.cleaned_data['alergias'],
                        "contacto_emergencia": form.cleaned_data['contacto_emergencia'],
                        "telefono_emergencia": form.cleaned_data['telefono_emergencia'],
                    }
                }
            )
            return redirect('home')
    else:
        initial_data = {
            "direccion": mongo_user.get("direccion", ""),
            "telefono": mongo_user.get("telefono", ""),
            "antecedentes_medicos": mongo_user.get("antecedentes_medicos", ""),
            "medicamentos_actuales": mongo_user.get("medicamentos_actuales", ""),
            "alergias": mongo_user.get("alergias", ""),
            "contacto_emergencia": mongo_user.get("contacto_emergencia", ""),
            "telefono_emergencia": mongo_user.get("telefono_emergencia", ""),
        }
        form = UpdateUserForm(instance=user, initial=initial_data)

    return render(request, 'edit_user.html', {'form': form})