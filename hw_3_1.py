# Функція №1
from datetime import datetime

def get_days_from_today(date_str: str) -> int:
    """
    Функція в якості аргументу отримує строку у форматі 'РРРР-ММ-ДД'
    і повертає різницю між поточною датою та заданою датою як ціле число
    """
    try:
        date_object = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print(f"Помилка: дата '{date_str}' має бути у форматі РРРР-ММ-ДД")
        return None

    current_date = datetime.today().date()
    date_difference = date_object.toordinal() - current_date.toordinal()
    return date_difference

#print(get_days_from_today("2021-12-21"))

