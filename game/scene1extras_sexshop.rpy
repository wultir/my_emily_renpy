label day1_sex_shop:
    scene bg xxx_store_01_day with Dissolve(1.0)

    mc_thoughts "I've never been to a place like this! It feels dirty and i'm nervous."
    mc_thoughts "Let's just focus and calm down!"
    mc_thoughts "Hm is it empty? No one is here?"
    mc_thoughts "What's that sound? Moaning?"

    scene bg 00_25 with Dissolve(1.0)

    "?" "Hey there and welcome! I was.. getting a massage. Back problems!"
    "?" "So what can i get you?"

    mc "Hi. I need a dildo.."
    mc "I want a dildo i mean."
    mc "I want to buy one.."

    "?" "Riight. We have a huge collection of dildos! I'll just call my dildo expert."
    "?" "She knows evertyhing about them. Hold on."
    "?" "PRIIINCESSS! COME HERE!"

    with hpunch


label day1_sex_shop_girl:
    scene bg xxx_store_01_day with Dissolve(1.0)

    show xxx_girl 01_01 at center with Dissolve(1.0):
        yanchor 0.75
        zoom 1.29
        linear 5.0 yanchor 1.1
        pause 0.5
        linear 3.0 yanchor 0.75
    pause 8.0
    show xxx_girl at center:
        yanchor 0.75
        zoom 1.29

    xg "Hiya!"
    xg "What is it daddy?"

    "Guy" "Help this guy choosing a dido, you know these things! Be a good little princess and come back massaging me when you are done.."

    xg "Yeah! I'm the expert hihi I'll be back soon"
    xg "Follow me! It's just over here"

    window hide

    show xxx_girl 01_02 at center with Dissolve(1.0):
        yanchor 0.75
        zoom 1.29
        pause 0.5
        parallel:
            linear 4.0 yanchor 0.62
        parallel:
            linear 4.0 zoom 3.85
        parallel:
            linear 4.0 xoffset -60
        pause 0.5
        parallel:
            linear 3.0 zoom 1.29
        parallel:
            linear 3.0 yanchor 0.75
        parallel:
            linear 3.0 xoffset 0
    pause 9.0
    show xxx_girl 01_02 at center:
        yanchor 0.75
        zoom 1.29
    pause 0.5
    hide xxx_girl 01_02 with Dissolve(1.0)
    pause 0.5

    scene bg 00_26 with Dissolve(1.0)

    xg "So what kind are you looking for? We have everything!! Monster, huge bbc, fantasy, dog, tentacles, horse, fist, plugs, vibrators.. We have every type of dildo you could ever need!"

    mc "Oh ehh. Just something that's little bigger than me. That would be great!"

    xg "Oki, we can fix that! But how big is your cock?"

    menu:
        "Oh ah. 10cm.. M m m maybe.. [pink]":
            $ mem_chloe_name = "Tiny"
            xg "Really? OMG! hihi."
            xg "That's sooo tiny!"
            xg "But I bet It must be cute.. Hihihi"
        "Little smaller than average":
            xg "Oki...."
            xg "Let's pick one of our smallest!"

    scene bg 00_27 with Dissolve(1.0)

    show waiting at topleft
    pause
    hide waiting
    
    xg "Found it!"

    scene bg 00_28 with Dissolve(1.0)

    xg "This is one of the smallest we have! Smaller ones just don't sell."
    xg "It's about 15cm usable size."
    xg "It means from balls up!"

    with hpunch

    xg "OH wait!!!"

    show bg 00_27 with Dissolve(1.0)

    xg "I have something much better!"


    scene bg 00_28A with Dissolve(1.0)

    xg "This one!"
    xg "It's little longer at 22cm but usable lenght is 18cm,"
    xg "It's only 10$ more, but it's made from much more realistic materials!"

    menu:
        "Do you have it in different colors? [pink]":
            show bg 00_27
            with Dissolve(1.0)

            xg "Of course we do!"

            jump day1_sex_shop_black
        "Thank you! I'm fine with this [green]":
            $ inventory_dildo = "white"
            jump day1_sex_shop_done 


label day1_sex_shop_black:
    scene bg 00_28B with Dissolve(1.0)

    xg "Black. Our top selling color!"
    xg "Which color would you want?"

    menu:
        "Black [black]":
            jump day1_sex_shop_black_dildo
        "White":
            jump day1_sex_shop_white_dildo


label day1_sex_shop_black_dildo:
    $ inventory_dildo = "black"
    $ mc_kinks_black += 1
    $ mc_cuckpoints += 1
    xg "Best choice. I prefer black too!"
    xg "It's just... better.."
    xg "Do you want anything else?"

    mc "T t t this will be all for now.."

    jump day1_sex_shop_done


label day1_sex_shop_white_dildo:
    $ inventory_dildo = "white"

    xg "Oki! Have fun with it!"
    xg "Is this everything?"
    
    mc "Yes. Thank you!"

    jump day1_sex_shop_done


label day1_sex_shop_done:
    xg "Oki. That will be 35$!"
    xg "You will soon be back for bigger ones! Have fun, See you later and thank you!"
    xg "Huggies!"

    scene bg black with Dissolve(1.0)

    "You thank her and leave"
    "Back home 15 minutes later"

    scene bg black with Dissolve(1.0)

    jump day1_phone