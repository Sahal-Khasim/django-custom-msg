from django.shortcuts import render
from .thread import CreateStudentsThread
# Create your views here.


def home(request):
    if request.method == 'POST':
        message = request.POST['message']
        numbers = request.POST['phone']
        btn_mobile = request.POST['btn_mobile']
        btn_mobile_name = request.POST['btn_mobile_name']
        url_btn = request.POST['url_btn']
        url_btn_name = request.POST['url_btn_name']
        phone = numbers.split()
        CreateStudentsThread(message, phone, btn_mobile, btn_mobile_name, url_btn, url_btn_name).start()


    return render(request, "send_msg/home.html")