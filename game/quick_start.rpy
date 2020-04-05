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


label quick_start_dildo:
    show text "{color=#ffffff}{size=36}Day 1 Thursday{/size}{/color}" at topright with Dissolve(1.0):
        offset (-10, 10)

    show bg 00_26 with Dissolve(1.0)

    "Which dildo did you choose?"

    menu:
        "{color=[black_choice]}Black{/color}":
            $ inventory_dildo = "black"
            $ em_kinks_black += 1
        "{color=[white_choice]}White{/color}":
            $ inventory_dildo = "white"


label quick_start_video:
    show bg 00_35 with Dissolve(1.0)

    "What type of porn did you watch with Emily?"
    "(Black on white made Emily fascinated by the color pink)"

    menu:
        "{color=[black_choice]}Black bull fucks my blonde wife{/color}":
            $ mem_emily_pink = True
            $ em_kinks_black += 1
            show bg 00_38A with Dissolve(1.0)
        "{color=[white_choice]}19 year white guy fucks my mature wife{/color}":
            show bg 00_38B with Dissolve(1.0)


label quick_start_day2:
    hide text with Dissolve(1.0)
    show text "{color=#ffffff}{size=36}Day 2 Friday{/size}{/color}" at topright with Dissolve(1.0):
        offset (-10, 10)

    if mem_emily_pink:
        jump quick_start_pink_work
    else:
        jump quick_start_work_done

label quick_start_pink_work:
    show bg 0133 with Dissolve(1.0)

    "While wearing pink at work James complimented and made Emily feel good and blush. Did she thank him or ignore him?"
    "(Thanking James could lead to something)"

    menu:
        "{color=[pink_choice]}Emily thanked James{/color}":
            $ em_loves_james += 1
            jump quick_start_work_done
        "{color=[white_choice]}Emily ignored James{/color}":
            jump quick_start_work_done


label quick_start_work_done:
    show bg 0137 with Dissolve(1.0)

    "Did you tell Elanor her breasts are sexy when she wanted your honest opinion?"
    "(If you did you also found and read the note hidden in her handbag)"

    menu:
        "{color=[pink_choice]}Yes! Sexy gilf!{/color}":
            $ ele_loves_mc = "love"
            $ mem_eleanor_secret_player = True
            jump quick_start_jack_elise
        "{color=[white_choice]}Noooo I'm not interested in her{/color}":
            jump quick_start_jack_elise
    

label quick_start_jack_elise:
    show bg 0120 with Dissolve(1.0)

    "Did you tell Jack it's ok to go after Elise if he feels like it?"

    menu:
        "{color=[white_choice]}Yes{/color}":
            $ j_loves_elise = 1
            jump quick_start_day3
        "{color=[black_choice]}No{/color}":
            jump quick_start_day3


label quick_start_day3:
    hide text with Dissolve(1.0)
    show text "{color=#ffffff}{size=36}Day 3 Saturday{/size}{/color}" at topright with Dissolve(1.0):
        offset (-10, 10)

    show bg 0314 with Dissolve(1.0)

    "Emily accidentally gave you and Jack a sexy dance not knowing he was there. When she realised what she had done she felt embarrassed and ugly. Jack comforted her"
    "Jack apologized to you for telling Emily she's beautiful and sexy. How did you react?"
    "(Telling him it's ok results in Jack's feelings growing for her)"

    menu:
        "{color=[pink_choice]}You told Jack he did nothing wrong{/color}":
            $ j_loves_emily = 1
            jump quick_start_bull
        "{color=[red_choice]}You didn't like it{/color}":
            jump quick_start_bull


label quick_start_bull:
    show bg bullask with Dissolve(1.0)

    "When looking at your profile on taboo palace Black Prince contacted you. Are you interested in him?"

    menu:
        "{color=[pink_choice]}Yes I am{/color}":
            $ bull_marcus = True
            jump quick_start_day5
        "{color=[red_choice]}No I'm not{/color}":
            $ bull_marcus = False
            jump quick_start_day5


label quick_start_day5:
    hide text with Dissolve(1.0)
    show text "{color=#ffffff}{size=36}Day 5 Monday{/size}{/color}" at topright with Dissolve(1.0):
        offset (-10, 10)

    show bg 0568 with Dissolve(1.0)

    "When you were in the park with Emily and met the old man did you let Emily play with your butt and did the old man notice this?"

    menu:
        "{color=[pink_choice]}Yes he did{/color}":
            $ henry_mem_saw_buttplay = True
            show bg 0568b with Dissolve(1.0)
            pause 1.0
            jump quick_start_look_old_man_peeing
        "{color=[red_choice]}No he didn't{/color}":
            $ henry_mem_saw_buttplay = False
            jump quick_start_look_old_man_peeing


label quick_start_look_old_man_peeing:
    show bg 0576 with Dissolve(1.0)

    "Did you and Emily look when the old man needed to pee and thought he was alone?"

    menu:
        "{color=[pink_choice]}Yes... Yes we did{/color}":
            $ henry_mem_saw_penis = True
            jump quick_start_misc
        "{color=[red_choice]}Eww.. Naaaa!{/color}":
            $ henry_mem_saw_penis = False
            jump quick_start_misc


label quick_start_misc:
    hide text with Dissolve(1.0)
    show text "{color=#ffffff}{size=36}Misc{/size}{/color}" at topright with Dissolve(1.0):
        offset (-10, 10)

    show bg black with Dissolve(1.0)

    "Does Emily like to smoke?"

    menu:
        "{color=[white_choice]}Emily smokes{/color}":
            $ em_kinks_smoking = 2
            jump quick_start_mommy
        "{color=[white_choice]}Emily doesn't like smoking{/color}":
            jump quick_start_mommy


label quick_start_mommy:
    "Did you and Emily get into some kinky mom/son roleplay?"

    menu:
        "{color=[white_choice]}Yes mom{/color}":
            $ em_kinks_incest_play = True
            "Wow... You kinky son of a bitch!"
            jump quick_start_done
        "{color=[white_choice]}No we did not!{/color}":
            $ em_kinks_incest_play = False
            jump quick_start_done

label quick_start_done:
    window hide
    hide text with Dissolve(1.0)
    stop music fadeout 1.0

    jump day6_start
