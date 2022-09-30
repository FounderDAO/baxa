import rest_framework.request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.models import Country, District, Region
from apps.accounts.serializers import CountrySerializer, DistrictSerializer, RegionSerializer, ProfileSerializer


# Create your views here.


class CountryCreateView(APIView):
    def post(self, request: rest_framework.request.Request):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response("Not added!")

    def get(self, request: rest_framework.request.Request, id: int):
        country = Country.objects.filter(id=id)
        if country and request.user.is_staff:
            country[0].delete()
            return Response("Delete!")
        return Response("Not delete!")


class CountryEditingView(APIView):
    def post(self, request: rest_framework.request.Request, id):
        country = Country.objects.filter(id=id)
        if country and request.user.is_staff:
            return Response("Editing!")
        return Response("Not editing!")


class RegionCreateView(APIView):
    def post(self, request: rest_framework.request.Request):
        serializer = RegionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response("Not added!")

    def get(self, request: rest_framework.request.Request, id: int):
        region = Region.objects.filter(id=id)
        if region and request.user.is_staff:
            return Response("Deleted!")
        return Response("Not deleted!")


class RegionEditView(APIView):
    def post(self, request: rest_framework.request.Request, id: int):
        region = Region.objects.filter(id=id)
        if region and request.user.is_staff:
            return Response("Editing!")
        return Response("Not editing!")


class DistrictCreateView(APIView):
    def post(self, request: rest_framework.request.Request):
        serializer = DistrictSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response("Not added!")

    def get(self, request: rest_framework.request.Request, id: int):
        district = District.objects.filter(id=id)
        if district and request.user.is_staff:
            district[0].delete()
            return Response("Deleted!")
        return Response("Not deleted")


class DistrictEditView(APIView):
    def post(self, request: rest_framework.request.Request, id: int):
        district = District.objects.filter(id=id)
        if district and request.user.is_staff:
            return Response("Editing!")
        return Response("Not editing!")


class ProfileCreateView(APIView):
    def post(self, request: rest_framework.request.Request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response("Not added!")


class ProfileEditView(APIView):
    def post(self, request: rest_framework.request.Request):
        pass
