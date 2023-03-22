"""

Класс для взаимодествия с сервисом одноразовых сообщений.
Create at 26.01.2023 16:15:35
~/core/privnote.py
"""

__author__ = 'tunderof'
__copyright__ = 'KIB, 2023'
__license__ = 'KIB'
__credits__ = [
    'tunderof',
]
__version__ = "20230322"
__status__ = 'Develop'  # "Production"


from typing import Optional

from core.base import Link, Message
from core.base import BaseSdarn

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

from webdriver_manager.chrome import ChromeDriverManager

class PrivnoteSdarn(BaseSdarn):
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    _base_url = 'https://privnote.com/'

    @classmethod
    def raw_write(cls, row_message: Message) -> Link:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=cls.chrome_options)
        driver.set_window_size(1920, 1080)
        driver.get(cls._base_url)
        wait = WebDriverWait(driver, 10)
        textarea = wait.until(EC.element_to_be_clickable((By.ID, "note_raw")))
        textarea.click().send_keys(Message)
        wait.until(EC.element_to_be_clickable((By.ID, "encrypt_note"))).click()
        url_to_note = wait.until(EC.visibility_of_element_located((By.ID, "note_link_input"))).get_property("value")
        driver.quit()
        return url_to_note

    @classmethod
    def check_read(cls, link: Link) -> bool:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=cls.chrome_options)
        driver.set_window_size(1920, 1080)
        driver.get(Link)
        try:
            driver.find_element(By.ID, "link_ok")
            return True
        except NoSuchElementException:
            return False
        finally:
            driver.quit()


    @classmethod
    def raw_read(cls, link: Link) -> Optional[Message]:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=cls.chrome_options)
        driver.set_window_size(1920, 1080)
        driver.get(Link)
        wait = WebDriverWait(driver, 10)
        but_to_read = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='confirm_button']")))
        but_to_read.click()
        textarea = wait.until(EC.visibility_of_element_located((By.ID, "note_contents"))).get_attribute("value")
        driver.quit()
        return textarea



