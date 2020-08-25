from selenium import webdriver

class Driver:

    _driver = None

    def get(self):
        if self._driver is None:
            firefoxProfile = webdriver.FirefoxProfile()
            firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
            firefoxProfile.set_preference("dom.webnotifications.enabled", False)

            self._driver = webdriver.Firefox(
                firefox_profile=firefoxProfile, executable_path=r"./support/geckodriver"
            )

        return self._driver

