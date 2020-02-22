from django.conf.urls import url
from . import views

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),
    url(r'^yageyinpin/$',views.audios, name='audios'),
    url(r'^yageyinpin/(?P<audio_id>\d+)/$',views.audio, name='audio'), # 雅歌音频内容

    url(r'^yanchangshipin/$',views.video, name='video'),
    url(r'^xueshuzhuanti/$',views.academic, name='academic'),
    url(r'^fangtanshilu/$',views.interview, name='interview'),
    url(r'^shigewenzhai/$',views.poem, name='poem'),
    url(r'^shifanjiaocai/$', views.normal, name='normal'),
    url(r'^guofengsecai/$', views.folk, name='folk'),
]

app_name = 'gfyg'