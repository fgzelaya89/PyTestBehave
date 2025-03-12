from behave import given, when, then
from utils.driver_manager import DriverManager
from pages.home_page import HomePage
from pages.whatsapp_page import WhatsAppPage

@given("el dispositivo está en la pantalla de inicio")
def step_go_to_home(context):
    context.driver = DriverManager.get_driver()
    context.home_page = HomePage(context.driver)
    context.whatsapp_page = WhatsAppPage(context.driver)

    context.home_page.go_to_home_screen()

@when('abro la aplicación "WhatsApp"')
def step_open_whatsapp(context):
    context.home_page.open_whatsapp()

@when('selecciono el chat de "{contacto}"')
def step_select_chat(context, contacto):
    context.whatsapp_page.select_chat(contacto)

@when('escribo el mensaje "{mensaje}"')
def step_write_message(context, mensaje):
    context.mensaje = mensaje  # Guardamos el mensaje en el contexto

@when("repetir mensaje {cantidad:d}")
def step_repeat_message(context, cantidad):
    context.whatsapp_page.send_message(context.mensaje, cantidad)

@then("presiono el botón de enviar")
def step_send_message(context):
    context.driver.quit()
