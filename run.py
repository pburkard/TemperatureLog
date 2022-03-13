from weather_bme280 import BME280

i2c_bus_number = 3
i2c_address = 0x76
weatherSensor = BME280(address=i2c_address, bus=i2c_bus_number)

def get_temperature() -> float:
    return weatherSensor.getTemperature()

def get_pressure() -> float:
    return weatherSensor.getPressure()

def get_humidity() -> float:
    return weatherSensor.getHumidity()

print(get_temperature())
