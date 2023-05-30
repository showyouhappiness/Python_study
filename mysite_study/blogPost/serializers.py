from rest_framework import serializers
from .models import blogPost


class blogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = blogPost  # 指定序列化的模型
        fields = '__all__'  # 将所有字段都序列化
