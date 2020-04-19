label wait_for_click(img=True):
    $ quick_menu = False
    window auto hide
    if img:
        show waiting at topleft with Dissolve(1.0)
    pause
    hide waiting with Dissolve(1.0)

    $ quick_menu = True
    return
