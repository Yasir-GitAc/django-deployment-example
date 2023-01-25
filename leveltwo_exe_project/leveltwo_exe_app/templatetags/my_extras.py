from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
  """
  this cuts out all value of 'arg' from the string
  """
  return value.replace(arg,'')

#u have to register ur filter function.like below.first arg is what u want to call it.
# second the function itself .

#register.filter('cut',cut)

#we can do this in a better way with decorators..like above line 5.

