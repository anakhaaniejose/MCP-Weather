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
    weather_data = {
        "san francisco": "Sunny, 72 degrees F",
        "new york": "Cloudy, 65 degrees F",
        "london": "Rainy, 58 degrees F",
        "tokyo": "Clear, 68 degrees F"
    }
    # Here you would implement the logic to fetch the weather data from an API
    # For demonstration purposes, we'll return a dummy weather report
    location_key = location.lower()
    if location_key in weather_data:
        return f"The current weather in {location} is {weather_data[location_key]}."
    else:
        return f"No weather information found for '{location}'."

if __name__ == "__main__":
    mcp.run()