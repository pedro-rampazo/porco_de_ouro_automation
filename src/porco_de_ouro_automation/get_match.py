import os
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
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/jxl,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Cookie': 'FOOTSTATS_TOKEN=eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJieUJRZ05PMlpwaGF1LXNtNGVXd3BDbXIxUTdOcnJ6cXVHbXktWVcwNWRFIn0.eyJleHAiOjE3OTM5MDQ1OTMsImlhdCI6MTc5Mzg5MDE5MywianRpIjoidHJydGNjOmE3ZGYxZDk2LWJiMzQtMjgwMC1hYzVlLWNhZWE2ZGU5YWRiNSIsImlzcyI6Imh0dHBzOi8vc3NvLmZvb3RzdGF0cy5jb20uYnIvYXV0aC9yZWFsbXMvaTJhLWRldiIsImF1ZCI6WyJyZWFsbS1tYW5hZ2VtZW50IiwiYWNjb3VudCJdLCJzdWIiOiI4ZWE1NzE3My04NGZmLTRiYzctYTc0ZS1hNjFmYjc3MzJhMTciLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJwYWxtZWlyYXNwcm9kdcOnw6NvIiwiYWNyIjoiMSIsInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsImRlZmF1bHQtcm9sZXMtaTJhLWRldiIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsicmVhbG0tbWFuYWdlbWVudCI6eyJyb2xlcyI6WyJjcmVhdGUtY2xpZW50Iiwidmlldy1jbGllbnRzIiwicXVlcnktY2xpZW50cyIsIm1hbmFnZS1jbGllbnRzIl19LCJwYWxtZWlyYXNwcm9kdcOnw6NvIjp7InJvbGVzIjpbInVtYV9wcm90ZWN0aW9uIl19LCJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6InNvY2Nlci1nYXRoZXItYXBpX3Njb3BlcyIsImNsaWVudEhvc3QiOiIzLjIzMS40Ny4yMTEiLCJjbGllbnRJZCI6InBhbG1laXJhc3Byb2R1w6fDo28iLCJjbGllbnRBZGRyZXNzIjoiMy4yMzEuNDcuMjExIn0.VaDH4kSL8MHo0_z2_30FQAMP2a7cH8vhV0F0EKCVZBM8ODsNF4HHMEvQyanh4IDLwBNNvdRXiqYCGPvgUYI7XTi8OZFJvBYUeDnIPFnBgxPCoDiZ9Nlwg6x6GWVxAVv7uqzob6P7CJ9YvQaElUtdNEZD014E72lQLX7VpyBUtJaWZBVOSGmUrZPixD7nNDXxPIB2Fn5g_y9rbnFWQYBBwaGVJTBCXukaXwfa5l6ODbzaFycsPVc_WZQc9_gAM8_qP8UaBn1PX7zfdXgo2q96DSVsWZcr3QW1jnbEvs4KU28MLY5ZghAgT2tAe31tX6ng8C7P5kCee9PNmACj8A9ZJw',
        'Priority': 'u=0, i',
        'Sec-Ch-Ua': '"Not:A-Brand";v="8", "Chromium";v="156", "Google Chrome";v="156"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36'
    }
    url = "https://palmeiras.com.br/wp-json/apiverdao/v1/jogos-mes/?mes={month}&ano={year}&v=1"
    today_month = datetime.date.today().month
    today_year = datetime.date.today().year
    match_selected = {}
    while not bool(match_selected):
        response = requests.get(url.format(month=today_month, year=today_year), timeout=10, headers=headers)
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

    return info_match

if __name__ == "__main__":
    match = main()
    print(match)
    