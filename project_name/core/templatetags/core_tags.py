from django import template
from django.core.urlresolvers import reverse


register = template.Library()


@register.simple_tag(takes_context=True)
def active(context, url, *args, **kwargs):
    """ 
    add 'active' class to element if url 'namespace:name' is in request.
    
    USAGE: 
    
    returns 'active' if full url is matched:
    
    active 'namespace:name' args
    active 'namespace:name' args
    
    returns 'active' if url segment is matched:
    
    active 'namespace:name' args segment=True
    active 'namespace:name' args segment=True
    """
    
    request = context['request']
    segment = kwargs.get('segment')
    
    if segment:
        if reverse(url, args=args) in request.path:
            return 'active'
    else:
        if request.path == reverse(url, args=args):
            return 'active'
    return ''


@register.simple_tag(takes_context=True)
def append_to_get(context, k, v):
    """
    add a get parameter to the parameters already present in the url
    
    USAGE: 
    
    append_to_get k v
    
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
    for k in params.keys():
        result.append(template % (k, params[k]))
    
    return '?' + '&'.join(result) + prefix + append


@register.simple_tag
def proportional(x, y, factor):
    """ return a ratio multiplied by a factor """
    if all(isinstance(x, int) or isinstance(x, float) for x in (x, y, factor)):
        return x / y * factor
    return ''