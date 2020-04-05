label the_end_04:
    scene bg music with Dissolve(1.0)
    call wait_for_click(False)

    scene bg black with Dissolve(1.0)

    $ renpy.music.set_volume(0.5, 0, channel="music")
    play music "audio/bgm/Music/bensound-endlessmotion.ogg" fadein  3.0

    show text "{font=fonts/GreatVibes-Regular.ttf}{color=#f686b8}{size=100}My Emily{/size}{/color}{/font}" as end_text1 with Dissolve(6.0):
        pos (666, 65)
        anchor (0,0)
    show text "{font=fonts/Elsie-Regular.ttf}{color=#f686b8}{size=50}v 0.4a{/size}{/color}{/font}" as end_text2 with Dissolve(5.0):
        pos (976, 177)
        anchor (0,0)
    hide end_text1
    hide end_text2
    with Dissolve(8.0)

    show text "{font=fonts/Elsie-Regular.ttf}{color=#8fcdff}{size=50}Music by https://www.bensound.com/royalty-free-music{/size}{/color}{/font}" as end_text1 with Dissolve(3.0):
        pos (486, 76)
        anchor (0,0)
    show text "{font=fonts/Elsie-Regular.ttf}{color=#8fcdff}{size=50}Audionautix.com{/size}{/color}{/font}" as end_text2 with Dissolve(3.0):
        pos (1050, 192)
        anchor (0,0)
    pause 3.0
    hide end_text1
    hide end_text2
    with Dissolve(1.0)

    show text "{font=fonts/Elsie-Regular.ttf}{color=#f686b8}{size=50}and{/size}{/color}{/font}" as end_text1 with Dissolve(1.0):
        pos (648, 371)
        anchor (0,0)
    show text "{font=fonts/Elsie-Regular.ttf}{color=#8fcdff}{size=50}https://danosongs.com{/size}{/color}{/font}" as end_text2 with Dissolve(3.0):
        pos (81, 574)
        anchor (0,0)
    show text "{font=fonts/Elsie-Regular.ttf}{color=#8fcdff}{size=50}Exzel Music Publishing{/size}{/color}{/font}" as end_text3 with Dissolve(3.0):
        pos (284, 693)
        anchor (0,0)
    pause 3.0
    hide end_text1
    hide end_text2
    hide end_text3
    with Dissolve(1.0)

    show text "{font=fonts/Elsie-Regular.ttf}{color=#f686b8}{size=60}Thank you for playing{/size}{/color}{/font}" with Dissolve(3.0):
        pos (595, 387)
        anchor (0,0)
    pause 3.0
    hide text with Dissolve(3.0)
    pause 1.0
    show text "{font=fonts/Elsie-Regular.ttf}{color=#f686b8}{size=60}Next update will be out...{/size}{/color}{/font}" with Dissolve(3.0):
        pos (567, 488)
        anchor (0,0)
    pause 3.0
    hide text with Dissolve(3.0)
    pause 1.0
    show text "{font=fonts/Elsie-Regular.ttf}{color=#f686b8}{size=60}When it's ready{/size}{/color}{/font}" with Dissolve(3.0):
        pos (723, 85)
        anchor (0,0)
    show troll with Dissolve(1.0):
        pos (820, 179)
        anchor (0,0)
    pause 3.0
    hide troll with Dissolve(5.0)
    hide text with Dissolve(1.0)

    stop music fadeout 5.0
    pause 5.0
    
    $ renpy.music.set_volume(1.0, 0, channel="music")
    jump bonus_christmas
