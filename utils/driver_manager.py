from appium import webdriver
from appium.options.android import UiAutomator2Options

class DriverManager:
    """ Clase para manejar la configuración del driver de Appium """

    @staticmethod
    def get_driver():
        capabilities = {
            "platformName": "Android",
            "automationName": "uiautomator2",
            "deviceName": "RFCT40C2HWD",
            "appPackage": "com.whatsapp",
            "appActivity": ".Main",
            "language": "es",
            "locale": "ES",
            "noReset": True,
            "fullReset": False
        }

        options = UiAutomator2Options().load_capabilities(capabilities)
        return webdriver.Remote(command_executor="http://localhost:4723", options=options)
