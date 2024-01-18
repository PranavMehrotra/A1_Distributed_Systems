#to check if concurrent home and heartbeat requests can be handled. monitor timing on both server side and client side 

import aiohttp
import asyncio
import datetime

async def send_requests_a():
    while True:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Client A - Sending Home Request at: {current_time}")
        async with aiohttp.ClientSession() as session:
            async with session.get('http://127.0.0.1:5000/home') as response:
                print(f"Client A - Home Request Response: {await response.text()}")

        await asyncio.sleep(2)  # Sleep for 2 seconds between requests

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try :
        loop.run_until_complete(send_requests_a())
    finally:
        loop.close()
        