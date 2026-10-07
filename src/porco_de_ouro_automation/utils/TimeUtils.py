import datetime

class TimeUtils:
    def __init__(self):
        self.week_days = [
            "Segunda-Feira",
            "Terça-Feira",
            "Quarta-Feira",
            "Quinta-Feira",
            "Sexta-Feira",
            "Sábado",
            "Domingo"
        ]
        self.months = [
            "Janeiro",
            "Feveiro",
            "Março",
            "Abril",
            "Maio",
            "Junho",
            "Julho",
            "Agosto",
            "Setembro",
            "Outubro",
            "Novembro",
            "Dezembro"
        ]
    
    def get_date_with_day_month(self, day_month):
        date_obj = day_month.split("/")
        date_obj = datetime.date(datetime.date.today().year, int(date_obj[-1]), int(date_obj[0]))
        return date_obj