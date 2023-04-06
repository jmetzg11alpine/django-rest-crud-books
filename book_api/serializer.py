# from rest_framework import serializers
# from book_api.models import Book

# class BookSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=100)
#     number_of_pages = serializers.IntegerField()
#     published_date = serializers.DateField()
#     quantity = serializers.IntegerField()

#     def create(self, data):
#         return Book.objects.create(**data)

#     def update(self, instance, data):
#         instance.title = data.get('title', instance.title)
#         instance.number_of_pages = data.get('number_of_pages', instance.number_of_pages)
#         instance.published_date = data.get('published_date', instance.published_date)
#         instance.quantity = data.get('quantity', instance.quantity)

#         instance.save()
#         return instance

from rest_framework import serializers
from book_api.models import Book
from django.forms import ValidationError

class BookSerializer(serializers.ModelSerializer):

    magic_number = serializers.SerializerMethodField()

    class Meta:
        model = Book
        # does all the create and update stuff
        # fields = ('title', 'number_of_pages', 'published_date', 'quantity')
        fields = '__all__'

    # custom validations for data
    # here there will be data with title of Diet Coke
    def validate_title(self, value):
        if value == 'Diet Coke':
            raise ValidationError("no diet coke please")
        return value

    # validation of objects
    def validate(self, data):
        if data['number_of_pages'] > 200 and data['quantity'] > 200:
            raise ValidationError("too heavy for inventory")
        return data

    # can make custom fields
    def get_magic_number(self, data):
        return data.quantity * data.number_of_pages