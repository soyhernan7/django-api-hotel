from django.db import models

from simple_history.models import HistoricalRecords

class BaseModel(models.Model):
    """Base Para todos los modelos"""
        
    id = models.AutoField(primary_key = True)
    active = models.BooleanField('Active', default = True)
    created_at = models.DateField('Created At', auto_now=False, auto_now_add=True, null=True)
    modified_at = models.DateField('Updated At', auto_now=True, auto_now_add=False, null=True)
    # changed_by = HistoricalRecords(user_model="users.User", inherit=True,)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        abstract = True
        verbose_name = 'BaseModel'
        verbose_name_plural = 'BaseModels'