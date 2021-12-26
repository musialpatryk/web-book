from django import template

register = template.Library()

@register.filter(name="has_group")
def has_group(user, role):
    for group in user.groups.all():
        if group.name == role:
            return True

    return False