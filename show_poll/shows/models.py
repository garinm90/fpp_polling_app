from django.db import models
from django.core.validators import validate_ipv4_address


class Show(models.Model):
    user = models.OneToOneField(
        'users.CustomUser', on_delete=models.CASCADE, related_name='show')
    ip_address = models.GenericIPAddressField(null=True,
                                              blank=True, protocol='IPv4')
    show_username = models.CharField(max_length=255)
    show_password = models.CharField(max_length=255)


class Playlist(models.Model):
    show = models.ForeignKey(
        Show, on_delete=models.CASCADE, related_name="playlists",)
    name = models.CharField(max_length=255)
    total_duration = models.DurationField()
    sequence = models.CharField(max_length=255)
