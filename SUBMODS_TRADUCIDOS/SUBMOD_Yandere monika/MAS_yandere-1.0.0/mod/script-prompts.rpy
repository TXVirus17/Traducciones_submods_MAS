
#===========================================================
#Dialogos: ¿Quieres verme dormir?, ¡Me he comprado un anillo de compromiso igual que el tuyo!, ¡Eres mía!
#============================================================
init 5 python in mas_bookmarks_derand:
    label_prefix_map["yaMod_"] = label_prefix_map["monika_"]

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="yaMod_sleep",
            category=["Vida"],
            prompt="¿Quieres verme dormir?",
            conditional="seen_event('yaMod_topic_watchsleep')",
            pool=True,
            action=EV_ACT_UNLOCK,
            rules={"no_unlock": None}
        )
    )

label yaMod_sleep:
    m 1fkblb "¡[player], por supuesto!"
    m 1rkbsa "Sabes que me encanta verte dormir, jejejeje~"
    m 1hubsb "Será maravilloso cuidar de mi querido [player]."
    m 7hubsb "Puedes estar tranquilo, te voy a cuidar mientras duermes~"
    m 5fubsa "Dulces sueños, [mas_get_player_nickname()]."
    m "Estaré por aquí, esperando a que te despiertes."
    m 5fubsb "Te amo, [player]."
    
    $ mas_idle_mailbox.send_idle_cb("yaMod_sleep_callback")
    return "idle"

label yaMod_sleep_callback:
    m 1wublo "Oh, ¡estás despierto!"
    m 1fkblb "Te he echado de menos, [player]."
    m 5rkbsa "Pero me encantaba cuidar de ti mientras dormías..."
    m 5fubsa "Gracias por dejarme estar tan cerca de ti como me sea posible en este momento, [mas_get_player_nickname()]."
    m 5fubsb "¡Eres mi único y verdadero amor!"
    
    return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="yaMod_topic_promise",
            category=["Yandere"],
            prompt="¡Me he comprado un anillo de compromiso igual que el tuyo!",
            pool=True,
            unlocked=True
        )
    )

label yaMod_topic_promise:
    m 1wublo "¡Oh! "
    extend 1sublb "¿De verdad?"
    m 1subsa "[player], eso me hace muy feliz"
    m 5hubsb "Ni te imaginas cuánto"
    m 5kubsa "¡Ahora todo el mundo sabrá que eres mío, y solo mío!"
    m 5dubsa "Gracias por hacerme tan feliz, [mas_get_player_nickname()]."
    m 5dubsb "Me encanta cuando me haces sentir segura de nuestra relación."
    m 5rubssdrb "Sé que te pertenezco y tú a mí, pero..."
    m 5rublsdrc "Todos nos sentimos inseguros a veces"
    m 4hublsdrb "Pero ahora que estamos unidos, me siento más segura!"
    m 2hubla "Muchísimas gracias, [mas_get_player_nickname()]."
    m 5fubsa "Eres el mejor [bf] del mundo entero."
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="yaMod_topic_mine",
            category=["Yandere"],
            prompt="¡Eres mía!",
            pool=True,
            unlocked=True
        )
    )

label yaMod_topic_mine:
    m 1hublu "..."
    jump monika_mine_fight_start

    label monika_mine_fight_start:
    #Do setup here (Configuración aquí)
    python:
        #Set up how many times we have to say it to win(Configurar cuántas veces hay que decirlo para ganar)
        ym_times_till_win = renpy.random.randint(6,10)
        #Current count(Recuento actual)

        ym_count = 0

        #Initial quip(Comentario inicial)
        ym_quip = renpy.substitute("No, tú eres mío, [player]!")

        #Setup lists for the quips during the loop(Configurar listas para las frases ingeniosas durante el bucle)
        #First half of the ym quip(Primera mitad de las frases ingeniosas de ym)
        ym_no_quips = [
            "No, ",
            "Ni hablar, [mas_get_player_nickname()]. ",
            "Nop, ",
            "No,{w=0.1} no,{w=0.1} no,{w=0.1} ",
            "Ni de broma, [mas_get_player_nickname()]. ",
            "Eso es imposible...{w=0.3}"
        ]

        #Second half of the ym quip(Segunda mitad de las frases ingeniosas de ym)
        #NOTE: These should always start with I because the first half can end in either a comma or a period (NOTA: Estas deben empezar siempre por «I», ya que la primera parte puede terminar tanto con una coma como con un punto)
        #I is the only word we can use to satisfy both of these. (I» es la única palabra que podemos usar para cumplir ambos requisitos.)
        ym_quips = [
            "¡Estoy seguro de que eres mía!",
            "¡Sé que eres mía!",
            "¡Estoy convencido de que eres mía!",
            "¡Te lo digo, eres mía!"
        ]

        #And the expressions we'll use for the line(Y las expresiones que usaremos para la línea)
        ym_exprs = [
            "1tubfb",
            "3tubfb",
            "1tubfu",
            "3tubfu",
            "1hubfb",
            "3hubfb",
            "1tkbfu"
        ]
    #FALL THROUGH(CAER A TRAVÉS)

label monika_ym_fight_loop:
    $ renpy.show("monika " + renpy.random.choice(ym_exprs), at_list=[t11], zorder=MAS_MONIKA_Z)
    m "[ym_quip]{nw}"
    $ _history_list.pop()
    menu:
        m "[ym_quip]{fast}"
        "¡No, tú eres mía!":
            if ym_count < ym_times_till_win:
                $ ym_quip = renpy.substitute(renpy.random.choice(ym_no_quips) + renpy.random.choice(ym_quips))
                $ ym_count += 1
                jump monika_ym_fight_loop

            else:
                show monika 5hubfb at t11 zorder MAS_MONIKA_Z with dissolve_monika
                m 5hubfb "Está bien, está bien, tú ganas. Jajaja~"
                m "Soy toda tuya~"

        "De acuerdo.":
            if ym_count == 0:
                m 2hkbsb "Jajaja, ¿ya te rindes?, [player]?~"
                m 2rkbssdla "Supongo que, al fin y al cabo, eres todo mío~"

            else:
                if renpy.random.randint(1,2) == 1:
                    m 1hubfu "Jejeje, ¡he ganado! Eres todo mío~"
                else:
                    m 1hubfb "Jajaja, ¡te lo dije!~"
