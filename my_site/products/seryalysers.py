from .models import Product, Category, File


from rest_framework import serializers





class categoryseryalysers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id', 'parent', 'title']

class fileseryalysers(serializers.ModelSerializer):
    class Meta:
        model=File
        fields=['id', 'title', 'description', 'file', 'time_create']

class poroductseryalysers(serializers.HyperlinkedModelSerializer):
    categories=categoryseryalysers(many=True)
    file_set=fileseryalysers(many=True)
#******اگه بخواهیم آبجکت دلخواه بدهیم*****
    foo=serializers.SerializerMethodField()
    class Meta:
        model=Product
        fields=['id', 'title', 'description', 'avatar', 'categories', 'time_create', 'file_set', 'foo', 'url']
    
    def get_foo(self, obj):
        return str(obj.id)+"Hello"
    