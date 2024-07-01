from django import forms
from equipement.models import  Equipement, DocEquipement


class EquipForm(forms.ModelForm):
   def __init__(self, *args, **kwargs):
        super(EquipForm, self).__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            if field_name not in ['Appareil', 'Num', 'Emplacement']:  # Remplacez par les noms des champs que vous souhaitez rendre obligatoires
                field.required = False
   class Meta:
     model = Equipement
     fields = '__all__'


class Equip_pdf_Form(forms.ModelForm):
   def __init__(self, *args, **kwargs):
        initial_equipement = kwargs.pop('initial_equipement', None)
        super(Equip_pdf_Form, self).__init__(*args, **kwargs)
        if initial_equipement:
            self.fields['equipement'].initial = initial_equipement
        
   class Meta:
     model = DocEquipement
     fields = ['equipement', 'pdf']

class Equip_Img_Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        initial_equipement = kwargs.pop('initial_equipement', None)
        super(Equip_Img_Form, self).__init__(*args, **kwargs)
        if initial_equipement:
            self.fields['equipement'].initial = initial_equipement

    class Meta:
        model = DocEquipement
        fields = ['equipement', 'image']


# class ListingForm(forms.ModelForm):
#    class Meta:
#      model = Listing
#      #fields = '__all__'
#      exclude = ('sold',)