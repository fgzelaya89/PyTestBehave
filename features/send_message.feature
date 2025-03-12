Feature: Enviar mensaje en WhatsApp

  Scenario: Enviar mensaje a un contacto desde la pantalla de inicio
    Given el dispositivo está en la pantalla de inicio
    When abro la aplicación "WhatsApp"
    And selecciono el chat de "Fernando"
    And escribo el mensaje "hola"
    And repetir mensaje 5
    Then presiono el botón de enviar
