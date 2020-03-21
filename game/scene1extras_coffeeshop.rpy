label day1_coffee_shop:
    show bg coffee_01_day with dissolve

    "You go and find a table then join Emily who's about to place your order"

    em "So we would like to order two Money milker specials. With fries"

    cw "Good choice! Those are a total hit! "
    cw "You just can't get rid of them."
    cw "Sadly..."
    cw "That will be 40$! Just take a seat and wait.. You might not get anything..."
    cw "Hahahaha"

    "Emily looks at you with a shocked look on her face"

    em "Okkkey we. will. just. sit. there"


label scene00_29:
    scene bg 00_29 with dissolve

    show waiting at topleft
    pause


label day1_coffe_shop_waiting:
    scene bg coffee_01_day with dissolve

    window show
    show emily 01_07 at right with dissolve:
        yalign 0.5
        yoffset -100

    em "That waitress was odd!"
    em "I just hope those burgers are good. 40$ Dang it. It's way too much for us right now"
    em "James recommended the burgers here. Said it was like licking an angel haha"

    show emily 01_08 at right with dissolve:
        yalign 0.5
        yoffset -100

    pause 0.5

    em "Look.. I really didn't want to tell you about this..."
    em "But we are in a bit of trouble. Money wise"
    em "Alot actually.."

    "You just look at her. You had no idea about your financial situation. You are bad with numbers so you never really understood and never showed interest in it. Because Emily is like a wizard with numbers"

    em "Our apartment loan is killing us right now. And has been for a while.  We should have about 450$ extra each month. We are at minus 400$... Each month..."
    em "We are minus 10.000$ on top of our loan. Our loan should get smaller each month. Not bigger"
    em "We have to start thinking about selling soon babe"

    mc "I'm sorry. I had no idea!"

    em "I know. I didn't want to worry you"
    em "You really have to find work soon. I'm already working for James and teaching classes part time. I enjoy it, but it's so stressy!"

    menu:
        "{color=[pink_choice]}I'll find something, don't worry!{/color}":
            jump day1_coffe_shop_getwork
        "{color=[red_choice]}We could sell your butt!  ;){/color}":
            jump day1_coffe_shop_sellyou


label day1_coffe_shop_getwork:
    $ mc_cuckpoints += 1

    show emily 01_09A at right with dissolve:
            yalign 0.5
            yoffset -100

    em "Good. Thank you!"
    em "I know it's hard to find something. But we really need it. Anything!"

    jump day1_coffe_shop_kiss


label day1_coffe_shop_sellyou:
    $ mc_cuckpoints -= 1

    show emily 01_09B at right with dissolve:
            yalign 0.5
            yoffset -100

    em "That's NOT funny!"
    em "Deep breaths Em, deep breaths"
    em "I'm not going to get angry now. But you have to find work somewhere"

    mc "Sorry baby. It was just a bad joke.."

    em "Good! Let's just wait for the burgers"

    jump day1_coffe_shop_burgers


label day1_coffe_shop_kiss:
    show emily 01_10 at right with dissolve:
        yalign 0.5
        yoffset -100

    em "Anyways. Let's just forget about anything important tonight and just enjoy our evening together!"
    em "Come here. I want a kiss!"

    show emily 01_11 at right with dissolve:
        yalign 0.5
        yoffset -100

    "Emily stands up and bends over the table to reach you"

    show emily 01_12A at right with dissolve:
        yalign 0.5
        yoffset -100

    mc_thoughts "That guy is really checking her out. He must have a great view of those red panties.."
    mc_thoughts "He's a real creep. But it's a bit exciting at the same time"
    mc_thoughts "Should i kiss her longer? That way he would get a better look.."

    menu:
        "{color=[pink_choice]}Longer Kiss{/color}":
            jump day1_coffe_shop_longer_kiss
        "{color=[red_choice]}Stop{/color}":
            mc_thoughts "No. I don't want that creep to see anything more!"
            jump day1_coffe_shop_burgers


label day1_coffe_shop_longer_kiss:
    show emily 01_12B at right with dissolve:
        yalign 0.5
        yoffset -100

    "Emily's a bit taken back first. But she gives in and enjoys your long kiss"

    mc_thoughts "Oh this is exciting. I wonder how much he can see?"
    mc_thoughts "I wonder how big dick he has? How would i feel if he was fucking her right now. And while I'm kissing Em..."
    mc_thoughts "Time to stop. I don't want to start anything stupid right now"


label day1_coffe_shop_burgers:
    "Your hamburgers arrive"

    show emily 01_13 at right with dissolve:
        yalign 0.5
        yoffset -100

    em "They look so yummy!"
    em "Ohhh myyy gaaawd"
    em "It's the best meat ever that's entered my mouth!"
    em "The sauce is sooo yummy and complements the burger so perfectly"

    "You pretend to enjoy it. You love burgers. But this is the worst thing ever. It tastes moldy"
    "Like an old moldy roadkill frog covered in maggots that's been though a couple of old unclean rectums"
    "You wish you could nuke wherever this crap was invented. And every place containing it!"
    "And people keep paying for it?"

    show emily 01_07 at right with dissolve:
        yalign 0.5
        yoffset -100

    em "That was great! We have to come here again!"

    mc "I yeNoaiJayeah"

    em "Are you ok?"
    em "Oh it's already dark!"
    em "Let's start to go home. I believe i promised something else for you tonight"

    "Emily winks"
    "You both leave"

    hide emily with dissolve
    pause 0.5

    jump day1_coffee_shop_exit
