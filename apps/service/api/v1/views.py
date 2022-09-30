from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import rest_framework.request

from .models import Service, Comment
from .serializers import ServiceSerializer, CommentSerializer


class ServiceView(APIView):
    def get(self, request: rest_framework.request.Request):
        service = Service.objects.all()
        if service:
            serializers = ServiceSerializer(service, many=True)
            return Response(serializers.data)
        return Response("Not service!")


class ServiceCreateView(APIView):
    def post(self, request: rest_framework.request.Request, *args, **kwargs):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse("Added!")
        return HttpResponse("Not added!")


class ServiceDeleteView(APIView):
    def get(self, request: rest_framework.request.Request, id):
        service = Service.objects.filter(id=id)
        if service:
            if service[0].author.id == request.user.id or service[0].owner.id == request.user.id:
                service[0].delete()
                return Response("Deleted!")
        return Response("Not deleted!")


class ServiceEditView(APIView):
    def post(self, request: rest_framework.request.Request, id: int):
        service = Service.objects.filter(id=id)
        if service:
            if service[0].author.id == request.user.id or service[0].owner.id == request.user.id:
                return Response("Editing!")
        return Response("Not editing!")


class CommentCreateView(APIView):
    def post(self, request: rest_framework.request.Request):
        comment_serializer = CommentSerializer(data=request.data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return Response("Added!")
        return Response("Not added!")


class CommentDeleteView(APIView):
    def get(self, request: rest_framework.request.Request, id: int):
        comment = Comment.objects.filter(id=id)
        if comment:
            if comment[0].user.id == request.user.id:
                comment[0].delete()
                return Response("Delete!")
        return Response("Not delete!")


class CommentEditView(APIView):
    def post(self, request: rest_framework.request.Request, id:int):
        comment = Comment.objects.filter(id=id)
        if comment:
            if comment[0].user.id:
                return Response("Editing!")
        return Response("Not editing!")
