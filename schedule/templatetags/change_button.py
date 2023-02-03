
from django import template


register = template.Library()

@register.simple_tag
def update_btn_text(request, btn):

    updated = request.GET.copy

    if updated["text"] == "Complete":
        btn.configure(text="Undo")
    else:
        btn.configure(text="Complete")

    return updated.configure
