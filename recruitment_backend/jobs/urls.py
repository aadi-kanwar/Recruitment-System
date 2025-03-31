from django.urls import path
from .views import ApplicationListView, JobListCreateView, ApplicationCreateView

urlpatterns = [
    path("jobs/", JobListCreateView.as_view(), name="job-list"),
    path("applications/", ApplicationListView.as_view(), name="application-list"),  # ✅ Correct URL
    path("applications/create/", ApplicationCreateView.as_view(), name="application-create"),  # ✅ For POST
]
