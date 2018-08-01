from django.conf.urls import  include, url
from . import views

urlpatterns = (
    # Examples:
    url(r'^$', views.index, name='index'),
    # url(r'^api/user/$', 'api_user'),
    url(r'^skin_config/$', views.skin_config, name='skin_config'),
    url(r'^login/$', views.Login, name='login'),
    url(r'^logout/$', views.Logout, name='logout'),
    url(r'^exec_cmd/$', views.exec_cmd, name='exec_cmd'),
    url(r'^file/upload/$', views.upload, name='file_upload'),
    url(r'^file/download/$', views.download, name='file_download'),
    url(r'^setting', views.setting, name='setting'),
    url(r'^terminal/$', views.web_terminal, name='terminal'),
    url(r'^juser/', include('juser.urls')),
    url(r'^jasset/', include('jasset.urls')),
    url(r'^jlog/', include('jlog.urls')),
    url(r'^jperm/', include('jperm.urls')),
)
