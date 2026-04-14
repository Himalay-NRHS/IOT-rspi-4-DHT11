import time
import board
import adafruit_dht

sensor = adafruit_dht.DHT11(board.D4)

while True:
    try:
        temperature_c = sensor.temperature
        humidity = sensor.humidity

        if temperature_c is not None and humidity is not None:
            print(f"Temp={temperature_c:.1f}C Humidity={humidity:.1f}%")

    except RuntimeError as error:
        print(error.args[0])

    except Exception as error:
        sensor.exit()
        raise error

    time.sleep(3)
