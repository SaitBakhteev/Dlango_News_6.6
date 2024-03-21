from datetime import datetime
from django.template.defaultfilters import register

@register.simple_tag()
def current_date(value):
    return datetime.strptime(value, "%d.%M.%Y")