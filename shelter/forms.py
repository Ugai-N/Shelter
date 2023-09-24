from datetime import date, datetime

from django import forms

from shelter.models import Dog, Parent


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class DogForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Dog
        fields = '__all__'

    def clean_birth(self):
        cleaned_data = self.cleaned_data.get('birth')
        if datetime.now().year - cleaned_data.year > 100:
            raise forms.ValidationError('more than 100 years')
        return cleaned_data


class ParentForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Parent
        fields = '__all__'
