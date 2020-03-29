# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Message from god (intro narration)
define mg = Character("Message from god")
# God (game over narration)
define god = Character("God")

# Main character
default mc_cuckpoints = 0
default mc_kinks_black = 0
default mc_kinks_give_anal = 0
default mc_kinks_sph = 0
default mc_kinks_pee = 0
default mc_kinks_penis = 0
default mc_kinks_exhibit = 0
default mc_kinks_cum = 0
default mc_kinks_sissy = 0
default mc_kinks_butt_play = 0
default mc_name = "?"
define mc = Character("[mc_name]")
define mc_thoughts = Character("[mc_name]", what_italic = True)

# Emily
default em_kinks_exhibit = 0
default em_kinks_black = 0
default em_kinks_rec_anal = 0
default em_kinks_sph = 0
default em_kinks_smoking = 0
default em_kinks_cheating = 0
default em_kinks_cheat_jack = 0
default em_loves_james = 0
default em_loves_jack = 0
default em_kinks_sub = 0
default em_kinks_incest_play = 0
define em = Character("Emily")
define em_thoughts = Character("Emily", what_italic = True)

# Elise (Emily's sister)
define el = Character("Elise")

# Eleanor (Emily's mother)
default ele_loves_mc = ""
define ele = Character("Eleanor")

# Gabriela (Emily's best friend)
define g = Character("Gabriela")

# James (Emily's boss)
define jm = Character("James")

# Jack (MC's best friend)
default j_loves_elise = 0
default j_loves_emily = 0
default j_mem_em_car = False
define j = Character("Jack")
define jtease = Character("Jack in a girly teasing voice")

# Goddess Victoria (taboo site domina)
define gv = Character("Goddess Victoria")

# Sex shop girl
define xg = Character("Girl")

# Coffee shop waitress
define cw = Character("Waitress")

# 611 checkout girl
define cg = Character("Checkout girl")

# Walter Walker (school principal)
define sp = Character("Principal")
define ww = Character("Master Walker")

# School students
define mi = Character("Mimi")
define ash = Character("Ash")
define da = Character("Darell")
define ch = Character("Chloe")
define ty = Character("Tyler")

# Black Prince (Taboo Palace black bull)
default bull_marcus = False
define bp = Character("Black Prince")

# Victoria's Sin salesgirl
define sg = Character("Salesgirl")

# Old man in park (Henry)
default henry_mem_saw_buttplay = False
default henry_mem_saw_penis = False
define om = Character("Old man")

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

default mem_chloe_name = ""
default mem_emily_color = ""
default mem_short_emily = 0
default mem_short_player = ""
default mem_short_massage = False
default mem_eleanor_secret_player = False

default inventory_dildo = ""
default some_test = 10

# Choice colors
define pink_choice = "#F790C0"
define red_choice = "#C4161C"
define green_choice = "#64991E"
define white_choice = "#FFFFFF"

# The game starts here.

label start:
    stop music

    jump intro
