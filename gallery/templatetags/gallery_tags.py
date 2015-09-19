from django import template

register = template.Library()

@register.inclusion_tag('gallery/taglist.html')
def list_tags(tags):
    return {'tags': tags.all}