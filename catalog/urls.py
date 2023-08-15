from django.urls import path
from . import views
from catalog.apps import CatalogConfig
from catalog.views import CatalogListView, ContactsFormView, ProductCreateView, ProductUpdateView
from django.views.decorators.cache import cache_page

app_name = CatalogConfig.name

urlpatterns = [
    path('', cache_page(60) (CatalogListView.as_view()), name='home'),
    path("categories/", views.categories, name="categories"),
    path('contacts/', ContactsFormView.as_view(), name='contacts'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('create/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
]

