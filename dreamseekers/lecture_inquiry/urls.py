from django.urls import path
from .views import inquiry,inquiry_index,inquiry_detail

urlpatterns = [
    path('inquiry',inquiry, name='inquiry'),
    path('inquiry/list',inquiry_index,name='inquiry_index'),
    path('inquiry/list/<int:pk>/',inquiry_detail,name='inquiry_detail'),
]
