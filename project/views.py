from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 7, "name": "Картофель фри", "quantity": 0},
    {"id": 8, "name": "Кепка", "quantity": 124},
]


def get_home_page(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html")


def get_about(request: HttpRequest) -> HttpResponse:
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

    context = {"about_data": about_data}

    return render(request, "about.html", context)


def get_item(request: HttpRequest) -> HttpResponse:
    context = {"items": items}

    return render(request, "items.html", context)


def get_item_detail(request: HttpRequest, item_id: int) -> HttpResponse:
    item = next((item for item in items if item["id"] == item_id), None)
    return render(request, "item_detail.html", {"item": item})
