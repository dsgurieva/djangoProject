from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, CreateView, UpdateView
from django import forms
from catalog.models import Product, Version
from catalog.forms import ProductForm, VersionForm


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


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'main/product_form.html'
    success_url = reverse_lazy('catalog:home')


    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data


    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)








