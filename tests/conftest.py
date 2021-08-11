import pytest
from selene.support.shared import browser

import config


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.browser_name = config.settings.browser_name

    driver = _maybe_driver_from_settings(config.settings)
    if driver:
        browser.config.driver = driver

    yield

    if config.settings.browser_quit_after_each_test:
        browser.quit()
    browser.clear_local_storage()


def _maybe_driver_from_settings(settings: config.Settings):
    from selenium import webdriver

    options = None
    if settings.browser_name == 'chrome':
        options = webdriver.ChromeOptions()
        options.headless = settings.headless
    elif settings.browser_name == 'firefox':
        options = webdriver.FirefoxOptions()
        options.headless = settings.headless

    driver = None
    if settings.remote_url:
        options.set_capability('enableVNC', settings.remote_enableVNC)
        options.set_capability('screenResolution', settings.remote_screenResolution)
        driver = webdriver.Remote(
            settings.remote_url,
            options=options,
        )
    else:
        from webdriver_manager.chrome import ChromeDriverManager
        from webdriver_manager.firefox import GeckoDriverManager
        driver = {
            'chrome': lambda: webdriver.Chrome(
                ChromeDriverManager().install(),
                options=options,
            ),
            'firefox': lambda: webdriver.Firefox(
                GeckoDriverManager().install(),
                options=options,
            ),
        }[settings.browser_name]()
    if settings.browser_window_maximize:
        driver.maximize_window()
    else:
        driver.set_window_size(
            width=settings.browser_window_width,
            height=settings.browser_window_height
        )
    return driver

