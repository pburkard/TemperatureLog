import logging
import os
import datetime
import time
from modules.weather_bme280 import BME280
from modules.uv_ltr390 import LTR390
from modules.light_tsl2591 import TSL2591

i2c_bus_number = 3
i2c_address = 0x76
weatherSensor = BME280(address=i2c_address, bus=i2c_bus_number)
lightSensor = TSL2591(bus=i2c_bus_number)
uvSensor = LTR390(bus=i2c_bus_number)

logger = logging.getLogger("EnvironmentLog")
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

def get_lux() -> float:
    return lightSensor.get_lux()

def get_uv() -> float:
    return uvSensor.getUV()

def get_als() -> float:
    return uvSensor.getALS()

def save_temperature_to_file(temperature, time):
    File_object = open(rf"data/{datetime.date.today().strftime('%d-%m-%Y')}.txt", "a")
    File_object.write(f"{time},{str(temperature)}\n")
    File_object.close()

def log_environment_data():
    logger.info("----- measurement start -----")
    try:
        time = datetime.datetime.now()
        hour = f"{time.hour}:{time.minute}"
        temperature = get_temperature()
        logger.info(f"Temperature: {temperature} °C")
        save_temperature_to_file(round(temperature, 1), hour)
        logger.info(f"Pressure: {get_pressure()} hPa")
        logger.info(f"Humidity: {get_humidity()} %")
    except Exception as ex:
        logger.error(ex)
    try:
        logger.info(f"Lux: {get_lux()}")
    except Exception as ex:
        logger.error(ex)
    try:
        logger.info(f"UV: {get_uv()}")
        logger.info(f"ALS: {get_als()}")
    except Exception as ex:
        logger.error(ex)
    # try:
    #     take
    # except Exception as ex:
    #     logger.error(ex)

log_environment_data()
