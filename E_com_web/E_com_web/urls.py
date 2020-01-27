from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from.import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name="E_com homepage"),
    path('shop/', include('shop.urls')),
    path('blog/', include('blog.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
