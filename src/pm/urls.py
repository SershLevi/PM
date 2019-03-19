from django.contrib import admin
from django.urls import path, include

from pm.settings import actual as settings

# TODO: Укзадать наименование в адинке и прочем
admin.site.site_header = "UMSRA Admin"
admin.site.site_title = "UMSRA Admin Portal"
admin.site.index_title = "Welcome to UMSRA Researcher Portal"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),
    path('accounts/', include('accounts.urls')),
    # path('about/',),

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
