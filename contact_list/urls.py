from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactList, ContactDetail
from django.urls import path, include

# router = DefaultRouter()
# router.register(r'contact', ContactViewSet, basename='contact')

# urlpatterns = router.urls

urlpatterns = [
    path('list', ContactList.as_view(), name='contact-list'),
    path('list/<int:pk>', ContactDetail.as_view(), name='contact-detail'),
]
