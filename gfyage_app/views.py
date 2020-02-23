from django.shortcuts import render, get_object_or_404
from .models import Audio
import markdown


def index(request):
    # 国风雅歌主页
    return render(request, 'gfyage_app/index.html')


def audios(request):
    # 雅歌音频
    audios = Audio.objects.filter().order_by('id')[0]
    context = {'audio': audios}
    return render(request, 'gfyage_app/audios.html', context)


def audio(request, audio_id):
    # 音频详细界面
    audio = Audio.objects.get(id=audio_id)
    audio.SingerIntro = markdown.markdown(audio.SingerIntro, extensions=['markdown.extensions.extra',  # 用于标题、表格、引用这些基本转换
                                                           'markdown.extensions.codehilite',  # 用于语法高亮
                                                           'markdown.extensions.toc',])[3:-4:1]  # 用于生成目录
    audio.SongIntro = markdown.markdown(audio.SongIntro,
                                          extensions=['markdown.extensions.extra',  # 用于标题、表格、引用这些基本转换
                                                      'markdown.extensions.codehilite',  # 用于语法高亮
                                                      'markdown.extensions.toc', ])  # 用于生成目录
    context = {'audio': audio}
    return render(request, 'gfyage_app/audio.html', context)


def video(request):
    # 演唱视频
    return render(request, 'gfyage_app/video.html')


def academic(request):
    # 学术专题
    return render(request, 'gfyage_app/academic.html')


def interview(request):
    # 访谈实录
    return render(request, 'gfyage_app/interview.html')


def poem(request):
    # 诗歌文摘
    return render(request, 'gfyage_app/poem.html')


def normal(request):
    # 师范教材
    return render(request, 'gfyage_app/normal.html')


def folk(request):
    # 国风色彩
    return render(request, 'gfyage_app/folk.html')
