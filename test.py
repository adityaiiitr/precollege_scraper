from playwright.sync_api import sync_playwright
import json

def send_request_with_playwright(phone_number):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Use `headless=True` if you don't want to see the browser
        context = browser.new_context()

        # Create a new page
        page = context.new_page()

        # Navigate to Flipkart (to establish cookies if necessary)
        page.goto('https://www.flipkart.com')

        # Prepare the request URL and payload
        url = 'https://1.rome.api.flipkart.com/api/7/user/otp/generate'
        payload = {
            "loginId": phone_number
        }

        # Execute the POST request with the specified headers and payload
        response = page.request.post(
            url,
            headers={
                'Content-Type': 'application/json',
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br, zstd',
                'Accept-Language': 'en-US,en;q=0.9',
                'Connection': 'keep-alive',
                'Host': '1.rome.api.flipkart.com',
                'Origin': 'https://www.flipkart.com',
                'Referer': 'https://www.flipkart.com/',
                'Sec-CH-UA': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
                'Sec-CH-UA-Mobile': '?0',
                'Sec-CH-UA-Platform': '"Windows"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 FKUA/website/42/website/Desktop',
                # Add your actual cookies here if needed
                'Cookie': 'T=cm2dmf96s0af72ceqbjrf70pc-BR1729188898372; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjFkOTYzYzUwLTM0YjctNDA1OC1iMTNmLWY2NDhiODFjYTBkYSJ9.eyJleHAiOjE3MzA5MTY4OTgsImlhdCI6MTcyOTE4ODg5OCwiaXNzIjoia2V2bGFyIiwianRpIjoiYjVkOTBiNTItMDk0My00ZjZlLWI5ZDMtYjc1Zjc0MWU4NjUyIiwidHlwZSI6IkFUIiwiZElkIjoiY20yZG1mOTZzMGFmNzJjZXFianJmNzBwYy1CUjE3MjkxODg4OTgzNzIiLCJrZXZJZCI6IlZJRkNBNUJDNzk3QzFENDdCQzgyOEIxMEQ2QjI1QUI5ODIiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJDSCIsIm0iOnRydWUsImdlbiI6NH0.BmcBvOYiHP5FHs8kD_M-9bDgMaUo-5hIGkJav4Cxf-U; ...'
            },
            data=json.dumps(payload)
        )

        # Print the response
        print(response.text())

        # Close the browser
        browser.close()

# Example usage:
for i in range(20):
    phone_number = '+918340632956'  # Input custom phone number here
    send_request_with_playwright(phone_number)
