from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Reservation, Event
from .utils import send_telegram_message


@receiver(post_save, sender=Reservation)
def reservation_changed(sender, instance, created, **kwargs):
    if created:
        message = f"New reservation created: {instance}"
    else:
        message = f"Reservation updated: {instance}"
    send_telegram_message(message)


@receiver(post_delete, sender=Reservation)
def reservation_deleted(sender, instance, **kwargs):
    message = f"Reservation deleted: {instance}"
    send_telegram_message(message)


@receiver(post_save, sender=Event)
def event_created(sender, instance, created, **kwargs):
    if created:
        message = f"New event created: {instance.name}\nDate: {instance.date}\nTime: {instance.time}\nDescription: {instance.description}"
        send_telegram_message(message)