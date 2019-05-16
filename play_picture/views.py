import time
import _thread

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from play_picture.models import User, Suggester, Suggestion, Task, Picture


# Create your views here.


class IndexView(generic.TemplateView):
    template_name = 'play_picture/index.html'


class LoginView(generic.TemplateView):
    template_name = 'play_picture/login.html'


class AboutMeView(generic.TemplateView):
    template_name = 'play_picture/about-me.html'


class ServiceView(generic.TemplateView):
    template_name = 'play_picture/services.html'


class GalleryView(generic.TemplateView):
    template_name = 'play_picture/gallery.html'


class ContactView(generic.TemplateView):
    template_name = 'play_picture/contact.html'


class PersonalView(generic.DetailView):
    model = User
    template_name = 'play_picture/personal.html'


def validate(request):
    try:
        user = User.objects.get(username=request.POST['username'])
    except User.DoesNotExist:
        return JsonResponse({'stat': 1001, 'msg': '用户不存在'})

    real_pwd = user.password
    if request.POST['password'] == real_pwd:
        return JsonResponse({'stat': 1000, 'msg': user.id})
    else:
        return JsonResponse({'stat': 1001, 'msg': '密码错误'})


def register(request):
    try:
        user = User.objects.get(username=request.POST['username'])
    except User.DoesNotExist:
        new_user = User(nickname=request.POST['nickname'], email=request.POST['email'],
                        username=request.POST['username'], password=request.POST['password'])
        new_user.save()
        return JsonResponse({'stat': 1000, 'msg': new_user.id})

    return JsonResponse({'stat': 1001, 'msg': '用户已存在'})


def commit_s(request):
    name = request.POST['name']
    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']
    try:
        suggester = Suggester.objects.get(name=name)
    except Suggester.DoesNotExist:
        suggester = Suggester(name=name, email=email)
        suggester.save()

    suggestion = Suggestion(suggester=suggester, subject=subject, content=message)
    suggestion.save()

    return HttpResponse("建议提交成功!")


def img_handler(content, style, user, n_task):
    # do something here
    print(content, '\n', style)

    time.sleep(10)
    n_pic = Picture(user=user, img_path='/img/gallery/default.png', description='no description',
                    pub_date=timezone.now())
    n_pic.save()
    n_task.progress = 100
    n_task.state = 1
    n_task.save()


def commit_t(request):
    user = get_object_or_404(User, pk=request.POST['id'])
    content = request.POST['content']
    style = request.POST['style']

    n_task = Task(user=user, s_time=timezone.now(), c_time=0, progress=0, state=0)
    n_task.save()

    # 开个新线程进行图像处理
    _thread.start_new_thread(img_handler, (content, style, user, n_task,))

    return JsonResponse({'status': 'success', 'msg': '任务提交成功'})


def edit(request):
    user = get_object_or_404(User, pk=request.POST['id'])

    nickname = request.POST['nickname']
    age = request.POST['age']
    email = request.POST['email']

    user.nickname = nickname
    user.age = age
    user.email = email
    user.save()

    return JsonResponse({'status': 'success', 'msg': '信息修改成功'})


def get_time(request):
    # 更新task信息
    tasks = Task.objects.get(user_id=request.POST['id'])

    for task in tasks:
        task.c_time = timezone.now() - task.s_time
        print(task.c_time)
        task.save()

    return HttpResponse(1000)
