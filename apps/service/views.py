from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import rest_framework.request

from apps.core.models import Status
from .models import Service, Comment, ServiceImage, CommentImage
from .serializers import ServiceSerializer, CommentSerializer, ServiceImageSerializer, CommentImageSerializer


class ServiceView(APIView):
    def get(self, request: rest_framework.request.Request):
        service = Service.objects.filter(status=Status.ACTIVE)
        if service:
            return service_view()
        return Response("Not service!")


class ServiceCreateView(APIView):
    def post(self, request: rest_framework.request.Request, *args, **kwargs):
        data = request.data
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            new_service_id = serializer.data["id"]
            for i in range(int(data['file-number'])):
                image_serializer = ServiceImageSerializer(
                    data={'service': new_service_id, "file": data['file-' + str(i)]})
                if image_serializer.is_valid():
                    image_serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
        data = request.data
        comment_serializer = CommentSerializer(data=data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            new_service_id = comment_serializer.data["id"]
            for i in range(int(data['file-number'])):
                image_serializer = CommentImageSerializer(
                    data={'comment': new_service_id, "file": data['file-' + str(i)]})
                if image_serializer.is_valid():
                    image_serializer.save()
            return Response(comment_serializer.data)
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
    def post(self, request: rest_framework.request.Request, id: int):
        comment = Comment.objects.filter(id=id)
        if comment:
            if comment[0].user.id:
                return Response("Editing!")
        return Response("Not editing!")


def service_view():
    data = []
    service = Service.objects.filter(status=Status.ACTIVE)

    if service:
        for i in service:
            append = {"service": ServiceSerializer(i, many=False).data, "serviceImg": "", "comment": ""}
            serviceImg = ServiceImage.objects.filter(i.id, status=Status.ACTIVE)
            if serviceImg:
                append["serviceImg"] = ServiceImageSerializer(serviceImg, many=True).data
            comments = Comment.objects.filter(service=i.id, status=Status.ACTIVE)
            comment_arr = []
            if comments:
                for comment in comments:
                    comment_serializer = {"comment": CommentSerializer(comment, many=False).data, "comment_img": ""}
                    comment_img = CommentImage.objects.filter(comment=comment.id, status=Status.ACTIVE)
                    if comment_img:
                        comment_serializer["comment_img"] = CommentImageSerializer(comment_img, many=False).data
                    comment_arr.append(comment_serializer)
            append["comment"] = comment_arr
            data.append(append)
        return Response(data)
