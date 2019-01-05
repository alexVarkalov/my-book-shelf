from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from book_shelf.models.author import Author
from book_shelf.serializers.author import AuthorSerializer
from rest_framework import status


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('uuid')
    serializer_class = AuthorSerializer

    def get_queryset(self):
        queryset = Author.objects.all().order_by('uuid')
        firstname = self.request.query_params.get('firstname', None)
        if firstname:
            queryset = queryset.filter(firsname__icontains=firstname).order_by('uuid')
        lastname = self.request.query_params.get('lastname', None)
        if lastname:
            queryset = queryset.filter(lastname__icontains=lastname).order_by('uuid')
        return queryset

    def retrieve(self, request, *args, **kwargs):
        queryset = Author.objects.all()
        author = get_object_or_404(queryset, uuid=kwargs.get('uuid'))
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
