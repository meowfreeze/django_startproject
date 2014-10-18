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


@register.simple_tag(takes_context=True)
def append_to_get(context, k, v):
    """
    add a get parameter to the parameters already present in the url
    
    USAGE: {% append_to_get k v %}
    
    """
    params = context['request'].GET.copy()
    
    # prevent duplicate keys
    params.pop(k, None)
    
    template = '%s=%s'
    append = template % (k, v)
    
    if params:
        prefix = '&'
    else:
        prefix = ''
    
    result = []
    for k, v in params.iteritems():
        result.append(template % (k, v))
    
    return '?' + '&'.join(result) + prefix + append