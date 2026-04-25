#youre mine forever(Eres mío para siempre)
init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_yaMod_youremineforever",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None)
        ),
        code="BYE"
    )

label bye_yaMod_youremineforever:
    m 1eub "Hasta luego, [mas_get_player_nickname()]."
    m 3rua "Y oye..."
    m 3eub "No te olvides. "
    extend 5fubsa "Eres mío para siempre~"
    return 'quit'

#other girls
init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_yaMod_othergirls",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None)
        ),
        code="BYE"
    )

label bye_yaMod_othergirls:
    m 1ruc "[player]..."
    m 1rud "No vas a..."
    extend 1wksdrd "salir con otras chicas, ¿verdad?"
    m 1wksdrc "..."
    m 2wksdrd "No puedes.  "
    extend 2cud "Y no lo harás."
    m 2cub "Solo eres mío. "
    extend "Para siempre. ¿Lo entiendes?{nw}"
    $ _history_list.pop()
    menu:
        m "Para siempre. ¿Lo entiendes?{fast}"

        "Si":
            pass

        "Si":
            pass

        "Si":
            pass

        "Si":
            pass

        "Si":
            pass

        "Si":
            pass

        "Si":
            pass

        "Si":
            pass

        "Si":
            pass

        "Si":
            pass

    m 2cua "Bien."

return 'quit'
