from rest_framework import viewsets, pagination, filters
from rest_framework.filters import SearchFilter
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeePagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = EmployeePagination
    filter_backends = [filters.OrderingFilter, SearchFilter]
    ordering_fields = ['first_name', 'last_name', 'email', 'phone', 'birth']
    ordering = ['first_name']
    
    # Define the search fields
    search_fields = ['first_name', 'last_name', 'email', 'phone']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        
        if start_date and end_date:
            queryset = queryset.filter(birth__range=[start_date, end_date])
        elif start_date:
            queryset = queryset.filter(birth__gte=start_date)
        elif end_date:
            queryset = queryset.filter(birth__lte=end_date)
        
        return queryset
