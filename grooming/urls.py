from .views import (UserListCreate, UserDetail, PetListCreate, PetDetail, GroomingListCreate, GroomingDetail,
                    ReservationListCreate, ReservationDetail, AvailabilityListCreate, AvailabilityDetail, AvailabilityReservationListCreate, ScheduleListCreate,ScheduleCreateView,EventCreate)
from django.urls import path

urlpatterns = [
    path("users/", UserListCreate.as_view(), name="user_list_create"),
    path("users/<int:pk>/", UserDetail.as_view(), name="user_detail"),
    path("pets/", PetListCreate.as_view(), name="pet_list_create"),
    path("pets/<int:pk>/", PetDetail.as_view(), name="pet_detail"),
    path("groomings/", GroomingListCreate.as_view(), name="room_list_create"),
    path("groomings/<int:pk>/", GroomingDetail.as_view(), name="grooming_detail"),
    path("reservations/", ReservationListCreate.as_view(), name="reservation_list_create"),
    path("reservations/<int:pk>/", ReservationDetail.as_view(), name="reservation_detail"),
    path("availability/", AvailabilityListCreate.as_view(), name="availability_list_create"),
    path("availability/<int:pk>/", AvailabilityDetail.as_view(), name="availability_detail"),
    path("availability/reservations/<str:date>/", AvailabilityReservationListCreate.as_view(), name="available_reservation"),
    path("schedule/<int:availability_id>/", ScheduleListCreate.as_view(), name="schedule_list_create"),
    path('schedule/create/', ScheduleCreateView.as_view(), name='schedule_create'),
    path("event/create/", EventCreate.as_view(), name='event_create'),
]