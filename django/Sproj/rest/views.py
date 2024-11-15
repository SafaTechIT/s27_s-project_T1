from django.template.defaultfilters import title
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from dbmng import models


# user properties
class user(APIView):
    # get user properties
    def get(self, request):
        userid = request.get["id"]
        query = models.users.objects.get(uid=userid)
        serializer = serializers.UserSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        query = models.users.objects.all()
        serializer = serializers.UserSerializer(query, many=True)
        models.users.objects.get(request.data).delete()
        return Response(serializer.data, status=status.HTTP_200_OK)


# tags detail
class tag(APIView):
    def get(self, request):
        query = models.tags.objects.all()
        serializer = serializers.UserSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        query = models.tags.objects.all()
        serializer = serializers.UserSerializer(query, many=True)
        models.tags.objects.get(request.data).delete()
        return Response(serializer.data, status=status.HTTP_200_OK)


# all posts query
class allposts(APIView):
    def get(self, request):
        query = models.post.objects.all()
        serializer = serializers.UserSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# single post detail
class post(APIView):
    def get(self, request):
        title = request.get["title"]
        query = models.post.objects.get(title=title)
        serializer = serializers.UserSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete post with post title
    def delete(self, request):
        title = request.get["title"]
        query = models.post.objects.all()
        serializer = serializers.UserSerializer(query, many=True)
        models.post.objects.get(title=title).delete()
        return Response(serializer.data, status=status.HTTP_200_OK)


# comment of post
class comment(APIView):
    def get(self, request):
        # search post for comment
        search = request.GET["post"]
        query = models.comments.objects.filter(title=search)
        serializer = serializers.UserSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        query = models.comments.objects.all()
        serializer = serializers.UserSerializer(query, many=True)
        models.comments.objects.get(request.data).delete()
        return Response(serializer.data, status=status.HTTP_200_OK)


# reply of comments
class reply(APIView):
    # search for reply of comment
    def get(self, request):
        search = request.GET["comment"]
        query = models.reply.objects.filter(comment=search)
        serializer = serializers.UserSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        query = models.reply.objects.all()
        serializer = serializers.UserSerializer(query, many=True)
        models.reply.objects.get(request.data).delete()
        return Response(serializer.data, status=status.HTTP_200_OK)
