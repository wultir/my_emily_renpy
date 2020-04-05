label bonus_christmas:
    $ renpy.music.set_volume(1.0, 0, channel="music")
    play music "audio/bgm/Music/Jingle_Bells_3.ogg" fadein 5.0

    scene bg black with Dissolve(1.0)

    show text "{font=fonts/Elsie-Regular.ttf}{color=#f50505}{size=81}Here's your small christmas present{/size}{/color}{/font}" as christmas_text1 with Dissolve(5.0):
        pos (538, 121)
        anchor (0,0)
    show text "{font=fonts/Elsie-Regular.ttf}{color=#f50505}{size=50}Atleast it's better than socks!{/size}{/color}{/font}" as christmas_text2 with Dissolve(1.0):
        pos (898, 222)
        anchor (0,0)
    show text "{font=fonts/Elsie-Regular.ttf}{color=#f50505}{size=70}Love you all.. Almost all..{/size}{/color}{/font}" as christmas_text3 with Dissolve(1.0):
        pos (529, 315)
        anchor (0,0)

    show santa walking_animated with Dissolve(1.0):
        align(0,0)

    show transsnow with Dissolve(1.0)

    pause 10.0
    hide christmas_text1
    hide christmas_text2
    hide christmas_text3
    with Dissolve(1.0)

    hide transsnow with Dissolve(1.0)
    pause 1.0
    hide santa walking_animated width Dissolve(1.0)

label bonus_christmas_c1:
    scene bg c1 with Dissolve(5.0)
label bonus_christmas_c2:
    scene bg c2 with Dissolve(5.0)
label bonus_christmas_c3:
    scene bg c3 with Dissolve(5.0)
label bonus_christmas_c4:
    scene bg c4 with Dissolve(5.0)
label bonus_christmas_c5:
    scene bg c5 with Dissolve(5.0)


label bonus_christmas_c6:
    play music "audio/bgm/Music/Record_Scratch.ogg" noloop 
    pause 1.0
    scene bg c6 with Dissolve(1.0)


label bonus_christmas_c7:
    play music "audio/bgm/Music/AwayInAMangerEDM.ogg"
    pause 1.0
    scene bg c7 with Dissolve(7.0)


label bonus_christmas_c8:
    scene bg c8 with Dissolve(7.0)


label bonus_christmas_c9:
    scene bg c9 with Dissolve(7.0)


label bonus_christmas_c10:
    scene bg c10 with Dissolve(7.0)


label bonus_christmas_c11:
    scene bg c11 with Dissolve(8.0) # TODO: Uses fadeIn in tyrano


label bonus_christmas_c12:
    scene bg c12 with dissolve:
        zoom 2.0
        align (0.5, 0.5)
        linear 7.0 zoom 1.0
    pause 7.0


label bonus_christmas_c13:
    scene bg c13 with Dissolve(5.0)


label bonus_christmas_c14:
    scene bg c14 with Dissolve(5.0)


label bonus_christmas_c15:
    scene bg c15 with Dissolve(5.0)
    scene bg c15a with Dissolve(1.0)
    scene bg c15b with Dissolve(1.0)
    scene bg c15a with Dissolve(1.0)
    scene bg c15b with Dissolve(1.0)
    scene bg c15a with Dissolve(1.0)
    scene bg c15b with Dissolve(1.0)
    scene bg c15a with Dissolve(1.0)
    scene bg c15b with Dissolve(1.0)
    scene bg c15a with Dissolve(1.0)
    scene bg c15b with Dissolve(1.0)


label bonus_christmas_c16:
    scene bg c16 with dissolve:
        zoom 2.0
        align (0.5, 0.5)
        linear 6.5 zoom 1.0
    pause 6.5


label bonus_christmas_c17:
    scene bg c17 with Dissolve(5.0)


label bonus_christmas_c18:
    scene bg c18 with Dissolve(5.0)


label bonus_christmas_c19:
    scene bg c19 with Dissolve(5.0)


label bonus_christmas_c20:
    scene bg c20 with Dissolve(5.0)


label bonus_christmas_c21:
    scene bg c21 with Dissolve(5.0)


label bonus_christmas_c22:
    scene bg c22 with Dissolve(4.0) # TODO: fadeIn in tyrano


label bonus_christmas_c23:
    scene bg c23 with dissolve:
        zoom 2.0
        align (0.5, 0.5)
        linear 5.5 zoom 1.0
    pause 5.5

label bonus_christmas_c24:
    scene bg c24 with Dissolve(6.0)


label bonus_christmas_c25:
    scene bg c25 with Dissolve(2.0) # TODO: fadeIn in tyrano


label bonus_christmas_c26:
    scene bg c26 with dissolve:
        zoom 2.0
        align (0.5, 0.5)
        linear 4.5 zoom 1.0
    pause 4.5


label bonus_christmas_c27:
    scene bg c27 with Dissolve(5.0)


label bonus_christmas_c28:
    scene bg c28 with Dissolve(5.0)


label bonus_christmas_c29:
    scene bg c29 with Dissolve(5.0)


label bonus_christmas_c30:
    scene bg c30 with Dissolve(5.0)


label bonus_christmas_c31:
    scene bg c31 with Dissolve(5.0)


label bonus_christmas_c32:
    scene bg c32 with Dissolve(5.0)


label bonus_christmas_c33:
    scene bg c33 with Dissolve(5.0)


label bonus_christmas_end:
    scene bg white with Dissolve(5.0)

    pause 1.0

    scene bg black with Dissolve(1.0)


    show text "{font=fonts/Elsie-Regular.ttf}{color=#f50505}{size=100}Merry Christmas{/size}{/color}{/font}" as christmas_text1 with Dissolve(5.0):
        pos (538, 121)
        anchor (0,0)
    show text "{font=fonts/Elsie-Regular.ttf}{color=#f50505}{size=50}and{/size}{/color}{/font}" as christmas_text2 with Dissolve(1.0):
        pos (898, 222)
        anchor (0,0)
    show text "{font=fonts/Elsie-Regular.ttf}{color=#f50505}{size=100}A happy new year{/size}{/color}{/font}" as christmas_text3 with Dissolve(4.0):
        pos (529, 315)
        anchor (0,0)

    pause 1.0
    hide christmas_text1
    hide christmas_text2
    hide christmas_text3
    with Dissolve(1.0)
