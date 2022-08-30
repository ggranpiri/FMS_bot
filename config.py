TOKEN = '5193700613:AAGGLMJOLpAw_vBeeoDohcPERZ70ZZoxW30'

ADMINS = 1089524173, 979923466

# Словарь, который будет содержать данные вида Класс: id Классного советника
LETTERS = {
    'Бета': 0,
    'Гамма': 0,
    'Дельта': 0,
    'Эпсилон': 0,
    'Дзета': 0,
    'Эта': 1154607773,  # Игорь Валентинович Панченко
    'Тета': 0,
    'Йота': 812263756,     # Сергей Александрович Минденко
    'Каппа': 0,
    'Лямбда': 0
}

# Время утренних напоминаний
MORNING_TIME = '07:00'
# Время вечерних напоминаний
EVENING_TIME = '20:00'
# Время напоминаний в пятницу
FRIDAY_TIMES = ['08:20', '12:10', '14:15']
# Время подачи отчета в пятницу
FRIDAY_REPORT_TIME = '15:15'
# Время отправления отчета классным советникам
REPORT_TIME = '08:00'

# Сущности положительных и отрицательных ответов
YES, NO = 'да', 'нет'
POSITIVE = [YES, 'oui', 'lf', 'дп', 'yes', 'yep', 'ыыы', '+']
NEGATIVE = [NO, 'pas', 'no', '-']

# Список каникул (ДД.ММ). Должен дополняться
HOLIDAYS = ['01.09', '31.10', '01.05', '02.05', '09.05', '10.05']

# Названия файлов
USERS = 'users.json'
LOGS = 'logs.txt'
STATISTIC = 'stat.json'

# Кодировка, использующаяся повсеместно (кроме той консоли Линукса)
ENCODING = 'utf-8'

# Всякие константы названий "колонок" или полей словаря
NAME = 'name'
CLASS = 'class'
LUNCH = 'lunch'
VISIT = 'school_visit'
REASON = 'reason'
ALWAYS = 'permanently'

# Название списков, под которыми хранятся списки в файле users.json
STUDENTS = 'students'
CLASSES = 'classes'
DELETED = 'deleted'
