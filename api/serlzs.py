from rest_framework.serializers import (
    Serializer, ModelSerializer, HyperlinkedModelSerializer,

)


from core.models import Blog,Book,Author

class BSerl(ModelSerializer):

    class Meta:
        model=Blog
        fields='__all__'


class BooSerl(ModelSerializer):

    class Meta:
        model=Book
        fields='__all__'
        depth=1


class AuthSerl(ModelSerializer):
    book_set=BooSerl(many=True)
    class Meta:
        model=Author
        fields='__all__'