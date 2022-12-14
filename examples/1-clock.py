import asyncio
from datetime import datetime

hours_el = Element("hours")
minutes_el = Element("minutes")
seconds_el = Element("seconds")

while True:
    now = datetime.now()
    hours_el.write(now.strftime("%H"))
    minutes_el.write(now.strftime("%M"))
    seconds_el.write(now.strftime("%S"))
    await asyncio.sleep(1)
