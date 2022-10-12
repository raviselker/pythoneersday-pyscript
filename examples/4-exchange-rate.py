import asyncio
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
from pyodide import JsException
from pyodide.http import pyfetch

# Get your free API key at https://currencyscoop.com/api-documentation
API_KEY = "REPLACE_FOR_OWN_API_KEY"
BASE_URL = "https://api.currencyscoop.com/v1/latest"
FROM_CURRENCY = "EUR"
TO_CURRENCY = "USD"
API_URL = f"{BASE_URL}?base={FROM_CURRENCY}&symbols={TO_CURRENCY}&api_key={API_KEY}"

UPDATE_INTERVAL = 5 * 60  # Every 5 minutes

exchange_rate_div = Element("exchange-rate")
plot_div = Element("lineplot")

times = []
rates = []


async def loop_exchange():
    while True:
        console.log("Fetching latest exchange rate...")
        await get_exchange_rate()
        await asyncio.sleep(UPDATE_INTERVAL)


async def get_exchange_rate():
    try:
        response = await pyfetch(
            url=API_URL,
            method="GET",
        )
        if response.ok:
            data = await response.json()
            time = data["response"]["date"]
            rate = data["response"]["rates"]["USD"]
            times.append(datetime.fromisoformat(time[:-1]))
            rates.append(rate)
            await handle_new_data(rate)

    except JsException:
        return None


async def handle_new_data(rate):
    exchange_rate_div.write(rate)
    await update_plot()


async def update_plot():
    times_array = np.array(times)
    rates_array = np.array(rates)
    fig = plt.figure()
    plt.plot(times_array, rates_array)
    plot_div.write(fig)


await loop.run_until_complete(loop_exchange())
