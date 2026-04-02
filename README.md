# (Real-Time Intraday Trading Tool)

A real-time stock scanner built in Python that analyzes NIFTY stocks using technical indicators like VWAP, RSI, MACD, Moving Averages, and ORB (Opening Range Breakout) to generate trading signals.

--------------------------------------------------

FEATURES

- Real-time stock data using Yahoo Finance
- Technical indicators:
  - VWAP
  - RSI
  - MACD
  - Moving Averages (MA20, MA50)
- Strategy-based signal generation (BUY / STRONG BUY / NO SIGNAL)
- Live terminal dashboard using Rich library
- Score-based filtering for high-probability trades
- Auto-refresh every 5 seconds

--------------------------------------------------

STRATEGY LOGIC

The scanner assigns a score based on multiple conditions:

- High of Day Breakout
- VWAP Breakout
- Volume Spike
- RSI > 60
- MACD Crossover
- Moving Average Trend

Signal generation:
- Score >= 4 → STRONG BUY
- Score >= 3 → BUY
- Else → NO SIGNAL

--------------------------------------------------

PROJECT STRUCTURE

- app.py               → Flask API server
- scanner.py           → Main live scanner (terminal UI)
- run_scanner.py       → Run scanner via terminal
- data_fetcher.py      → Fetch stock data (yfinance)
- indicators.py        → Technical indicators
- strategy.py          → Signal generation logic
- nifty500.py          → List of NIFTY stocks
- test.py              → Single stock test script
- requirements.txt     → Dependencies
- run_app.bat          → Windows runner

--------------------------------------------------

INSTALLATION

1. Clone the repository:
   git clone <your-repo-url>
   cd stock-scanner

2. Install dependencies:
   pip install -r requirements.txt

Dependencies:
- flask
- pandas
- yfinance

--------------------------------------------------

USAGE

Run Live Scanner:
python scanner.py

OR
python run_scanner.py

--------------------------------------------------

Run Web App:
python app.py

Open in browser:
http://localhost:5000

API endpoint:
GET /api/scan

--------------------------------------------------

Test Single Stock:
python test.py

--------------------------------------------------

LIMITATIONS

- Uses Yahoo Finance (1-minute data) → may lag
- Not suitable for high-frequency trading
- No risk management included
- Requires internet connection

--------------------------------------------------

FUTURE IMPROVEMENTS

- Add Stop Loss & Target
- Add Options Data (OI, PCR)
- Add Order Flow / Footprint
- Build Web Dashboard
- Add Alerts (Telegram / Email)

--------------------------------------------------

AUTHOR

Rohit Kumar

--------------------------------------------------

LICENSE

This project is for educational purposes only.
Do not use directly for live trading without proper risk management.

--------------------------------------------------

SUPPORT

If you like this project:
- Star the repo
- Fork it
- Improve strategies
