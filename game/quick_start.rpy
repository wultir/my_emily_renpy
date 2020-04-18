label quick_start:
    stop music fadeout 3.0

    scene bg music with Dissolve(1.0)
    call wait_for_click(False)

    $ renpy.music.set_volume(0.3, 0, channel="music")
    play music "audio/bgm/the_burpy_burp_song.ogg" fadein 1.0

    show pussy at left with Dissolve(1.0)

    show bg christmas with Dissolve(0.01)

    god "This is a Quick Start... Duhhh.. Meant for those who have already played previous versions. Minimal bs where you can choose some of the biggest choices. (Not all). Just to get you going for the new content"
    god "Lets start with your name: (Dick is nice if you lack imagination)"

label quick_start_name:
    python:
        mc_name = renpy.input("Please enter your name:")
        mc_name = mc_name.strip()

    if not mc_name:
        "name please!"
        jump quick_start_name

    "Your name is set to: [mc_name] Small"


    # Dildo choice
    show text "{color=#ffffff}{size=36}Day 1 Thursday{/size}{/color}" at topright with Dissolve(1.0):
        offset (-10, 10)

    show bg 00_26 with Dissolve(1.0)

    "Which dildo did you choose?"

    menu:
        "Black [black]":
            $ inventory_dildo = "black"
            $ em_kinks_black += 1
        "White":
            $ inventory_dildo = "white"


    # Video choice
    show bg 00_35 with Dissolve(1.0)

    "What type of porn did you watch with Emily?"
    "(Black on white made Emily fascinated by the color pink)"

    menu:
        "Black bull fucks my blonde wife [black]":
            $ mem_emily_pink = True
            $ em_kinks_black += 1
            show bg 00_38A with Dissolve(1.0)
        "19 year white guy fucks my mature wife":
            show bg 00_38B with Dissolve(1.0)


    # Day 2
    hide text with Dissolve(1.0)
    show text "{color=#ffffff}{size=36}Day 2 Friday{/size}{/color}" at topright with Dissolve(1.0):
        offset (-10, 10)

    if mem_emily_pink:
        # Emily's reaction to James
        show bg 0133 with Dissolve(1.0)

        "While wearing pink at work James complimented and made Emily feel good and blush. Did she thank him or ignore him?"
        "(Thanking James could lead to something)"

        menu:
            "Emily thanked James [pink]":
                $ em_loves_james += 1
            "Emily ignored James":
                pass


    # MC's reaction to Eleanor
    show bg 0137 with Dissolve(1.0)

    "Did you tell Elanor her breasts are sexy when she wanted your honest opinion?"
    "(If you did you also found and read the note hidden in her handbag)"

    menu:
        "Yes! Sexy gilf! [pink]":
            $ ele_loves_mc = "love"
            $ mem_eleanor_secret_player = True
        "Noooo I'm not interested in her":
            pass
    

    # MC's reaction to Jack wanting to pursue Elise
    show bg 0120 with Dissolve(1.0)

    "Did you tell Jack it's ok to go after Elise if he feels like it?"

    menu:
        "Yes":
            $ j_loves_elise = 1
        "No [black]":
            pass

    # Day 3
    hide text with Dissolve(1.0)
    show text "{color=#ffffff}{size=36}Day 3 Saturday{/size}{/color}" at topright with Dissolve(1.0):
        offset (-10, 10)

    show bg 0314 with Dissolve(1.0)

    # MC's reaction to Jack perving on Emily
    "Emily accidentally gave you and Jack a sexy dance not knowing he was there. When she realised what she had done she felt embarrassed and ugly. Jack comforted her"
    "Jack apologized to you for telling Emily she's beautiful and sexy. How did you react?"
    "(Telling him it's ok results in Jack's feelings growing for her)"

    menu:
        "You told Jack he did nothing wrong [pink]":
            $ j_loves_emily = 1
        "You didn't like it [red]":
            pass


    # MC's interest in Marcus the black bull
    show bg bullask with Dissolve(1.0)

    "When looking at your profile on taboo palace Black Prince contacted you. Are you interested in him?"

    menu:
        "Yes I am [pink]":
            $ bull_marcus = True
        "No I'm not [red]":
            pass


    # Day 5
    hide text with Dissolve(1.0)
    show text "{color=#ffffff}{size=36}Day 5 Monday{/size}{/color}" at topright with Dissolve(1.0):
        offset (-10, 10)

    show bg 0568 with Dissolve(1.0)

    # Butt play in park
    "When you were in the park with Emily and met the old man did you let Emily play with your butt and did the old man notice this?"

    menu:
        "Yes he did [pink]":
            $ henry_mem_saw_buttplay = True
            show bg 0568b with Dissolve(1.0)
            pause 1.0
        "No he didn't [red]":
            pass


    # Watching henry pee in the park
    show bg 0576 with Dissolve(1.0)

    "Did you and Emily look when the old man needed to pee and thought he was alone?"

    menu:
        "Yes... Yes we did [pink]":
            $ henry_mem_saw_penis = True
        "Eww.. Naaaa! [red]":
            pass


    # Emily smoking
    hide text with Dissolve(1.0)
    show text "{color=#ffffff}{size=36}Misc{/size}{/color}" at topright with Dissolve(1.0):
        offset (-10, 10)

    show bg black with Dissolve(1.0)

    "Does Emily like to smoke?"

    menu:
        "Emily smokes":
            $ em_kinks_smoking = 2
        "Emily doesn't like smoking":
            pass


    # Mommy roleplay
    "Did you and Emily get into some kinky mom/son roleplay?"

    menu:
        "Yes mom":
            $ em_kinks_incest_play = True
            "Wow... You kinky son of a bitch!"
        "No we did not!":
            $ em_kinks_incest_play = False


    # End of quick start
    window hide
    hide text with Dissolve(1.0)
    stop music fadeout 1.0

    jump day6_start
