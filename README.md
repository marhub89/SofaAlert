# Bot Live Betting (Railway)

Questo bot unisce **Sofascore** + **API-Football** per mandare alert in tempo reale su Telegram.

## Deploy su Railway

1. Crea un repository GitHub con questi file.
2. Su Railway: **New Project** → **Deploy from GitHub repo**.
3. In **Variables** aggiungi:
   - `TELEGRAM_TOKEN`
   - `CHAT_ID`
   - `RAPIDAPI_KEY`
4. Railway farà il deploy automatico.
5. Nei logs vedrai: `✅ Bot LIVE avviato e in ascolto (Railway)!`
6. Riceverai notifiche su Telegram.

