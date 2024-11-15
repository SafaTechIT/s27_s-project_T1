from rest_framework import serializers
from dbmng import models

user=models.users
tag=models.tags
post=models.post
comment=models.comments
reply=models.reply
massage=models.massage
msrp=models.mreply
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'
class tagSerializer(serializers.ModelSerializer):
    class Meta:
        model = tag
        fields = '__all__'
class postSerializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = '__all__'
class commentSerializer(serializers.ModelSerializer):
    class Meta:
        model = comment
        fields = '__all__'
