from django.forms import BaseForm, Textarea, DateField, DateTimeField, TimeField
from django import forms

class FieldDjango():
    def charFile():
        return serialize_form(forms.CharField())


def serialize_form(form: 'BaseForm'):
    result = []
    for key, value in form.fields.items():
        field = {
            'name': key,
            'disabled': value.disabled,
            'required': value.required,
            'label': value.label,
            'help_text': value.help_text,
            **value.widget.attrs,
        }
        
        if key in form.initial:
            field['value'] = form.initial[key]
        if type(value.widget) is Textarea:
            field['type'] = 'textarea'
        elif type(value) is DateField:
            field['type'] = 'date'
        elif type(value) is DateTimeField:
            field['type'] = 'datetime'
        elif type(value) is TimeField:
            field['type'] = 'time'
        elif value.widget.is_hidden:
            field.type = 'hidden'
        else:
            field['type'] = value.widget.input_type
        if field['type'] == 'select' or field['type'] == 'radio':
            field['choices'] = [c for c in value.widget.choices]
            field['multiple'] = value.widget.allow_multiple_selected

        # if field['type'] == 'select' or field['type'] == 'radio' or field['type'] == 'checkbox':
        #     field['choices'] = [c for c in value.choices]
        #     # field['choices'] = [(c[0].value, c[1]) if c[0] else c for c in value.choices]
        #     field['multiple'] = value.widget.allow_multiple_selected
        elif field['type'] == 'number':
            if hasattr(value, 'decimal_places'):
                field.update({'decimal_places': value.decimal_places, 'max_digits': value.max_digits})
            if value.max_value is not None:
                field['max'] = value.max_value
            if value.min_value is not None:
                field['min'] = value.min_value
        elif field['type'] == 'datetime':
            if field['type'] in ['text', 'textarea']:
                if value.max_length is not None:
                    field['maxlength'] = value.max_length
                if value.min_length is not None:
                    field['minlength'] = value.min_length
        result.append(field)
    return result