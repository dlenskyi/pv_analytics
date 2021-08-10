import csv

from django.http import HttpResponse
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment; filename={}.csv".format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = _("Експортувати вибрані об'єкти у .csv")


class ViewSetPagination(PageNumberPagination):
    page_size = settings.PAGE_SIZE
    page_size_query_param = "page_size"
    last_page_strings = ("last",)
    max_page_size = settings.MAX_PAGE_SIZE

    def paginate_queryset(self, queryset, request, view=None):
        # Return all records if page query parameter is not in request
        if "page" not in request.query_params:
            return None
        return super().paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data):
        return Response(
            {
                "links": {
                    "next": self.get_next_link(),
                    "previous": self.get_previous_link(),
                },
                "count": self.page.paginator.count,
                "total_pages": self.page.paginator.num_pages,
                "results": data,
            }
        )
