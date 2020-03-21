# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Message from god (intro narration)
define mg = Character("Message from god")
# God (game over narration)
define god = Character("God")

# Main character
define mc_cuckpoints = 0
define mc_kinks_black = 0
define mc_kinks_give_anal = 0
define mc_kinks_sph = 0
define mc_kinks_pee = 0
define mc_kinks_penis = 0
define mc_kinks_exhibit = 0
define mc_kinks_cum = 0
define mc_name = "?"
define mc = Character("[mc_name]")
define mc_thoughts = Character("[mc_name]", what_italic = True)

# Emily
define em_kinks_exhibit = 0
define em_kinks_black = 0
define em_kinks_rec_anal = 0
define em_kinks_sph = 0
define em_kinks_smoking = 0
define em_kinks_cheating = 0
define em_kinks_cheat_jack = 0
define em_loves_james = 0
define em_loves_jack = 0
define em = Character("Emily")
define em_thoughts = Character("Emily", what_italic = True)

# Elise (Emily's sister)
define el = Character("Elise")

# Eleanor (Emily's mother)
define ele_loves_mc = ""
define ele = Character("Eleanor")

# Gabriela (Emily's best friend)
define g = Character("Gabriela")

# James (Emily's boss)
define jm = Character("James")

# Jack (MC's best friend)
define j_loves_elise = 0
define j_loves_emily = 0
define j_mem_em_car = False
define j = Character("Jack")

# Goddess Victoria (taboo site domina)
define gv = Character("Goddess Victoria")

# Sex shop girl
define xg = Character("Girl")

# Coffee shop waitress
define cw = Character("Waitress")

# 611 checkout girl
define cg = Character("Checkout girl")

# Black Prince (Taboo Palace black bull)
define bp = Character("Black Prince")
define bull_marcus = False

# Movie characters
define mw = Character("Wife")
define mh = Character("Husband")
define mb = Character("Black bull")
define mwb = Character("White bull")
define ms = Character("Shemale")
define mss = Character("Slut")

# End 1 characters
define dr = Character("Dr")
define a = Character("Amanda")

define mem_chloe_name = ""
define mem_emily_color = ""
define mem_short_emily = 0
define mem_short_player = ""
define mem_eleanor_secret_player = False

define inventory_dildo = ""

# Choice colors
define pink_choice = "#F790C0"
define red_choice = "#C4161C"
define green_choice = "#64991E"

# The game starts here.

label start:
    stop music

    jump intro
