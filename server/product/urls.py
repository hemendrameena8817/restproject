
from django.urls import path,include

urlpatterns = [
    path('Product', ProductView.as_view() ),
]