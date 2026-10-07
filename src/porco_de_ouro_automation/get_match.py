import requests
import datetime
from utils.TimeUtils import TimeUtils
    
def get_match(matches):
    today_date = datetime.date.today()
    for match in matches:
        match_date = TimeUtils().get_date_with_day_month(match["data_jogo"])
        if today_date == match_date or today_date < match_date:
            return match
    return dict()

def main():
    url = "https://apiverdao.palmeiras.com.br/wp-json/apiverdao/v1/jogos-mes/?mes={month}&ano={year}&v=1"
    today_month = datetime.date.today().month
    today_year = datetime.date.today().year
    match_selected = {}
    while not bool(match_selected):
        response = requests.get(url.format(month=today_month, year=today_year), timeout=10)
        response.raise_for_status()
        response = response.json()
        match_selected = get_match(response["jogos"])
        if not bool(match_selected):
            today_month += 1
            if today_month == 13:
                today_month = 1
                today_year += 1
    
    time_utils = TimeUtils()
    home_team = match_selected["time_casa"]
    away_team = match_selected["time_visitante"]
    stadium = match_selected["estadio"]    
    match_date = time_utils.get_date_with_day_month(match_selected["data_jogo"])
    match_week_day = time_utils.week_days[match_date.weekday()]
    match_hour = match_selected["hora1"]
    match_month = time_utils.months[match_date.month-1]
    match_championship = match_selected["campeonato"]
    match_transmission = match_selected["excecao"]
        
    info_match = f"*PRÓXIMO JOGO*:\n{home_team} X {away_team}\n{stadium}\n{match_week_day}, {match_date.day} de {match_month} - {match_hour}\n{match_championship}\nTransmissão: {match_transmission}"    

    print(info_match)

if __name__ == "__main__":
    main()