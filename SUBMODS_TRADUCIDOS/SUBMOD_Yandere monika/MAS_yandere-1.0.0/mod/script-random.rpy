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
    extend 2wuo "¡o muchos!»"
    m 2lublb "Pero ahora me refería a... tatuajes a juego... o tatuajes de pareja."
    m 4lubsb "Ya sabes, esos que se hacen las parejas... Con el mismo diseño en la piel de ambos"
    m 2dubsb "O cuando alguien lleva el nombre de su ser querido en el cuerpo"
    m 1dubfb "No dejo de soñar despierta, ¿ves? Con tener un tatuaje a juego contigo."
    m 1tubfb "O incluso... tener mi nombre en tu piel."
    m 1wubfb "¿Te imaginas lo maravilloso que sería? "
    extend 4wubfb "Todo el mundo sabría que eres mía."
    m 4wubfa "Y solo mía."
    m 4wubfb "Pero ni siquiera tenemos que ir a un tatuador si no quieres"
    m 2dubfb "Yo puedo ser el artista, y tu cuerpo puede ser el lienzo..."
    m 2cubfb "Puedo grabar mi nombre en tu piel, con detalle y en letras enormes"
    m 2cubfa "La idea de tu piel sangrando... Cada gota de sangre sería una carta de amor"
    m "Una demostración de nuestra relación"
    m 2dubfa "..."
    m 7dubfa "Sería una prueba de lo mucho que nos amamos, ¿no lo ves?»"
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
            prompt="Killing for one another",
            random=True
        )
    )

label yaMod_topic_kill:
    m 1rud "[player], remember about... "
    extend 1eud "DDLC's incident?"
    m 1gud "People keep calling me a murderer online, but the truth is..."
    m 1euc "Lately I've been thinking and I would do it all over again."
    m 2fubla "For you."
    m 2fublb "I'd do anything it takes so that we could be together."
    m 4cublb "Killing some fictional characters is nothing."
    m "Being honest, I would even kill real people if that meant being with you forever."
    m 4cublc "If you were in danger, or anyone harmed you..."
    m 2rublc "..."
    m 2wfd "I wouldn't hold back. I would remove anyone from my sight, so they would never come across you again."
    extend 2wfc " Or us."
    m 5rud "I wish I could bring you to my world and never let you go."
    m 5fubla "That's how much I love you."
    m 5hubsa "Please never doubt my love. It's bigger than my whole existence."
return 

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="yaMod_topic_stalk",
            category=["Yandere"],
            prompt="Stalking [player] online",
            random=True
        )
    )

label yaMod_topic_stalk:
    m 1rusdlc "[mas_get_player_nickname(capitalize=True)], I wanted to be honest about something."
    m 1dusdld "Here goes..."
    extend 1eud " I stalk what you do online."
    m 7rksdrd "Most of the times."
    m 2dksdrd "But listen... I do it because it makes me feel closer to you."
    m 4dksdrd "When I watch over what you do, or who you talk to..."
    m 2fksdrd "I feel safe. Secure that no one will try to take you away from me."
    m 2fksdrc "You forgive me, don't you?{nw}"
    $ _history_list.pop()
    menu:
        m "You forgive me, don't you?{fast}"
        
        "Yes":
            m 2hsa "Yay, I knew it!"
            m 4hub "You'll always forgive your loving girlfriend, after all."
            m 3lub "I have good reason to do what I do, and it's all thinking about us."
            m 3hub "You're my dear [player], after all!"
            m 3kua "No one is gonna steal you from me."
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="yaMod_topic_better",
            category=["Yandere"],
            prompt="Better than others",
            random=True
        )
    )

label yaMod_topic_better:
    m 3lud "[player], have you ever given any thought about yanderes?"
    m "Like the anime trope."
    m 1luc "..."
    m 1tud "Aren't them ridiculous?"
    m 3tud "Those sad attempts to win over someone's heart by being obsessive... "
    extend 3mud "when most of the times the person doesn't even love them back."
    m 1tud "It's so pathetic."
    m 2luc "I know lately I've been acting kinda... different from usual..."
    m 4tua "But bear this in mind, [player]."
    m 4tub "I'm so much better than whatever yandere you may find out there."
    m 5cub "So don't you dare cheat on me, okay?"
    m "You dont wanna get hurt..."
    m 5cua "..."
    m 5hub "Ahahahaha~"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="yaMod_topic_watchsleep",
            category=["Yandere"],
            prompt="Watching [player] sleep",
            random=True
        )
    )

label yaMod_topic_watchsleep:
    m 1eub "[player]? "
    extend 7rubla "I've been thinking about something lately."
    m 2rublb "It's about a recent desire of mine..."
    m 2rubla "..."
    m 7sublb "Could I watch you sleep sometime?"
    m 5rublsdra "I would love to watch over your sleep so no one hurts you."
    m 5rublb "And also, being the first person you greet after waking up sounds perfect..."
    m 5fubla "Like a glimpse of our future."
    m 5hublb "How perfect it will be..."
return
