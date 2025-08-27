from flask import Flask, request, render_template, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
import time
import random
import logging
import validators
import requests

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Sample Instagram accounts and proxies (replace with your own)
INSTAGRAM_ACCOUNTS = [
    ("your_username1", "your_password1"),
    ("your_username2", "your_password2")
]
PROXIES = [
    "http://user1:pass1@proxy1_host:port",  # Replace with valid proxy
    "http://user2:pass2@proxy2_host:port"
]

def login_to_instagram(driver, username, password):
    """Log in to Instagram."""
    try:
        driver.get("https://www.instagram.com/accounts/login/")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        WebDriverWait(driver, 15).until(EC.url_contains("instagram.com"))
        logger.info(f"Logged in to Instagram successfully with {username}")
        time.sleep(2)  # Wait for login to stabilize
    except Exception as e:
        logger.error(f"Instagram login failed for {username}: {str(e)}")
        raise

def find_option_element(driver, option_name):
    """Find the poll option element (e.g., 'A' or 'B') in Instagram story."""
    try:
        # Target Instagram story poll options (adjust based on inspection)
        elements = driver.find_elements(By.XPATH, "//*[contains(@class, 'poll-option') or contains(@class, 'story-poll')]//div[contains(text(), '{}')]".format(option_name))
        for element in elements:
            if option_name.lower() in element.text.lower() and element.is_displayed():
                return element

        # Fallback: Search within visible elements
        visible_elements = driver.find_elements(By.XPATH, "//*[contains(text(), '{}') and not(ancestor-or-self::*[contains(@style, 'display:none')])]".format(option_name))
        for element in visible_elements:
            if element.is_displayed():
                return element

        logger.warning(f"No element found for option '{option_name}'")
        return None
    except Exception as e:
        logger.error(f"Error finding option '{option_name}': {str(e)}")
        return None

def vote_on_poll(url, option_name, submit_selector, max_votes):
    """Automate voting on an Instagram poll with account and proxy rotation."""
    if not validators.url(url):
        return 0, ["Invalid URL format"]
    if not url.startswith("https://www.instagram.com/stories/"):
        return 0, ["URL must be an Instagram story URL"]
    if not option_name.strip():
        return 0, ["Option name cannot be empty"]

    total_vote_count = 0
    all_errors = []
    proxy_index = 0

    for username, password in INSTAGRAM_ACCOUNTS:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--enable-unsafe-swiftshader")
        chrome_options.add_argument(f"user-agent={random.choice([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
        ])}")
        if PROXIES:
            chrome_options.add_argument(f'--proxy-server={PROXIES[proxy_index % len(PROXIES)]}')
            proxy_index += 1

        vote_count = 0
        errors = []
        max_retries = 3

        try:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
            driver.set_page_load_timeout(60)
            login_to_instagram(driver, username, password)
        except WebDriverException as e:
            logger.error(f"WebDriver initialization failed for {username}: {str(e)}")
            errors.append(f"WebDriver initialization failed for {username}: {str(e)}")
            continue

        try:
            for attempt in range(1, max_retries + 1):
                while vote_count < max_votes:
                    try:
                        logger.info(f"Attempting vote {vote_count + 1}/{max_votes} for '{option_name}' with {username}")
                        driver.get(url)
                        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
                        if driver.find_elements(By.XPATH, "//*[contains(text(), 'This story is unavailable')]"):
                            errors.append("Story is unavailable or has expired")
                            break

                        poll_option = find_option_element(driver, option_name)
                        if not poll_option:
                            errors.append(f"Vote {vote_count + 1}: Option '{option_name}' not found")
                            break
                        if not poll_option.is_enabled() or not poll_option.is_displayed():
                            errors.append(f"Vote {vote_count + 1}: Option '{option_name}' is not clickable")
                            break
                        poll_option.click()  # Instagram stories auto-submit on option click

                        vote_count += 1
                        total_vote_count += 1
                        logger.info(f"Vote {vote_count} submitted successfully for '{option_name}' with {username}")
                        time.sleep(random.uniform(5, 15))  # Slower interval to avoid detection

                    except (NoSuchElementException, TimeoutException) as e:
                        logger.error(f"Vote {vote_count + 1} failed for {username}: {str(e)}")
                        with open(f"error_page_{username}_{vote_count + 1}.html", "w", encoding="utf-8") as f:
                            f.write(driver.page_source)
                        driver.save_screenshot(f"error_screenshot_{username}_{vote_count + 1}.png")
                        errors.append(f"Vote {vote_count + 1}: {str(e)}")
                        if attempt < max_retries:
                            logger.info(f"Retrying attempt {attempt + 1}/{max_retries} for {username}")
                            time.sleep(random.uniform(5, 10))
                            continue
                        else:
                            errors.append(f"Vote {vote_count + 1}: Max retries reached for {username}")
                            break
                    except WebDriverException as e:
                        if "net::ERR_INTERNET_DISCONNECTED" in str(e) or "net::ERR_NAME_NOT_RESOLVED" in str(e):
                            logger.error(f"Network error in vote {vote_count + 1} for {username}: {str(e)}")
                            errors.append(f"Vote {vote_count + 1}: Network error: {str(e)}")
                            if attempt < max_retries:
                                logger.info(f"Retrying attempt {attempt + 1}/{max_retries} due to network error for {username}")
                                time.sleep(random.uniform(5, 10))
                                continue
                            else:
                                errors.append(f"Vote {vote_count + 1}: Max retries reached for network error for {username}")
                                break
                        else:
                            logger.error(f"Unexpected error in vote {vote_count + 1} for {username}: {str(e)}")
                            errors.append(f"Vote {vote_count + 1}: Unexpected error: {str(e)}")
                            break

        except Exception as e:
            logger.error(f"General error for {username}: {str(e)}")
            errors.append(f"General error for {username}: {str(e)}")
        finally:
            try:
                driver.quit()
            except:
                pass

        all_errors.extend(errors)
        if vote_count >= max_votes:
            break

    return total_vote_count, all_errors

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vote', methods=['POST'])
def vote():
    url = request.form.get('poll_url', '').strip()
    option_name = request.form.get('option_name', '').strip()
    submit_selector = request.form.get('submit_selector', '').strip()
    try:
        max_votes = int(request.form.get('max_votes', 10))
        if max_votes < 1:
            return jsonify({'status': 'error', 'message': 'Number of votes must be positive'})
    except ValueError:
        return jsonify({'status': 'error', 'message': 'Invalid number of votes'})

    if not url or not option_name or not submit_selector:
        return jsonify({'status': 'error', 'message': 'All fields are required'})

    logger.info(f"Starting voting: URL={url}, Option={option_name}, Submit={submit_selector}, Votes={max_votes}")
    vote_count, errors = vote_on_poll(url, option_name, submit_selector, max_votes)

    response = {
        'status': 'success' if not errors else 'partial',
        'votes_cast': vote_count,
        'errors': errors
    }
    logger.info(f"Voting completed: {response}")
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)