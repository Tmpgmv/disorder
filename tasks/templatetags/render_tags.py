from django import template
from django.template import Template, Context

register = template.Library()

@register.simple_tag(takes_context=True)
def render_db_template(context, text):
    t = Template(text)
    return t.render(Context(context))