# Binance Futures Trading Bot

A command-line trading bot built using Python that connects to the Binance Futures Testnet API. The application allows users to place Market and Limit orders from the terminal while validating inputs using Pydantic and logging all requests and errors.

---

## Features

- Place Market Orders
- Place Limit Orders
- Input validation using Pydantic
- Command-line interface using Typer
- Logging of API requests and errors
- Environment variable support using python-dotenv
- Binance Futures Testnet integration

---

# Setup

## 1. Clone the repository

```bash
git clone https://github.com/shshy911/binance-futures-trading-bot.git
cd binance-futures-trading-bot
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

## 3. Create a `.env` file

Create a file named `.env` in the project root.

```env
BINANCE_API_KEY=YOUR_API_KEY
BINANCE_API_SECRET=YOUR_API_SECRET
```

Generate these keys from the Binance Futures Testnet.

---

# Running the Application

## Market Order

```bash
python cli.py BTCUSDT BUY MARKET 0.001
```

Example Output

```
Order ID: xxxxxxxxx
Symbol: BTCUSDT
Side: BUY
Order Type: MARKET
Status: NEW
Executed Quantity: 0.001
Average Price: ...
```

---

## Limit Order

```bash
python cli.py BTCUSDT BUY LIMIT 0.001 --price 67000
```

Example Output

```
Order ID: xxxxxxxxx
Symbol: BTCUSDT
Side: BUY
Order Type: LIMIT
Status: NEW
Executed Quantity: 0.000
Average Price: None
```

---

# Assumptions

- The application is configured to use the Binance Futures **Testnet**.
- Users already possess valid Binance Testnet API credentials.
- Internet connectivity is available when placing orders.
- The Binance API enforces its own trading rules (price limits, quantity filters, etc.). Invalid orders are rejected by the API and reported by the application.
- API credentials are stored securely in a local `.env` file and are **not** committed to the repository.

---

# Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── logging_config.py
│   ├── orders.py
│   └── validators.py
│
├── cli.py
├── requirements.txt
├── README.md
└── .gitignore
```