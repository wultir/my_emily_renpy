# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Message from god (intro narration)
define mg = Character("Message from god")

# Main character
define mc_cuckpoints = 0
define mc_kinks_black = 0
define mc_kinks_give_anal = 0
define mc_kinks_sph = 0
define mc_name = "?"
define mc = Character("[mc_name]")
define mc_thoughts = Character("[mc_name]", what_italic = True)

# Emily
define em_kinks_exhibit = 0
define em_kinks_black = 0
define em_kinks_rec_anal = 0
define em_kinks_sph = 0
define em_kinks_smoking = 0
define em = Character("Emily")
define em_thoughts = Character("Emily", what_italic = True)

# James (Emily's boss)
define jm = Character("James")

# Goddess Victoria (taboo site domina)
define gv = Character("Goddess Victoria")

# Sex shop girl
define xg = Character("Girl")

# Coffee shop waitress
define cw = Character("Waitress")

# Movie characters
define mw = Character("Wife")
define mh = Character("Husband")
define mb = Character("Black bull")
define mwb = Character("White bull")

define mem_chloe_name = ""
define mem_emily_color = ""
define mem_short_emily = 0

define inventory_dildo = ""

# Choice colors
define pink_choice = "#F790C0"
define red_choice = "#C4161C"

# The game starts here.

label start:
    stop music

    jump intro
