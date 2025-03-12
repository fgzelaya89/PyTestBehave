from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    """ Clase que maneja acciones en la pantalla de inicio """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_home_screen(self):
        """ Regresa a la pantalla de inicio """
        self.driver.press_keycode(3)  # Código 3 = Botón Home

    def open_whatsapp(self):
        """ Toca el icono de WhatsApp desde la pantalla de inicio """
        whatsapp_icon = self.wait.until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "WhatsApp"))
        )
        whatsapp_icon.click()
