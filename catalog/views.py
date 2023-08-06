from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, CreateView
from django import forms
from catalog.models import Product
from catalog.forms import ProductForm


class CatalogListView(ListView):
    model = Product
    template_name = 'main/home.html'
    success_url = reverse_lazy('catalog:home')


class Contacts(forms.Form):
    name = forms.CharField()


class ContactsFormView(FormView):
    template_name = 'main/contacts.html'
    form_class = Contacts
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        return super().form_valid(form)


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'main/product_form.html'
    success_url = reverse_lazy('catalog:home')




