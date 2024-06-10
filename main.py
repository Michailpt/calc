import datetime as dt

DAY_LIMIT_CALORIES = 1000
today = dt.datetime.today().date()
date_format = '%d.%m.%Y'

class CaloriesCalculator:
    """Калькулятор калорий7"""
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        """Добавляем запись"""
        self.records.append(record)
        print(self.records)

    def get_today_stats(self):
        """Считать, сколько калорий уже получено сегодня"""
        today = dt.datetime.today().date()
        today_calories = sum(record.amount for record in self.records if record.date == today)
        print(f'Сегодня получено {today_calories} кКал')

    def get_calories_remained(self):
        """Cколько ещё калорий можно/нужно получить сегодня"""
        today = dt.datetime.today().date()
        today_calories = sum(record.amount for record in self.records if record.date == today)
        res = self.limit - today_calories
        if res > 0:
            print(f'Сегодня можно съесть что-нибудь, но не более {res} кКал')
        else:
            print(f'Лимит исчерпан, перебор на {-res} кКал')

    def get_week_stats(self):
        """Считать, сколько калорий получено за последние 7 дней"""
        today = dt.datetime.today().date()
        week_ago = today - dt.timedelta(days=7)
        week_calories = sum(record.amount for record in self.records if week_ago <= record.date <= today)
        print(f'Получено за последние 7 дней {week_calories} кКал')

class Record:
    """Запись о приёме пищи"""
    def __init__(self, amount, date, comment):
        self.amount = amount
        self.date = date
        self.comment = comment

# Создаем объекты
r1 = Record(amount=200, comment='творог', date=today)
r2 = Record(amount=300, comment='курица', date=today - dt.timedelta(days=1))
r3 = Record(amount=150, comment='тунец', date=today)

calc_calories = CaloriesCalculator(limit=DAY_LIMIT_CALORIES)

# Добавляем записи
calc_calories.add_record(r1)
calc_calories.add_record(r2)
calc_calories.add_record(r3)

# Выводим результаты
calc_calories.get_today_stats()
calc_calories.get_calories_remained()
calc_calories.get_week_stats()
