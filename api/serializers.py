from rest_framework import serializers


from main.models import Cat, Dog

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ('owner', 'name', 'birthday')
        read_only_fields = ('owner', )


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ('owner', 'name', 'birthday')
        read_only_fields = ('owner', )