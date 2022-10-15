import datetime


def year(request):
    """Добавляет переменную с текущим годом."""
    now = int(datetime.datetime.today().year)
    return {
        "year": now,
    }
