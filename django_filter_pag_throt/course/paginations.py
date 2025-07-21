from rest_framework.pagination import PageNumberPagination

class ItemListPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 12
    page_size_query_param = "size"