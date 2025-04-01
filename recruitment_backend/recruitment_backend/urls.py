from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.conf import settings
from django.conf.urls.static import static

def redirect_to_api(request):
    return JsonResponse({"message": "API root. Use /api/jobs/ or /api/applications/."})

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("jobs.urls")),  # ✅ Replace 'jobs' with your actual app name
    path("", redirect_to_api),  # Redirect root requests to API message
]

# Serve media files during development (important for resume uploads)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
