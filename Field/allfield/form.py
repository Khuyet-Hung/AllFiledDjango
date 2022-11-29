from django.forms import *
from . import models

list_select = (
        ('1', 'Hello'),
        ('2', 'World'),
    )

class FieldForm(ModelForm):
    class Meta:
        model = models.Field
        fields = '__all__'
        widgets = {
            'boolean_field' : CheckboxInput(),
            'select_muitiple_filed' : SelectMultiple(choices=list_select)
        }
