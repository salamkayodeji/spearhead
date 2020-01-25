import django_filters
from .models import Category

class Categoryfilter(django_filters.FilterSet):

    class Meta:
        model = Category
        fields = ('category',)
        #30m by 30m