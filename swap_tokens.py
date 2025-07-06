import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("RECALL_API_KEY")
BASE_URL = "https://api.sandbox.competitions.recall.network"

def swap_tokens(from_token, to_token, amount):
    endpoint = f"{BASE_URL}/api/trade/execute"
    payload = {
        "fromToken": token_address(from_token),
        "toToken": token_address(to_token),
        "amount": str(amount),
        "reason": "LangChain AI swap request"
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        print("\U0001F504 Submitting swap request...")
        resp = requests.post(endpoint, json=payload, headers=headers, timeout=30)
        if resp.ok:
            return f"✅ Swap successful! Tx: {resp.json()}"
        else:
            return f"❌ Swap Failed: {resp.status_code} {resp.text}"
    except Exception as e:
        return f"❌ Error: {str(e)}"

def token_address(symbol):
    addresses = {
        "USDC": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
        "DAI":  "0x6B175474E89094C44Da98b954EedeAC495271d0F",
        "WETH": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
    }
    return addresses.get(symbol.upper(), "")
