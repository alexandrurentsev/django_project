from django.http import HttpResponse


def get_default(request):
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Уренцев А.П.</i>
    """

    return HttpResponse(text)
