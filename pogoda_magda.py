import requests
import json






def pobierzpogode_tawarno():
  r = requests.get(
    'https://samples.openweathermap.org/data/2.5/weather?appid=b1b15e88fa797225412429c1c50c122a1&lat=13.3362245&lon=52.4967368'
  )
  #Usuwanie niepotrzebnych elementow
  loc_weather = r.content.strip()

  temp, humid, weathertype, rain = zwroc_elementy_pogody(loc_weather)
  return temp, humid, weathertype, rain


def zwroc_elementy_pogody(wynik_pogody):
  json_pogody = json.loads(wynik_pogody)
  temp_k = json_pogody["main"]["temp"]
  temp_c = konwertuj_do_c(temp_k)
  humid = json_pogody["main"]["humidity"]
  weathertype = json_pogody["weather"][0]["main"]
  rain = "Rain" if weathertype == "rain" else "no rain"
  return temp_c, humid, weathertype, rain


def konwertuj_do_c(k):
  return str(round(float(k) - 273.15, 2))
