from selenium import webdriver

class Driver:

    def get(self):
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)

        return webdriver.Firefox(
            firefox_profile=firefoxProfile, executable_path=r"./support/geckodriver"
        )

