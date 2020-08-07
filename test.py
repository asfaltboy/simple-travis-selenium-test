from pathlib import Path
import os

from selenium.webdriver.firefox.webdriver import Options, WebDriver

def test_selenium_works():
    """ Initialize and authenticate the selenium driver """
    options = Options()
    print("CI:", os.getenv("CI"))
    print("PATH:", os.getenv("PATH"))
    if os.getenv("CI"):
        options.headless = True
        options.log.level = "trace"

    print(list(Path().iterdir()))
    try:
        driver = WebDriver(firefox_options=options)
        driver.get("https://example.com")
    except Exception():
        content = driver.execute_script(
            "return document.getElementsByTagName('html')[0].innerHTML"
        )
    print(list(Path().iterdir()))
    assert 'This domain is for use in illustrative examples in documents' in content
