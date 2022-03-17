# Temperature Logging
Components used for this project:
- Raspberry Pi 4b running Raspbian
- Waveshare environment sensor hat
- Used virtual environment venv
- Clone project in ```home/pi/``` (or you need to change path below)

To run file automatically, I used crontab:
1. Open terminal
2. Type crontab -e
3. Paste the following code into the file:
    ```*/30 * * * * cd /home/pi/TemperatureLog && /home/pi/TemperatureLog/{your venv name}/bin/python run.py command arg```
    This will run the script main.py in your venv every 30 minutes
4. Click ctrl+o to save, then ctrl+x to close
5. Script will run every 30 minutes