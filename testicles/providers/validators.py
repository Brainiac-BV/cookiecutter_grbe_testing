from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from datetime import date

def date_valid(val): 
    today = date.today() 
    #value = date(val) 
    if val < today: 
        return ValidationError(_('no time machine available'), params= {'val': val})

