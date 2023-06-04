import sys
import time
from spelling_checker import spell_check
from weatherapi import get_weather


def main():
    city_name = sys.argv[1]
    print("🔍 Initializing city name analysis...")
    time.sleep(1.5)
    city_name = spell_check(city_name)
    city_name = city_name.capitalize()
    if city_name == "City not found":
        print("\n❌ Apologies, but I couldn't find the city you're looking for! ❌")
        sys.exit()
    else:
        print("\n✅  City name analysis complete! Name successfully resolved:", city_name)
        time.sleep(1.5)
        print("\n🌤️  Engaging weather data retrieval protocol...")
        weather_data = get_weather(city_name)
        time.sleep(1)
        print("\n🌤️  Weather data acquisition successful! Here's what I found:")
        print("----------------------------------------------------------")
        time.sleep(1)
        print(weather_data)
        time.sleep(1)
        print("----------------------------------------------------------")


if __name__ == "__main__":
    main()
