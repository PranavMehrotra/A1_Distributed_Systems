#to check if concurrent home and heartbeat requests can be handled. monitor timing on both server side and client side 

import aiohttp
import asyncio
import datetime

async def send_requests_b():
    while True:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Client B - Sending Heartbeat Request at: {current_time}")
        async with aiohttp.ClientSession() as session:
            async with session.get('http://127.0.0.1:5000/heartbeat') as response:
                print(f"Client B - Heartbeat Request Response: {response.status}")

        await asyncio.sleep(3)  # Sleep for 3 seconds between requests

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_requests_b())
