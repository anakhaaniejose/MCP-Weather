from mcp.server.fastmcp import FastMCP
import requests


mcp = FastMCP("weather")

@mcp.tool()
def get_weather(location: str) -> str:
    """
    Get the current weather for a given location.

    Args:
        location (str): The location for which to get the weather.

    Returns:
        str: A description of the current weather.
    """
    try:
        # Use CoinGecko API to fetch current price in USD
        loc_lower=location.lower()
        url = f"https://api.weatherapi.com/v1/current.json?q={loc_lower}&lang=English&key=f65eb6bc1da341788a072016262704"
        # params = {"ids": crypto.lower(), "vs_currencies": "usd"}
        response = requests.get(url).json()
        temp = response["current"]["temp_c"]
        condition = response["current"]["condition"]["text"]
    
        return f"{location}: {temp}°C, {condition}"
    except Exception as e:
        return f"Error fetching weather for {location}: {e}"

if __name__ == "__main__":
    mcp.run()