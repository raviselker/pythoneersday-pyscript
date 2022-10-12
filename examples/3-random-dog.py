import asyncio

from js import console
from pyodide import JsException
from pyodide.http import pyfetch

API_URL = "https://dog.ceo/api/breeds/image/random"
image_el = document.querySelector("#dog")


async def get_random_dog():
    try:
        response = await pyfetch(
            url=API_URL,
            method="GET",
        )
        if response.ok:
            data = await response.json()
            return data["message"]

    except JsException:
        return None


async def random_dog_loop():
    while True:
        console.log("Fetching new dog image...")
        img_url = await get_random_dog()
        image_el.setAttribute("src", img_url)
        await asyncio.sleep(5)


await loop.run_until_complete(random_dog_loop())
