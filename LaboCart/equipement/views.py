import io
from django.shortcuts import render, redirect, get_object_or_404
from .forms import MatriceForm
from equipement.models import Equipement, DocEquipement, Matrice
from equipement.form import EquipForm, Equip_Img_Form, Equip_pdf_Form
from django.core import serializers
from django.http import JsonResponse
from django.contrib import messages
import pandas as pd
from .models import Matrice
from django.shortcuts import render, redirect
import pandas as pd
import io
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.encoding import smart_str
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import logging
import pandas as pd
from django.http import HttpResponse
from .models import Matrice, Equipement
from django.db.models import Q
from django.http import HttpResponse
from io import BytesIO
from fpdf import FPDF
from .models import Equipement, Matrice
from django.http import HttpResponse
import pandas as pd

import os

# Create a logger instance
logger = logging.getLogger(__name__)

def public_test(request):
    return HttpResponse("This is a public page")


def home(request):
    return render(request, 'cart.html', {})

def equipement_detail2(request, name):
    emplacements = Equipement.objects.filter(Emplacement__startswith='Laboratoire de cont')
    equipement=emplacements.filter( Appareil__startswith = name)
    return render(request, 'equip_detail2.html', {'equipement':equipement})

def equipement_detail1(request, name):
    emplacements = Equipement.objects.filter(Emplacement__startswith='Laboratoire Micro')
    equipement=emplacements.filter( Appareil__startswith = name)
    return render(request, 'equip_detail1.html', {'equipement':equipement})

def appareil_detail(request, app_id):
    appareil=Equipement.objects.get(Num=app_id)
    image_appareil = DocEquipement.objects.filter(equipement=appareil)
    return render(request, 'appareil-detail.html', {'appareil':appareil, 'image_appareil': image_appareil})

def voirPhysico(request):
    return render(request, 'labo2.html', {})

def voirChimio(request):
    return render(request, 'labo1.html', {})

def vEquipp(request):
    return render(request, 'equip2.html', {})

def vEquipc(request):
    return render(request, 'equip1.html', {})

def Equip_update(request, app_id):
    equipement = Equipement.objects.get(id= app_id)

    if request.method == 'POST':
        form = EquipForm(request.POST, instance=equipement)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('appareil-detail', equipement.id)
    else:
        form = EquipForm(instance=equipement)

    return render(request, 'Update_appareil.html', {'form': form, 'appareil':equipement})


def Equip_Img_update(request, app_id):
    equipement = Equipement.objects.get(id= app_id)
    #image_appareil = get_object_or_404(ImageEquipements, equipement=equipement)
    if request.method == 'POST':
        form = Equip_Img_Form(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.equipement = equipement
            image.image = request.FILES['image']
            image.save()
            return redirect('appareil-detail', equipement.id)
    else:
        form = Equip_Img_Form(initial_equipement=equipement)

    return render(request, 'Update_app_Img.html', {'form': form, 'appareil':equipement})

def Equip_pdf_update(request, app_id):
    equipement = Equipement.objects.get(id= app_id)
    #image_appareil = get_object_or_404(ImageEquipements, equipement=equipement)
    if request.method == 'POST':
        form = Equip_pdf_Form(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.equipement = equipement
            image.pdf = request.FILES['pdf']
            image.save()
            return redirect('appareil-detail', equipement.id)
    else:
        form = Equip_pdf_Form(initial_equipement=equipement)

    return render(request, 'Update_app_pdf.html', {'form': form, 'appareil':equipement})

def replace_image(request, image_id):
    image = get_object_or_404(DocEquipement, id=image_id)
    
    if request.method == 'POST':
        form = Equip_Img_Form(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('appareil-detail', app_id=image.equipement.id)
    else:
        form = Equip_Img_Form(instance=image)
    
    return render(request, 'replace_image.html', {'form': form, 'image': image})

def Update_img(request, app_id):
    appareil=Equipement.objects.get(Num=app_id)
    image_appareil = DocEquipement.objects.filter(equipement=appareil)
    return render(request, 'Update_img.html', {'appareil':appareil, 'image_appareil': image_appareil})

def matrice_detail(request, app_id):
    appareils = Equipement.objects.all()
    selected_group = None
    if request.method == 'POST':
        selected_group = request.POST.get('group')

    if selected_group:
        if selected_group == '1':
            appareil = appareils.filter(Appareil__contains='HPLC')
        elif selected_group == '2':
            appareil = appareils.filter(Appareil__contains='Spectrophotomètre')
        elif selected_group == '3':
            appareil = appareils.filter(Appareil__contains='Balance')
        elif selected_group == '4':
            appareil = appareils.filter(Appareil__contains='Enceinte climatique') | appareils.filter(Appareil__contains='Chambre climatique')
        else:
            appareil = appareils.filter(Emplacement__startswith='Laboratoire Micro')
    else:
        appareil = appareils  # Return all appareils if no group selected

    app = Equipement.objects.get(pk=app_id)
    matrice = Matrice.objects.filter(equipement=app)
    # print(matrice)
    return render(request, 'matrice.html', {'appareil': appareil, 'matrice': matrice})





def matrice_pagel(request):
    # appareils = Equipement.objects.filter(Password__iexact='oui')
    appareils = Equipement.objects.all()

    if request.method == 'POST':
        selected_group = request.POST.get('group')
        
        if selected_group:
            if selected_group == '1':
                appareil = appareils.filter(Appareil__contains='HPLC')
            elif selected_group == '2':
                appareil = appareils.filter(Appareil__contains='Spectrophotomètre')
            elif selected_group == '3':
                appareil = appareils.filter(Appareil__contains='Balance')
            elif selected_group == '4':
                appareil = appareils.filter(Appareil__contains='Enceinte climatique') | appareils.filter(Appareil__contains='Chambre climatique')
            elif selected_group == '5':
                appareil = appareils.filter(Emplacement__startswith='Laboratoire Micro')
            elif selected_group == 'autre':
                appareil = appareils.filter(
                    ~Q(Appareil__contains='HPLC') & 
                    ~Q(Appareil__contains='Spectrophotomètre') & 
                    ~Q(Appareil__contains='Balance') & 
                    ~Q(Appareil__contains='Enceinte climatique') & 
                    ~Q(Emplacement__startswith='Laboratoire Micro')
                )
            else:
                appareil = []
        else:
            appareil = []
        
        return render(request, 'matrice_page.html', {'appareil': appareil})
    
    return render(request, 'matrice_page.html', {})


def recherhce(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        appareils=Equipement.objects.filter(Appareil__contains= searched) | Equipement.objects.filter(Code_machine__contains= searched)
        if appareils:
            return render(request, 'recherche.html', {'appareils':appareils})
        messages.success(request,("Le mot que vous avez écris ne correspond à aucun équipement, merci de retester avec un autre mots clé!"))
        return render(request, 'cart.html')
    


def upload_excel(request, equipement_id):
    if request.method == 'POST' and 'excel_file' in request.FILES:
        excel_file = request.FILES['excel_file']
        
        # Use pandas to read the Excel file
        df = pd.read_excel(excel_file)

        # Iterate over rows in the DataFrame and save data to the database
        for index, row in df.iterrows():
            equipement = Equipement.objects.get(pk=equipement_id)
            print(row['login'], row['Nom'], row['Prenom'], row['Role'], row['Situation'], equipement)
            matrice = Matrice(
                login=row['login'],
                Nom=row['Nom'],
                Prenom=row['Prenom'],
                Role=row['Role'],
                Situation=row['Situation'],
                equipement=equipement
            )
            matrice.save()

    # Fetch all the Equipements with the password 'oui'
    appareil = Equipement.objects.filter(Password='oui') | Equipement.objects.filter(Password='Oui')
    
    # Get the Equipement object corresponding to the equipement_id
    app = Equipement.objects.get(pk=equipement_id)
    
    # Fetch all the Matrices associated with the Equipement
    matrice = Matrice.objects.filter(equipement=app)
    
    # Render the template with the retrieved data
    return render(request, 'matrice.html', {'appareil': appareil, 'matrice': matrice})



@csrf_exempt
def download_excel(request, equipement_id):
    # Fetch the Equipement object corresponding to the equipement_id
    equipement = Equipement.objects.get(pk=equipement_id)
    
    # Fetch all the Matrices associated with the Equipement
    matrice = Matrice.objects.filter(equipement=equipement)
    
    # Create a DataFrame from the Matrice data
    data = {
        'login': [m.login for m in matrice],
        'Nom': [m.Nom for m in matrice],
        'Prenom': [m.Prenom for m in matrice],
        'Role': [m.Role for m in matrice],
        'Situation': [m.Situation for m in matrice],
    }
    df = pd.DataFrame(data)
    
    # Create a BytesIO object to store the Excel file
    excel_buffer = io.BytesIO()
    
    # Write the DataFrame to the BytesIO object as an Excel file
    df.to_excel(excel_buffer, index=False)
    
    # Set the appropriate response headers
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{equipement.Code_machine}.xlsx"'
    
    # Write the BytesIO content to the response
    response.write(excel_buffer.getvalue())
    
    return response






def add_matrice_line(request, equipement_id):
    if request.method == 'POST':
        form = MatriceForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            nom = form.cleaned_data['Nom']
            prenom = form.cleaned_data['Prenom']
            role = form.cleaned_data['Role']
            situation = form.cleaned_data['Situation']
        
            matrice = Matrice(
                login=login,
                Nom=nom,
                Prenom=prenom,
                Role=role,
                Situation=situation,
                equipement_id=equipement_id  # Associate the matrice with the equipment
            )

            matrice.save()

            # Fetch all the Equipements with the password 'oui'
            appareil = Equipement.objects.filter(Password='oui') | Equipement.objects.filter(Password='Oui')
            
            # Get the Equipement object corresponding to the equipement_id
            app = Equipement.objects.get(pk=equipement_id)
            
            # Fetch all the Matrices associated with the Equipement
            matrice = Matrice.objects.filter(equipement=app)
            
            # Render the template with the retrieved data
            return render(request, 'matrice.html', {'appareil': appareil, 'matrice': matrice})

    else:
        form = MatriceForm()
    return render(request, 'add_matrice.html', {
        'form': MatriceForm(),
        'equipement_id': equipement_id
    })

def edit_retour(request, matrice_line_id):
    matrice = Matrice.objects.get(pk=matrice_line_id)
    return redirect('matrice_detail', matrice.equipement.id)



def edit(request, matrice_line_id):
    matrice = Matrice.objects.get(pk=matrice_line_id)
    if request.method == 'POST':
        form = MatriceForm(request.POST, instance=matrice)
        if form.is_valid():
            form.save()
            return redirect('matrice_detail', matrice.equipement.id)
    else:
        form = MatriceForm(instance=matrice)
    return render(request, 'edit_matrice.html', {'form': form, 'matrice': matrice})




def delete(request, matrice_line_id):
    matrice = Matrice.objects.get(pk=matrice_line_id)   
    matrice.delete()
    appareil = Equipement.objects.filter(Password='oui') | Equipement.objects.filter(Password='Oui')
            
            # Get the Equipement object corresponding to the equipement_id
    app = Equipement.objects.get(pk=matrice.equipement.id)
            
            # Fetch all the Matrices associated with the Equipement
    matrice = Matrice.objects.filter(equipement=app)
            
            # Render the template with the retrieved data
    return render(request, 'matrice.html', {'appareil': appareil, 'matrice': matrice}) 


def delete_all_matrice(request, equipement_id):
    # Fetch the Equipement object corresponding to the equipement_id
    equipement = get_object_or_404(Equipement, pk=equipement_id)

    if request.method == 'POST':
        # Fetch all the Matrices associated with the Equipement
        matrices = Matrice.objects.filter(equipement=equipement)
        
        # Iterate over each matrix and delete it
        for matrice in matrices:
            matrice.delete()

        # Redirect to a success page or the same page
        return redirect('matrice_detail', equipement_id=equipement_id)

    appareil = Equipement.objects.filter(Password__iexact='oui')

    # Fetch all the Matrices associated with the Equipement
    matrices = Matrice.objects.filter(equipement=equipement)

    # Render the template with the retrieved data
    return render(request, 'matrice.html', {'appareil': appareil, 'matrice': matrices})

def exporter_liste(request):
    return render(request, 'exporter.html', {})


def contact(request):
    return render(request, 'contact.html', {})




# Create your views here.   
 
def all_equipments(request):
    all_equipments = Equipement.objects.all() 
    page = request.GET.get('page', 1)
  
    paginator = Paginator(all_equipments, 7)
    try:
        equipements = paginator.page(page)
    except PageNotAnInteger:
        equipements = paginator.page(1)
    except EmptyPage:
        equipements = paginator.page(paginator.num_pages)
  
    return render(request, 'all_equipments.html', { 'all_equipments': equipements })


def search_equipments(request):
    query = request.GET.get('search')
    if query:
        # Perform search query using filter
        all_equipments = Equipement.objects.filter(Code_machine__icontains=query)
    else:
        # If no search query, return an empty queryset
        all_equipments = Equipement.objects.all()

    # Paginate the results
    page = request.GET.get('page', 1)
    paginator = Paginator(all_equipments, 7)
    try:
        equipements = paginator.page(page)
    except PageNotAnInteger:
        equipements = paginator.page(1)
    except EmptyPage:
        equipements = paginator.page(paginator.num_pages)

    return render(request, 'all_equipments.html', {'all_equipments': equipements, 'query': query})


def add_equipement(request):
    all_equipments = Equipement.objects.all()
    if request.method == 'POST':
        form = EquipForm(request.POST)
        if form.is_valid():
            form.save()

            return render(request, 'all_equipments.html', {'all_equipments': all_equipments})  # Redirect to the list of all equipments
    else:
        form = EquipForm()
    return render(request, 'Add_equipement.html', {'form': form})



class PDF(FPDF):
    def header(self):
        # Insert the logo image in the top-right corner
        image_path = os.path.join(os.path.dirname(__file__), 'Pharma5.png')
        self.image(image_path, x=150, y=8, w=50)
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'les matrices d accés des équipements', 0, 1, 'C')
        self.ln(20)  # Add more space after the header

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def equipment_table(self, equipment, matrices):
        self.set_font('Arial', 'B', 12)
        title = f'Code Machine: {equipment.Code_machine} - Model: {equipment.modele}'
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)  # Add some space before the table
        self.set_font('Arial', 'B', 10)
        self.cell(30, 10, 'Login', 1)
        self.cell(30, 10, 'Nom', 1)
        self.cell(30, 10, 'Prenom', 1)
        self.cell(30, 10, 'Role', 1)
        self.cell(30, 10, 'Situation', 1)
        self.cell(40, 10, 'Date Modification', 1)
        self.ln()

        self.set_font('Arial', '', 10)
        for matrix in matrices:
            self.cell(30, 10, matrix.login, 1)
            self.cell(30, 10, matrix.Nom, 1)
            self.cell(30, 10, matrix.Prenom, 1)
            self.cell(30, 10, matrix.Role, 1)
            self.cell(30, 10, matrix.Situation, 1)
            self.cell(40, 10, str(matrix.date_modfication), 1)
            self.ln()
        self.ln()

def filter_equipment(selected_category):
    category_mapping = {
        'HPLC': 'HPLC',
        'Spectrophotomètre': 'Spectrophotomètre',
        'Balance': 'Balance',
        'climatique': 'Enceinte climatique',
        'Laboratoire Micro': 'Laboratoire Micro'
    }

    equipment_with_matrices = Equipement.objects.filter(matrice__isnull=False)

    if selected_category and selected_category in category_mapping:
        category = category_mapping[selected_category]
        equipment_with_matrices = equipment_with_matrices.filter(Appareil__icontains=category)
    elif selected_category == 'autre':
        for category_name in category_mapping.values():
            equipment_with_matrices = equipment_with_matrices.exclude(Appareil__icontains=category_name)

    return equipment_with_matrices

def generate_pdf(request):
    if request.method == 'POST':
        selected_category = request.POST.get('category')
        equipment_with_matrices = filter_equipment(selected_category)

        pdf = PDF()
        pdf.add_page()

        for equipment in equipment_with_matrices:
            matrices = Matrice.objects.filter(equipement=equipment)
            pdf.equipment_table(equipment, matrices)

        buffer = BytesIO()
        pdf.output(buffer)
        buffer.seek(0)

        filename = f"{selected_category}.pdf" if selected_category != 'all' else "all_equipements.pdf"
        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename={filename}'

        return response
    else:
        return HttpResponse("Invalid request method", status=400)




def filter_equipment(selected_category):
    category_mapping = {
        'HPLC': 'HPLC',
        'Spectrophotomètre': 'Spectrophotomètre',
        'Balance': 'Balance',
        'climatique': 'Enceinte climatique',
        'Laboratoire Micro': 'Laboratoire Micro'
    }

    equipment_with_matrices = Equipement.objects.filter(matrice__isnull=False)

    if selected_category and selected_category in category_mapping:
        category = category_mapping[selected_category]
        equipment_with_matrices = equipment_with_matrices.filter(Appareil__icontains=category)
    elif selected_category == 'autre':
        for category_name in category_mapping.values():
            equipment_with_matrices = equipment_with_matrices.exclude(Appareil__icontains=category_name)

    return equipment_with_matrices

def generate_excel(request):
    if request.method == 'POST':
        selected_category = request.POST.get('category')
        equipment_with_matrices = filter_equipment(selected_category)

        equipement_matrices = {}
        for equipment in equipment_with_matrices:
            matrices = Matrice.objects.filter(equipement=equipment)
            equipement_matrices[equipment] = matrices

        all_matrices_data = pd.DataFrame()
        for equipment, matrices in equipement_matrices.items():
            matrices_data = pd.DataFrame(list(matrices.values()))

            # Remove 'id' and 'equipement_id' columns if they exist
            if 'id' in matrices_data.columns:
                matrices_data = matrices_data.drop(columns=['id'])
            if 'equipement_id' in matrices_data.columns:
                matrices_data = matrices_data.drop(columns=['equipement_id'])

            header_data = {'Equipement': f'{equipment.Code_machine} - Model: {equipment.modele}'}
            matrices_data = pd.concat([pd.DataFrame([header_data]), matrices_data])
            all_matrices_data = pd.concat([all_matrices_data, matrices_data])

        if not all_matrices_data.empty:
            filename = f"{selected_category}.xlsx" if selected_category != 'all' else "all_matrices.xlsx"
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = f'attachment; filename={filename}'
            all_matrices_data.to_excel(response, index=False)
            return response
        else:
            return HttpResponse("No matrices found.")
    else:
        return HttpResponse("Invalid request method", status=400)

