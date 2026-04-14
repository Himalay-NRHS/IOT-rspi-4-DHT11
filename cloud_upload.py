import time
import board
import adafruit_dht
import requests

sensor = adafruit_dht.DHT11(board.D4)

API_KEY = "YOUR_API_KEY"

while True:
    try:
        temperature_c = sensor.temperature
        humidity = sensor.humidity

        if temperature_c is not None and humidity is not None:
            url = "https://api.thingspeak.com/update"
            data = {
                "api_key": API_KEY,
                "field1": temperature_c,
                "field2": humidity
            }

            requests.post(url, data=data)

            print(f"Uploaded -> Temp={temperature_c:.1f}C Humidity={humidity:.1f}%")

    except RuntimeError as error:
        print(error.args[0])

    except Exception as error:
        sensor.exit()
        raise error

    time.sleep(15)