from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validar_altura(value):
    if value >= 28:
        raise ValidationError(
            _('Error {0} la altura es mayor  a 28'.format(value)),
        )