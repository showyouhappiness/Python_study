from django.shortcuts import render
from rest_framework import views, response, status, decorators, generics, mixins
from .models import blogPost
from .serializers import blogPostSerializer


# Create your views here.

@decorators.api_view(['GET', 'POST'])
def blogPostList(request):
    """
    基于函数视图的@api_view装饰器,获取、新增一个blogPost示例。
    """
    if request.method == 'GET':
        blog_list = blogPost.objects.all()
        serializer = blogPostSerializer(blog_list, many=True)
        return response.Response(serializer.data)

    elif request.method == 'POST':
        serializer = blogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)  # 201 代表成功创建了一个对象
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # 400 代表请求无效


@decorators.api_view(['GET', 'PUT', 'DELETE'])
def blogPostDetail(request, pk):
    """
    基于函数视图的@api_view装饰器,检索，更新或删除一个blogPost示例。
    """
    try:
        blog_post = blogPost.objects.get(pk=pk)
    except blogPost.DoesNotExist:
        return response.Response(status=status.HTTP_404_NOT_FOUND)  # 404 代表请求的资源不存在

    if request.method == 'GET':
        serializer = blogPostSerializer(blog_post)
        return response.Response(serializer.data)

    elif request.method == 'PUT':
        serializer = blogPostSerializer(blog_post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # 400 代表请求无效

    elif request.method == 'DELETE':
        blog_post.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)  # 204 代表成功处理了请求并且没有返回任何内容


class blogPostListView(views.APIView):
    """
    基于类视图的APIView
    """

    def get(self, request):
        blog_list = blogPost.objects.all()
        serializer = blogPostSerializer(blog_list, many=True)
        return response.Response(serializer.data)

    def post(self, request):
        serializer = blogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class blogPostDetailView(views.APIView):
    """
    基于类视图的APIView,检索，更新或删除一个blogPost示例。
    """

    def get_object(self, pk):
        try:
            return blogPost.objects.get(pk=pk)
        except blogPost.DoesNotExist:
            return response.Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        blog_post = self.get_object(pk)
        serializer = blogPostSerializer(blog_post, many=False)
        return response.Response(serializer.data)

    def put(self, request, pk, format=None):
        blog_post = self.get_object(pk)
        serializer = blogPostSerializer(blog_post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        blog_post = self.get_object(pk)
        blog_post.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)


class blogPostListMixin(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
    """
    基于类视图的GenericAPIView,使用混合类
    """
    queryset = blogPost.objects.all()
    serializer_class = blogPostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)  # 调用混合类的list方法,返回所有blogPost

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)  # 调用混合类的create方法,创建一个blogPost

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)  # 调用混合类的destroy方法,删除一个blogPost


class blogPostListMixinDetail(mixins.RetrieveModelMixin,
                              mixins.UpdateModelMixin,
                              mixins.DestroyModelMixin,
                              generics.GenericAPIView):
    """
    基于类视图的GenericAPIView,使用混合类
    """
    queryset = blogPost.objects.all()
    serializer_class = blogPostSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)  # 调用混合类的retrieve方法,检索一个blogPost示例。

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)  # 调用混合类的update方法,更新一个blogPost示例。

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)  # 调用混合类的destroy方法,删除一个blogPost示例。


class blogPostListGeneric(generics.ListCreateAPIView):
    """
    基于类视图的GenericAPIView,使用混合类
    """
    queryset = blogPost.objects.all()  # 指定查询集,返回所有blogPost,主要用于创建一个blogPost示例。
    serializer_class = blogPostSerializer  # 指定序列化类,不需要重写post方法


class blogPostListGenericDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    基于类视图的GenericAPIView,使用混合类
    """
    queryset = blogPost.objects.all()  # 指定查询集,返回所有blogPost,主要用于检索，更新或删除一个blogPost示例。
    serializer_class = blogPostSerializer  # 指定序列化类,不需要重写get,put,delete方法
