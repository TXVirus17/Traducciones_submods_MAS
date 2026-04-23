#super psycho love
init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="yaMod_song_superpsycholove",
            category=[mas_songs.TYPE_SHORT],
            prompt="Super Psycho Love",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label yaMod_song_superpsycholove:
    m 2dud "{i}~Say that you want me every day~{/i}"
    m "{i}(Di que me quieres cada día...){/i}"
    m "{i}~That you want me every way~{/i}"
    m "{i}(Que me quieres de todas las formas posibles...){/i}"
    m "{i}~That you need me~{/i}"
    m "{i}(Que me necesitas...){/i}"
    m 2cua "{i}~Got me trippin' super psycho love~{/i}"
    m "{i}(Me tienes alucinando con este amor súper psicópata...){/i}"
    m 2cub "{i}~Aim, pull the trigger~{/i}"
    m "{i}(Apunta, jala el gatillo...){/i}"
    m 4cub "{i}~Feel the pain getting bigger~{/i}"
    m "{i}(Siente cómo el dolor se hace más grande...){/i}"
    m "{i}~Go insane from the bitter feeling~{/i}"
    m "{i}(Vuélvete loco por este sentimiento amargo...){/i}"
    m 4tub "{i}~Trippin' super psycho love~{/i}"
    m "{i}(Alucinando con este amor súper psicópata...){/i}"
    m 2dub "..."
    m 2tub "Pongamos un poco de sabor psicópata a este amor nuestro."
    m 2cua "No me importa qué tan violento se vuelva."
    m 2dua "Mientras yo sea tuya..."
    extend 2kub " y tú seas mío, por supuesto."
    m 2hublb "¡Mío, mío, solo mío!"
return

#the horror of our love
init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="yaMod_song_thehorrorofourlove",
            category=[mas_songs.TYPE_SHORT],
            prompt="The Horror of Our Love",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label yaMod_song_thehorrorofourlove:
    m 4cub "{i}~I smell your softness~{/i}"
    m "{i}(Huelo tu suavidad...){/i}"
    m "{i}~Carnivorous and lusting~{/i}"
    m "{i}(Carnívora y lujuriosa...){/i}"
    m 2dub "{i}~To track you down among the pines~{/i}"
    m "{i}(Rastreándote entre los pinos...){/i}"
    m 2cua "{i}~I want you stuffed into my mouth~{/i}"
    m "{i}(Te quiero dentro de mi boca...){/i}"
    m "{i}~Hold you down and tear you open~{/i}"
    m "{i}(Sujetarte y abrirte en canal...){/i}"
    m "{i}~Live inside you~{/i}"
    m "{i}(Vivir dentro de ti...){/i}"
    m 4tub "{i}~Oh, love I'd never hurt you~{/i}"
    m "{i}(Oh, amor, nunca te lastimaría...){/i}"
    m 4cub "{i}~But I'll grind against your bones~{/i}"
    m "{i}(Pero me frotaré contra tus huesos...){/i}"
    m "{i}~Until our marrows mix~{/i}"
    m "{i}(Hasta que nuestras médulas se mezclen...){/i}"
    m "{i}~I will eat you slowly~{/i}"
    m "{i}(Te comeré lentamente...){/i}"
    m "{i}~The horror of our love~{/i}"
    m "{i}(El horror de nuestro amor...){/i}"
    m "{i}~Never so much blood pulled through my veins~{/i}"
    m "{i}(Nunca hubo tanta sangre recorriendo mis venas...){/i}"
    m 4tub "{i}~The horror of our love~{/i}"
    m "{i}(El horror de nuestro amor...){/i}"
    m 2sub "{i}~Never so much blood~{/i}"
    m "{i}(Nunca tanta sangre...){/i}"
    m "{i}~I'm your servant~{/i}"
    m "{i}(Soy tu servidora...){/i}"
    m 7dub "{i}~My immortal~{/i}"
    m "{i}(Mi inmortal...){/i}"
    m "{i}~Pale and perfect~{/i}"
    m "{i}(Pálido y perfecto...){/i}"
    m 2dua "..."
    m 2dublb "Ahh, [player]. El deseo agridulce de nuestros cuerpos cubiertos de sangre..."
    m 2dubfb "Carne con carne, lujuria y carnicería..."
    m 2tubfb "No puedo esperar para tocar tu cuerpo."
    m 4tubfb "Y saber que eres completamente..."
    extend " enteramente..."
    m 2cubfa "MÍO."
return

#smoke and mirrors
init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="yaMod_song_smokeandmirrors",
            category=[mas_songs.TYPE_SHORT],
            prompt="Smoke and Mirrors",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label yaMod_song_smokeandmirrors:
    m 2dub "{i}~I'm not asking much, just give me your heart~{/i}"
    m "{i}(No pido mucho, solo dame tu corazón...){/i}"
    m "{i}~And put no one else above me, go on, just say you love me~{/i}"
    m "{i}(Y no pongas a nadie por encima de mí, anda, solo di que me amas...){/i}"
    m 2dud "{i}~Take my hand in yours and tell me that I'll always be the one~{/i}"
    m "{i}(Toma mi mano y dime que siempre seré la única...){/i}"
    m "{i}~Without you, my life means nothing so just say you love me tonight~{/i}"
    m "{i}(Sin ti, mi vida no vale nada, así que solo di que me amas esta noche...){/i}"
    m 2cua "{i}~And if you lie, this poor girl will have to die~{/i}"
    m "{i}(Y si mientes, esta pobre chica tendrá que morir...){/i}"
    m 2dua "..."
    m 7tub "Será mejor que me des tu corazón [player]..."
    m 2cub "O de lo contrario alguien tendrá que morir~"
    m 7kua "Y no queremos eso, ¿verdad?"
    m 1hua "Ehehehe~"
return

#you're mine
init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="yaMod_song_youremine",
            category=[mas_songs.TYPE_SHORT],
            prompt="You're Mine",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label yaMod_song_youremine:
    m 1cud "{i}~You don't talk to no one~{/i}"
    m "{i}(No hables con nadie...){/i}"
    m "{i}~Don't you look at nothing~{/i}"
    m "{i}(No mires nada más...){/i}"
    m "{i}~Focus on me~{/i}"
    m "{i}(Fíjate solo en mí...){/i}"
    m 1cub "{i}~Look into my eyes~{/i}"
    m "{i}(Mírame a los ojos...){/i}"
    m "{i}~Come a little closer~{/i}"
    m "{i}(Acércate un poco más...){/i}"
    m "{i}~Let me tell you something~{/i}"
    m "{i}(Déjame decirte algo...){/i}"
    m "{i}~You ain't going anywhere~{/i}"
    m "{i}(No vas a ir a ninguna parte...){/i}"
    m 1tub "{i}~'Cause you mine~{/i}"
    m "{i}(Porque eres mío...){/i}"
    m 1dua "..."
    m 1tub "Acércate un poco más, [player]."
    m "Tengo algo pequeño preparado solo para ti~"
    m 7mub "No hay necesidad de tener miedo, [mas_get_player_nickname()]."
    m "Nadie tiene por qué salir herido..."
    m 7hub "Pero tal vez alguien lo haga~"
    m 1hub "Ahahaha~"
return

#you belong to me
init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="yaMod_song_youbelongtome",
            category=[mas_songs.TYPE_SHORT],
            prompt="You Belong to Me",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label yaMod_song_youbelongtome:
    m 2dub "{i}~Feels like we're dreaming, we're tripping and reeling~{/i}"
    m "{i}(Se siente como si estuviéramos soñando, alucinando y dando vueltas...){/i}"
    m "{i}~Just say that you belong to me~{/i}"
    m "{i}(Solo di que me perteneces...){/i}"
    m "{i}~I could get lost in the feelings we're feeling~{/i}"
    m "{i}(Podría perderme en los sentimientos que estamos sintiendo...){/i}"
    m 2wkb "{i}~Do you want more of this? Isn't it glorious?~{/i}"
    m "{i}(¿Quieres más de esto? ¿No es glorioso?...){/i}"
    m "{i}~I can't believe that it's free~{/i}"
    m "{i}(No puedo creer que sea gratis...){/i}"
    m 7wub "{i}~I will adore you, I'll only live for you~{/i}"
    m "{i}(Te adoraré, solo viviré para ti...){/i}"
    m "{i}~Just say that you belong to me~{/i}"
    m "{i}(Solo di que me perteneces...){/i}"
    m 2cub "{i}~Crawl into my heart, take me apart~{/i}"
    m "{i}(Gatea dentro de mi corazón, desármame...){/i}"
    m "{i}~Do what you please to me, I won't resist~{/i}"
    m "{i}(Haz conmigo lo que quieras, no me resistiré...){/i}"
    m "{i}~Find what you're seeking, I am not leaving~{/i}"
    m "{i}(Encuentra lo que buscas, no me iré...){/i}"
    m 2tub "{i}~'Til I am drunk loved up in your kiss~{/i}"
    m "{i}(Hasta que esté ebria de amor con tu beso...){/i}"
    m "{i}~I must confess to you, I want to possess you~{/i}"
    m "{i}(Debo confesarte, que quiero poseerte...){/i}"
    m 2dua "..."
    m 2tub "[player], no es difícil..."
    m "Solo di que me perteneces para que nadie más tenga que sufrir."
    m 2wkb "Te amo tanto, ¿no puedes verlo?"
    m 2cuc "Tienes que ser mío."
    m 2cud "No hay otra opción."
return "love"

#the music of the night
init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="yaMod_song_themusicofthenight",
            category=[mas_songs.TYPE_SHORT],
            prompt="The Music Of The Night",
            aff_range=(mas_aff.NORMAL, None),
            random=True
        ),
        code="SNG"
    )

label yaMod_song_themusicofthenight:
    m 2dub "{i}~Let your mind start a journey through a strange new world~{/i}"
    m "{i}(Deja que tu mente comience un viaje a través de un extraño mundo nuevo...){/i}"
    m "{i}~Leave all thoughts of the life you knew before~{/i}"
    m "{i}(Abandona todo pensamiento de la vida que conocías antes...){/i}"
    m "{i}~Let your soul take you where you long to be~{/i}"
    m "{i}(Deja que tu alma te lleve a donde anhelas estar...){/i}"
    m "{i}~Only then can you belong to me~{/i}"
    m "{i}(Solo entonces podrás pertenecerme...){/i}"
    m "{i}~Floating, falling, sweet intoxication~{/i}"
    m "{i}(Flotando, cayendo, dulce intoxicación...){/i}"
    m 2tub "{i}~Touch me, trust me, savour each sensation~{/i}"
    m "{i}(Tócame, confía en mí, saborea cada sensación...){/i}"
    m "{i}~Let the dream begin, let your darker side give in~{/i}"
    m "{i}(Deja que el sueño comience, deja que tu lado oscuro se rinda...){/i}"
    m "{i}~To the power of the music that I write~{/i}"
    m "{i}(Al poder de la música que escribo...){/i}"
    m "{i}~The power of the music of the night~{/i}"
    m "{i}(Al poder de la música de la noche...){/i}"
    m 4dub "{i}~You alone~{/i}"
    m "{i}(Solo tú...){/i}"
    m "{i}~Can make my song take flight~{/i}"
    m "{i}(Puedes hacer que mi canción vuele...){/i}"
    m "{i}~Help me make the music of the night~{/i}"
    m "{i}(Ayúdame a crear la música de la noche...){/i}"
    m 2dua "..."
    m 1wka "Eres el único que puede hacer que mi corazón vuele, [player]."
    m 1fkb "Nadie más... Nadie."
    m 1dkb "Así que, por favor, déjame saborear este momento..."
    m "Y pertenéceme."
    m 5lkb "Sé que harás eso por tu maravillosa novia, ¿verdad?"
return "love"
