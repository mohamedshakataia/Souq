import django_filters
from .models import jumia

class ProductFilter(django_filters.FilterSet):
    manufacture = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = jumia
        fields = ['manufacture' ,'category']