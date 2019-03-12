from django.contrib import admin
from django.urls import path, include

from pm.settings import actual

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls')),
    path('accounts/', include('accounts.urls')),
    # path('about/',),

]

if actual.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
