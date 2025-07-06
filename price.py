import requests

def get_token_price(symbol):
    symbol = symbol.lower()

    # Step 1: Search for the token dynamically on CoinGecko
    search_url = f"https://api.coingecko.com/api/v3/search?query={symbol}"
    try:
        search_res = requests.get(search_url)
        search_data = search_res.json()
        coins = search_data.get("coins", [])

        if not coins:
            return f"❌ Token '{symbol}' not found on CoinGecko."

        # Step 2: Use the first matching result
        token_id = coins[0]["id"]

        # Step 3: Fetch price using the token ID
        price_url = f"https://api.coingecko.com/api/v3/simple/price?ids={token_id}&vs_currencies=usd"
        price_res = requests.get(price_url)
        price_data = price_res.json()

        if token_id in price_data:
            price = price_data[token_id]["usd"]
            return f"💸 {symbol.upper()} is ${price} USD"
        else:
            return f"❌ Price not available for '{symbol.upper()}'."

    except Exception as e:
        return f"❌ Error fetching price: {str(e)}"