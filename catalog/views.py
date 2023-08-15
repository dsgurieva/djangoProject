from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, CreateView, UpdateView
from django import forms
from catalog.models import Product, Version, Category
from catalog.forms import ProductForm, VersionForm
from django.shortcuts import render
from django.core.cache import cache
from djangoProject import settings


def categories(request):
    if settings.CACHE_ENABLED:
        key = 'categori_list'
        category_list = cache.get(key)
        if category_list is None:
            category_list = Category.objects.all()
            cache.set(key, category_list)
    else:
        category_list = Category.objects.all()

    context = {
        'object_list': category_list,
        'title': 'Все категории наших товаров'
    }
    return render(request, 'main/categories.html', context)


class CatalogListView(LoginRequiredMixin, ListView):
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


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'main/product_form.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
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


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].user:
            return self.handle_no_permission()
        return kwargs












