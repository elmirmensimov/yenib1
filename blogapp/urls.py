from django.contrib import admin
from django.urls import path
from blogapp import views  # blogapp uygulamanızdaki views dosyasını dahil edin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
]