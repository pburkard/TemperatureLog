# Temperature Logging
Components used for this project:
- Raspberry Pi 4b running Raspbian
- Environment hat
- venv

To run file automatically, I used crontab:
1. open terminal
2. type crontab -e
3. paste the following code into the file:
    This will run the script main.py in the venv "env" every 30 minutes
    */30 * * * * cd /home/pi/TemperatureLog && /home/pi/TemperatureLog/{your venv name}/bin/python run.py command arg
4. click ctrl+o to save, ctrl+x to close
5. script will run every 30 minutes