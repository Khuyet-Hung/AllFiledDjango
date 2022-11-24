from django.forms import CheckboxSelectMultiple, ModelForm, RadioSelect, SelectMultiple, Textarea
from . import models


# class EmployeeForm(ModelForm):
#     class Meta:
#         model = models.Employee
#         fields = '__all__'

# class FormDemo(ModelForm):
#     class Meta:
#         model = models.Employee
#         fields = '__all__'


class FieldForm(ModelForm):
    class Meta:
        model = models.Field
        fields = '__all__'
        widgets = {
            'boolean_field' : RadioSelect(),
            'select_muitiple_filed' : SelectMultiple()
        }
