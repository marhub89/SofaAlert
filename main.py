import os
import time
import requests
import telepot

# Legge variabili d'ambiente
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
RAPIDAPI_KEY = os.environ.get("RAPIDAPI_KEY")

bot = telepot.Bot(TELEGRAM_TOKEN)

def send_alert(message):
    try:
        bot.sendMessage(CHAT_ID, message)
        print("Messaggio inviato:", message)
    except Exception as e:
        print("Errore invio messaggio:", e)

def get_sofascore_live():
    url = "https://api.sofascore.com/api/v1/sport/football/events/live"
    try:
        r = requests.get(url, timeout=10)
        data = r.json()
        return data.get("events", [])
    except Exception as e:
        print("Errore SofaScore:", e)
        return []

def get_api_football_live():
    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures?live=all"
    headers = {"x-rapidapi-key": RAPIDAPI_KEY, "x-rapidapi-host": "api-football-v1.p.rapidapi.com"}
    try:
        r = requests.get(url, headers=headers, timeout=10)
        return r.json().get("response", [])
    except Exception as e:
        print("Errore API-Football:", e)
        return []

def monitor():
    send_alert("✅ Bot LIVE avviato e in ascolto (Railway)!")
    while True:
        sofascore_matches = get_sofascore_live()
        football_matches = get_api_football_live()

        if not sofascore_matches and not football_matches:
            print("Nessuna partita live trovata...")
        else:
            for m in sofascore_matches[:3]:
                msg = f"⚽ SofaScore Live: {m.get('tournament',{}).get('name')} - {m.get('homeTeam',{}).get('name')} vs {m.get('awayTeam',{}).get('name')}"
                send_alert(msg)

            for f in football_matches[:3]:
                teams = f.get("teams", {})
                home = teams.get("home", {}).get("name")
                away = teams.get("away", {}).get("name")
                msg = f"📊 API-Football Live: {home} vs {away}"
                send_alert(msg)

        time.sleep(60)

if __name__ == "__main__":
    monitor()
