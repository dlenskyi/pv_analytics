from django.views.generic import TemplateView
from django.utils.translation import gettext as _
from django.conf import settings


class AnonymousSection(TemplateView):
    template_name = "sections/anonymous.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _("PV Analytics")
        context["settings"] = settings
        return context


class AdminSection(TemplateView):
    template_name = "sections/admin.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _("Admin")
        context["settings"] = settings
        return context
