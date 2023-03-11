# import the module
import python_weather
import asyncio
import os
city = input('Enter city name: ')
async def getweather(name):
  # declare the client. format defaults to the metric system (celcius, km/h, etc.)
  async with python_weather.Client(format=python_weather.METRIC) as client:

    # fetch a weather forecast from a city
    weather = await client.get(name)
  
    # returns the current day's forecast temperature (int)
    print(f"Now: {weather.current.temperature} C\n")
  
    # get the weather forecast for a few days
    for forecast in weather.forecasts:
      print(f"Astronomy for {forecast.date}:\
        \nmoon phase: {forecast.astronomy.moon_phase}\
        \nsun rise: {forecast.astronomy.sun_rise}\
        \nsunset: {forecast.astronomy.sun_set}\n")
  
      # hourly forecasts
      if forecast.hourly:
        print(f'Hourly forecast for {forecast.date}')
      for hourly in forecast.hourly:
        print(f'{hourly.description} at {hourly.time}: {hourly.temperature} C')

if __name__ == "__main__":
  # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
  # for more details
  if os.name == "nt":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

  asyncio.run(getweather(city))