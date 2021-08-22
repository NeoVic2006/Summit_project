from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from api import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
#from store.views import registerPage


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/', include('blog.urls')),
    path('store/', include('store.urls')),
    
    #path('api/blogs/', views.apibloglist),  # with function 
    path('api/blogs/', views.APIBlogList.as_view()),  # with class
    #path('register/', registerPage, name="register")

    #path('', include("django.contrib.auth.urls")),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'), 
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),  
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
