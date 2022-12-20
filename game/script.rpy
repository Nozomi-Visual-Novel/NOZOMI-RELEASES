#### SPLASH SCREEN SECTION ####
## Declarations For Splash Screen ##
image warning = 'images/splash/warning.png'
## Label To Start The Splash ##
label splashscreen:
    ## Renpy Video Declaration In .webm ##
    $ renpy.movie_cutscene("videos/intro.webm")
    ## Soft Transition ##
    scene black
    with dissolve
    ## Warning Scene ##
    scene warning
    with dissolve
    with Pause(3)
    ## Soft Transition ##
    scene black
    with dissolve
    ## Return To The Main Menu ##
    return

#### IMAGES DECLARATIONS ####
image bg roses = 'images/bg/flowers.png'
image bg hall = 'images/bg/hall.png'
image bg office = 'images/bg/office.png'
image bg room = 'images/bg/room.png'
image bg blood1 = 'images/bg/room_blood.png'
image bg blood2 = 'images/bg/room_blood_2.png'
image bg blood3 = 'images/bg/room_blood_3.png'
image izumi = 'images/characters/izumi_arm_cut.png'
image izumired = 'images/characters/izumi_red.png'
image izumicut = 'images/characters/izumi_arm.png'

#### CAHARACTERS DECLARATIONS ####
define izumi = Character("Izumi")
define annie = Character("Annie")
define azumi = Character("Azumi")
define edith = Character("Edith")
define unknow = Character("¿?")


#### GAME START ####
label start:

    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)
    ## Soft Dissolve & Music Change ##
    stop music
    with dissolve
    scene black
    with dissolve
    with Pause(2)
    play music 'audio/bgm/future_melody.wav'

    
    ## Dialogue Lines & Voices ##
    play sound 'audio/voices/iz1.wav'
    "{cps=40}Una suave brisa golpea mi cara y me hace despertar.{/cps}"
    ## New Scene ##
    scene bg roses
    with dissolve
    ## Dialogue Lines & Voices ##
    play sound 'audio/voices/iz2.wav'
    "{cps=40}Estoy rodeada de bellas flores, mis rosas favoritas.{/cps}"
    play sound 'audio/voices/iz3.wav'
    "{cps=40}A lo lejos veo un gran lago perfecto para pescar.{/cps}"
    play sound 'audio/voices/iz4.wav'
    "{cps=40}Está haciendo un clima perfecto el sol brilla y hace más reluciente este bello paisaje.{/cps}"
    play sound 'audio/voices/iz5.wav'
    "{cps=40}Mi familia está esperando adentro con rica y muy caliente comida.{/cps}"
    play sound 'audio/voices/ed1.wav'
    azumi "{cps=40}Izumi ven que se nos hace tarde.{/cps}"
    play sound 'audio/voices/iz6.wav'
    izumi "{cps=40}Ya voy mamá.{/cps}"
    play sound 'audio/voices/iz7.wav'
    "{cps=40}Este día no podría ser mejor.{/cps}"
    ## New Scene ##
    stop music
    scene black
    with dissolve
    play sound 'audio/voices/iz8.wav'
    "{cps=40}O bueno eso me gustaría decir.{/cps}"
    scene bg office
    with dissolve
    ## Dialogue Lines & Voices ##
    play sound 'audio/voices/ed2.wav'
    edith "{cps=40}KIMURA.{/cps}"
    play sound 'audio/voices/iz9.wav'
    izumi "{cps=40}Aja.{/cps}"
    play sound 'audio/voices/ed3.wav'
    edith "{cps=40}Es la cuarta vez que te escapas acaso no te das cuenta de lo grave que es esto.{/cps}"
    play sound 'audio/voices/iz10.wav'
    "{cps=40}Wow ya me he escapado 4 veces deberían de premiarme o algo así.{/cps}"
    play sound 'audio/voices/iz11.wav'
    izumi "{cps=40}Aja.{/cps}"
    play sound 'audio/voices/ed4.wav'
    edith "{cps=40}Izumi no podemos permitir que sigas cometiendo este acto de rebeldía.{/cps}"
    play sound 'audio/voices/iz12.wav'
    izumi "{cps=40}Aja.{/cps}"
    play sound 'audio/voices/ed5.wav'
    edith "{cps=40}Ah.{/cps}"
    play sound 'audio/voices/ed6.wav'
    edith "{cps=40}Mira Izumi si vuelves a cometer otra falta no tendremos otra opción que enviarte al centro de rehabilitación.{/cps}"
    play sound 'audio/voices/ed7.wav'
    edith"{cps=40}¿Eso es lo realmente quieres?{/cps}"
    play sound 'audio/voices/iz13.wav'
    "{cps=40}Mi gran sueño el centro de rehabilitación espero estar pronto allí.{/cps}"
    play sound 'audio/voices/iz14.wav'
    "{cps=40}Hora de planear mi nueva huida.{/cps}"
    play sound 'audio/voices/iz15.wav'
    izumi "{cps=40}Edith puedo irme ya estoy muy cansada.{/cps}"
    play sound 'audio/voices/ed8.wav'
    edith "{cps=40}Kimura escuchame nuestro objetivo es ayudarte ¿porque te opones tanto a ello?{/cps}"
    play sound 'audio/voices/iz16.wav'
    "{cps=40}De nuevo con esto, estoy harta.{/cps}"
    play sound 'audio/voices/iz17.wav'
    izumi "{cps=40}Preguntale a Holly.{/cps}"
    play sound 'audio/voices/iz18.wav'
    izumi "{cps=40}Ohh verdad que no puedes porque ustedes la mataron enfermos de mierda.{/cps}"
    play sound 'audio/voices/ed9.wav'
    edith "{cps=40}Izumi por última vez Holly no está muerta solo se movió a otro centro.{/cps}"
    play sound 'audio/voices/iz19.wav'
    izumi "{cps=40}Vaya que buena forma de encubrir sus asquerosos actos.{/cps}"
    play sound 'audio/voices/iz20.wav'
    izumi "{cps=40}Deberías ser actriz ¿no lo crees Edith?{/cps}"
    play sound 'audio/voices/iz21.wav'
    izumi "{cps=40}Eres igual de repugnante que todos aquí.{/cps}"
    play sound 'audio/voices/ed10.wav'
    edith "{cps=40}Fuera de mi oficina.{/cps}"
    play sound 'audio/voices/iz22.wav'
    izumi "{cps=40}Buenas noches Edith me alegra que nuestra charla haya sido tan amena y tranquila.{/cps}"
    play sound 'audio/voices/iz23.wav'
    "{cps=40}Maldita perra.{/cps}"
    play sound 'audio/voices/iz24.wav'
    stop music
    play music 'audio/bgm/second.wav'
    scene bg hall
    with dissolve
    "{cps=40}Salgo de la oficina con bastante calma y algo de asco.{/cps}"
    play sound 'audio/voices/iz25.wav'
    "{cps=40}Los largos pasillos casi infinitos y el crepúsculo del sol casi imperceptible y el olor putrefacto hacen inconfundible este lugar.{/cps}"
    play sound 'audio/voices/iz26.wav'
    "{cps=40}Miro en una sala y hay niños recibiendo clases de inglés.{/cps}"
    play sound 'audio/voices/iz27.wav'
    "{cps=40}Que suerte tienen esos mocosos.{/cps}"
    play sound 'audio/voices/iz28.wav'
    "{cps=40}En otra sala hay varios chicos castigados en jaulas como si fueran animales.{/cps}"
    play sound 'audio/voices/iz29.wav'
    "{cps=40}Me sorprende que no me hayan enviado allí otra vez.{/cps}"
    play sound 'audio/voices/iz30.wav'
    "{cps=40}Pasaba la mayor parte de mi día allí acostada mirando al techo sola con mis pensamientos.{/cps}"
    play sound 'audio/voices/iz31.wav'
    "{cps=40}Ese sucio y casi desprendido techo en el cual los insectos aman estar era allí en donde podía vivir mis mejores momentos.{/cps}"
    play sound 'audio/voices/iz32.wav'
    "{cps=40}Alejada de toda esta porquería.{/cps}"
    scene bg room
    with dissolve
    play sound 'audio/voices/iz33.wav'
    "{cps=40}Finalmente llego a mi habitación en donde una inconfundible voz me saluda.{/cps}"
    play sound 'audio/voices/an1.wav'
    unknow "{cps=40}¡Izumi!{/cps}"
    play sound 'audio/voices/iz34.wav'
    "{cps=40}Por supuesto no podía ser nadie más que mi gran amiga Annie.{/cps}"
    play sound 'audio/voices/iz35.wav'
    annie "{cps=40}¡Annie!{/cps}"
    play sound 'audio/voices/iz36.wav'
    "{cps=40}Corro apresuradamente donde Annie a darle un abrazo.{/cps}"
    play sound 'audio/voices/iz37.wav'
    "{cps=40}No puedo creer que lo necesitara tanto, todos mis pensamientos se desvanecen y sólo se fijan en ahora Annie.{/cps}"
    play sound 'audio/voices/an2.wav'
    annie "{cps=40}Vaya mira quien vuelve después de haber tenido su cuarta fuga.{/cps}"
    play sound 'audio/voices/an3.wav'
    annie "{cps=40}¿Cómo dejaste que te descubrieran de nuevo? ya estabas fuera Izu.{/cps}"
    play sound 'audio/voices/iz38.wav'
    izumi "{cps=40}Ya sabes que esa gente está en todos lados no pude reconocerlos.{/cps}"
    play sound 'audio/voices/iz39.wav'
    "{cps=40}Nuevamente.{/cps}"
    play sound 'audio/voices/an4.wav'
    annie "{cps=40}Ah si, pero mira quien no quiso llevarme de nuevo.{/cps}"
    play sound 'audio/voices/iz40.wav'
    "{cps=40}Annie cambia su expresión de felicidad a una más seria.{/cps}"
    play sound 'audio/voices/iz41.wav'
    izumi "{cps=10}Annie creeme que de verdad intente que saliéramos nuevamente juntas, pero me ha sido muy difícil y…{/cps}"
    play sound 'audio/voices/an5.wav'
    annie "{cps=40}Ja, ja, ja ya calmate Izu solo estaba bromeando yo saldré cuando lo necesite tengo mis métodos.{/cps}"
    play sound 'audio/voices/iz42.wav'
    izumi "{cps=40}Ya veo…{/cps}"
    play sound 'audio/voices/an6.wav'
    annie "{cps=40}Tranquilizate Izu sabes que no podría enojarme contigo después de lo de Holly.{/cps}"
    play sound 'audio/voices/an7.wav'
    annie "{cps=40}No sabes como la extraño.{/cps}"
    play sound 'audio/voices/iz43.wav'
    izumi "{cps=40}Yo igual, pero oye creeme algún día tendremos nuestra venganza en nombre de Holly ¿está bien?{/cps}"
    play sound 'audio/voices/iz44.wav'
    "{cps=40}Comenzando por Edith todo sería perfecto.{/cps}"
    play sound 'audio/voices/an8.wav'
    annie "{cps=40}Sé que lo haremos gracias Izu.{/cps}"
    play sound 'audio/voices/iz45.wav'
    "{cps=40}Annie nuevamente me abraza parece que de verdad me extraño.{/cps}"
    play sound 'audio/voices/an9.wav'
    annie "{cps=40}Oye hablando de cosas más positivas esta noche con los chicos vamos a robar el cargamento de alimentos ¿te nos unes?{/cps}"
    play sound 'audio/voices/iz46.wav'
    izumi "{cps=40}Créeme que de verdad me encantaría, pero estoy muy cansada todo el tema de mi reingreso me dejó agotada.{/cps}"
    play sound 'audio/voices/an10.wav'
    annie "{cps=40}Está bien no te fuerces prometo traerte algo bueno.{/cps}"
    play sound 'audio/voices/iz47.wav'
    izumi "{cps=40}Gracias Annie sin duda eres la mejor.{/cps}"
    play sound 'audio/voices/an11.wav'
    annie "{cps=40}Oye para eso están las amigas.{/cps}"
    play sound 'audio/voices/iz48.wav'
    "{cps=40}Lo único bueno de toda esta mierda es Annie y espero que siga siendo así.{/cps}"
    play sound 'audio/voices/iz49.wav'
    izumi "{cps=40}Oye Annie voy a cambiarme podrías salir por favor.{/cps}"
    play sound 'audio/voices/an12.wav'
    annie "{cps=40}Oh sí claro perdona algún día tendré ese beneficio te lo aseguro.{/cps}"
    play sound 'audio/voices/iz50.wav'
    "{cps=40}Annie se comporta muy raro a veces.{/cps}"
    play sound 'audio/voices/an13.wav'
    annie "{cps=40}Bueno Izu te dejo, ten buena noche.{/cps}"
    play sound 'audio/voices/iz51.wav'
    izumi "{cps=40}Igualmente Annie.{/cps}"
    play sound 'audio/voices/iz52.wav'
    "{cps=40}Annie se va corriendo rápidamente entre aquellos pasillos que llevan a la nada.{/cps}"
    stop music
    play music 'audio/bgm/wind.wav'
    play sound 'audio/voices/iz53.wav'
    "{cps=40}Prendo la luz y aseguro mi puerta.{/cps}"
    play sound 'audio/voices/iz54.wav'
    izumi "{cps=40}Hogar dulce hogar{/cps}"
    play sound 'audio/voices/iz55.wav'
    "{cps=40}Caminó lenta y temblorosamente entre la profundidad de mi habitación.{/cps}"
    play sound 'audio/voices/iz56.wav'
    "{cps=40}Finalmente llego a mi sucia y vieja cama.{/cps}"
    play sound 'audio/voices/iz57.wav'
    izumi "{cps=40}Es hora.{/cps}"
    play sound 'audio/voices/iz58.wav'
    "{cps=40}Saco de mi bolsa una cuchilla.{/cps}"
    play sound 'audio/voices/iz59.wav'
    "{cps=40}No puedo creer que lo haga nuevamente.{/cps}"
    play sound 'audio/voices/iz60.wav'
    "{cps=40}Pero es mi única opción para salir de todo.{/cps}"
    play sound 'audio/voices/iz61.wav'
    show izumi
    with moveinbottom
    "{cps=40}Empiezo a cortar mi brazo nuevamente.{/cps}"
    show izumi
    scene bg blood1
    show izumi
    play sound 'audio/voices/iz62.wav'
    izumi "{cps=30}Pensamientos felices.{/cps}"
    show izumired
    stop music
    play music 'audio/bgm/second_reverse.wav'
    scene bg blood2
    show izumired at Shake((0.5, 1.0, 0.5, 1.0), 99.0, dist=5)  
    play sound 'audio/voices/iz63.wav'
    izumi "{cps=20}Pensamientos felices.{/cps}"
    show izumicut at Shake((0.5, 1.0, 0.5, 1.0), 99.0, dist=7)  
    scene bg blood3
    show izumicut at Shake((0.5, 1.0, 0.5, 1.0), 99.0, dist=7)   
    play sound 'audio/voices/iz64.wav'
    izumi "{cps=9}PENSAMIENTOS FELICES.{/cps}"

    # This ends the game.