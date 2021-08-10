from django.urls import path, include


urlpatterns = [
    path("admin/", include("pv_analytics.api.v1.admin.urls")),
    path("base/", include("pv_analytics.api.v1.base.urls")),
]
