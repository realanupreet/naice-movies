
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from movieapp import views
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
app_name = 'main'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('', views.index),
    # path('login/', user_views.login_request, name='login'),
    # path('login/POST', user_views.login_request, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('logout/', user_views.logout_request, name='logout'),
    path('index/', views.index),
    path('details/<int:id>/', views.details),
    # path('login/POST', views.index),
]
urlpatterns = urlpatterns + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
