from django.db import models
from django.utils.translation import gettext_lazy as _



class Branch(models.Model):
    custom_number = models.PositiveBigIntegerField(_('custom no'), null=True, blank=True)
    arabic_name = models.CharField(max_length=255, null=True, blank=True)
    arabic_description = models.CharField(max_length=255, null=True, blank=True)
    english_name = models.CharField(max_length=255, null=True, blank=True)
    english_description = models.CharField(max_length=255, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.arabic_name or self.english_name or f'Branch {self.pk}'
