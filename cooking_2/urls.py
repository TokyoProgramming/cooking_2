from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# from two_factor.urls import urlpatterns as tf_urls
# from two_factor.gateways.twilio.urls import urlpatterns as tf_twilio_urls

#
# from two_factor.admin import AdminSiteOTPRequired
#
# admin.site.__class__ = AdminSiteOTPRequired


urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
    path('account/', include('account.urls')),
    path('', include('blog.urls')),
    path('contact/', include('contact.urls')),

    # path('', include(tf_urls)),
    # path('', include(tf_twilio_urls)),

] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
