from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse


def signup(request):
    data = dict()
    if request.method == 'GET':
        data['title'] = 'Регистрация'
        return render(request, 'account/signup.html', context=data)
    elif request.method == 'POST':
        # 1- Извлечение данных из словаря POST:
        name_x = request.POST.get('name')
        email_x = request.POST.get('email')
        pass1_x = request.POST.get('pass1')
        pass2_x = request.POST.get('pass2')

        # 2 - тех проверка
        data['name'] = name_x
        data['email'] = email_x
        data['pass1'] = pass1_x
        data['pass2'] = pass2_x

        # 3 - Валидация данных на стороне сервера:
        if pass1_x != pass2_x:
            data['color'] = 'red'
            data['report'] = 'Введенные пароли не совпадают!'
        elif name_x == '...':
            # остальные провеки ...
            pass
        else:
            # Регистрация
            user = User.objects.create_user(name_x, email_x, pass1_x)
            user.save()
            if user is None:
                data['color'] = 'red'
                data['report'] = 'В регистрации отказано!'
            else:
                data['report'] = 'Регистрация успешно завершена'
                data['color'] = 'cadetblue'
        # Fin - Отправка репорта
        data['title'] = 'Отчет о регистрации'
        return render(request, 'account/report.html', context=data)


def signin(request):
    data = dict()
    if request.method == 'GET':
        data['title'] = 'Авторизация'
        return render(request, 'account/signin.html', context=data)
    elif request.method == 'POST':
        # 1 Получение данных из формы авторизации
        name_x = request.POST.get('name')
        pass1_x = request.POST.get('pass1')
        # 2 Получение подлиности значений логин/пароль
        user = authenticate(request, name=name_x, password=pass1_x)
        # 3- Валидация данных на стороек сервера:
        if user is None:
            data['color'] = 'red'
            data['report'] = 'Пользователь не найден!'
            data['title'] = 'Отчет об авторизации'
            return render(request, 'account/report.html', context=data)
        else:
            login(request, user)
            return redirect('/index')

def signout(request):
    logout(request)
    return redirect('/index')
