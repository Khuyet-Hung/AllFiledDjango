from django.forms import CheckboxSelectMultiple, ModelForm, RadioSelect, SelectMultiple, Textarea
from django  import forms
from . import models


class FieldForm(ModelForm):
    class Meta:
        model = models.Field
        fields = '__all__'
        widgets = {
            'boolean_field' : RadioSelect(),
            'select_muitiple_filed' : SelectMultiple()
        }
