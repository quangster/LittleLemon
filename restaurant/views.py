from django.shortcuts import render
from django.http import HttpResponse

from .serializers import BookingSerializer, MenuSerializer
from .models import Menu, Booking

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets


class MenuItemView(ListCreateAPIView):
    model = Menu
    queryset = model.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]


class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    model = Menu
    queryset = model.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


# Create your views here.
def index(request):
    return render(request, 'restaurant/index.html', {})
