from django.shortcuts import render

# Create your views here.

# api/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import Analyze



@api_view(['POST'])
def player_analysis(request):
    batter_name = request.data.get('batter_name')
    pitcher_name = request.data.get('pitcher_name')

    print(batter_name)

    print(pitcher_name)

    # Add any data processing logic here

    if batter_name and pitcher_name:
        # Example: create or process data here
        message = Analyze.analyze(batter_name,pitcher_name)

        return Response({"message": message.content}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)

