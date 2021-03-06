"""ata_mgmt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls, name='user_managment'),
	#url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^', admin.site.urls, name='home'),
#	url(r'^accounts/logout/$', auth_views.logout_then_login, name='logout'),
#	url(r'^accounts/login/$', auth_views.login, name='login'),
#	url(r'^accounts/user_edit/$', 'site1.views.user_edit', name='user_edit'),
#   url(r'^edit/(?P<arg_id>\w+)$', 'site1.views.edit_item', name='edit_item'),
#    url(r'^delete/(?P<arg_id>\d+)$', 'site1.views.del_item', name='delete_item'),
    url(r'^WjbzeYCe', 'site1.views.ssl'),
    url(r'^api/(?P<arg_mac>[a-zA-Z0-9]+)/sip/(?P<arg_2>[a-z]+)/registered/(?P<arg_3>[0-1])', 'site1.views.api_sip'),
    url(r'^api/(?P<arg_mac>[a-zA-Z0-9]+)/cellular/signal/(?P<arg_2>[a-z]+)', 'site1.views.api_cell'),
    url(r'^api/(?P<arg_mac>[a-zA-Z0-9]+)/internet/(?P<arg_2>[a-z]+)', 'site1.views.api_inet'),
    url(r'^api2/(?P<arg_api_key>[a-zA-Z0-9]+)/((?P<arg_mac>[a-zA-Z0-9]+)/)?status', 'site1.views.api2_state'),
    url(r'^api2/(?P<arg_api_key>[a-zA-Z0-9]+)/new_device', 'site1.views.api2_new_device'),
    url(r'^api2/(?P<arg_api_key>[a-zA-Z0-9]+)/(?P<arg_mac>[a-zA-Z0-9]+)/reboot', 'site1.views.api2_reboot'),
    url(r'^api2/(?P<arg_api_key>[a-zA-Z0-9]+)/(?P<arg_mac>[a-zA-Z0-9]+)/update', 'site1.views.api2_update'),
    url(r'^api/(?P<arg_mac>[a-zA-Z0-9]+)/update', 'site1.views.api_update'),
]
# ======================================

admin.autodiscover()
