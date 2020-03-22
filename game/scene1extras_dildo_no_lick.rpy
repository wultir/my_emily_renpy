label day1_dildo_no_lick:
    scene bg black with Dissolve(1.0)

    show waiting at topleft
    pause 1.0
    hide waiting

    if inventory_dildo == "black":
        show emily sex_10A at top with Dissolve(1.0)
    if inventory_dildo == "white":
        show emily sex_09A at top with Dissolve(1.0)

    "You press the tip of the dildo against her pussy and start rubbing it carefully in circles around her opening"

    em "More more"

    if inventory_dildo == "black":
        show emily sex_10B at top with Dissolve(1.0)
    if inventory_dildo == "white":
        show emily sex_09B at top with Dissolve(1.0)

    "You slowly start pressing the head in.  "
    "It goes in surprisingly easy inside her. But you dont want to hurt her so you just keep fucking her slowly and not deeper than the head "

    em "AHHH GOD "
    em "Keep going ah this feels amaaazing keeep keep going ohh don't stop "

    "You keep going on untill she starts to turn around "

    if inventory_dildo == "black":
        jump day1_black_dildo_turn_around
    if inventory_dildo == "white":
        jump day1_white_dildo_turn_around
