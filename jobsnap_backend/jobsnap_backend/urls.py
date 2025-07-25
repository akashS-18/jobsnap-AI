from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/generator/', include('generator.urls')),
    path('api/jobai/', include('jobai.urls')),
]