#imports
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

#const
USER = get_user_model()

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(
        verbose_name=_("Criando em"),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Atualizando em"),
        auto_now=True
    )

    class Meta:
        ordering = ['-created_at']
        abstract = True
        
class MonitoredModel(BaseModel):
    created_by = models.ForeignKey(
        verbose_name=_("Criado por"),
        to=USER,
        on_delete=models.SET_NULL
    )
    
    class Meta:
        abstract = True