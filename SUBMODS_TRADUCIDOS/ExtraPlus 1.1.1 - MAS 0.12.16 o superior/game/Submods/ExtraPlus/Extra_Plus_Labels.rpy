#===========================================================================================
#TRADUCCION POR TX_Virus (TERMINADO)
#===========================================================================================
# RETURN_LABELS 
#===========================================================================================

label view_extraplus:
    python:
        store.player_zoom = store.mas_sprites.zoom_level
        store.disable_zoom_button = False
        mas_RaiseShield_dlg()
        extra_button_zoom()
        Extraplus_show()
    return

label screen_extraplus:
    show monika idle at t11
    python:
        store.disable_zoom_button = False
        Extraplus_show()
    return
    
label close_extraplus:
    show monika idle at t11
    python:
        store.mas_sprites.zoom_level = store.player_zoom
        mas_DropShield_dlg()
        disable_button_zoom()
    jump ch30_visual_skip
    return

label close_dev_extraplus:
    show monika idle at t11
    python:
        mas_DropShield_dlg()
        disable_button_zoom()
    jump ch30_visual_skip
    return

label show_boop_screen:
    show monika staticpose at t11
    python:
        store.disable_zoom_button = True
        store.mas_sprites.reset_zoom()
    call screen boop_revamped
    return

label return_boop_screen:
    python:
        store.disable_zoom_button = False
        store.mas_sprites.zoom_level = store.player_zoom
        store.mas_sprites.adjust_zoom()
    jump screen_extraplus
    return

label close_boop_screen:
    show monika idle at t11
    python:
        store.disable_zoom_button = False
        store.mas_sprites.zoom_level = store.player_zoom
        store.mas_sprites.adjust_zoom()
        disable_button_zoom()
    jump ch30_visual_skip
    return

label hide_images_rps:
    hide e_rock
    hide e_paper
    hide e_scissors
    hide e_rock_1
    hide e_paper_1
    hide e_scissors_1
    $ rps_your_choice = 0
    call screen RPS_mg
    return

label extra_restore_bg(label="ch30_visual_skip"):
    python:
        mas_extra_location(locate=False)
        disable_button_zoom()
        HKBHideButtons()
    hide monika
    scene black
    with dissolve
    pause 2.0
    call spaceroom(scene_change=True)
    python:
        HKBShowButtons()
        renpy.jump(label)
    return

#===========================================================================================
# Label 
#===========================================================================================

#====Cafe

label go_to_cafe:
    python:
        check_file_status(cafe_sprite, '/game/Submods/ExtraPlus/submod_assets/backgrounds')
        mas_extra_location(locate=True)
        extra_seen_background("cafe_sorry_player", "gtcafev2", "check_label_cafe")

label check_label_cafe:
    pass

label gtcafe:
    show monika 1eua at t11
    if mas_isDayNow():
        m 3sub "¿Quieres ir a la cafetería?"
        m 3hub "¡Me alegra escuchar eso, [player]!"
        m 1hubsa "¡Sé que será una cita genial!"
        m 1hubsb "Vámonos entonces [mas_get_player_nickname()]~"
        jump cafe_init

    elif mas_isNightNow():
        m 3sub "Oh, ¿quieres ir a la cafetería?"
        m 3hub "Es muy romántico que hayas decidido ir esta noche."
        m 1eubsa "¡Esta cita va a ser genial!"
        m 1hubsb "Vamos, [mas_get_player_nickname()]~"
        jump cafe_init
    else:
        m 1eub "Será otro día entonces, [mas_get_player_nickname()]."
        jump screen_extraplus
    return

label gtcafev2:
    show monika 1eua at t11
    if mas_isDayNow():
        m 3wub "¿Quieres que volvamos a ir al café?"
        m 2hub "¡La última vez que fuimos me divertí muchísimo ^^!"
        m 2eubsa "Me alegra mucho oírlo, [player]!"
        m 1hubsb "Bueno, vamos [mas_get_player_nickname()]~"
        jump cafe_init
    elif mas_isNightNow():
        m 3wub "Oh, ¿quieres volver a ir a la cafetería?"
        m 2hub "La última vez que fuimos, fue muy romántico, jeje~"
        m 2eubsa "¡Me emociona mucho volver a ir, [player]!"
        m 1hubsb "Entonces vamos, [mas_get_player_nickname()]~"
        jump cafe_init
    else:
        m 1eub "Bueno, será la proxima vez, [mas_get_player_nickname()]."
        jump screen_extraplus
    return

label cafe_talk:
    show monika staticpose at t21
    python:
        store.disable_zoom_button = True
        cafe_menu = [
            ("¿Qué tal tu día [m_name]?", 'extra_talk_feel'),
            ("¿Cuál es tu mayor ambición?", 'extra_talk_ambition'),
            ("Nuestra comunicación es muy limitada, ¿no crees?", 'extra_talk_you'),
            ("¿Cómo ves nuestra relación dentro de 10 años?", 'extra_talk_teen'),
            ("¿Cuál es el mejor recuerdo que tienes ahora mismo?", 'extra_talk_memory'),
            ("¿Tienes alguna fobia?", 'extra_talk_phobia')
        ]

        items = [
            ("¿Podemos irnos?", 'cafe_leave', 20),
            ("No, nada", 'to_cafe_loop', 0)
        ]
    call screen extra_gen_list(cafe_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=False)
    return

label to_cafe_loop:
    show monika staticpose at t11
    $ store.disable_zoom_button = False
    call screen dating_loop(extraplus_acs_emptyplate, extraplus_acs_emptycup, "cafe_talk", "monika_no_dessert", "monika_boopcafebeta", boop_enable=True)
    return

label cafe_leave:
    show monika 1hua at t11
    m 1eta "Oh, ¿quieres que nos vayamos?"
    m 1eub "¡Me parece bien!"
    m 3hua "Pero antes de irnos..."
    jump cafe_hide_acs

label comment_cafe:
    m 1hubsa " Gracias por invitarme a salir."
    m 1eubsb "¡Es hermoso tener esos momentos en pareja!"
    m 1eubsa "Soy muy afortunada de haberte conocido y que sigas eligiéndome cada día"
    m 1ekbsa "¡Te amo, [mas_get_player_nickname()]!"
    $ mas_DropShield_dlg()
    $ mas_ILY()
    jump ch30_visual_skip
    return

#====Restaurant====#

label go_to_restaurant:
    python:
        check_file_status(restaurant_sprite, '/game/Submods/ExtraPlus/submod_assets/backgrounds')
        mas_extra_location(locate=True)
        extra_seen_background("restaurant_sorry_player", "gtrestaurantv2", "check_label_restaurant")

label check_label_restaurant:
    pass

label gtrestaurant:
    show monika 1eua at t11
    if mas_isDayNow():
        m 3sub "Oh,{w=0.3} ¿quieres ir al restaurante?"
        m 3hub "Me alegra mucho escuchar eso,{w=0.3} [player]!"
        m "Qué detalle por tu parte invitarme a una cita."
        if mas_anni.isAnni():
            m "Y nada menos que en nuestro aniversario,{w=0.3} ¡qué oportuno, [player]~!"
            $ persistent._extraplusr_hasplayergoneonanniversary == True
        m 1hubsa "¡Sé que va a ser genial!"
        m 1hubsb "Bien,{w=0.3}vamos [mas_get_player_nickname()]~"
        jump restaurant_init

    elif mas_isNightNow():
        m 3sub "Oh,{w=0.3} ¿quieres ir a un restaurante? "
        m "Qué hermoso detalle de tu parte."
        if mas_anni.isAnni():
            m "Y nada menos que en nuestro aniversario,{w=0.3} ¡qué romantico [player]~!"
            $ persistent._extraplusr_hasplayergoneonanniversary == True
        m 1hubsb "Vamos, [mas_get_player_nickname()]~"
        jump restaurant_init
    else:
        m 1eub "Será otro día entonces,{w=0.3} [mas_get_player_nickname()]."
        jump screen_extraplus
    return

label gtrestaurantv2:
    show monika 1eua at t11
    if mas_isDayNow():
        m 3wub "Oh, ¿quieres volver al restaurante?"
        if persistent._extraplusr_hasplayergoneonanniversary == True:
            m "Hmm~ Todavía estoy pensando en aquella vez que nos llevaste allí por nuestro aniversario,"
            extend "Fue,{w=0.3} tan romántico~"
            m "¡Me alegra que podamos volver~!"
        else: 
            m 2hub "¡La última vez que fuimos, me la pasé genial!"
            m 2eubsa "Me alegra escuchar eso, [player]!"
        m 1hubsb "Bueno, vámonos entonces [mas_get_player_nickname()]~"
        jump restaurant_init

    elif mas_isNightNow():
        m 3wub "Oh, ¿quieres volver a salir a comer afuera?"
        if persistent._extraplusr_hasplayergoneonanniversary == True:
            m "Hmm~{w=0.3} Todavía estoy pensando en la vez que nos llevaste allí por nuestro aniversario,"
            extend "¡De verdad sabes cómo hacer que nuestra noche sea maravillosa!"
            m "¡Me hace muy feliz que podamos volver a ir~!"
        else: 
            m 2hub "La última vez que fuimos, fue tan romantico~"
            m 2eubsa "¡Así que me alegra que podamos volver a ir, [player]!"
        m 1hubsb "Vamonos entonces, [mas_get_player_nickname()]~"
        jump restaurant_init
    else:
        m 1eub "Será la próxima vez, entonces, [mas_get_player_nickname()]."
        jump screen_extraplus
    return

label restaurant_talk:
    show monika staticpose at t21
    python:
        store.disable_zoom_button = True
        restaurant_menu = [
            ("¿Cómo has estado este día, [m_name]?", 'extra_talk_doing'),
            ("Si pudieras vivir en cualquier lugar, ¿dónde sería?", 'extra_talk_live'),
            ("¿Qué cambiarías de ti misma si pudieras?", 'extra_talk_change'),
            ("Si fueras un superhéroe, ¿qué poderes tendrías?", 'extra_talk_superhero'),
            ("¿Tienes algún lema en la vida?", 'extra_talk_motto'),
            ("Aparte de lo necesario, ¿qué es lo único sin lo que no podrías pasar un día?", 'extra_talk_without'),
            ("¿Tu vaso está medio lleno o medio vacío?", 'extra_talk_glass'),
            ("¿Qué es lo que más te molesta, [m_name]?", 'extra_talk_annoy'),
            ("¿Podrias describirte en tres palabras?.", 'extra_talk_3words'),
            ("¿Qué crees que es lo primero que se le viene a la mente a todo el mundo cuando piensa en ti?", 'extra_talk_pop'),
            ("Si fueras un animal, ¿qué animal serías?", 'extra_talk_animal'),
        ]

        items = [
            ("¿Podemos irnos?", 'restaurant_leave', 20),
            ("No nada", 'to_restaurant_loop', 0)
        ]
    call screen extra_gen_list(restaurant_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=False)
    return

label to_restaurant_loop:
    show monika staticpose at t11
    $ store.disable_zoom_button = False
    call screen dating_loop(extraplus_acs_pudding, extraplus_acs_icecream, "restaurant_talk", "monika_no_food", "monika_booprestaurantbeta", boop_enable=True)
    return

label restaurant_leave:
    show monika 1hua at t11
    m 1eta "Oh,{w=0.3} ¿estás listo para irnos?"
    m 1eub "¡Suena bien para mí!"
    m 3hua "Espera antes de irnos..."
    jump restaurant_hide_acs

#===========================================================================================
# Others
#===========================================================================================
#====Cafe====#

label monika_no_dessert:
    show monika staticpose at t11
    if monika_chr.is_wearing_acs(extraplus_acs_fruitcake):
        python:
            monika_chr.remove_acs(extraplus_acs_fruitcake)
            monika_chr.wear_acs(extraplus_acs_emptyplate)
        m 1hua "Jejeje, parece que me he acabado mi pastel de frutas."
        m 1eub "Me ha gustado mucho~"
    elif monika_chr.is_wearing_acs(extraplus_acs_chocolatecake):
        python:
            monika_chr.remove_acs(extraplus_acs_chocolatecake)
            monika_chr.wear_acs(extraplus_acs_emptyplate)
        m 1hua "Vaya, me he acabado mi pastel de chocolate."
        m 1sua "Estaba tan dulce~"
    if monika_chr.is_wearing_acs(extraplus_acs_coffeecup):
        python:
            monika_chr.remove_acs(extraplus_acs_coffeecup)
            monika_chr.wear_acs(extraplus_acs_emptycup)
        m 3dub "Además, este café también estaba muy bueno."
    if dessert_player == True:
        m 1etb "Por cierto, ¿ya te has terminado el postre?{nw}"
        $ _history_list.pop()
        menu:
            m "Por cierto, ¿ya te has terminado el postre?{fast}"
            "¡Sip!":
                m 1hubsa "Ejejeje~"
                m 1hubsb "¡Espero que te haya gustado!"
            "Todavía no":
                m 1eubsa "No te preocupes, [mas_get_player_nickname()], come tranquilo."
                m 1eubsb "Te esperaré~"
    else:
        m 1ekc "Me dijiste que no me preocupara."
        m 1ekb "Pero supongo, supongo que al menos te tomarás una taza de café."
    m 1hua "Avísame si quieres volver otra vez."
    jump to_cafe_loop
    return

label cafe_hide_acs:
    #Code inspired by YandereDev
    if monika_chr.is_wearing_acs(extraplus_acs_fruitcake):
        if monika_chr.is_wearing_acs(extraplus_acs_coffeecup) or monika_chr.is_wearing_acs(extraplus_acs_emptycup):
            m 3eub "Tengo que guardar este pastel de frutas."
            m 3eub "También, voy a guardar esta taza, ya vuelvo."
            python:
                monika_chr.remove_acs(extraplus_acs_fruitcake)
                monika_chr.remove_acs(extraplus_acs_coffeecup)
                monika_chr.remove_acs(extraplus_acs_emptycup)
        else:
            m 3eub "Tengo que guardar este pastel de frutas; ahora mismo vuelvo."
            $ monika_chr.remove_acs(extraplus_acs_fruitcake)

    elif monika_chr.is_wearing_acs(extraplus_acs_chocolatecake):
        if monika_chr.is_wearing_acs(extraplus_acs_coffeecup) or monika_chr.is_wearing_acs(extraplus_acs_emptycup):
            m 3eua "Necesito guardar este pastel de chocolate."
            m 3eua "También guardaré esta taza, espera un momento."
            python:
                monika_chr.remove_acs(extraplus_acs_chocolatecake)
                monika_chr.remove_acs(extraplus_acs_coffeecup)
                monika_chr.remove_acs(extraplus_acs_emptycup)
        else:
            m 3eua "Tengo que guardar este pastel de chocolate, dame un minuto."
            $ monika_chr.remove_acs(extraplus_acs_chocolatecake)

    elif monika_chr.is_wearing_acs(extraplus_acs_emptyplate):
        if monika_chr.is_wearing_acs(extraplus_acs_coffeecup) or monika_chr.is_wearing_acs(extraplus_acs_emptycup):
            m 3hua "Iré a guardar este plato antes."
            m 3hua "También guardaré esta taza, no tardaré mucho."
            python:
                monika_chr.remove_acs(extraplus_acs_emptyplate)
                monika_chr.remove_acs(extraplus_acs_coffeecup)
                monika_chr.remove_acs(extraplus_acs_emptycup)
        else:
            m 3hua "Voy a guardar este plato, dame un momento."
            $ monika_chr.remove_acs(extraplus_acs_emptyplate)

    call mas_transition_to_emptydesk
    pause 2.0
    call mas_transition_from_emptydesk("monika 1eua")
    m 1hua "¡Listo, vamos, [player]!"
    call extra_restore_bg("comment_cafe")
    return

#====Restaurant====#

label monika_no_food:
    show monika staticpose at t11
    if monika_chr.is_wearing_acs(extraplus_acs_pasta):
        python:
            monika_chr.remove_acs(extraplus_acs_pasta)
            monika_chr.wear_acs(extraplus_acs_remptyplate)
        m 1hua "Vaya, ya me terminé la pasta"
        m 1eub "Me ha encantado~"
        m "Ahora voy por el postre, ¡Ya regreso!"
        $ monika_chr.remove_acs(extraplus_acs_remptyplate)
        call mas_transition_to_emptydesk
        pause 2.0
        $ monika_chr.wear_acs(extraplus_acs_icecream)
        call mas_transition_from_emptydesk("monika 1eua")

    elif monika_chr.is_wearing_acs(extraplus_acs_pancakes):
        python:
            monika_chr.remove_acs(extraplus_acs_pancakes)
            monika_chr.wear_acs(extraplus_acs_remptyplate)
        m 1hua "Awww, me he acabado mis pancakes."
        m 1sua "Estaban deliciosos~"
        m "Tengo antojo de un postre, ¡enseguida vuelvo!"
        $ monika_chr.remove_acs(extraplus_acs_remptyplate)
        call mas_transition_to_emptydesk
        pause 2.0
        $ monika_chr.wear_acs(extraplus_acs_pudding)
        call mas_transition_from_emptydesk("monika 1eua")

    elif monika_chr.is_wearing_acs(extraplus_acs_waffles):
        python:
            monika_chr.remove_acs(extraplus_acs_waffles)
            monika_chr.wear_acs(extraplus_acs_remptyplate)
        m 1hua "Ay, parece qu terminé mis waffles."
        m 1sua "Estaban muy deliciosos~"
        m "Iré por el postre. ¡Espérame aqui!"
        $ monika_chr.remove_acs(extraplus_acs_remptyplate)
        call mas_transition_to_emptydesk
        pause 2.0
        $ monika_chr.wear_acs(extraplus_acs_pudding)
        call mas_transition_from_emptydesk("monika 1eua")

    if food_player == True:
        m 1etb "Por cierto, ¿Ya terminaste de comer?{nw}"
        $ _history_list.pop()
        menu:
            m "Por cierto, ¿Ya terminaste de comer?{fast}"
            "¡Claro!":
                m 1hubsa "Jejeje~"
                m 1hubsb "¡Espero te haya gustado tanto como a mí! ^^"
            "Todavía no":
                m 1eubsa "No te preocupes, [player], come despacio."
                m 1eubsb "Esperaré hasta que termines~"
    else:
        m 1ekc "Me dijiste que no me preocupara."
        m 1ekb "Pero, supongo que al menos tienes algo de beber contigo."
    m 1hua "Avísame si quieres volver."
    jump to_restaurant_loop
    return

label restaurant_hide_acs:
    #Code inspired by YandereDev
    if monika_chr.is_wearing_acs(extraplus_acs_candles):
        if monika_chr.is_wearing_acs(extraplus_acs_pasta) or monika_chr.is_wearing_acs(extraplus_acs_icecream):
            m 3eub "Tengo que guardar estas velas."
            m "¡Nunca se es demasiado precavido con el fuego!"
            m 3eub "También, guardaré este plato, ya vuelvo."
            python:
                monika_chr.remove_acs(extraplus_acs_candles)
                monika_chr.remove_acs(extraplus_acs_pasta)
                monika_chr.remove_acs(extraplus_acs_icecream)

        else:
            m 3eub "Tengo que guardar estas velas."
            m "¡No queremos quemar algo por accidente!"
            $ monika_chr.remove_acs(extraplus_acs_candles)

    elif monika_chr.is_wearing_acs(extraplus_acs_flowers):
        m 3eua "Voy a guardar estas flores, no tardaré mucho."
        python:
            monika_chr.remove_acs(extraplus_acs_flowers)

    elif not monika_chr.is_wearing_acs(extraplus_acs_flowers):
        if monika_chr.is_wearing_acs(extraplus_acs_pancakes) or monika_chr.is_wearing_acs(extraplus_acs_pudding) or monika_chr.is_wearing_acs(extraplus_acs_waffles):
            m 3eua "Espera, iré a guardar este plato."
            python:
                monika_chr.remove_acs(extraplus_acs_waffles)
                monika_chr.remove_acs(extraplus_acs_pancakes)
                monika_chr.remove_acs(extraplus_acs_pudding)

    call mas_transition_to_emptydesk
    pause 2.0
    call mas_transition_from_emptydesk("monika 1eua")
    m 1hua "¡Todo listo, vámonos [player]!"
    call extra_restore_bg
    return


################################################################################
## MENUS
################################################################################

label plus_walk:
    show monika idle at t21
    python:
        walk_menu = [
            ("Cafe", 'go_to_cafe'),
            ("Restaurante", 'go_to_restaurant')
        ]
        store.disable_zoom_button = True
        m_talk = renpy.substitute(renpy.random.choice(date_talk))
        renpy.say(m, m_talk, interact=False)
        items = [
            ("No, nada", 'screen_extraplus', 20)
        ]
    call screen extra_gen_list(walk_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=True)
    return

label plus_minigames:
    show monika idle at t21
    python:
        global ttt
        minigames_menu = [
            minigames("Encuentra la pelotita", 'minigame_sg', None),
            minigames("Piedra, papel o tijeras", 'minigame_rps', None)
        ]
        ttt = minigames("Tres en raya", 'minigame_ttt', ttt_prep)
        minigames_menu.append(ttt)
        
        store.disable_zoom_button = True
        m_talk = renpy.substitute(renpy.random.choice(minigames_talk))
        renpy.say(m, m_talk, interact=False)
        items = [
            ("No, nada", 'screen_extraplus', 20)
        ]
    call screen extra_gen_list(minigames_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=True)
    return

label plus_tools:
    show monika idle at t21
    python:
        tools_menu = [
            ("Mira el afecto de [m_name]", 'aff_log'),
            ("Crea un regalo para [m_name]", 'plus_make_gift'),
            ("Cambiar el título de la ventana", 'extra_window_title'),
            ("[m_name], quiero crear una copia de seguridad", 'mas_backup'),
            ("Hey, [m_name], ¿puedes lanzar una moneda?", 'coinflip')
            
        ]
        if renpy.has_screen("chibika_chill"):
            tools_menu.append(("¡Holi [player]!", 'extra_dev_mode'))
        store.disable_zoom_button = True
        items = [
            ("Repositorio de GitHub del creador", 'github_submod', 20),
            ("No, nada", 'screen_extraplus', 0)
        ]
    call screen extra_gen_list(tools_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=True)
    return



################################################################################
## GIFTS
################################################################################

label plus_make_gift:
    show monika idle at t21 
    #DIALOGO DE ADVERTENCIA CON LOS REGALOS
    $ renpy.call_screen("dialog", message="Nota: Los nombres de los regalos pueden cambiar dependiendo de la traducción y la versión, por lo que algunos regalos podrían no funcionar.", ok_action=Return())
    python:
        gift_menu = [
            ("Regalo personalizado", 'plus_make_file'),
            ("Comestibles", 'plus_groceries'),
            ("Objetos", 'plus_objects'),
            ("Lazos", 'plus_ribbons')
        ]

        items = [
            ("Regresar", 'plus_tools', 20)
        ]
    call screen extra_gen_list(gift_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=True)
    return

label plus_make_file:
    show monika idle at t11

    python:
        makegift = mas_input(
            prompt=("Escribe el nombre del regalo :p."),
            allow=" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789",
            screen_kwargs={"use_return_button": True, "return_button_value": "cancelar"},
        )

        if not makegift:
            renpy.jump("plus_make_file")
        elif makegift == "cancelar":
            renpy.jump("plus_make_gift")
        else:
            filepath = os.path.join(renpy.config.basedir, 'characters', makegift + ".gift")
            with open(filepath, "a"):
                pass  # just create an empty file
            renpy.notify("¡Regalo creado correctamente!")
            renpy.jump("plus_make_gift")
            
    return

label plus_groceries:
    show monika idle at t21
   
    python:
        groceries_menu = [
            extra_gift("Café (coffee.gift)", 'coffee.gift'),
            extra_gift("Café (cafe.gift)", 'cafe.gift'),
            extra_gift("Café (café.gift)", 'café.gift'),
            extra_gift("Chocolates", 'chocolates.gift'),
            extra_gift("Cupcake", 'cupcake.gift'),
            extra_gift("Caramelo de leche", 'fudge.gift'),
            extra_gift("Chocolate caliente", 'hotchocolate.gift'),
            extra_gift("Dulces", 'candy.gift'),
            extra_gift("Bastones de caramelo", 'candycane.gift'),
            extra_gift("Caramelos de maíz", 'candycorn.gift'),
            extra_gift("Galletas de navidad", 'christmascookies.gift')
        ]

        items = [
            ("Regresar", 'plus_make_gift', 20)
        ]
    call screen extra_gen_list(groceries_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=True)
    return

label plus_objects:
    show monika idle at t21
    python:
        objects_menu = [
            extra_gift("Anillo de promesa", 'promisering.gift'),
            extra_gift("Rosas", 'roses.gift'),
            extra_gift("Peluche de Quetzal", 'quetzalplushie.gift'),
            extra_gift("Termo para café", 'justmonikathermos.gift')
        ]

        items = [
            ("Regresar", 'plus_make_gift', 20)
        ]
    call screen extra_gen_list(objects_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=True)
    return
            
label plus_ribbons:
    show monika idle at t21
    python:
        ribbons_menu = [
            extra_gift("Lazo negro", 'blackribbon.gift'),
            extra_gift("Lazo azul", 'blueribbon.gift'),
            extra_gift("Lazo morado oscuro", 'darkpurpleribbon.gift'),
            extra_gift("Lazo esmeralda", 'emeraldribbon.gift'),
            extra_gift("Lazo gris", 'grayribbon.gift'),
            extra_gift("Lazo verde", 'greenribbon.gift'),
            extra_gift("Lazo morado claro", 'lightpurpleribbon.gift'),
            extra_gift("Lazo durazno", 'peachribbon.gift'),
            extra_gift("Lazo rosado", 'pinkribbon.gift'),
            extra_gift("Lazo platino", 'platinumribbon.gift'),
            extra_gift("Lazo rojo", 'redribbon.gift'),
            extra_gift("Lazo rubí", 'rubyribbon.gift'),
            extra_gift("Lazo zafiro", 'sapphireribbon.gift'),
            extra_gift("Lazo plateado", 'silverribbon.gift'),
            extra_gift("Lazo cerceta", 'tealribbon.gift'),
            extra_gift("Lazo amarillo", 'yellowribbon.gift')
        ]
        

        items = [
            ("Regresar", 'plus_make_gift', 20)
        ]
    call screen extra_gen_list(ribbons_menu, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, items, close=True)
    return