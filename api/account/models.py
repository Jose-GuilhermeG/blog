#imports
from django.db import models
from api.core.constants import LONG_FILED_LENGTH, MEDIUM_FILED_LENGTH
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.


#models
class User(
    AbstractUser
):
    name = models.CharField(
        verbose_name=_("Nome publico do usuario"),
        max_length=MEDIUM_FILED_LENGTH,
        unique=False,
        blank=False
    )
    
    username = models.CharField(
        verbose_name=_("Nome de usuario"),
        max_length=MEDIUM_FILED_LENGTH,
        unique=True,
        help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.")
    )
    
    image = models.ImageField(
        verbose_name= _("Imagem do usuario"),
        upload_to='users/profiles/',
        blank=True,
        null=True,
        help_text=_("Optional. Upload an image for the user profile.")
    )
    
    email = models.EmailField(
        verbose_name=_("Email do usuario"),
        max_length=LONG_FILED_LENGTH,
        unique=True,
        help_text=_("Required. Enter a valid email address.")
    )
    
    created_at = models.DateTimeField(
        verbose_name=_("Criando em"),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Atualizando em"),
        auto_now=True
    )
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = _("Usuario")
        verbose_name_plural = _("Usuarios")
        ordering = ['-created_at']