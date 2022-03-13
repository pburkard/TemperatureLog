import logging
import os
import datetime
from weather_bme280 import BME280

i2c_bus_number = 3
i2c_address = 0x76
weatherSensor = BME280(address=i2c_address, bus=i2c_bus_number)

logger = logging.getLogger("TemperatureLog")
filelogger_dir_name = "logfiles"
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
# console logging
# ch = logging.StreamHandler()
# ch.setLevel(levelConsole)
# ch.setFormatter(formatter)
# logger.addHandler(ch)
# file logging
current_dir = os.getcwd()
filelogger_dir = rf"{current_dir}/{filelogger_dir_name}"
if not os.path.isdir(filelogger_dir):
    os.mkdir(filelogger_dir)
logfile_name = f"EnvironmentLog_{datetime.date.today().strftime('%d-%m-%Y')}.log"
logfile_path = rf"{filelogger_dir}/{logfile_name}"
fh = logging.FileHandler(logfile_path)
fh.setFormatter(formatter)
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

def get_temperature() -> float:
    return weatherSensor.getTemperature()

def get_pressure() -> float:
    return weatherSensor.getPressure()

def get_humidity() -> float:
    return weatherSensor.getHumidity()

logger.info(get_temperature())
