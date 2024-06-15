from django.shortcuts import render
from .models import User, Pet, Grooming, Reservation, Availability, Schedule, Event
from .serializers import (UserSerializer, PetSerializer, GroomingSerializer, ReservationSerializer,
                          AvailabilitySerializer, ScheduleSerializer, EventSerializer)
# from rest_framework.response import Response
# from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .filters import AvailabilityFilter
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import Http404


# Create,update and delete users view
class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Create,update and delete Pet view
class PetListCreate(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class PetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


# Create,update and delete Grooming view
class GroomingListCreate(generics.ListCreateAPIView):
    queryset =Grooming.objects.all()
    serializer_class = GroomingSerializer


class GroomingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grooming.objects.all()
    serializer_class = GroomingSerializer


# Create,update and delete a Reservation date view
class ReservationListCreate(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


# Create,update and delete Availability date view
class AvailabilityListCreate(generics.ListCreateAPIView):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AvailabilityFilter


class AvailabilityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer


class AvailabilityReservationListCreate(generics.ListCreateAPIView):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer

    def get_queryset(self):
        date = self.kwargs['date']
        return Availability.objects.filter(date=date)


# Create,update and delete Schedule view, validations.
class ScheduleListCreate(generics.ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        availability_id = self.kwargs.get('availability_id')
        availability = get_object_or_404(Availability, pk=availability_id)
        if not Schedule.objects.filter(availability_id=availability).exists():
            raise Http404("No hay disponibilidad de fechas.")
        return Schedule.objects.filter(availability_id=availability)


class ScheduleCreateView(generics.ListCreateAPIView):
    model = Schedule
    fields = ['available_dates', 'available_hours', 'availability_id']
    success_url = reverse_lazy('schedule_list')


# Create
class EventCreate(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

