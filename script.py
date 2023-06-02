from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the Selenium driver and options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run Chrome in headless mode
chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Set up the driver
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

# Function to interact with the ChatGPT API using Selenium
def reverse_chat_gpt(message):
    # Navigate to ChatGPT page
    driver.get('https://example.com/chatgpt')
    time.sleep(2)  # Wait for page to load

    # Enter user message and submit
    user_input = driver.find_element_by_id('user_input')
    user_input.send_keys(message)
    user_input.submit()
    time.sleep(2)  # Wait for response

    # Extract and return bot response
    bot_response = driver.find_element_by_id('bot_response').text
    return bot_response

# Main script
while True:
    user_message = input('User: ')
    if user_message.lower() == 'exit':
        break

    response = reverse_chat_gpt(user_message)
    print('Bot:', response)

# Close the browser
driver.quit()
