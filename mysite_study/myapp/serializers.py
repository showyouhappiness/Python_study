from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # 和['id', 'name', 'email', 'password']等价，两者都是将所有字段都序列化
