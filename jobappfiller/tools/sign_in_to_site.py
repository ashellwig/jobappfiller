# Copyright (C) 2025 Ash Hellwig <ahellwig.dev@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""Signs into career site to begin our attempt to automate this process."""

import os
from time import sleep

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By

from jobappfiller.util.logger import setup_logger


def signin_to_salesforce(
        driver: WebDriver,
        username: str | None,
        password: str | None
) -> None:
    # Signin Button (On Base URL in the corner).
    signin_button = driver.find_element(
            By.CSS_SELECTOR,
            ".css-ptkkss:nth-child(3)"
    )
    signin_button.click()

    # Username field.
    if username is None:
        username = os.getenv("CAREER_SITE_USERNAME")
    else:
        pass

    username_field = driver.find_element(By.XPATH, "//form/div/div/div/input")
    username_field.click()
    username_field.send_keys(username)

    # Password field.
    if password is None:
        password = os.getenv("CAREER_SITE_PASSWORD")
    else:
        pass

    password_field = driver.find_element(By.XPATH, "//div[2]/div/div/div/input")
    password_field.click()
    password_field.send_keys(password)

    # Submit button on the signin form.
    signin_submit = driver.find_element(
            By.XPATH,
            "//form/div[3]/div/div/div/div/div"
    )
    signin_submit.click()


def automated(
        username: str,
        password: str,
        site_url: str | None = None
) -> None:
    # Setup the logger
    logger = setup_logger(log_file="signin_to_site.log")

    # Get the environment variables.
    logger.info("Loading environment variables...")
    load_dotenv()
    if os.getenv("CAREER_SITE_URL") is not None:
        logger.debug("Environment variables loaded!")

    if site_url is None:
        site_url = os.getenv("CAREER_SITE_URL")
    else:
        pass

    # Define the webdriver.
    options = webdriver.FirefoxOptions()
    drv = webdriver.Firefox(options=options)

    ## Visit the Base URL of the Career site.
    logger.debug("Visiting %s", site_url)

    drv.get(site_url)
    drv.set_window_size(615, 1012)

    # Signin to the website.
    logger.debug("Running the sigin_to_salesforce function now...")
    signin_to_salesforce(driver=drv, username=username, password=password)

    # Close the Browser
    logger.debug("Closing the browser in 15 seconds.")
    sleep(15)
    logger.debug("Goodbye!")
    drv.quit()
