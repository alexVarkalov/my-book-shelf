from rest_framework import serializers
from book_shelf.models.author import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('uuid', 'created', 'updated', 'firstname', 'lastname')
