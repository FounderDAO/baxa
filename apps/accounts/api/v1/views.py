import rest_framework.request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from apps.core.models import Status
from django.http import Http404
from rest_framework.decorators import  permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from apps.service.models import Country, District, Region, User
from .serializers import CountrySerializer, DistrictSerializer, RegionSerializer, ProfileSerializer, \
    AccountSerializer
from ...models import Profile
from drf_yasg.utils import swagger_auto_schema

# Create your views here.


class CountryList(APIView):
    """
    List all countreis, or create a new country.
    """
    @swagger_auto_schema(
        responses={200: CountrySerializer(many=True),
                   401: 'Unauthorized',
                   404: 'No countries found'},
        tags=['Get Countries'],
        operation_description="Method to fetch all the countries",
    )


    def get(self, request, format=None):
        country = Country.objects.all()
        serializer = CountrySerializer(country, many=True)
        return Response(serializer.data)


    @swagger_auto_schema(
        description="Method to post a new building",
        request_body=CountrySerializer,
        responses={200: CountrySerializer(many=False),
                   401: 'Unauthorized',
                   201: 'Country Added'},
        tags=['Create, Update and Delete Country'],
        operation_description="Method to post a new Country",
    )
    def post(self, request, format=None):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CountryDetail(APIView):
    """
    Retrieve, update or delete a country instance.
    """

    @swagger_auto_schema(
        auto_schema=None,
    )
    def get_object(self, pk):
        try:
            return Country.objects.get(pk=pk)
        except Country.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        responses={200: CountrySerializer(many=True),
                   401: 'Unauthorized',
                   404: 'No country found for the given id'},
        tags=['Get Country'],
        operation_description="Method to fetch a country",
    )
    def get(self, request, pk, format=None):
        country = self.get_object(pk)
        serializer = CountrySerializer(country)
        return Response(serializer.data)


    @swagger_auto_schema(
        description="Method to update a country",
        request_body=CountrySerializer,
        responses={200: CountrySerializer(many=True),
                   401: 'Unauthorized',
                   201: 'Country updated'},
        tags=['Create, Update and Delete Country'],
        operation_description="Method to update a country",
    )
    def put(self, request, pk, format=None):
        country = self.get_object(pk)
        serializer = CountrySerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        description="Method to delete a country",
        request_body=CountrySerializer,
        responses={200: CountrySerializer(many=True),
                   401: 'Unauthorized',
                   201: 'Country deleted'},
        tags=['Create, Update and Delete Country'],
        operation_description="Method to update a country",
    ) 
    def delete(self, request, pk, format=None):
        country = self.get_object(pk)
        country.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class CountryDetailView(APIView):
#     def get(self, request: rest_framework.request.Request):
#         country = Country.objects.filter(status=Status.ACTIVE)
#         if country:
#             return country_list()
#         return Response("Not country!")


class RegionList(APIView):
    """
    List all regions, or create a new region.
    """
    @swagger_auto_schema(
        responses={200: RegionSerializer(many=True),
                   401: 'Unauthorized',
                   404: 'No regions found'},
        tags=['Get Regions'],
        operation_description="Method to fetch all the regions",
    )


    def get(self, request, format=None):
        region = Region.objects.all()
        serializer = RegionSerializer(region, many=True)
        return Response(serializer.data)


    @swagger_auto_schema(
        description="Method to post a new building",
        request_body=RegionSerializer,
        responses={200: RegionSerializer(many=False),
                   401: 'Unauthorized',
                   201: 'Region Added'},
        tags=['Create, Update and Delete Region'],
        operation_description="Method to post a new Region",
    )
    def post(self, request, format=None):
        serializer = RegionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class RegionDetail(APIView):
    """
    Retrieve, update or delete a region instance.
    """

    @swagger_auto_schema(
        auto_schema=None,
    )
    def get_object(self, pk):
        try:
            return Region.objects.get(pk=pk)
        except Region.DoesNotExist:
            raise Http404


    @swagger_auto_schema(
        responses={200: RegionSerializer(many=True),
                   401: 'Unauthorized',
                   404: 'No region found for the given id'},
        tags=['Get Region'],
        operation_description="Method to fetch a region",
    )
    def get(self, request, pk, format=None):
        region = self.get_object(pk)
        serializer = RegionSerializer(region)
        return Response(serializer.data)


    @swagger_auto_schema(
        description="Method to update a region",
        request_body=RegionSerializer,
        responses={200: RegionSerializer(many=True),
                   401: 'Unauthorized',
                   201: 'Region updated'},
        tags=['Create, Update and Delete Region'],
        operation_description="Method to update a region",
    )
    def put(self, request, pk, format=None):
        region = self.get_object(pk)
        serializer = RegionSerializer(region, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        description="Method to delete a region",
        request_body=RegionSerializer,
        responses={200: RegionSerializer(many=True),
                   401: 'Unauthorized',
                   201: 'Region deleted'},
        tags=['Create, Update and Delete Region'],
        operation_description="Method to update a region",
    ) 
    def delete(self, request, pk, format=None):
        region = self.get_object(pk)
        region.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class DistrictList(APIView):
    """
    List all districts, or create a new district.
    """
    @swagger_auto_schema(
        responses={200: DistrictSerializer(many=True),
                   401: 'Unauthorized',
                   404: 'No districts found'},
        tags=['Get Districts'],
        operation_description="Method to fetch all the districts",
    )
    def get(self, request, format=None):
        district = District.objects.all()
        serializer = DistrictSerializer(district, many=True)
        return Response(serializer.data)


    @swagger_auto_schema(
        description="Method to post a new building",
        request_body=DistrictSerializer,
        responses={200: DistrictSerializer(many=False),
                   401: 'Unauthorized',
                   201: 'District Added'},
        tags=['Create, Update and Delete District'],
        operation_description="Method to post a new District",
    )
    def post(self, request, format=None):
        serializer = DistrictSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class DistrictDetail(APIView):
    """
    Retrieve, update or delete a district instance.
    """

    @swagger_auto_schema(
        auto_schema=None,
    )
    def get_object(self, pk):
        try:
            return District.objects.get(pk=pk)
        except District.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        responses={200: DistrictSerializer(many=True),
                   401: 'Unauthorized',
                   404: 'No district found for the given id'},
        tags=['Get District'],
        operation_description="Method to fetch a district",
    )
    def get(self, request, pk, format=None):
        district = self.get_object(pk)
        serializer = DistrictSerializer(district)
        return Response(serializer.data)


    @swagger_auto_schema(
        description="Method to update a district",
        request_body=DistrictSerializer,
        responses={200: DistrictSerializer(many=True),
                   401: 'Unauthorized',
                   201: 'District updated'},
        tags=['Create, Update and Delete District'],
        operation_description="Method to update a district",
    )
    def put(self, request, pk, format=None):
        district = self.get_object(pk)
        serializer = DistrictSerializer(district, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        description="Method to delete a district",
        request_body=DistrictSerializer,
        responses={200: DistrictSerializer(many=True),
                   401: 'Unauthorized',
                   201: 'District deleted'},
        tags=['Create, Update and Delete District'],
        operation_description="Method to update a district",
    ) 
    def delete(self, request, pk, format=None):
        district = self.get_object(pk)
        district.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class  ProfileCreateView(APIView):
    """
    List all profiles, or create a new profile.
    """
    @swagger_auto_schema(
        responses={200: ProfileSerializer(many=True),
                   401: 'Unauthorized',
                   404: 'No profiles found'},
        tags=['Get Profiles'],
        operation_description="Method to fetch all the profiles",
    )


    def get(self, request, format=None):
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data)


    @swagger_auto_schema(
        description="Method to post a new building",
        request_body=ProfileSerializer,
        responses={200: ProfileSerializer(many=False),
                   401: 'Unauthorized',
                   201: 'Profile Added'},
        tags=['Create, Update and Delete Profile'],
        operation_description="Method to post a new Profile",
    )
    def post(self, request, format=None):
        profile = Profile.objects.filter(user=request.user.id)
        if not profile:
            serializer = ProfileSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Have this profile!")



class ProfileDetail(APIView):
    """
    Retrieve, update or delete a profile instance.
    """

    @swagger_auto_schema(
        auto_schema=None,
    )
    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404


    @swagger_auto_schema(
        responses={200: ProfileSerializer(many=True),
                   401: 'Unauthorized',
                   404: 'No profile found for the given id'},
        tags=['Get Profile'],
        operation_description="Method to fetch a profile",
    )
    def get(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

# class ProfileDetailView(APIView):
#     def get(self, request: rest_framework.request.Request):
#         profile = Profile.objects.filter(user=request.user.id)
#         if profile:
#             serializer = ProfileSerializer(profile[0], many=False)
#             return Response(serializer.data)
#         return Response("Not profile!")


    @swagger_auto_schema(
        description="Method to update a profile",
        request_body=ProfileSerializer,
        responses={200: ProfileSerializer(many=True),
                   401: 'Unauthorized',
                   201: 'Profile updated'},
        tags=['Create, Update and Delete Profile'],
        operation_description="Method to update a profile",
    )
    def put(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        description="Method to delete a profile",
        request_body=ProfileSerializer,
        responses={200: ProfileSerializer(many=True),
                   401: 'Unauthorized',
                   201: 'Profile deleted'},
        tags=['Create, Update and Delete Profile'],
        operation_description="Method to update a profile",
    ) 
    def delete(self, request, pk, format=None):
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





# class AccountDetail(APIView):
#     def get(self, request: rest_framework.request.Request):
#         serializer = AccountSerializer(request.user, many=False)
#         return Response(serializer.data)


class AccountList(APIView):
    """
    List all accounts, or create a new account.
    """
    @swagger_auto_schema(
        responses={200: AccountSerializer(many=True),
                   401: 'Unauthorized',
                   404: 'No accounts found'},
        tags=['Get Accounts'],
        operation_description="Method to fetch all the accounts",
    )


    def get(self, request, format=None):
        account = User.objects.all()
        serializer = AccountSerializer(account, many=True)
        return Response(serializer.data)


    @swagger_auto_schema(
        description="Method to post a new building",
        request_body=AccountSerializer,
        responses={200: AccountSerializer(many=False),
                   401: 'Unauthorized',
                   201: 'Account Added'},
        tags=['Create, Update and Delete Account'],
        operation_description="Method to post a new Account",
    )
    def post(self, request, format=None):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AccountDetail(APIView):
    """
    Retrieve, update or delete a account instance.
    """

    @swagger_auto_schema(
        auto_schema=None,
    )
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        responses={200: AccountSerializer(many=True),
                   401: 'Unauthorized',
                   404: 'No account found for the given id'},
        tags=['Get Account'],
        operation_description="Method to fetch a account",
    )
    def get(self, request, pk, format=None):
        account = self.get_object(pk)
        serializer = AccountSerializer(account)
        return Response(serializer.data)


    @swagger_auto_schema(
        description="Method to update a account",
        request_body=AccountSerializer,
        responses={200: AccountSerializer(many=True),
                   401: 'Unauthorized',
                   201: 'Account updated'},
        tags=['Create, Update and Delete Account'],
        operation_description="Method to update a account",
    )
    def put(self, request, pk, format=None):
        account = self.get_object(pk)
        serializer = AccountSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        description="Method to delete a account",
        request_body=AccountSerializer,
        responses={200: AccountSerializer(many=True),
                   401: 'Unauthorized',
                   201: 'Account deleted'},
        tags=['Create, Update and Delete Account'],
        operation_description="Method to update a account",
    ) 
    def delete(self, request, pk, format=None):
        account = self.get_object(pk)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





# def country_list():
#     country = Country.objects.filter(status=Status.ACTIVE)
#     data = {"countries": CountrySerializer(country, many=True).data, "regions": [], "districts": []}
#     region = Region.objects.filter(country=country[0].id, status=Status.ACTIVE)
#     if region:
#         district = District.objects.filter(region=region[0].id, status=Status.ACTIVE)
#         if district:
#             data["regions"] = RegionSerializer(region, many=True).data
#             data["districts"] = DistrictSerializer(district, many=True).data
#             return Response(data)


# def region_list(id):
#     region = Region.objects.filter(country=id, status=Status.ACTIVE)
#     data = {"regions": RegionSerializer(region, many=True).data, "districts": []}
#     district = District.objects.filter(region=region[0].id, status=Status.ACTIVE)
#     if district:
#         data["districts"] = DistrictSerializer(district, many=True).data
#         return Response(data)


