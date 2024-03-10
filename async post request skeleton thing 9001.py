import aiohttp
import asyncio
import threading
import time

# Define the headers for the POST request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://xn--rl8hlm.tk/",
    "Origin": "https://xn--rl8hlm.tk",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Content-Length": "0",
    "TE": "trailers"
}

# Function to send a single POST request and check the response
async def send_request(session, url, i):
    try:
        async with session.post(url, headers=headers) as response:
            if response.status == 418:
                print("Server is claiming to be a teapot. All is well.")
                print("-----------------", i, "------------------")
                print("Response status code:", response.status)
                print("Response body:", await response.text())
                print("-----------------", i, "------------------")
            else:
                print("Server responded with an unusual response code (not 418).")
                print("Response status code:", response.status)
                print("Response body:", await response.text())
    except Exception as e:
        print("An error occurred while sending the request:", e)

# Function to automate sending requests concurrently using threading
def automate_requests_concurrently(url, num_requests):
    async def run_requests():
        async with aiohttp.ClientSession() as session:
            for i in range(num_requests):
                await send_request(session, url, i)

    asyncio.run(run_requests())

# Run the function and get user input
if __name__ == "__main__":
    url = "https://xn--rl8hlm.tk/thank"

    num_threads = int(input("How many threads do you want to use? "))
    num_requests_per_thread = int(input("How many requests per iteration per thread? "))

    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=automate_requests_concurrently, args=(url, num_requests_per_thread))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
