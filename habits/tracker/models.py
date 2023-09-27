from django.conf import settings
from django.db import models
from django.utils import timezone


class HabitUnit(models.Model):
    symbol = models.CharField(max_length=20)
    human_readable_name = models.CharField(max_length=20)

    def __str__(self):
        return self.human_readable_name


class HabitType(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class HabitStatus(models.Model):
    STATUS_CHOICES = [
        ('Achieved', 'Achieved'),
        ('Active', 'Active'),
        ('Paused', 'Paused'),
        ('Inactive', 'Inactive'),
        ('Deleted', 'Deleted'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    type = models.ForeignKey(HabitType, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='Active')
    active_from = models.DateTimeField(default=timezone.now)
    active_to = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.user}'s {self.type} habit"

    class Meta:
        verbose_name_plural = 'Habit statuses'


class HabitEntry(models.Model):
    numeric_value = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    text_value = models.CharField(max_length=100, blank=True)
    status = models.ForeignKey(
        HabitStatus, on_delete=models.CASCADE, null=True)
    unit = models.ForeignKey(HabitUnit, on_delete=models.CASCADE)

    def is_numeric(self):
        return self.numeric_value is not None

    def __str__(self):
        if self.is_numeric():
            return f'{self.numeric_value} {self.unit.symbol}'
        else:
            return self.text_value

    class Meta:
        verbose_name_plural = 'Habit entries'


class HabitTarget(models.Model):
    numeric_value = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    text_value = models.CharField(max_length=100, blank=True)
    status = models.ForeignKey(
        HabitStatus, on_delete=models.CASCADE, null=True)
    unit = models.ForeignKey(HabitUnit, on_delete=models.CASCADE)

    def is_numeric(self):
        return self.numeric_value is not None

    def __str__(self):
        if self.is_numeric():
            return f'{self.numeric_value} {self.unit.symbol}'
        else:
            return self.text_value
