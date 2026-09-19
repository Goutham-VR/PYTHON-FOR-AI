import django_filters
from apiview.models import Product

#=====================================================================================================================================================
class ProductFilter(django_filters.FilterSet): # "Create a filter configuration for my Product model."
    class Meta:
        model=Product # Model Name For Filter
        fields=['category'] # "I want users to filter Products using the category field." [] for fields is mandatory here not like serializers

#=====================================================================================================================================================
# using two or more fields in filter
class ProductFilterMultipleFields(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['category', 'price']

# using this we can call url like:
# /ProductListView/?price=50000                       filtering by price
# /ProductListView/?category=Mobile                   filtering by category
# /ProductListView/?category=Mobile&price=50000       filtering by category & price

#=====================================================================================================================================================
# If we want some range
class ProductFilterRange(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price',lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price',lookup_expr='lte')
    class Meta:
        model = Product
        fields = ['category', 'min_price', 'max_price']

#=====================================================================================================================================================
# lookup Expression
# gte → greater than or equal to
# gt → greater than
# lte → less than or equal to
# lt → less than
# exact → exactly equal
# contains → contains text

# pattern
# filter_name = django_filters.FilterType(
#     field_name='model_field',
#     lookup_expr='lookup'
# )

class ProductFilterForAllLookup(django_filters.FilterSet):
    # 1. exact — exactly equal
    price_exact = django_filters.NumberFilter(field_name='price',lookup_expr='exact')
    # 2. gt — greater than
    price_gt = django_filters.NumberFilter(field_name='price',lookup_expr='gt')
    # 3. gte — greater than or equal to
    price_gte = django_filters.NumberFilter(field_name='price',lookup_expr='gte')
    # 4. lt — less than
    price_lt = django_filters.NumberFilter(field_name='price',lookup_expr='lt')
    # 5. lte — less than or equal to
    price_lte = django_filters.NumberFilter(field_name='price',lookup_expr='lte')

    # Text-based lookups
    # 6. contains
    name_contains = django_filters.CharFilter(field_name='name',lookup_expr='contains')
    # 7. icontains - icontains is case-insensitive.
    name_icontains = django_filters.CharFilter(field_name='name',lookup_expr='icontains')
    # 8. startswith
    name_startswith = django_filters.CharFilter(field_name='name',lookup_expr='startswith')
    # 9. istartswith - Case-insensitive version:
    name_istartswith = django_filters.CharFilter(field_name='name',lookup_expr='istartswith')
    # 10. endswith
    name_endswith = django_filters.CharFilter(field_name='name',lookup_expr='endswith')
    # 11. iendswith - Case-insensitive version:
    name_iendswith = django_filters.CharFilter(field_name='name',lookup_expr='iendswith')

    class Meta:
        model=Product
        fields=['price_exact',
                'price_gt',
                'price_gte',
                'price_lt',
                'price_lte',
                'name_contains',
                'name_icontains',
                'name_startswith',
                'name_istartswith',
                'name_endswith',
                'name_iendswith']
        
#=====================================================================================================================================================
# Custom Filter Methods.
# for this kind of url :  /ProductListView/?price_type=cheap
# then i want 'cheap' to mean price < 1000 
class ProductFilter(django_filters.FilterSet):
    price_type = django_filters.CharFilter(method='filter_price_type' ) # Custom filter creation
    def filter_price_type(self, queryset, name, value): # Method for custom filter

        # self      → your ProductFilter object
        # queryset  → current set of products
        # name      → name of the filter
        # value     → value entered in the URL

        if value == 'cheap':
            return queryset.filter(price__lt=10000)
        if value == 'expensive':
            return queryset.filter(price__gte=50000)
        return queryset

    class Meta:
        model = Product
        fields = ['price_type']

#=====================================================================================================================================================
# Choice Filter Methods.
# ChoiceFilter is useful when you want the user to select from a fixed set of choices.

# ?price_type=cheap
# ?price_type=medium
# ?price_type=expensive

class ProductFilterChoice(django_filters.FilterSet):

    category = django_filters.ChoiceFilter(
        choices=[
            ('Mobile', 'Mobile'),
            ('Computer', 'Computer'),
            ('Tablet', 'Tablet'),
        ]
    )

    class Meta:
        model = Product
        fields = ['category']

# choice filter fith lookup are also possible
# category = django_filters.ChoiceFilter(
#     choices=[
#         ('Mobile', 'Mobile'),
#         ('Computer', 'Computer'),
#         ('Tablet', 'Tablet'),
#     ],
#     lookup_expr='iexact'
# )

# MultipleChoiceFilter
class ProductFilterMultipleChoice(django_filters.FilterSet):

    category = django_filters.MultipleChoiceFilter(
        choices=[
            ('Mobile', 'Mobile'),
            ('Computer', 'Computer'),
            ('Tablet', 'Tablet'),
        ]
    )

    class Meta:
        model = Product
        fields = ['category']


#======================================================================================================================================================
# Filter by relation ship
from api.models import Employee

class EmployeeFilterRelation(django_filters.FilterSet):
    department = django_filters.CharFilter(
        field_name='department__name', #using __ to perform relationship call : field_name='relationship__field' we can also use foregn key
        lookup_expr='iexact'
    )
    class Meta:
        model = Employee
        fields = ['department']

#======================================================================================================================================================
# Next: Auto-generated Lookups with Meta.fields
# Instead of manually declaring filters like : price_gte = django_filters.NumberFilter(field_name='price',lookup_expr='gte') django-filter gives us a shorter way.
class ProductFilterAutoGeneratedLookups(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'price': ['exact', 'gt', 'gte', 'lt', 'lte'],
            'name': ['icontains', 'startswith'],
        }

# Manual filter → you control the filter name.
# Meta.fields lookup → django-filter generates the name using field__lookup.

#======================================================================================================================================================
# ModelChoiceFilter
# filtering using a model's available objects
from api.models import Department
class EmployeeFilterModelChoice(django_filters.FilterSet):
    department = django_filters.ModelChoiceFilter(
        queryset=Department.objects.all() # "The choices for this filter should come from the Department table."
    )
    class Meta:
        model = Employee
        fields = ['department']

# ModelMultipleChoiceFilter
# Suppose departments are:
# 1 → Computer
# 2 → Commerce
# 3 → Mathematics
# Filtering multiple departments
# You can request: /EmployeeListView/?department=1&department=3

class EmployeeFilterModelMultipleChoice(django_filters.FilterSet):
    department = django_filters.ModelMultipleChoiceFilter(queryset=Department.objects.all())
    class Meta:
        model = Employee
        fields = ['department']

# This is different from the earlier MultipleChoiceFilter. MultipleChoiceFilter → choices are manually defined:
# ModelMultipleChoiceFilter → choices come from a database model:


#======================================================================================================================================================
# RangeFilter 
# filtering values within a range, such as: price between 10,000 and 50,000
# replacement for numberfilter with gte and lte
# RangeFilter can also be used with other types, such as dates
    
class ProductFilterRange(django_filters.FilterSet):
    price_range = django_filters.RangeFilter(field_name='price')
    class Meta:
        model = Product
        fields = ['price_range']

#======================================================================================================================================================
# BooleanFilter
# BooleanFilter is used when the field contains a True / False value.
# model has boolean field to work with this
# eg model:
# class ProductTwo(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.IntegerField()
#     is_available = models.BooleanField(default=True) # Here

from FilteringAPIView.models import ProductTwo

class ProductFilter(django_filters.FilterSet):
    is_available = django_filters.BooleanFilter(field_name='is_available')
    class Meta:
        model = ProductTwo
        fields = ['is_available']

# /ProductListView/?is_available=true 
# /ProductListView/?is_available=false

#======================================================================================================================================================
# DateFilter and Date-Range Filtering
# DateFilter is used when you want to filter records based on a date.

# Eg Model:
# class Order(models.Model):
#     customer_name = models.CharField(max_length=100)
#     amount = models.IntegerField()
#     order_date = models.DateField()

from FilteringAPIView.models import Order

class OrderFilter(django_filters.FilterSet):
    order_date = django_filters.DateFilter(field_name='order_date')
    order_date_after  = django_filters.DateFilter(field_name='order_date',lookup_expr='gte')
    order_date_before  = django_filters.DateFilter(field_name='order_date',lookup_expr='lte')
    class Meta:
        model = Order
        fields = ['order_date',
                  'order_date_after',
                  'order_date_before']