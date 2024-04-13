from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 7, "name": "Картофель фри", "quantity": 0},
    {"id": 8, "name": "Кепка", "quantity": 124},
]


def get_default(request):
    h_1 = "Изучаем django"
    text = "Автор: Уренцев А.П"


    context = {"h_1": h_1, "text": text}

    return render(request, 'home.html', context)


def get_about(request):
    name = "александр"
    patronymic = "павлович"
    surname = "уренцев"
    number = "8-923-600-01-02"
    email = "urentsev@mail.ru"

    about_data = {
        "имя": name,
        "отчество": patronymic,
        "фамилия": surname,
        "телефон": number,
        "email": email,
    }


    context = {'about_data': about_data}

    return render(request, 'about.html', context)


def get_item(request, number):
    try:
        result = items[number]
    except:
        result = f"Товар с id={number} не найден"
    return result
