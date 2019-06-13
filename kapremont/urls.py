from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
                  path('jet/', include('jet.urls', 'jet')),
                  path('admin/', admin.site.urls),
                  path('fond/', include('fond.urls')),
                  path('sobstvenikam/', include('sobstvenikam.urls')),
                  path('ckeditor/', include('ckeditor_uploader.urls')),
                  path('reports/', include('reports.urls')),
                  path('bargaining/', include('bargaining.urls')),
                  path('', include('news.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
