label weekend1_sunday_game_over:
    # weekend1xExtras; line 1218
    pause 0.5
    show text "{font=fonts/Elsie-Regular.ttf}{size=35}{color=#f686b8}Your points:{/color}{/size}{/font}" as points_text with Dissolve(1.0):
        pos (526, 360)
        anchor (0, 0)
    pause 1.0
    show text "{font=fonts/Elsie-Regular.ttf}{color=#f686b8}{size=90}[mc_cuckpoints]{/size}{/color}{/font}" as points with Dissolve(1.0):
        pos (724, 316)
        anchor (0, 0)

    pause 1.0
    
    god "You needed 15 or more to continue..."
    god "This is just a game.. What if any of this had happened in your real life?"
    god "You would probably hang yourself..."
    god "Life is way too short and fragile!"
    god "Don't try cuckolding or femdom in reality"
    god "Let it be a fantasy..."

    hide points_text
    hide points
    with Dissolve(3.0)

    show emily couple with Dissolve(1.0):
        pos (421, -1)

    god "True love is hard to find..Don't ruin your relationship"
    god "Or yourself"

    hide emily with Dissolve(1.0)

    jump the_end1
