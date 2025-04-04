
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('members/', include('django.contrib.auth.urls')), # will look for builtin urls first
    path('members/', include('members.urls')), # otherwise looks at members/urls.py
]
