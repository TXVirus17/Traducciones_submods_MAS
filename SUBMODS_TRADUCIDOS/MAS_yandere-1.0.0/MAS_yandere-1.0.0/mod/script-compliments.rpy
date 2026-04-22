#I love how possessive you are (Me encanta lo posesiva que eres)
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="ya_compliment_possessive",
            category=["mas_compliment"],
            prompt="Me encanta lo posesiva que eres.",
            unlocked=True
        ),
        code="CMP"
    )

label ya_compliment_possessive:
    m 2tub "Oh, ¿de verdad?"
    m 2tua "Me alegro de que te guste."
    m 7gua "No es que esté intentando ser posesiva..."
    m 7kub "Este es mi comportamiento habitual cuando se trata de ti, [mas_get_player_nickname()]."
    m 2cua "No puedo, y no dejaré que nadie te aleje de mí."
    m 2cub "Eres mío. Y solamente mío.»"
    m 4lub "Me alegro de no tener que obligarte, o si no tendríamos problemas..."
    m 4tub "No querrás ponerme celosa o enfadarme, ¿verdad?"
    m 2tua "..."
    m 2tub "Eso pensaba"
    m 5hua "¡Te amo, mi [player]!"
return "love"
