# PENDIENTE DE REVISIÓN
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="noroses_housewife",
            category=["Vida"],
            prompt="¿Y si fuera un amo de casa para ti?",
            pool=True,
            unlocked=True
        )
    )

label noroses_housewife:
    m 1wuo "¿[player]?... ¿Cómo supiste que esto era algo que siempre soñé?"
    m 5gublu "Llegar a casa y encontrarte allí... "
    m 5dublu "Con una cara sorprendida y feliz, limpiando tus manos con un paño para que puedas venir a saludarme."
    m 5dublb "Tú barrerías tu cabello desordenado de tu rostro y vendrías corriendo, diciendo '¡Bienvenida de vuelta!'"
    m "Yo te abrazaría y sentiría un leve olor a dulces, solo para descubrir que me cocinaste algo para cuando regresara."
    m 5dubsb "Habría un poco de crema batida en tu rostro y yo la besarían, jugando a piquetearte..."
    m 5dubfb "Y justo en ese momento, sabría que nunca he sido más feliz."
    m 4fubfb "Vivir contigo, compartiendo esos momentos cotidianos..."
    m 1fubfa "Es mi sueño."
    m "Quiero ver todos los lados de ti, verte siendo tu versión más linda y adorarte."
    m 1fubfb "Haré que te sientas amado todos los días."
    m "No puedo esperar para cruzar el umbral así podremos hacer esto nuestra realidad, [mas_get_player_nickname()]."
    m 5hubsb "¡Serás mi lindo y tierno amo de casa! Ehehehe~"
return
