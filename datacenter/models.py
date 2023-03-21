import datetime
from django.db import models
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        entered_at = self.entered_at
        leaved_at = self.leaved_at

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(self):
        """Получение времени нахождения в хранилище"""
        duration = localtime() - localtime(self.entered_at)
        if self.leaved_at:
            duration = localtime(self.leaved_at) - localtime(self.entered_at)
        return duration

    def format_duration(self):
        """Формат полученного времени нахождения в хранилище"""
        duration = str(self.get_duration()).split(":")
        return f'{duration[0]} ч  {duration[1]} мин'

    def is_visit_long(self, minutes=10):
        """Подозрителен ли?"""
        sec = minutes * 60
        minuts = datetime.timedelta(seconds=sec)
        duration = self.get_duration()
        if duration > minuts:
            return True
        else:
            return False
