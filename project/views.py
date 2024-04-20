from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from main_app.models import Item


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
    # получение всех items
    items = Item.objects.all()
    context = {"items": items}

    return render(request, "items.html", context)


def get_item_detail(request: HttpRequest, item_id: int) -> HttpResponse:
    """
    Возвращает item по id
    """
    item = Item.objects.filter(id=item_id)
    return render(request, "item_detail.html", {"item": item[0]})
