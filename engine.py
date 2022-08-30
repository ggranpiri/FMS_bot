from telebot.types import *
# Нереализованная фича с вариантами вопросов
# from random import choice
from datetime import datetime as dt, timedelta as td, date
import pymorphy2

from config import *

# Чтобы изменять слова
morph = pymorphy2.MorphAnalyzer()


def get_date() -> str:
    """Получение строки с датой и временем сейчас"""
    return dt.now().strftime("%d.%m.%Y %H:%M:%S")


def get_planning_day(formatted=True, need_date=True, na=False, strong=False, need_weekday=True) -> Union[str, date]:
    """Получение строки с датой и временем, на которые будут записаны данные"""
    # Возможно, стоит разделить эту функцию на много разных, каждая из которых будет отвечать за свой параметр
    # И вызывать эту, но только для получения даты в формате datetime

    months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
              'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    next_days = ['сегодня', 'завтра']
    weekdays = ['понедельник', 'вторник', 'среду', 'четверг', 'пятницу', 'субботу', 'воскресенье']
    v_weekdays = [['в ', 'во '][day[:2] == 'вт'] + day for day in weekdays] + next_days
    na_weekdays = ['на ' + day for day in weekdays + next_days]

    # Дата сейчас
    now = dt.now()
    report_time = now.replace(**dict(zip(['hour', 'minute'], map(int, REPORT_TIME.split(':')))))
    delta = now > report_time + td(hours=strong)    # Если время после 8:00, запись уже на следующий день

    # if now.weekday() == 4:
    #     fri_rep_time = now.replace(**dict(zip(['hour', 'minute'], map(int, FRIDAY_REPORT_TIME.split(':')))))
    #     delta = now > fri_rep_time + td(hours=strong)
    # else:
    #     delta = now > report_time + td(hours=strong)    # Если время после 8:00, запись уже на следующий день

    while (now + td(days=delta)).strftime('%d.%m') in HOLIDAYS or (now + td(days=delta)).weekday() == 6:
        delta += 1

    planning_date = now + td(days=delta)

    if not formatted:   # Бывает, что нужна именно дата в типе date
        return planning_date.date()

    # if delta == 0:  # Значит можно заменить на "сегодня"
    #     weekday = [v_weekdays, na_weekdays][na][-2]
    # elif delta == 1:  # Значит можно заменить на "завтра"
    #     weekday = [v_weekdays, na_weekdays][na][-1]
    # else:
    #
    # Но пользователям фича не понравилась

    weekday = [v_weekdays, na_weekdays][na][planning_date.weekday()]

    return f'{weekday}' * need_weekday + f' ({planning_date.day} {months[planning_date.month - 1]})' * need_date


def dump(obj: Union[list, dict, str], filename: str) -> None:
    """Функция для упрощения внесения данных в файлы"""
    if isinstance(obj, str):
        open(filename, 'w', encoding=ENCODING).write(obj)
    else:  # Для записи с использованием моей функции format_json
        json.dump(obj, open(filename, 'w', encoding=ENCODING), ensure_ascii=False, indent=2)


def make_bool_keyboard(one_time=True) -> ReplyKeyboardMarkup:
    """Возвращает клавиатуру, состоящую из кнопок 'Да' и 'Нет'"""
    keyboard = ReplyKeyboardMarkup(True, one_time_keyboard=one_time)
    keyboard.add(KeyboardButton(YES.capitalize()), KeyboardButton(NO.capitalize()))
    return keyboard


def make_keyboard(values: iter, one_time=True) -> ReplyKeyboardMarkup:
    """Возвращает клавиатуру, содержащую кнопки со значениями values"""
    keyboard = ReplyKeyboardMarkup(True, one_time_keyboard=one_time)
    for value in values:
        key1 = KeyboardButton(value)
        keyboard.add(key1)
    return keyboard


def get_fullname(message: Message) -> str:
    """Возвращает ФИ пользователя, под которыми он зарегистрирован в Телеграмм"""
    name = (message.from_user.last_name or ' ') + ' ' + message.from_user.first_name
    return name.strip().title()


def reform(word: str, main_word: int) -> str:
    """Возвращает слово, измененное под числительное, переданное вторым параметром"""
    word_form: pymorphy2.analyzer.Parse = morph.parse(word)[0]
    return word_form.make_agree_with_number(main_word).word


def make_empty_message(chat_id: int) -> Message:
    """Создание (имитация) пустого сообщения от пользователя"""
    # Кажется, этого не было задумано в этой библиотеке

    chat = Chat(int(chat_id), None)
    return Message(0, chat, '', chat, '', '', '')


def format_json(m, level=0, indent=4) -> str:
    """Получает список или словарь, возвращает строку, отформатированную почти по формату JSON.
    Писал сам, в целях экономии символов в файле STAT"""
    margin = ' ' * indent * level
    if isinstance(m, dict):
        text = '{' + '\n' * bool(m)
        for n, i in enumerate(m, 1):
            text += margin + ' ' * indent + f'"{str(i)}": '
            text += format_json(m[i], level + 1, indent=indent)
            if n != len(m):
                text += ',\n'
            else:
                text += '\n'
        text += '}'
    else:
        if m and isinstance(m[0], list):
            text = '[\n'
            for n, i in enumerate(m, 1):
                text += margin + ' ' * indent
                text += format_json(i, level + 1, indent=indent)
                if n != len(m):
                    text += ',\n'
                else:
                    text += '\n'
            text += margin + ']'

        else:
            text = str(list(m)).replace("'", '"')
    return text
