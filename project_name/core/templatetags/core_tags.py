from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag
def active(request, urls):
    """ 
    add 'active' class to element if 'url_name' is in request.
    usage: {% active request 'url_name' %} 
    
    """
    if request.path in (reverse(url) for url in urls.split()):
        return 'active'
    return ''