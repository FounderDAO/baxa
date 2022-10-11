import rest_framework.request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.core.models import Status
from apps.service.models import Country, District, Region
from .serializers import CountrySerializer, DistrictSerializer, RegionSerializer, ProfileSerializer, \
    AccountSerializer
from ...models import Profile


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
    def post(self, request: rest_framework.request.Request, id: int):
        country = Country.objects.filter(id=id)
        if country and request.user.is_staff:
            return Response("Editing!")
        return Response("Not editing!")


class CountryDetailView(APIView):
    def get(self, request: rest_framework.request.Request):
        country = Country.objects.filter(status=Status.ACTIVE)
        if country:
            return country_list()
        return Response("Not country!")


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


class RegionDetailView(APIView):
    def get(self, request: rest_framework.request.Request, id: int):
        country = Region.objects.filter(country=id, status=Status.ACTIVE)
        if country:
            return region_list(id)
        return Response("Not region!")


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


class DistrictDetailView(APIView):
    def get(self, request: rest_framework.request.Request, id: int):
        country = District.objects.filter(region=id, status=Status.ACTIVE)
        if country:
            serializer = DistrictSerializer(country, many=True)
            return Response(serializer.data)
        return Response("Not district!")


class ProfileCreateView(APIView):
    def post(self, request: rest_framework.request.Request):
        profile = Profile.objects.filter(user=request.user.id)
        if not profile:
            serializer = ProfileSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response("Not added!")
        return Response("Have this profile!")


class ProfileEditView(APIView):
    def post(self, request: rest_framework.request.Request):
        pass


class ProfileDetailView(APIView):
    def get(self, request: rest_framework.request.Request):
        profile = Profile.objects.filter(user=request.user.id)
        if profile:
            serializer = ProfileSerializer(profile[0], many=False)
            return Response(serializer.data)
        return Response("Not profile!")


class AccountDetail(APIView):
    def get(self, request: rest_framework.request.Request):
        serializer = AccountSerializer(request.user, many=False)
        return Response(serializer.data)


def country_list():
    country = Country.objects.filter(status=Status.ACTIVE)
    data = {"countries": CountrySerializer(country, many=True).data, "regions": [], "districts": []}
    region = Region.objects.filter(country=country[0].id, status=Status.ACTIVE)
    if region:
        district = District.objects.filter(region=region[0].id, status=Status.ACTIVE)
        if district:
            data["regions"] = RegionSerializer(region, many=True).data
            data["districts"] = DistrictSerializer(district, many=True).data
            return Response(data)


def region_list(id):
    region = Region.objects.filter(country=id, status=Status.ACTIVE)
    data = {"regions": RegionSerializer(region, many=True).data, "districts": []}
    district = District.objects.filter(region=region[0].id, status=Status.ACTIVE)
    if district:
        data["districts"] = DistrictSerializer(district, many=True).data
        return Response(data)
