from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
                       url(r'^$', 'blog.views.home', name='home'),
                       url(r'^ver_post/(?P<id_post>[0-9]+)/$', 'blog.views.ver_post', name='vermipost'),
                       url(r'^contactame/$', 'blog.views.contact', name='contactame'),
                       
)