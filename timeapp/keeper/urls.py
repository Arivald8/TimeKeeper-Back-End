from django.urls import path
from . import views

urlpatterns = [
    path('', views.ActivityListAPIView.as_view(), name='activities_list'),
    path('create/', views.CreateActivity.as_view(), name='create_activity'),
    path('<int:id>/', views.ActivityRetrieveAPIView.as_view(), name='activities_detail'),
    path('<str:activity_date>/', views.ActivityDateList.as_view(), name='activity_date'),
    path('update/<int:pk>/<str:activity_date>/', views.RetrieveActivityTime.as_view(), name='update_activity'),
    path('weekly/<str:activity_date>/', views.WeeklyActivityView.as_view(), name='weekly_dates'),
]