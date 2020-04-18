label day5_goodnight:
    scene bg 0596 with Dissolve(1.0)

    em "Yaaaawns*"
    em "I'm so tired babe"
    em "What a crazy day today was.."

    mc "Yeah.."

    em "Hey"
    em "Why are you looking at me like that?"

    menu:
        "Because you are so sexy and you made me so horny today [pink]":
            jump day5_you_are_so_sexy
        "I'm just tired End day [red]":
            # Port note: Changed to end of day instead of end of game version.
            jump day6_start


label day5_you_are_so_sexy:
    scene bg 0597 with Dissolve(1.0)
    call wait_for_click

    "Emily starts to dance sexy and sensually"
    "You didn't get to cum today so you become rock hard at once"
    "She starts to talk in a really sexy voice"

    em "Yeah?"
    em "What part made you so horny?"
    em "Is it my breasts maybe?"
    em "Or..."

    scene bg 0598 with Dissolve(1.0)
    call wait_for_click

    em "Is it my big butt?"

    if em_kinks_rec_anal == 1:
        jump day5_anal
    else:
        jump day5_continue_anal


label day5_anal:
    em "Or maybe it's my virgin butt that you can't have?"
    em "Mmm"
    em "Imagine how tight it must be.."
    em "Do you want to lick it again?"
    em "To press your cute little tongue deep inside my anal"
    em "To swallow and taste it..."
    em "Pressing your nose inside and smelling all of me..."
    em "You want that babe?"

    #
    if em_kinks_black == 1:
        jump day5_black_love
    else:
        jump day5_continue_anal


label day5_black_love:
    em "You know black men love big white booty..."
    em "Is that it?"
    em "Ohhh you are so naughty.."
    em "Mmm a tall big muscular black man fucking your girlfriends tight little virgin ass"
    em "Would you hold my hands and kiss me while I'm crying and trying to get used to a big black cock deep inside my ass?"
    em "Naughty naughty little boy"
    em "You love me enough to lick me clean after they have fucked and cummed inside my holes.."
    em "Right?"


label day5_continue_anal:
    scene bg 0599 with Dissolve(1.0)

    em "Or is it something else?"
    em "Hmmmm..."
    em "What could it be?"
    em "Do you maybe want to finally taste my pussy?"
    em "Are you man enough for that?"
    em "..."
    em "Or do you want mommy to teach you?"

    menu:
        "Yes mommy please teach me! [pink]":
            jump day5_yes_mommy
        "Stay silent [red]":
            jump day5_stay_silent


label day5_stay_silent:
    scene bg 05100 with Dissolve(1.0)

    em "Not in the mood to talk huh?"
    em "So what do we have here?"

    "Emily removes your undies "

    scene bg 05101 with Dissolve(1.0)

    em "What should I do with this..."
    em "Thing?"

    jump day5_stay_silent_done


label day5_yes_mommy:
    $ em_kinks_incest_play = True

    em "Ahhhh "
    em "Ohh yesss"
    em "My little baby!"
    em "Let mommy help you"

    scene bg 05100 with Dissolve(1.0)

    em "Oh my!"
    em "What do we have here?"
    em "You naughty little boy!"
    em "Mommy needs to remove your cute red panties"

    em "Emily removes your undies "

    scene bg 05101 with Dissolve(1.0)

    if em_kinks_sph == 1:
        jump day5_emily_sph
    else:
        jump day5_no_sph


label day5_emily_sph:
    em "Oh.."
    em "Is this is?"
    em "Hahahaha"
    em "My poor little baby!"
    em "You can't please any woman with this tiny little disgusting dick..."
    em "It looks like a big clit!"
    em "Hahaha"

    "Those words makes your little dick twitch"

    mc "Ohh god"

    em "A clit piercing would look nice on it.."
    em "It's worthless.. I should just put it in permanent chastity"
    em "A tiny little cage..."
    em "At least I wouldn't need to be ashamed every time I see it after that.."
    em "That tiny cage would never come off baby.."
    em "You would never be able to get hard again.. This tiny disgusting little thing would try.."
    em "But it would only hurt you and after a few years you would slowly start to become impotent.."
    em "Yes.."
    em "No more tiny dicks.."
    em "So what should I do with it?"
    em "Bite it?"


label day5_no_sph:
    em "What should I do with this..."
    em "Thing?"


label day5_stay_silent_done:
    menu:
        "Please suck my tiny worthless cock [pink]":
            jump day5_suck_sph
        "Can you please suck it [red]":
            jump day5_suck_no_sph


label day5_suck_sph:
    scene bg 05102 with Dissolve(1.0)
    call wait_for_click

    if em_kinks_incest_play:
        jump day5_mommy_sph
    else:
        jump day5_not_mommy_sph


label day5_mommy_sph:
    em "...."
    em "Please? You forgot something..."

    mc "Please mom suck my tiny worthless little cock..."
    mc "I can't take much more!"
    mc "I'll cum soon mom"

    em "Good boy!"

    "Emily moans and licks your glans for a few seconds before stopping"

    em "Did you like that?"

    mc "Yes! Please mommy, do it more!"

    em "NO!"
    em "Don't you know how wrong this is??"
    em "That's ALL you will get!"
    em "What kind of boy asks his mother to give him a blowjob?"
    em "A really twisted one.."
    em "What do you think your father would say??"
    em "I will have to spank you later... Hard and long untill your disgusting little thing dies"
    em "God I'm so happy you didn't get your father's cock.... He's so much bigger than my little angel here"
    em "Maybe I'll let you watch next time he wants to fuck your mommy?"
    em "He likes to fuck me so hard honey.. He dosen't take a no for an answer.. He knows how wet I become eventually when he rips my clothes away and pushes me down like a little slut.."
    em "Mommy is such a good whore!"

    mc "Ahhhhhh"

    em "I know!"
    em "I'll tell your father you are ready to be trained as a fuck toy!"
    em "We have waited for it for so long.. His friends will be happy too.. Your mommy starts to become really loose after all the years of fucking all those big hard cocks"
    em "Your little virgin ass pussy will come in handy for us all.."
    em "Mommy loves you!"

    jump day5_lick_done


label day5_not_mommy_sph:

    em "...."
    em "Why should I do that?"

    mc "Please baby do it.."
    mc "I can't take much more!"
    mc "I'll cum soon!"

    em "I guess I could lick it..."

    "Emily licks the glans for a few seconds then stops"

    em "Happy now?"

    mc "Please more, I'm begging you baby.. Please"

    em "Hmm.."
    em "Nah.."
    em "I don't like your taste"
    em "And"
    em "I need a bigger one babe"

    jump day5_lick_done


label day5_suck_no_sph:
    scene bg 05102 with Dissolve(1.0)
    call wait_for_click

    em "I guess I could lick it..."

    "Emily licks the glans for a few seconds then stops"

    em "Happy now?"

    mc "Please more, I'm begging you baby.. Please"

    em "Hmm.."
    em "Nah.."
    em "You don't make me happy enough!"
    em "And"
    em "I need a bigger one babe"


label day5_lick_done:
    scene bg 05103 with Dissolve(1.0)

    em "Now I'm happy and this is all you'll get"
    em "You are so cute when this frustrated.. But It's ok babe"
    em "This is exactly how it should be.."
    em "My tiny guy harder than stone and ready to burst any second"
    em "I like this feeling!"
    em "No.."
    em "I LOVE this feeling!"

    mc "Awww baby. I really need to cum, I can't do anything while this horny! "
    mc "Please.."

    em "It's ok babe.."

    if em_kinks_incest_play:
        jump day5_mommy_end


    scene bg 05104 with Dissolve(1.0)

    em "You will learn.."
    em "Now give me a kiss!"

    "Emily get's up and gives you a long wet kiss while rubbing your cock with her knee"

    mc "Ahhhh baby pleaseeee"

    em "Shhh!"
    em "Good night babe"

    scene bg 05105 with Dissolve(1.0)

    "You both lay down naked. Emily presses her body against yours and giggles"

    em "Don't you dare to cum without permission!"
    em "Understood?"

    mc "Yyyes baby"

    em "Good boy!"
    em "Goodnight"
    em "Love you!"

    mc "Goodnight"
    mc "I love you more!"

    "Sleeping dosen't come easy with your rock hard trembling cock rubbing against her pussy and ass"
    "But eventually you manage to fall asleep..."

    jump day6_start


label day5_mommy_end:
    scene bg 05104 with Dissolve(1.0)

    em "You will learn.."
    em "Now give mommy a real goodnight kiss!"

    mc "Kiss*"

    em "..."
    em "Sigh'"
    em "It seems I have to teach you how to kiss too..."

    "Emily get's up and gives you a long sloppy wet kiss with lots of moaning while rubbing your cock with her knee"

    mc "Mmphumph"
    mc "Ahhhh mommy pleaseeee"
    mc "Just a little bit more!"
    mc "I'mm Iimm cumming"

    "Emily stops at once and grabs your cock and testicles with one hand and squeezes hard. Not enough to make you scream in pain, but enough for you to not cum. Then she looks at you"

    em "You... will... not... cum!"
    em "You were a good boy tonight.. But not good enough.."
    em "You have to earn your orgasms from now on"

    mc "But.."

    em "Shhh!"
    em "Time to snuggle my little angel"

    "She lays down beside you and drags you in close to her "

    scene bg 05105 with Dissolve(1.0)

    "You cling tightly against her and she presses her ass and pussy against you hard"

    em "Yeees my little angel"
    em "Mommy loves this position!"
    em "Do you too?"

    "You are so horny and frustrated that you are on verge of tears. You answer with a trembling voice"

    mc "Yy yes Mommy"

    em "Aww you can cry baby.. I love your little angel tears.. Let it all out my baby"
    em "But baby.."
    em "Don't you dare to put that thing inside me or cum without permission!"
    em "Understood?"

    mc "Yyyes"

    em "Good boy!"
    em "Goodnight"
    em "Mommy loves you!"

    mc "Goodnight"
    mc "I love you more mom!"

    "Sleeping dosen't come easy with your rock hard trembling cock rubbing against her pussy and ass"
    "But eventually you manage to fall asleep..."

    jump day6_start

