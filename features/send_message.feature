Feature: Enviar mensaje en WhatsApp

  Background:
    Given el dispositivo está en la pantalla de inicio

  Scenario Outline: Enviar mensaje a un contacto desde la pantalla de inicio
    When abro la aplicación "WhatsApp"
    And selecciono el chat de "Fernando"
    And escribo el mensaje "<msj>"
    And repetir mensaje 5
    Then presiono el botón de enviar
    Examples:
      | msj |
      | h   |
