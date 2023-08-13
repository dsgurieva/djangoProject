from django import forms
from catalog.models import Product, Version
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        #fields = '__all__'
        exclude = ('user',)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in forbidden_words:
            if word in name.lower() or word in description.lower():
                raise ValidationError(f"Слово '{word}' недопустимо в названии или описании.")


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
