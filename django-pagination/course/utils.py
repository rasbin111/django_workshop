from rest_framework.pagination import PageNumberPagination, CursorPagination


class Custompagination(PageNumberPagination):
    page_size = 7
    page_size_query_param = 'page_size'
    max_page_size = 9

class CursorCustomPagination(CursorPagination):
    page_size = 7
    ordering = 'title'