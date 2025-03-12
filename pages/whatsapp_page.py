from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WhatsAppPage:
    """ Clase que maneja acciones dentro de WhatsApp """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def select_chat(self, contacto):
        """ Selecciona el chat de un contacto específico """
        chat = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{contacto}")'))
        )
        chat.click()

    def send_message(self, mensaje, cantidad=1):
        """ Envía un mensaje a un chat abierto, opcionalmente repetido """
        input_box = self.wait.until(
            EC.presence_of_element_located((AppiumBy.ID, "com.whatsapp:id/entry"))
        )

        for _ in range(cantidad):
            input_box.send_keys(mensaje)
            send_button = self.wait.until(
                EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Enviar"))
            )
            send_button.click()
