from django import template
register = template.Library()

@register.filter(name='addclass')
def addclass(field, css):
    return field.as_widget(attrs={"class":css})

@register.filter(name='addattrs')
def addattrs(field, attributes):
    return field.as_widget(attrs=attributes)

@register.filter(name='htmlattrs')
def htmlattributes(value, arg):
    attrs = value.field.widget.attrs
    
    keys = arg.split(',') 

    for key in keys:
        args = key.split(':')
        args[0] = args[0].replace(' ', '')
        attrs[args[0]] = args[1]

    rendered = str(value)
    return rendered



