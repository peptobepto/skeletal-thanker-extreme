import aiohttp
import asyncio
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

# Function to automate sending requests concurrently
reqs = 0
async def automate_requests_concurrently(url):
    async with aiohttp.ClientSession() as session:
        while True:
            tasks = [send_request(session, url, i) for i in range(0, reqs)]
            await asyncio.gather(*tasks)

#run the function and get user input
if __name__ == "__main__":
    url = "https://xn--rl8hlm.tk/thank"
    reqs = int(input("how many concurrent requests do you want to send?"))
    print("Cooking up these requests in.")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    asyncio.run(automate_requests_concurrently(url))

#is simple
