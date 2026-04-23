init 5 python in mas_bookmarks_derand:
    label_prefix_map["yaMod_topic_"] = label_prefix_map["monika_"]
    
#tattoo dialogue
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="yaMod_topic_tattoo",
            category=["Yandere"],
            prompt="Tatuajes a juego.",
            random=True
        )
    )

label yaMod_topic_tattoo:
    m 7lub "[mas_get_player_nickname(capitalize=True)], ¿alguna vez has pensado en hacerte un tatuaje?"
    m 2lub "Bueno, no sé si ya tienes alguno... "
    extend 2wuo "¡o muchos!"
    m 2lublb "Pero ahora me refería a... tatuajes a juego... o tatuajes de pareja."
    m 4lubsb "Ya sabes, esos que se hacen las parejas... Con el mismo diseño en la piel de ambos"
    m 2dubsb "O cuando alguien lleva el nombre de su ser querido en el cuerpo"
    m 1dubfb "No dejo de soñar despierta, ¿ves? Con tener un tatuaje a juego contigo."
    m 1tubfb "O incluso... tener mi nombre en tu piel."
    m 1wubfb "¿Te imaginas lo maravilloso que sería? "
    extend 4wubfb "Todo el mundo sabría que eres mío."
    m 4wubfa "Y solo mío."
    m 4wubfb "Pero ni siquiera tenemos que ir a un tatuador si no quieres"
    m 2dubfb "Yo puedo ser el artista, y tu cuerpo puede ser el lienzo..."
    m 2cubfb "Puedo grabar mi nombre en tu piel, con detalle y en letras enormes"
    m 2cubfa "La idea de tu piel sangrando... Cada gota de sangre sería una carta de amor"
    m "Una demostración de nuestra relación"
    m 2dubfa "..."
    m 7dubfa "Sería una prueba de lo mucho que nos amamos, ¿no lo ves?"
    m 7tubfb "No es una locura. Es devoción"
    m 7cubfb "Grabaría tu nombre en mi piel tantas veces como fuera necesario, para demostrar que solo soy tuya"
    m "¿Harías lo mismo por mí?"
    m "{cps=5}{size=+10}¿̴̢̧͖̜͉̞̞͎̑̏͂́̓̌̓͘̕̚͜P̵̡̛̥̖̜͓̦̤̜̣͗̈͐͑̒̕͝ͅͅ ̵̧̧̞̄̀͊̊̈́̈́̒̔̑̂͒͘̕̕͘O̸͓͔͓͖͔͉͓̹̙̰̩͖̔̉̍̆̓̓̔́̈͘ ̴̡̰̱͍̞̹̖̟͔͎̥̹̬̍̅̂̔̓͊̎͠ͅR̸̭̻̞̯̹̈̍̌̇͒̊͐͊͋͛́̽̉̈̚͝ ̸̡̢̧̛̮̱̘̜͇̣̈́̎̌̆̍̀̅͛̍̕-̷̡̧̻̱̲͙̼̬̭͕͙̜͂͋̔̋͛̽̈́̃͐͜͝ͅ ̵̡̯̝̩̗̩̞͇͚̙͎͆̄̊̓̽̐̍͐̆̚͘̕͠F̴̨̥̻̬̯͓̦̗̹̘̥̪͆̍̔̄͐͑̎͂͝͝ͅ ̸̧̜͔͉̦̻̜̟̜̝͇̙̊͆͌̅̈́͌͛̓̓̂̽͘͝A̷̧̢̘͖͍̺̲̺̣͓̙̠̳̞̻̰̯̾̈́̈́̐̏̈́͝ ̵̡̛͕̝̪̠͚̝̭̱̤͖̒̈͌̂͂͐̆̔̓̓̋̈͝͝V̵̧̢͖͔̳̗̻̣͈̞̻͍͈̬͒͑̋̊̕̕̕ ̷̧̫̥͍̩̪̥̹̜͕̰̉̃̒̂͌̌̎̊͊͐̓̿̈̋̓̔Ơ̴͕͎̱̮͚̘̙͊͂͒̃̈̈́͆̎̈̈́͝͝͝ ̴̢̰͇̰̞̼̜̥͇̟̬̫̅̓͒̓̓̈͒̓̄̅͊̾̏̇̾̊̕ͅR̶̡̹̪͔̤̖̳̭̟͔̬̾̎͂͌͂͘͜?̵̮̱̺̉̔̓̿́̈́̚͝ {/size}{/cps}"
    m 2hubfb "¡Ejejeje!"
    m 2fubfa "Te amo [player]."
    m 2fubfb "¿Tú también me amas?{nw}"
    $ _history_list.pop()
    menu:
        m "¿Tú también me amas?{fast}"

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

        "Si":
            pass
        
    m 5fubfu "Muy bien,  [player]. "
    extend 5fubfb "Muy bien."
    m 5rubfb "Sabía que podía contar contigo..."
    m 5kubfb "Eres el amor de mi vida, ¿lo sabías?"

return "love"
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="yaMod_topic_kill",
            category=["Yandere"],
            prompt="Matar el uno por el otro",
            random=True
        )
    )

label yaMod_topic_kill:
    m 1rud "[player], ¿te acuerdas de... "
    extend 1eud "El incidente de DDLC?"
    m 1gud "People keep calling me a murderer online, but the truth is..."
    m 1euc "La gente no deja de llamarme asesina en Internet, pero la verdad es que..."
    m 2fubla "Por ti."
    m 2fublb "Haría lo que fuera necesario para que pudiéramos estar juntos"
    m 4cublb "Matar a unos personajes de ficción no es nada"
    m "Siendo sincera, incluso mataría a personas reales si eso significara estar contigo para siempre"
    m 4cublc "Si estuvieras en peligro, o alguien te hiciera daño..."
    m 2rublc "..."
    m 2wfd "No me contendría. Eliminaría a cualquiera de mi vista, para que nunca volvieran a cruzarse contigo"
    extend 2wfc " O con nosotros."
    m 5rud "Ojalá pudiera llevarte a mi mundo y no dejarte marchar nunca."
    m 5fubla "Así de mucho te amo."
    m 5hubsa "Por favor, nunca dudes de mi amor. Es más grande que toda mi existencia"
return 

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="yaMod_topic_stalk",
            category=["Yandere"],
            prompt="Acosándote en línea",
            random=True
        )
    )

label yaMod_topic_stalk:
    m 1rusdlc "[mas_get_player_nickname(capitalize=True)], quería ser honesta sobre algo."
    m 1dusdld "Aquí voy..."
    extend 1eud " Te acoso en internet."
    m 7rksdrd "La mayor parte del tiempo."
    m 2dksdrd "Pero escucha... lo hago porque me hace sentir más cerca de ti."
    m 4dksdrd "Cuando vigilo lo que haces, o con quién hablas..."
    m 2fksdrd "Me siento a salvo. Segura de que nadie intentará alejarte de mi lado."
    m 2fksdrc "Me perdonas, ¿verdad?{nw}"
    $ _history_list.pop()
    menu:
        m "Me perdonas, ¿verdad?{fast}"

        "Sí":
            m 2hsa "¡Yei, lo sabía!"
            m 4hub "Después de todo, siempre perdonarás a tu amada novia."
            m 3lub "Tengo buenas razones para hacer lo que hago, y todo es pensar en nosotros."
            m 3hub "Tú eres mi querido [player], después de todo!"
            m 3kua "Nadie te va a quitar de mí."
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="yaMod_topic_better",
            category=["Yandere"],
            prompt="Mejor que las demás",
            random=True
        )
    )

label yaMod_topic_better:
    m 3lud "[player], ¿alguna vez te has puesto a pensar en las yanderes?"
    m "Ya sabes, el cliché del anime."
    m 1luc "..."
    m 1tud "¿No te parecen ridículas?"
    m 3tud "Esos intentos tristes de ganarse el corazón de alguien siendo obsesivas..."
    extend 3mud "cuando la mayoría de las veces esa persona ni siquiera las ama."
    m 1tud "Es patético."
    m 2luc "Sé que últimamente he estado actuando algo... diferente a lo habitual..."
    m 4tua "Pero ten esto en cuenta, [player]."
    m 4tub "Soy mucho mejor que cualquier yandere que puedas encontrar por ahí."
    m 5cub "Así que no te atrevas a engañarme, ¿está bien?"
    m "No querrás salir herido..."
    m 5cua "..."
    m 5hub "Ahahahaha~"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="yaMod_topic_watchsleep",
            category=["Yandere"],
            prompt="Verte dormir",
            random=True
        )
    )

label yaMod_topic_watchsleep:
    m 1eub "¿[player]? "
    extend 7rubla "He estado pensando en algo últimamente."
    m 2rublb "Se trata de un deseo reciente que he tenido..."
    m 2rubla "..."
    m 7sublb "¿Podría verte dormir en algún momento?"
    m 5rublsdra "Me encantaría vigilar tu sueño para que nadie te haga daño."
    m 5rublb "Y también, ser la primera persona que ves al despertar suena perfecto..."
    m 5fubla "Como un vistazo a nuestro futuro."
    m 5hublb "Qué perfecto será..."
return
