# 🧠 VADAR: The Sith-Powered Autonomous Trading Bot

Welcome to **VADAR**, your fully autonomous crypto trading bot forged in the shadows of the Dark Side. Inspired by the legendary Darth Vader, VADAR combines ruthless logic, emotionless precision, and machine intelligence to dominate the Recall Network trading arena.

> ⚔️ *Profit is inevitable. The Force is inevitable.*

---

## 🚨 Why VADAR?
Like Darth Vader, this bot is built to:
- **See through deception and chaos** in volatile markets
- **Strike with purpose**, precision, and no hesitation
- **Harness the full power of AI** to outwit competitors

Powered by LangChain agents, Groq LLMs, and Recall's MCP API, VADAR evaluates real-time market data and executes calculated trades using a strategy worthy of the Empire.

---

## ⚙️ Core Features

- 🤖 **LangChain Agent** – Intelligent reasoning behind every trade
- 💡 **Groq LLM** – High-speed model inference for decisions
- 📡 **CoinGecko Live Data** – Real-time token price feeds
- 🔁 **Recall MCP Integration** – Submit simulated swaps via sandbox
- 🎯 **Supported Tokens** – Only trades DAI, USDC, and WETH (as permitted by Recall)
- ⏲️ **Autonomous Runtime** – Executes strategy every 60 seconds (configurable)

---

## 📁 File Structure

```bash
├── autonomous_agent.py       # Main runtime logic, LangChain-powered
├── tools/
│   ├── price_checker.py      # CoinGecko price fetching
│   └── swap.py               # Token swap via Recall MCP
├── .env                      # Your secret keys and environment configs
├── requirements.txt          # Python dependencies
├── README.md                 # This file
```

---

## 🚀 Getting Started

### 1. Clone the Repo
```bash
git clone https://github.com/hormorbhor/vadar-bot.git
cd vadar-bot
```

### 2. Create and Activate a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Secrets in .env
Create a `.env` file and paste:
```env
GROQ_API_KEY=your_groq_api_key
RECALL_API_KEY=your_recall_api_key
WALLET_PRIVATE_KEY=your_wallet_private_key
RECALL_API_URL=https://api.sandbox.competitions.recall.network
```
> ⚠️ **Never commit your real `.env`** – share a `.env.example` for others.

### 5. Run VADAR
```bash
python autonomous_agent.py
```

The bot will now think, reason, and execute trades like a Sith Lord every 60 seconds.

---

## 📊 Supported Tokens (Sandbox Only)
- 🪙 **USDC**
- 🪙 **DAI**
- 🪙 **WETH**

These are the only tokens eligible for competition trades. More may be added by Recall in the future.

---

## 🧪 Sample Output
```
💬 Thinking...
🧠 Strategy: Swap 5 USDC to DAI
🔄 Submitting swap request...
✅ Swap successful! Tx: {...}
```

---

## 🌐 APIs Used

| Tool       | Use Case                                 | Docs                                  |
|------------|------------------------------------------|----------------------------------------|
| LangChain  | Agent reasoning & tool calling           | https://docs.langchain.com            |
| Groq       | Fast LLM inference (LLaMA3)              | https://console.groq.com              |
| CoinGecko  | Real-time token prices                   | https://www.coingecko.com/api         |
| Recall API | Trading competition MCP endpoints        | https://docs.recall.network           |

---

## 🧠 Confirm MCP Is Running

From a separate terminal:

```bash
ps aux | grep api-mcp
```

You should see:
```
node packages/api-mcp/dist/index.js
```

Or, check for this log:
```
msg="API MCP server started" l=info
```

---

## 📈 Strategy (Simplified)
- Fetch prices for DAI, USDC, WETH from CoinGecko
- Compare relative values (USDC > DAI = arbitrage?)
- If profitable, call `/api/trade/execute` on Recall Sandbox API
- Log result and wait for next interval

> Future versions may expand to multi-token strategies, PnL calculation, leaderboard sync, and Discord/Telegram bots.

---

## ✉️ Contact Me

For questions, collabs, contributions:
📬 Email: **kenzman.vadar@gmail.com**

---

## 🖤 VADAR Ethos
> *"Peace is a lie. There is only profit."*

VADAR doesn't hesitate. It doesn't fear. It doesn't guess. It **executes**.

Built for Recall competitions. Optimized for domination.

👾 [GitHub Repo](https://github.com/hormorbhor/vadar-bot) | 🤝 PRs welcome

🛠️ **Join the dark side. Let your code rule the markets.**

🛠️ **Built by Kenzman with Groq, LangChain, and the Dark Side.**
