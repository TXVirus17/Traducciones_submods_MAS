#===========================================================================================
# TRADUCCION POR TX_Virus (PARCIALMENTE TERMINADO) 
#===========================================================================================
# MINIGAME#1
#===========================================================================================

#====Shell Game
label minigame_sg:
    $ check_file_status(cup_list, '/game/Submods/ExtraPlus/submod_assets/sprites')
    show monika 1eub at t11
    m 3hua "¡Empecemos entonces!, Selecciona una dificultad{nw}"
    menu:
        "¡Empecemos entonces!, Selecciona una dificultad{fast}"
        "Fácil":
            m 3hubsb "¿Conque quieres jugar algo simple, [player]? "
            extend 1hua "¡Empecemos entonces!"
            python:
                cup_speed += 0.5
                difficulty_sg = 1
        "Intermedio":
            m 3eub "¿Quieres jugar algo más casual? "
            extend 3sua "¡Empecemos de una vez!"
            python:
                cup_speed = 0.5
                difficulty_sg = 2
        "Difícil":
            m 1tubsb "Parece que deseas un reto...{w=0.3} ¿no es así, [player]?"
            m 3eub "jejejeje, ¡Entonces prepárate!"
            python:
                cup_speed -= 0.3
                difficulty_sg = 3

label restart_sg:
    $ config.allow_skipping = False
    show monika 1eua at t21

    pause 0.2

    show cup zorder 12 as cup_1:
        xpos cup_coordinates[0] ypos -400
        easein_bounce 0.5 ypos 250

    show cup zorder 12 as cup_2:
        xpos cup_coordinates[1] ypos -400
        pause 0.1
        easein_bounce 0.5 ypos 250

    show cup zorder 12 as cup_3:
        xpos cup_coordinates[2] ypos -400
        pause 0.2
        easein_bounce 0.5 ypos 250

    pause 1.0

    show ball zorder 12 behind cup_2:
        xpos cup_coordinates[1] ypos 335

    show cup as cup_2:
        linear 0.5 ypos 110

    m 1kua "Ahí está la pelotita, ¡no la pierdas de vista, [player]!"

    show cup as cup_2:
        linear 0.5 ypos 250

    m 3hub "¡Muy bien, veamos si sabes dónde está!"

    hide ball

    show cup as cup_1:
        xpos cup_coordinates[0] ypos 250

    show cup as cup_2:
        xpos cup_coordinates[1] ypos 250

    show cup as cup_3:
        xpos cup_coordinates[2] ypos 250

    python:
        cup_coordinates_real[0] = 695
        cup_coordinates_real[1] = 925
        cup_coordinates_real[2] = 1155

        original_cup[0] = 0
        original_cup[1] = 1
        original_cup[2] = 2

        ball_position = 1
        disable_esc()
        mas_MUMURaiseShield()
        afm_pref = renpy.game.preferences.afm_enable
        renpy.game.preferences.afm_enable = False
    show screen score_minigame(game="sg")

label loop_game:
    show monika 1eua
    show screen extra_no_click
    python:
        move_cup_1 = renpy.random.randint(0,2)
        move_cup_2 = renpy.random.randint(0,2)
        while move_cup_2 == move_cup_1:
            move_cup_2 = renpy.random.randint(0,2)

        temp_cup_position = cup_coordinates_real[move_cup_2]
        cup_coordinates_real[move_cup_2] = cup_coordinates_real[move_cup_1]
        cup_coordinates_real[move_cup_1] = temp_cup_position

        temp_original_cup = original_cup[move_cup_2]
        original_cup[move_cup_2] = original_cup[move_cup_1]
        original_cup[move_cup_1] = temp_original_cup

        if original_cup[move_cup_1] == ball_position:
            ball_position = original_cup[move_cup_2]

        elif original_cup[move_cup_2] == ball_position:
            ball_position = original_cup[move_cup_1]

    $ renpy.pause(cup_speed, hard='True')

    play sound "Submods/ExtraPlus/submod_assets/sfx/cup_shuffle.mp3"

    show cup as cup_1:
        ease cup_speed xpos cup_coordinates_real[0]

    show cup as cup_2:
        ease cup_speed xpos cup_coordinates_real[1]

    show cup as cup_3:
        ease cup_speed xpos cup_coordinates_real[2]

    if shuffle_cups != 3:
        $ shuffle_cups += 1
        jump loop_game

    pause 1.0

    show screen shell_game_minigame

    "¡Listo!, selecciona un vaso:"

label check_label:

    $ _current_turn += 1

    hide screen shell_game_minigame

    show cup as cup_1:
        xpos cup_coordinates[0] ypos 250

    show cup as cup_2:
        xpos cup_coordinates[1] ypos 250

    show cup as cup_3:
        xpos cup_coordinates[2] ypos 250
    python:
        cup_coordinates_real[0] = 695
        cup_coordinates_real[1] = 925
        cup_coordinates_real[2] = 1155

    #Se muestra los vasos y debe de elegir un vaso
    if cup_choice == 0:

        show cup as cup_1:
            linear 0.5 ypos 110

        if cup_choice == ball_position:
            show ball zorder 12 behind cup_1:
                xpos cup_coordinates[0] ypos 335

    elif cup_choice == 1:

        show cup as cup_2:
            linear 0.5 ypos 110

        if cup_choice == ball_position:
            show ball zorder 12 behind cup_2:
                xpos cup_coordinates[1] ypos 335

    elif cup_choice == 2:

        show cup as cup_3:
            linear 0.5 ypos 110

        if cup_choice == ball_position:
            show ball zorder 12 behind cup_3:
                xpos cup_coordinates[2] ypos 335

    if _plus_comment is True:
        m 1sub "[renpy.substitute(renpy.random.choice(_plus_complies))]"

    elif _plus_comment is False:
        m 1hub "[renpy.substitute(renpy.random.choice(_plus_not_met))]"

    if cup_choice != ball_position:

        m 1lub "El vaso correcto es{w=0.3}.{w=0.3}.{w=0.3}."

        if ball_position == 0:

            show cup as cup_1:
                linear 0.5 ypos 110

            show ball zorder 12 behind cup_1:
                xpos cup_coordinates[0] ypos 335

        elif ball_position == 1:

            show cup as cup_2:
                linear 0.5 ypos 110

            show ball zorder 12 behind cup_2:
                xpos cup_coordinates[1] ypos 335

        elif ball_position == 2:

            show cup as cup_3:
                linear 0.5 ypos 110

            show ball zorder 12 behind cup_3:
                xpos cup_coordinates[2] ypos 335

        m 1hua "¡Este!"

    show cup as cup_1:
        linear 0.5 xpos cup_coordinates[0] ypos 250

    show cup as cup_2:
        linear 0.5 xpos cup_coordinates[1] ypos 250

    show cup as cup_3:
        linear 0.5 xpos cup_coordinates[2] ypos 250

    pause 1.0

    hide ball
    $ shuffle_cups = 0
    jump loop_game
    return

#===========================================================================================
# TALKING GAME
#===========================================================================================

label shell_game_result:
    hide screen score_minigame
    python:
        enable_esc()
        mas_MUMUDropShield()
        renpy.game.preferences.afm_enable = afm_pref
    hide ball
    show cup as cup_1:
        xpos cup_coordinates[0] ypos 250
        easeout_expo 0.5 ypos -400
    show cup as cup_2:
        xpos cup_coordinates[1] ypos 250
        pause 0.1
        easeout_expo 0.5 ypos -400
    show cup as cup_3:
        xpos cup_coordinates[2] ypos 250
        pause 0.2
        easeout_expo 0.5 ypos -400
    pause 0.8
    hide cup_1
    hide cup_2
    hide cup_3
    hide screen extra_no_click
    show monika at t11

    if _current_turn == 0:
        m 3ekd "[player], ni siquiera hemos empezado a jugar :c"
        m 2gkp "Llevaba un rato queriendo jugar contigo...{w=1.0}"
        m 2etb "Pero,{w=0.5} quieres seguir jugando?{nw}"
        menu:
            "¿Pero, quieres seguir jugando?{fast}"
            "Sí":
                jump restart_sg
            "No":
                m 1hua "Vale, jugaremos en otra ocasión"

    elif _current_turn <= 10 or _current_turn >= 10:
        if _correct_answers == _current_turn:
            m 1hub "Solo jugamos unas cuantas partidas,pero{w=0.1}.{w=0.1}.{w=0.1}.¡Ya me has causado una buena impresión!"
            m 1hub "Lo has hecho genial en todas las partidas."
            m 1hua "Supongo que se nos acabó el tiempo..."
            m 1eua "Espero podamos jugar más la próxima vez"
            m 1eub "¡Estoy deseándolo!"
        elif _correct_answers < _current_turn:
            m 1hua "No te preocupes por haber fallado."
            m 3hub "¡Lo has hecho muy bien!"
            m 3hub "¡Solo es cuestión de practicar y verás cómo todo se vuelve más fácil!"
            m 3hua "La próxima vez lo harás mucho mejor~"
        elif _correct_answers == 0:
            m 1eka "[player], estoy preocupada..."
            m 1ekb "Llevamos jugando [_current_turn] y no has ganado ninguna"
            m 1etd "¿Te falta motivación o estás distraído?"
            if difficulty_sg == 1:
                m 1eua "Bueno, ya que estás en el modo más fácil..."
                m 1rkb "Supongo que te aburriste porque las copas avanzaban muy lento; ya sabes que es así."
                m 1rkb "Tendrás que probar los otros niveles de dificultad si quieres ponerte a prueba."
                m 1hua "En fin, dejemos todo esto para otro dia"
            elif difficulty_sg == 2:
                m 1eua "En el nivel de dificultad normal..."
                m 1rkb "Viste que no era gran cosa y no prestaste atención al juego"
                m 3hua "Ya sabes, puedes probar el nivel de dificultad difícil si quieres.."
                m 3hua "¡Quizás te motive a seguir adelante!"
                m 3hka "O puedes dejarlo para otro día, ¡tú decides!"
            elif difficulty_sg == 3:
                #============== ACA ESTOY HASTA AHORA 
                m 1eua "Teniendo en cuenta que estás en la dificultad difícil..."
                m 1rkb "No te tomaste el tiempo de seguir la pelota."
                m 1rsb "Aunque... por reflejo deberías haberla golpeado en algún momento."
                m 1rsb "Pero no fue así."
                m 3hua "Si te apetece jugar otra cosa, deja a un lado los minijuegos y hagamos algo que te motive ^^."
                if renpy.seen_label("to_cafe_loop"):
                    m 1eubsa "Podemos volver a salir juntos, por ejemplo, a la cafetería a la que fuimos."
                    m 1eubsb "Quizás eso te anime un poco."
                    m 2eka "Pero si lo que quieres es no hacer absolutamente nada..."
                    m 2dka "Espero que mi presencia te baste~"
        m 1dubla "Y gracias por tomarte el tiempo de jugar conmigo, [mas_get_player_nickname()]."

    elif _current_turn >= 50:
        if _correct_answers == _current_turn:
            m 2sub "Vaya, siempre me sorprendes con todo lo que haces, [mas_get_player_nickname()]."
            m 2sub "¡Felicidades!"
            m 3hub "¡Qué buenos reflejos tienes!"
            m 3hua "No me preocuparé de que falles en algún juego de feria, jejeje~"
            m 1tubsb "¡Me encantaría que me ganes un osito de peluche cuando tengamos una cita allí!"
        elif _correct_answers < _current_turn:
            m 3hua "Hiciste lo que pudiste, [mas_get_player_nickname()]."
            m 3hub "¡Me alegro mucho por ti!"
            m 3hub "Ya estábamos [_current_turn] rondas jugando."
            m 1ekb "Así que entiendo que no pudiste seguir adelante y lo dejaste en este punto."
            m 5hua "¡Pero algún día lo lograrás!, solo ten paciencia y practica un poco."
        elif _correct_answers == 0:
            m 1esb "Tengo una duda, [player]."
            m 1eka "Llevas intentándolo [_current_turn] veces y aún no has acertado ninguno."
            m 1etd "¿Te pasa algo?"
            if difficulty_sg == 1:
                m 1eka "Bueno, ya estas en el nivel facil..."
                m 1eta "¿Querias entrenar mejor tus reflejos poco a poco?"
                m 1hua "No hay nada de malo en hacerlo al revés."
                m 3ekb "Aunque intenta no olvidar que el juego consiste en ver donde esta la palota."
            elif difficulty_sg == 2:
                m 1eka "Al estar en dificultad intermedia..."
                m 1eta "¿Estas entrenando para poder perder cada ronda?"
                m 1hua " Me imagino que vas a llegar mas lejos, ya que estamo en la ronda [_current_turn]."
                m 1rtd "Aunque me pregunto de donde te a salido esa idea [player]..."
                m 1gsu "Mejor me guardare mis dudas, ¡solo observare hasta donde puedes llegar!"
            elif difficulty_sg == 3:
                m 1eka "Teniendo en cuenta que estas en la dificultad mas dificil..."
                m 1hua "creo que has dado lo mejor de ti para superar este reto."
                m 1etb "¿Querias llegar a mas de [_current_turn] rondas con fallos?"
                m 1eub "¡Pues te animo a que lo consigas, vamos tu puedes [player]!"
                m 1lta "Quizas te preguntes si me preocupas que falles hasta la ronda [_current_turn] "
                m 1dua "En realidad no, en este momento creo que lo estas haciendo a proposito -.-"
                m 1hksdlb "Siento animarte a fallar en lugar de acertar cada ronda ,jajajaja~"
                m 1hksdlb "Pero ya lo estas haciendo, ¡asi que no tengo mas remedio que apoyarte!"
        m 1eua "Aunque me alegra que te guste este minijuego, jeje."
        if renpy.seen_label("game_chess"):
            m 3eub "No es como el ajedrez, aquí hay que usar estrategias..."
            m 3eub "Pero es bueno jugar otros juegos, ¿no crees?"
        m 1eka "No pensé que te gustaría tanto porque la dinámica es muy sencilla"
        m 4hub "Bueno, de todos modos, ¡gracias por jugar conmigo, [mas_get_player_nickname()]!"
        m 4hub "Jugaremos en otra ocasión, si te parece bien"

    elif _current_turn >= 100:
        if _correct_answers == _current_turn:
            m 1hua "Tengo que felicitarte, [player]."
            m 1hub "Has acertado todas las rondas, ¡eso demuestra lo concentrado que has estado!"
            m 1hublb "¡Estoy orgullosa de ti!"
            m 1ekb "Me encantaría darte algo de premio, pero no puedo hacer nada desde aquí, jajaja~..."
            m 3hua "Sí, ¡realmente has entrenado mucho!"
            m 1eub "Se me da la impresión de que se te dan bien los juegos de ritmo."
            m 1eta "¿O es tu sistema de defensa personal 0.0? "
            extend 1sua "Si es así, me alegra oirlo"
        elif _correct_answers < _current_turn:
            m 1hua "Nada mal, [player]."
            m 1hub "¡Lo has dado todo después de haber intentado [_current_turn] veces!"
            m 1eka "Es normal que te sientas un poco cansado "
            m 1eka "Pero no te desanimes"
            m 3eub "La próxima vez lo harás mucho mejor, créeme~"
        elif _correct_answers == 0:
            m 1hka "No sé qué pensar de esto"
            m "Llevamos [_current_turn] rondas y no has acertado ni una"
            m 1etb "A este punto, ¿me da la impresión de que es una especie de reto personal?"
            if difficulty_sg == 1:
                m 1eua "Bueno, estamos en la dificultad más fácil.."
                m 3wud "¡Es sencillo lograrlo!, sin embargo, es algo que lleva tiempo"
                m 3hub "¡Me sorprende cuánto tiempo y esfuerzo has invertido!"
            elif difficulty_sg == 2:
                m 1eua "Estamos en una dificultad más alta que la fácil.."
                m 3eub "Tenías la oportunidad de acertar al menos uno."
                m 1hub "Me encantaría ver tu cara mientras haces esto, jejeje~"
            elif difficulty_sg == 3:
                m 1eua "Teniendo en cuenta que estamos en la dificultad más dificil..."
                m 1sub "Me sorprende el tiempo que has invertido."
                m 1hub "Te has tomado muy en serio, en el sentido qué has fallado a propósito, jejeje~"
        m 1hubsa "Bueno, te agradezco que te hayas tomado el tiempo de jugar conmigo, ¡me lo he pasado muy bien!"
        m 3eka "Y además, descansa un poco la vista, que hemos estado jugando por mucho tiempo..."
        m 3hub "¡Te lo has ganado!"
        m 1dub "Siempre me preocupará tu salud, [mas_get_player_nickname()]."
        m 1dua "Y no te preocupes por mí, te estaré esperando."

    window hide
    python:
        cup_speed = 0.5
        _current_turn = 0
        _correct_answers = 0
    jump close_extraplus
    return