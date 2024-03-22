import pandas as pd
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Items
from .serializers import ItemSerializer


# Create your views here.
"this api for inserting calculated annual data into a local sqlite"
class InstertItemView(APIView):
    def get(self, request):
        try:
            data = pd.read_excel("./20210309_2020_1 - 4 (1).xls")
            unique_well_number = data["API WELL  NUMBER"].unique()
            for well_number in unique_well_number:
                item = Items.objects.filter(api_well_number=well_number).first()
                if not item:
                    Items.objects.create(
                        api_well_number=well_number,
                        oil=data[data["API WELL  NUMBER"] == well_number]["OIL"].sum(),
                        gas=data[data["API WELL  NUMBER"] == well_number]["GAS"].sum(),
                        brine=data[data["API WELL  NUMBER"] == well_number]["BRINE"].sum(),
                    )
            return Response({"message": "Items added into DB"}, status=status.HTTP_200_OK)
        except FileNotFoundError:
            return Response({"error": "File not found"}, status=status.HTTP_404_NOT_FOUND)

"""this api for get data bassed on the api_well_number"""
class GetItemView(APIView):
    def get(self, request):
        well_value = request.GET.get("well")
        try:
            item = Items.objects.get(api_well_number=well_value)
            serializer = ItemSerializer(item)
            return Response(serializer.data)
        except Items.DoesNotExist:
            return Response(
                {"error": "Item does not exist"}, status=status.HTTP_404_NOT_FOUND
            )
