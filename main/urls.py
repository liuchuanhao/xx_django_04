
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')), # 富文本编辑器
    url(r'^search', include('haystack.urls')), # 全文检索框架
    url(r'^user/', include('user.urls', namespace='user')), # 用户模块

]
