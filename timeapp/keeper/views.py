from django.http.request import HttpRequest
from django.shortcuts import render
from rest_framework import generics
from .serializers import ActivityListSerializer
from .models import Activity
from keeper import serializers
import datetime


class ActivityListAPIView(generics.ListAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivityListSerializer

class ActivityRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = Activity.objects.all()
    serializer_class = ActivityListSerializer


class ActivityDateList(generics.ListAPIView):
    serializer_class = ActivityListSerializer

    def get_queryset(self):
        activity_date = self.kwargs['activity_date']
        return Activity.objects.filter(activity_date=activity_date)

class CreateActivity(generics.CreateAPIView):
    serializer_class = ActivityListSerializer
    queryset = Activity.objects.all()

class RetrieveActivityTime(generics.RetrieveUpdateAPIView):
    serializer_class = ActivityListSerializer
    def get_queryset(self):
        activity_date = self.kwargs['activity_date']

        return Activity.objects.filter(activity_date=activity_date)

class WeeklyActivityView(generics.ListAPIView):
    serializer_class = ActivityListSerializer
    
    def get_queryset(self):
        def next_weekday(weekday, selected_date):
            # weekday -> int -> 0 = Monday, 1=Tuesday, 2=Wednesday...
            selected_split = selected_date.split("-")
            converted_date = datetime.date(year=int(selected_split[0]), month=int(selected_split[1]), day=int(selected_split[2]))
            days_ahead = weekday - converted_date.weekday()
            if days_ahead <= 0: # Target day already happened this week
                days_ahead += 7
            return converted_date + datetime.timedelta(days_ahead)

        activity_date = self.kwargs['activity_date']
        next_monday = next_weekday(weekday=0, selected_date=activity_date)

        return Activity.objects.filter(activity_date__range=[activity_date, next_monday])

