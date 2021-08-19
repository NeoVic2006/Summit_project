from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from api import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/', include('blog.urls')),
    path('store/', include('store.urls')),
    #path('api/blogs/', views.apibloglist),  # with function 
    path('api/blogs/', views.APIBlogList.as_view()),  # with class

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'), 
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),  
]
