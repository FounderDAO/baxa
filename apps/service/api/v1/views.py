from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import rest_framework.request

from apps.core.models import Status
from apps.service.models import Service, Comment, ServiceImage, CommentImage, Category
from .serializers import ServiceSerializer, CommentSerializer, ServiceImageSerializer, \
    CommentImageSerializer, CategorySerializer


class ServiceView(APIView):
    def post(self, request: rest_framework.request.Request):
        if request.data == "profile":
            service = Service.objects.filter(status=Status.ACTIVE, author=request.user.id)
            if service:
                return service_view(request.data["data"], request.user.id)
        else:
            service = Service.objects.filter(status=Status.ACTIVE)
            if service:
                return service_view("", request.user.id)
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
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceDeleteView(APIView):
    def get(self, request: rest_framework.request.Request, id):
        service = Service.objects.filter(id=id)
        if service:
            if service[0].author.id == request.user.id or service[0].owner and service[0].owner.id == request.user.id:
                service[0].status = Status.DELETED
                service[0].save()
                return Response("Deleted!")
        return Response("Not deleted!")


class ServiceEditView(APIView):
    def post(self, request: rest_framework.request.Request, id: int):
        service = Service.objects.filter(id=id)
        if service:
            if service[0].author.id == request.user.id or service[0].owner.id == request.user.id:
                return Response("Editing!")
        return Response("Not editing!")


class ServiceDetailView(APIView):
    def get(self, request: rest_framework.request.Request, id: int):
        service = Service.objects.filter(id=id, status=Status.ACTIVE)
        if service:
            return service_detail_view(id)
        return Response("Not editing!")


class CommentCreateView(APIView):
    def post(self, request: rest_framework.request.Request):
        data = request.data
        comment_serializer = CommentSerializer(data=data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            comment_img = []
            new_service_id = comment_serializer.data["id"]
            for i in range(int(data['file-number'])):
                image_serializer = CommentImageSerializer(
                    data={'comment': new_service_id, "file": data['file-' + str(i)]})
                if image_serializer.is_valid():
                    image_serializer.save()
                    comment_img.append(image_serializer.data)
            return Response({"comment": comment_serializer.data, "img": comment_img})
        return Response("Not added!")


class CommentDeleteView(APIView):
    def get(self, request: rest_framework.request.Request, id: int):
        comment = Comment.objects.filter(id=id)
        if comment:
            if comment[0].user.id == request.user.id:
                comment[0].status = Status.DELETED
                comment[0].save()
                return Response("Delete!")
        return Response("Not delete!")


class CommentEditView(APIView):
    def post(self, request: rest_framework.request.Request, id: int):
        comment = Comment.objects.filter(id=id)
        if comment:
            if comment[0].user.id:
                return Response("Editing!")
        return Response("Not editing!")


def service_view(name, account_id=None):
    data = []
    if name == "profile":
        service = Service.objects.filter(status=Status.ACTIVE, author=account_id)
        for i in service:
            append = {"service": ServiceSerializer(i, many=False).data, "serviceImg": "", "comment": ""}
            serviceImg = ServiceImage.objects.filter(service=i.id, status=Status.ACTIVE)
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
    elif not name:
        service = Service.objects.filter(status=Status.ACTIVE)[:4]
        for i in service:
            append = {"service": ServiceSerializer(i, many=False).data, "serviceImg": [], "comment": []}
            serviceImg = ServiceImage.objects.filter(service=i.id, status=Status.ACTIVE)
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
    elif name == "services":
        service = Service.objects.filter(status=Status.ACTIVE)
        for i in service:
            append = {"service": ServiceSerializer(i, many=False).data, "serviceImg": "", "comment": ""}
            serviceImg = ServiceImage.objects.filter(service=i.id, status=Status.ACTIVE)
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


def service_detail_view(id: int):
    # service serializer data
    service = ServiceSerializer(Service.objects.get(id=id)).data
    # service img object
    service_img = ServiceImage.objects.filter(service=id)
    service_img_serializer = []
    if service_img:
        service_img_serializer = ServiceImageSerializer(service_img, many=True).data
    comments = []
    comment = Comment.objects.filter(service=id, status=Status.ACTIVE)
    if comment:
        for i in comment:
            comment_img = CommentImage.objects.filter(comment=i.id)
            if comment_img:
                comments.append({'comment': CommentSerializer(i, many=False).data,
                                 'img': CommentImageSerializer(comment_img, many=True).data})
    return Response({'service': service, 'img': service_img_serializer, 'comments': comments})


class CategoryCreateView(APIView):
    def post(self, request: rest_framework.request.Request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response("Not added!")

    def get(self, request: rest_framework.request.Request, id):
        category = Category.objects.filter(id=id)
        if category:
            category[0].delete()
        return Response("deleted!")


class CategoryEdit(APIView):
    def post(self, request: rest_framework.request.Request, id):
        category = Category.objects.filter(id=id)
        if category:
            category[0].parent = request.data['parent']
            category[0].name = request.data['name']
            category[0].description = request.data['description']

    def get(self, request: rest_framework.request.Request):
        category = Category.objects.filter(status=Status.ACTIVE, parent=None)
        if category:
            serializer = CategorySerializer(category, many=True)
            return Response(serializer.data)
        return Response("Not category!")
