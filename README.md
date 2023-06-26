# weather-cli <img src="icons/icon.png" alt="WeatherTool" width="45"/>

Command line tool powered by python code written with the help of comment driven develpoment backed by GitHub Copilot.

# Inspiration <img src="icons/inspiration.png" alt="Inspiration" width="45"/>

![CodeGladiators23](icons/cg.png)

This tool is collaboratively developed for the [GitHub Copilot Hack in CodeGladiators 2023](https://www.techgig.com/codegladiators/github-copilot-hackathon) held by TechGig.

- [Tool Presentation](https://docs.google.com/presentation/d/1XZ_aivvg0hR2ARfoQQjU0ziPMjVuBPF6mMqtTAT57-8/edit?usp=sharing)

# Setup <img src="icons/setup.png" alt="Setup" width="30"/>

Clone the repository and run the following command:

```bash
docker build --tag weather-cli:latest .
```

# Usage <img src="icons/usage.png" alt="Usage" width="30"/>

```bash
docker run --rm -it weather-cli <city-name>
```

# Output <img src="icons/output.png" alt="Output" width="30"/>

```bash
docker run --rm -it weather-cli Pari
```

```bash
🔍 Initializing city name analysis...

Did you mean parit instead?

Press y for yes or n for no: n

Did you mean paris instead?

Press y for yes or n for no: y

✅  City name analysis complete! Name successfully resolved: Paris

🌤️  Engaging weather data retrieval protocol...

🌤️  Weather data acquisition successful! Here's what I found:
----------------------------------------------------------
{'city_name': 'Paris', 'temperature': '19.49°C', 'description': 'clear sky'}
----------------------------------------------------------
```

# Architecture <img src="icons/arch-icon.png" alt="Architecture" width="30"/>

<img src="arch.png" alt="WeatherTool Architecture"/>

# Team <img src="icons/team.png" alt="Team" width="30"/>

- Salil Gautam [@salil-gtm](https://github.com/salil-gtm)
- Gobilla Mothy [@G-Slient](https://github.com/G-Slient/)
- Kranthi Kiran [@kranthik13](https://github.com/kranthik13/)