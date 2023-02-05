from django.urls import path



from.import views2
from.import views

app_name = 'diary'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    path('inquiry2/', views2.Inquiry2View.as_view(), name="inquiry2"),
    path('diary-list/', views.DiaryListView.as_view(), name="diary_list"),
    ]
