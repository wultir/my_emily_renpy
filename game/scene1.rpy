# Scene 1 (intro and first day)

label intro:
    scene bg black

    mg "You have to be 18+ or 72+ depending on what country you are from. If not, press X at upper right corner and forget about this"
    mg "This visual novel game is not porn. But it deals with a very strong and realistic kink which of course contains strong sexual content!"
    mg "Any character that has any type of inappropriate or any type of adult content is strictly minimum 18 years old"
    mg "This is a work of fiction. Names, characters, businesses, places, events, locales, and incidents are either the products of the author’s imagination or used in a fictitious manner. Any resemblance to actual persons, living or dead, real or not, or actual events is purely coincidental."
    mg "English it not my native language"
    mg "A dead tree has better writing abilites than me. So be warned!"
    mg "Critique and any kind of help is welcomed"
    mg "You can right click your mouse to hide/unhide the textbox at any time"
    mg "Pink choices often mean, submissive,yes,I want more, continue etc."
    mg "Red choices often mean, no,stop,hell no, abort,stop kink, etc"

    show bg music with Dissolve(1.0)

    mg "If you see this message then it means there will most likely be music or some type of sounds after clicking. If there isn't then I simply forgot to add it in :p"
    mg "It's to give you a heads up so you don't wake up your whole house with loud rock music in the middle of the night with your pants down..."
    mg "Perv.."
    mg "There won't be music playing now after you click anywhere..."
    mg "Have fun!"

    show bg 00_01 with Dissolve(1.0)

    show text "{color=#ffffff}{size=36}Day 1 Thursday{/size}{/color}" at topright with Dissolve(1.0):
        offset (-10, 10)

    mc "This is you..  24 years old and175cm tall and pretty slim. Shy and horrendously low self esteem. Your best and only friend is Jack. He's the reason you survived school. He's a big guy, the biggest you've ever seen. He's tough of the outside but inside he's a big softie."
    mc "He's a couple years older than you and you always saw him more like a brother or father"
    mc "He just got back home after being out protecting the country.... Or the low oil prices... For 2 long years"
    mc "You'll see him soon!"
    mc "You come from a lower middle class home with 1 parent. Your mother. 3 years ago Jack introduced you to a sexy girl online. He knew you were a virgin and he's always there to help you. Somehow despite you being silent and awkward she wanted to see you"
    mc "You finally built up the courage to go meet her after 1 year of online chatting. The only thing you remember from your first date is how nervous you were. You were stammering all night and spilling drinks.. Yes.. 2 drinks..."
    mc "She must have thought it was cute because here you are!"
    mc "Turns out her parents are wealthy and she owns a nice apartment in the city center. She asked you to move in 3 months ago"

    hide text with Dissolve(1.0)


label input_mc_name:
    $ quick_menu = False
    python:
        mc_name = renpy.input("Please enter your name:")
        mc_name = mc_name.strip()

    if not mc_name:
        "name please!"
        jump input_mc_name

    $ quick_menu = True
    "Your name is set to: [mc_name] Small"


label day1_start:
    show bg 00_02 with Dissolve(1.0)

    "..."

    scene bg 00_03 with Dissolve(1.0)
    call wait_for_click

    show bg 00_04 with Dissolve(1.0)
    "There she is!!"
    "This is Emily White. She's your girlfriend. Or fiancée since you proposed to her last week!"
    "She's a independent 29 year old girl with a strong will. But a strong soft heart!"
    "You have been together for  about 2 years, after chatting for about 1 year. You still have a hard time to understand why she likes you"
    "She works as a receptionist at a law firm and part time as a teacher"
    "She's a bit of a prude in bed"
    "You are horny 24/7 because your sex life is boring and bad. If you are good you might get a handjob every other week or so. You haven't had vaginal sex for about a year now. But you did get a few blowjobs when you moved in.You wanted to try anal with her once but you got slapped pretty hard that day"
    "So it's pretty much daily jerking for you. You dont think she knows"
    "It's frustrating! But you love her very much and she means everything for you!"

    show bg 00_05 with Dissolve(1.0)

    em "Aaaahhhh. I thought you were still sleeping! How long have you been up?"

    mc "Long enough to realize i love you!"

    em "Haha!"
    em "You wont get lucky now silly.. But nice try!"
    em "I need to get ready for work"

    show bg 00_06 with Dissolve(1.0)
    em "Kiss*"

    show bg 00_07 with Dissolve(1.0)
    "You have had some troubling thoughts for a while now.."
    "They just get harder and harder to control, and they become more and more extreme.."
    "You get rock hard while fantasizing about her fucking others while not giving you anything. Controlling you, humiliating you and worse.. The more extreme it is the harder you come"
    "You are watching cuckold or femdom porn daily. And in secret"
    "After the deed is done you feel very ashamed, dirty and jealous. You have no idea why you have these fantasies. You dont want them!"
    "You hate yourself for having them and you feel even more worthless as a man! You know you would get heartbroken if she would have sex with someone other than you"
    "A couple weeks ago you found a site called Taboo Palace. It seems to be the biggest and most serious pay site for singles and couples about all kinds of taboos. Mostly about femdom and cuckolding."
    "You have decided to finally open a account there hoping you will find some answers and learn something. Maybe you can learn how to control yourself and those fantasies you have?"


    scene bg 00_08 with Dissolve(1.0)
    call wait_for_click

    mc_thoughts "Oh no!"
    mc_thoughts "Can't focus..."
    mc_thoughts "Need to fuck..."
    mc_thoughts "NOW!"

    show bg 00_09 with Dissolve(1.0)
    mc "She certainly didn't choose me for my rock hard 10 centimeters. Or my non existent wealth!"
    mc "Pufff.. There goes my underwear. I swear I'm the fastest man on this planet to lose them"
    mc "I'm so happy she dosent look like the girls from all the other games i play where they claim to be my 45 year old mother who looks to be 4 years under 18 and a body drawn by a retarded monkey who just found the breast and butt size scale sliders. Ghhhh. Hate those games!"
    mc "But i wish i had the 27cm elephant formed dicks they ALWAYS have!"
    mc "Anyways.. What should i do with that lovely and sexy butt in front of me?"

    menu:
        "Press your dick against her butt":
            jump press_dick_against_butt
        "Press your face against her butt [pink]":
            $ mc_cuckpoints += 1
            jump press_face_against_butt


# Press your dick against her butt
label press_dick_against_butt:
    scene bg 00_10 with Dissolve(1.0)
    call wait_for_click

    jump press_against_butt_done


# Press your face against her butt
label press_face_against_butt:
    scene bg 00_10a with Dissolve(1.0)
    call wait_for_click


label press_against_butt_done:
    show bg house01_bedroom_day_pc with Dissolve(1.0)

    show emily 01_01 at left with Dissolve(1.0)

    em "Aiiieeee*"
    em "WHAT THE HELL ARE YOU DOING??"

    show emily 01_02 at left with Dissolve(1.0)

    em "You cant sneak up on me like that! What's wrong with you?"
    em "Just sit down... and wait while I'm getting dressed for work!"

    hide emily with Dissolve(1.0)

    show bg 00_11 with Dissolve(1.0)
    mc_thoughts "Crap!"
    mc_thoughts "Damn you penis and the ideas you give me.."
    mc_thoughts "How can i smooth this out?   'Hey, its not my fault. It's yours for not letting me fuck'..."
    mc_thoughts "Yeah right.. Can't say that if i want her to stay together with me... Think! Think!"


    show bg 00_12 with Dissolve(1.0)
    em "Babe, why did you do that?"

    mc "Because i love you and you are so sexy. It's just..."
    mc "Ah fuck it. We have no sex life! I barely remember how your puss...vagina looks like! I need sex!"

    "Emily just stares at you with a shocked expression.."

    mc_thoughts "Ahhhhhh fuuuuuck. Now I'm royally fucked!"

    em "I...I...I know. I'm sorry! "
    em "I know guys need it alot, we women don't... So it's easy to forget."
    em "Hmm.."

    em "How about this?"
    em "I'll take you out to a restaurant tonight and we can talk about it?"
    em "I really have to go now. But before..."


    show bg 00_13 with Dissolve(1.0)

    em "Give me a big kiss!"
    em "Kiss*"

    show bg 00_14 with Dissolve(1.0)

    em "Oh what's this?"

    em "It seems [mc_name] Jr is still waiting!"
    em "Be a good boy and you might get rewarded tonight.."


    show bg 00_15 with Dissolve(1.0)

    em "Talk to you later babe. Take a shower and look for jobs today!"
    em "I really have to run now! Byeee"


    show bg 00_16 with Dissolve(1.0)
    
    mc_thoughts "Shit. I must have stretched a muscle in my back when i jumped out from the bed!"


    show bg 00_18 with Dissolve(1.0)

    mc_thoughts "Time to shower and then i'm gonna look up that taboo site"

    "You brush your teeth, pee and take a shower"


label day1_taboo_site_signup:
    show bg house01_bedroom_day_pc with Dissolve(1.0)

    "Some time later..."

    mc_thoughts "Let's check that site out!"

    show bg pc with Dissolve(1.0)

    $renpy.pause(2)

    show pc tb_01 at top with Dissolve(1.0)

    mc_thoughts "Hm. I'm hard as a rock again!"
    mc_thoughts "Let's click on My profile."

    show pc tb_02 at top with Dissolve(1.0)

    mc_thoughts "100$!!!"
    mc_thoughts "Oh well. Let's do it!"
    mc_thoughts "I hope Emily won't take a look at my expenses on this credit card she gave some time ago.."

    "Many, many clicks later.."
    "And 30 minutes "

    mc_thoughts "DONE!"
    mc_thoughts "....."
    mc_thoughts "Click here to start building your profile......"
    mc_thoughts "SHIT! How long will this take?"

    show pc tb_01 at top with Dissolve(1.0)

    mc_thoughts "Are you single? Or a couple?"
    mc_thoughts "Couple!"
    mc_thoughts "Fill this box about her:"
    mc_thoughts "29 year. 170cm tall. Medium breasts."
    mc_thoughts "Fill this box about you:"
    mc_thoughts "24 year. 175cm tall. 10-11cm at erect."
    mc_thoughts "Is she submissive?"
    mc_thoughts "I don't think so"
    mc_thoughts "Are you submissive?"
    mc_thoughts "I think so"
    mc_thoughts "How many sexual partners has she had?"
    mc_thoughts "5? Maybe"
    mc_thoughts "How many sexual partners have you had?"
    mc_thoughts "This is my first"
    mc_thoughts "How long have you been together?"
    mc_thoughts "2 years"
    mc_thoughts "What is your relationship status?"
    mc_thoughts "Soon to be married"

    "And the questions just go on and on..."

    "Another 30 minutes later..."

    mc_thoughts "Finally done........ What now?"
    mc_thoughts "Upload a picture for our profile with our faces showing.."
    mc_thoughts "Fuuuuuuuuck.."
    mc_thoughts "I don't care,, let's do it, It's a paysite after all. Expensive too! No one we know will see it "
    mc_thoughts "And if they do, why are they here too? Both parties will just pretend it never happened! Win-win"

    "Uploaded*"

    "Now as a last step write a little about why you are here and what you are looking for"

    mc_thoughts "Gah come oooonnnn!"
    mc_thoughts "Ok ok.."
    mc_thoughts "Hmm"
    mc_thoughts "I'm the boyfriend writing this... My girlfriend does not know about this site.. Yet... I'm here because I'm curious and hope to know more. Mainly about cuckolding and femdom"
    mc_thoughts "I'll fill out more later. Bye"

    mc_thoughts "I feel like a retard now."
    mc_thoughts "Shit 3 hours have passed already!"
    mc_thoughts "I desperately need to pee!"

    hide pc with Dissolve(1.0)

    "You run to the bathroom"


label day1_bathroom_after_site:
    show bg house01_bathroom_day with Dissolve(1.0)

    mc_thoughts "Almost. Soon there.. 1 more second!"


    show bg 00_19 with Dissolve(1.0)

    mc_thoughts "Ahhhhhh. I love this feeling! It's like a different and milder type of a orgasm.."
    mc_thoughts "Same with poopi... What??"


    show bg 00_20 with Dissolve(1.0)

    mc_thoughts "Hnnnghhhhhghh"
    mc_thoughts "SHIT"
    mc_thoughts "SHIIIIT"

    mc_thoughts "How can I still be rock hard after all this time?"
    mc_thoughts "I better clean this up before I do anything else"

    
label day1_meanwhile_emily_work:
    scene bg black with Dissolve(1.0)

    "Meanwhile at Emily's workplace"

    show bg 00_21 with Dissolve(1.0)

    em_thoughts "I know i forgot something today... But what?"
    em_thoughts "And i wonder why [mc_name] acted like that this morning"
    em_thoughts "He just never complained before, but I can understand him. It's not like I have given him too much sex.."
    em_thoughts "I just don't think about sex much at all..."
    em_thoughts "No..."
    em_thoughts "That's a lie, why do I lie to myself?"
    em_thoughts "I love him very much! But sex with him just sucks"
    em_thoughts "He's nothing like any other guy I've ever had. It's the worst sex I've ever had.. He climaxes too early, Isn't that well equipped and doesn't know how to use it "
    em_thoughts "But... he's the kind of guy you want to live with for the rest of your life! He's hot, shy, cute, romantical, caring and loves me very much. I think he would do anything for me... And..."
    em_thoughts "He is young! I wanted to find a hot young stud to fuck me silly! That's how I met this guy called Jack on a sex chatting site. He always told me to send sexy pictures of myself and to masturbate in front of the webcam for him. It felt so wrong and illegal, but I loved it!"
    em_thoughts "After a couple of months our online relationship just started to fade. Maybe he just grew bored of me? And he never showed me how he looked... down there.. I wonder what his penis looks like?... Enough of these thoughts Em!"
    em_thoughts "One night he started to talk about this other guy who's 3 years younger than him, how great he is and all that. Then he asked if I wanted to chat with him"
    em_thoughts "3 years younger!! Of course i wanted to meet him! I was hoping he would be the sexy young hunk who could meet me in real life.."
    em_thoughts "Anyway... That's how i met [mc_name]. Turns out he wasn't a big hunk with big muscles who could fuck me silly "
    em_thoughts "It took like 1 year to finally convince him to meet me, so I kinda guessed he was shy and I knew he was a virgin at this point. But it was a hot thought to be able to take a sexy young boys virginity"
    em_thoughts "When we finally met he was so shy and cute. I just fell in love with him the moment he spilled his drink.. Hihi"
    em_thoughts "Besides you can't get everything you want!"
    em_thoughts "So I chose my awkward shy little guy and a future with him.  I have no regrets"
    em_thoughts "Now.... What the hell did i forget??"


    show bg 00_22 with Dissolve(1.0)

    em_thoughts "Yup i painted my nails.. Did i put on any makeup?"
    em_thoughts "Hmmm no.. It's something else"

    "?" "Ahem"
        

    show bg 00_23 with Dissolve(1.0)

    em_thoughts "Oh"
    em_thoughts "That's my boss James Moore. One of the best lawyers in the country"
    em_thoughts "Also one of my daddys best friend. That's how i got work here. Just as a receptionist, but you got to start somewhere. Right?"
    em_thoughts "He has a bit of a scottish accent. I love to listen to him. Many see him as a stiff type. Professional and strictly business. But I don't see him that way. He's relaxed and full of bad jokes when he's around"
    em_thoughts "I've known him forever. He and dad used to hang out alot. Mr Moore also used to babysit me sometimes. He is great and has never treated me badly"
    em_thoughts "He almost feels like a dad to me. Need to be careful so i dont accidentally call him that by mistake hihi"
    em_thoughts "We haven't hung out since i was a teenager, it would feel strange to do so today i think"

    jm "There's my favorite girl in this whole building!"


    scene bg 00_24 with Dissolve(1.0)
    call wait_for_click


label day1_emily_james_lobby:
    show bg work_wife_lobby_day with Dissolve(1.0)

    show emily 01_03 at left with Dissolve(1.0)

    show james 01_01 at right with Dissolve(1.0)

    em "Hey! I'm the ONLY girl working here!"
    
    show emily 01_04 at left with Dissolve(1.0)

    jm "Hence the whole building thing after my favorite girl.."
    jm "Just kidding! You are the.........."

    show james 01_02 at right with Dissolve(1.0)

    jm "cough cough*"

    show james 01_03 at right with Dissolve(1.0)

    jm "What's the origin of the word \"Boob\"?"

    em "Ehh??"

    jm "The \"B\" is the aerial view, the \"oo\" is the front view, the \"b\" is the side view."
    jm "You are giving me the O O"

    em "Wha"
    
    jm "Look down Em.."

    show emily 01_05 at left with Dissolve(1.0)

    em "OH MY GOD!"

    jm "Haha. Boobs are proof men can concentrate on two things at once"

    show emily 01_06 at left with Dissolve(1.0)

    em "This is soooo embarrassing!"
    em "I forgot to put my bra on because [mc_name] .... Distracted me this morning!"
    
    jm "Relax girl. I've seen you naked plenty of times! Sure it was long ago but you are still the same girl"
    jm "I just came down to say good morning and to tease you a bit. I got to go and make some phone calls now.  See you later. And..."
    jm "You have grown nicely. Hahaha!"

    hide james with Dissolve(1.0)

    em "I'm going to die!"

    hide emily with Dissolve(1.0)


label day1_gv_chat:
    scene bg black with Dissolve(1.0)
    "Meanwhile back home"


    show bg house01_bedroom_day_pc with Dissolve(1.0)

    mc_thoughts "Pheew. I hate cleaning!"
    mc_thoughts "Let's finally check the taboo site again. I think i forgot to log out"

    mc_thoughts "What's this?"

    show pc tb_chat_victoria_01 at top with Dissolve(1.0)

    gv "Hello"

    "You sit down and start to type with nervous hands"

    mc "H hey"

    gv "..."
    gv "I wont bite you! Not yet ;)"
    gv "I just saw your profile. And you made me interested"

    mc "Oh. Thank you! How did i manage to do that? I just created my page here."

    gv "Excellent! You are only new once.."
    gv "I like submissive fresh innocent cute guys."

    "You blush. It's so long since someone random said something so nice to you"

    gv "You look so cute blushing like that!"
    gv "I read your profile and your fiancée doesn't know anything? Tell me about yourself, her and your situation!"

    "It feels weird, but it feels nice to talk with someone who's interested. You only have 1 friend who you see rarely. So you end up telling her everything about yourself, Emily and your awful sexlife."

    gv "I know why Emily's never in the mood for sex. I'll be honest with you. But you already know the answer to that. Don't you?"

    menu:
        "She's cheating on me? [black]":
            gv "Nope. Although i wouldn't be surprised if she's already cucking you."
            gv "She needs a cock she can feel. She can't feel yours! "
        "My penis is not that big? [pink]":
            gv "Yes. Good boy! "
            gv "She needs a big cock that can stretch her and make her scream! "
            gv "Your tiny teeny thingy won't give her anything at all.. "
            gv "But don't get sad.. It is just the way it is! You can never give her true pleasure "
            gv "But you can still make sure she gets pleasure.. "
            gv "As her boyfriend and lover that's your job... Right? "
            gv "To always make sure your girl gets what she needs and deserves! "
            gv "Seeing her getting pleasured the way she needs is the only pleasure you deserve... "
        "She just doesn't need sex? [red]":
            gv "No you idiot! "
            gv "She needs a real cock. Not your pencil sized clit! "

    gv "Start with buying her a dildo!  "
    gv "Nothing too big and expensive. You don't want to scare her. You seem to have a finger sized clit that's about 8-12 cm. So buy her like 15 - 20 cm and at least twice your girth. Normal sized in other words.. "
    gv "You said you will talk about your non existent sexlife tonight after dining out. Be good to her, be sensual and romantic all day. And when you come home, start to talk "
    gv "Bring the size question, she will admit after awhile. Just give her wine before. Calm her, say it's ok. It's normal. Say it would turn you on to see her getting bigger sizes "
    gv "Cuddle and kiss. Watch a porn movie with her. Something with big cocks. Then just present her new dildo to her "
    gv "You can thank me later ;) "

    mc "Thank you. Wait!... How can you know my size? I never wrote that or told you!"

    gv "... "
    gv "Your profile text just screams tiny dicked cuck... "
    gv "And we are video chatting.. Or you are ;) "

    mc "Wha What?"

    gv "Just go and buy the dildo. Now!"
    gv "We will talk later!"

    "Goddess Victoria has gone offline"

    hide pc with Dissolve(1.0)


    scene bg black with Dissolve(1.0)
    "After 15 minutes you arrive at a sex shop"

    mc_thoughts "Right. That just happened.."
    mc_thoughts "I've got nothing to lose, so let's ju do it!"

    jump day1_sex_shop


label day1_phone:
    show bg house01_entry_day with Dissolve(1.0)

    "ring ring*"

    show phone mc_em_call at top with Dissolve(1.0):
        yoffset -40

    mc "Hi baby!"

    em "You! You! Youuuuuu..."
    em "You made me forget my bra because you jumped me this morning! You damn horny... tool!"
    em "So i accidentally flashed my breasts to James, my boss!"

    mc "..."

    "You feel bad and maybe a little jealous. But the thought of another man seeing your baby like that and maybe even becoming horny makes your dick twitch and you feel it getting harder"

    em "Hello??"

    menu:
        "I'm sorry! But it is kind of hot! [pink]":
            jump day1_phone_hot
        "Oh no. I'm so sorry!":
            em "You better be!"
            em "It was so embarrassing!"
            jump day1_phone_done


label day1_phone_hot:
    $ em_kinks_exhibit += 1
    $ mc_cuckpoints += 1

    em "I know! Just oh my god It was so"
    em "WAIT! WHAT?"
    em "Let's see how fucking hot you think it is when I go there and FUCKING FUCK HIM!!!!!"
    em "...."
    em "I need to breath deeply... Relax Em.. He is just trying to be funny.."
    em "Gahh that was a bad joke"
    em "You need to stop with those!"

    mc "I'm sorry baby"
    mc "I love you!"


label day1_phone_done:
    em "Grrr. I hope James will forget that"
    em "Just don't forget dinner tonight. You know how I hate cooking and it's some time ago since we were out together. I have to stop now but talk to you later"
    em "Kisses"

    hide phone with Dissolve(1.0)
    pause 1.0

    show bg house01_bedroom_day_pc with Dissolve(1.0)

    mc "I'm exhausted"
    mc "I'll just take a short nap.."


label day1_emily_returned_home:
    scene bg black with Dissolve(1.0)

    em "BAAAABE" with hpunch

    show bg house01_bedroom_day_pc with Dissolve(1.0)

    show emily 01_07A at left with Dissolve(1.0)

    em "Babe"

    mc "Oh hey! Good morning!"

    em "..."
    em "It's not morning! I just got home from work"
    em "Dinner out, remember?"
    em "Get ready babe"
    em "The taxi will be here soon"

    "You jump up and start to get ready"

    hide emily with Dissolve(1.0)
    pause 0.5

    show bg house01_entry_day with Dissolve(1.0)

    "You both get ready and start to leave"

    mc "Can't wait! I'm starving! I forgot to eat anything today"

    em "What? Again?"
    em "That's why you are so skinny"

    "She gives your butt a playful slap and says in a deep southern accent:"
    em "But ima liking this skinny bootie"

    show bg house01_ext_day with Dissolve(1.0)
    
    show taxi day at truecenter with Dissolve(1.0)

    "You both get inside the taxi and you are soon at your destination"

    hide taxi with Dissolve(1.0)

    jump day1_coffee_shop


label day1_coffee_shop_exit:
    show bg house01_ext_night with Dissolve(1.0)
    show taxi night at truecenter with Dissolve(1.0)
    "Little bit later"

    hide taxi with Dissolve(1.0)
    pause 0.5

    show bg house01_entry_night with Dissolve(1.0)

    em "Let's get into our nighties and watch some tv!"

    mc "Yes let's do that. But i know something you would like more"

    em "Ohh and what would that be?"

    mc "Get changed, get yourself some wine and come here so i can massage your feet!"


label day1_tv:
    show bg 00_30 with Dissolve(1.0)

    "You quickly get changed and sit down to wait for Emily"

    em "YAY! You know how much i love to get my feet massaged!"
    em "I can't wait"


    show bg 00_31 with Dissolve(1.0)

    em "I'll just put this bottle down here "

    show bg 00_32 with Dissolve(1.0)

    em "Let me take this off too! "
    em "First that heavenly burger, now wine and massage "


    show bg 00_33 with Dissolve(1.0)

    em "Oh god. That's so good "
    em "Both of you! "

    mc "I wanted to ask you something baby "

    em "Ahh soo gooood! You can ask me anything right now "


    show bg 00_34 with Dissolve(1.0)

    "She's already getting a bit tipsy and relaxed to give you a great view "

    mc "You have to promise to be 200%% honest with me "

    em "Of course babe "
    em "What's wrong? "

    mc "Why don't you enjoy it anymore... I mean it was great in the beginning.. "
    mc "Am i too small for you? My dic..penis.. "

    "You feel every muscle in the foot tense up "

    em "I i I... You... It's just that I'm not that interested in sex. You know that babe! "

    mc "Please be brutally honest with me! We are going to get married. We have to promise to never lie to each others "
    mc "You can't hurt me, there's help for that kind of bedroom problem.. "

    em "I     I just don't feel so much when we have sex. Maybe i have a loose vagina? I never cared about it. It was never a problem for me. I don't think you are too small.... "
    em "... "

    "Emily looks at you nervously "

    em "We had much more sex when we just met. That's true.. But it never gave me much.. So I just prefer to help you receive orgasms sometimes.. "
    em "I took your virginity. Asked you to move in. Said yes to marry you. I don't care how big or small we are down there! "

    "You both stand up and embrace each other in a hug "


    show bg 00_36 with Dissolve(1.0)
    ".. "


    show bg 00_35 with Dissolve(1.0)

    em "I feel so good now babe "
    em "Pinky promises to always be completely honest with each other! "
    em "Wait.. What did you mean by  "
    em "There's help for that kind of bedroom problem?? "

    mc "I have a gift for you "

    em "Should i be worried now? "

    mc "No no! I think you will be happy! "
    mc "And.. and.. I want.. us.. too... "
    mc "Watch a porn movie together..  "
    mc "I know you hate those. But let's just try something different tonight "

    em "Oh pheew. Yes.. yes i accept "
    em "I was worried you had bought a dog or a car or something we can't afford! "

    mc "Get comfortable baby. I'm just going to get something "

    "You go and grab the dildo and a usb stick with 2 of your favorite porn movies in it "


    scene bg black with Dissolve(1.0)

    $ quick_menu = False
    show waiting at topleft
    show bg 00_37 with Dissolve(1.0)
    pause 1.0
    hide waiting
    $ quick_menu = True

    mc_thoughts "WOW! "
    mc_thoughts "I'm just going to hide the dildo here behind the sofa pillow for now "
    mc_thoughts "She's clearly affected by the wine now, she feels great and relaxed. Agreed to watch porn and even got undressed.. I might get lucky tonight! "
    mc_thoughts "Which one of the movies should i choose? "

    menu:
        "Black bull fucks my blonde wife [pink]":
            jump day1_movie_black
        "19 year white guy fucks my mature wife":
            jump day1_movie_white

label day1_movie_black:
    show bg 00_38A with Dissolve(1.0)

    $ mc_kinks_black += 1
    $ em_kinks_black += 1
    $ mem_emily_pink = True
    $ mc_cuckpoints += 1

    em "They look great together. It looks like it's homemade. I wonder if they are married?"
    
    show tv blackb1 at topright with Dissolve(1.0)

    em "Ohhhh. He's a great kisser!"
    em "I want to get kissed like that too babe!"

    em "There's no way she's caressing his penis. Look how long her strokes are!"

    show tv blackb2 at topright with Dissolve(1.0)

    "Emilys jaw hits the floor"

    em "OH MY FUCKING GOD"
    em "Noooooo wayyyy"
    em "Jeezes"
    em "Now i've seen it all"

    show tv blackb3 at topright with Dissolve(1.0)

    "After some time Emily has calmed down after the initial dick size shock and started to get into the movie again"

    em "Look you can see her wedding ring. This is definitely home made!"
    em "And those pink panties look pretty. Pink goes great with blondes!"

    "The camera shows another white man sitting in the room watching. And he finally starts to talk"

    mh "How do you like my wife?"

    mb "She's great. Those cocksucker lips know exactly how to suck!"

    mh "Just wait until you get to try her pussy! It's always wet for bbc"
    mh "Haha"

    mw "Yes! I can't wait! I'm a slut! We want you to make me pregnant tonight"

    mb "Of course slut! I can't wait to shoot my fertile seed deep into your slutty cunt"

    mh "Yeah we are ready for a third one now. So no anal tonight. All needs to go inside her sloppy cunt"

    mw "Moans'"

    show tv blackb4 at topright with Dissolve(1.0)

    em "Whaaaaaaat just happened?"
    em "She is cheating on him in front of her husband?"
    em "Why? Why would she do that? And why would he enjoy that?"

    mb "Damn you are sucking like a mad cock addict! Does your white slim hubby not give you enough cock?"

    mw "Pfft. That tiny cocked sissy can't satisfy me. He gets nothing from me. Never has,, never will.."
    mw "I get to fuck whoever i want whenever i want. He gets to watch if he's lucky.."
    mw "After you have filled my pussy with your cum and he has swallowed some of it. I might make him suck you off if you still want more!"
    mw "..."
    mw "What do you say sissy?"

    mh "Thank you honey"

    mb "Bend over bitch and get naked"

    show tv blackb5 at topright with Dissolve(1.0)

    "Emily seems lost and in deep thoughts"

    show tv blackb6 at topright with Dissolve(1.0)

    em "..."

    show tv blackb7 at topright with Dissolve(1.0)

    mb "I knew i could just go balls deep in your used loose cunt with one hard push"

    mh "She loves that! There's nothing she can't take in one push!"

    mw "Crazy moaning sounds*"

    "You can see Emilys hand is over her pussy. Like she's holding it"

    show tv blackb8 at topright with Dissolve(1.0)

    mb "Ride me slut!"
    mb "Time to make you mine now"

    "You both watch as he grabs her hard and starts to fuck her at superhuman speed. Bottoming out each time"

    mw "Yes yes cervix, each time.. yes. more"

    em "Ahh"

    "You look over and see her massaging herself carefully"

    show tv blackb9 at topright with Dissolve(1.0)

    mb "Are you ready to become pregnant whore?"

    mw "YEEEEEEEEEEEEEEEEES! Deep inside me!!!"
    mw "We need to spread your superior genes.. Sissys gene pool needs to die out"

    "You get a closeup shot and can see how the huge dick just starts pumping cum inside her, and how her pussy is milking it"

    em "Moans* Wet sounds*"

    "She's fingering herself now and is really wet"

    show tv blackb10 at topright with Dissolve(1.0)

    mw "Sissy call that other guy. I need him to come and fuck me right now! I need more cum inside me"
    mw "But lick me clean before!"

    mh "Yes honey!"

    "Movie ends"

    jump day1_movie_end


label day1_movie_white:
    show bg 00_38B with Dissolve(1.0)

    mc "Lets watch this tonight"

    show tv whitew1 at topright with Dissolve(1.0)

    #Emily
    em "Aww that's romantic. Look how sensual she is sucking off her husband like that"
    em "I might give you that tonight!"
    em "But why's she gagging so much?"

    show tv whitew2 at topright with Dissolve(1.0)

    em "OH NO... What's that? Oh my goood. Its huuuuge!"
    em "I can't belive it!"

    show tv whitew3 at topright with Dissolve(1.0)

    em "What a great man preparing his wife"
    em "But she will need it! Hihi"

    show tv whitew4 at topright with Dissolve(1.0)

    em "Hey! She's kinda chubby like me!"
    em "Maybe that's you and me in the future making movies for ourselves?"

    show tv whitew5 at topright with Dissolve(1.0)

    "The camera shows the husband sitting on a chair filming them"

    mh "Do you like him baby? I knew he always wanted to fuck you!"

    mw "Yes! Thank you baby! I love his cock! It's so big. Is your huge cock ready to fuck me?"

    mwb "I'm ready, just sit down on it! Is it ok if i cum inside you?"

    mw "Yes! You have to cum inside me! But dont tell Bob you are fucking his mom! Ok?"

    mwb "Course mam! But you are not the only mom im fucking. Friends mothers are the best!"

    show tv whitew6 at topright with Dissolve(1.0)

    mw "Here let me just spread it to help you!"
    mw "Can you feel me dripping on your huge cock? Jam it inside now!"

    mh "This is so beautiful! Jam that 19 year old cock inside her now!"

    "Emily seems deeply shocked. But curious and can't take her eyes of the tv"

    show tv whitew7 at topright with Dissolve(1.0)

    "She starts to ride him hard. And the husband never stops talking how beautiful she is, how sexy. Wife keeps talking back saying how much she loves him, other cocks"
    "Both husband and the bull keeps kissing her. She is in heaven."

    em "Ohhh"

    "Emily is really starting to enjoy the show"

    "You both watch as the bull pushes up deep inside her and starts to cum"

    show tv whitew8 at topright with Dissolve(1.0)

    mw "Here let me clean your cock up. I also want to taste your cum"
    mw "Hubby come here, kiss me! He tastes great"

    "Movie ends"


label day1_movie_end:
    show bg 00_39 with Dissolve(1.0)

    em "That was.... "
    em "We can do this more times.."
    em "If you want it i mean.."
    
    mc "Baby.."
    mc "That gift i mentioned earlier. Emmm.. "
    mc "I got you this.."

    em "Oh?"
    em "What is it babe?"

    if inventory_dildo == "black":
        jump day1_black_dildo
    if inventory_dildo == "white":
        jump day1_white_dildo


label day1_black_dildo:
    show bg 00_40B with Dissolve(1.0)

    $ mem_short_emily += 1

    em "OH MY GOD!"
    em "It's so HUUUUGE!"
    em "And black.."
    em "It looks like the guys di... Penis we just watched!"
    em "Oh my god, it will never fit! Are you crazy??"

    show bg 00_41B with Dissolve(1.0)

    mc "I wanted to give you something big. You deserve it"
    mc "It would be a dream to see you take it. That would be so hot"

    em "I.... wow"
    em "The wine.. That movie..."
    em "I'm really wet babe"

    "You notice how she's dripping already"


    show bg 00_42B with Dissolve(1.0)

    em "Oh look!"
    em "Hihi"
    em "Look at the size difference..."
    em "You are so small compared to this huge black one"

    mc "Aahh"

    em "I want to try it, We have to try it!"
    em "Come here babe. Follow me"


    scene bg 00_43 with Dissolve(1.0)
    call wait_for_click


    show bg 00_44 with Dissolve(1.0)

    em "You really want to see me take that black monster?"

    mc "YES YES"

    em "I'm doing this for you babe"
    em "Start rubbing it against me "
    em "But take it slow!"


    scene bg 00_45B with Dissolve(1.0)
    call wait_for_click

    mc_thoughts "Wow. I've never seen her like this. This horny!"
    mc_thoughts "She's whimpering ,shaking and her pussy is so wet. "
    mc_thoughts "And it's not even inside her yet. Just resting against her wet pussy"
    mc_thoughts "I'm just going to move it in circles around her for a few seconds. I want to make her crazy!"

    em "F FF FUCK ME!"
    em "please! Use it.."
    em "Now!"

    mc_thoughts "That didn't take long!"
    mc_thoughts "She's such a hot slut right now"
    mc_thoughts "Should i lick her ass while pressing the dildo in just a little bit?"

    menu:
        "Yes! Lick it! [pink]":
            jump day1_black_dildo_lick
        "Eww. Nope! NO! [red]":
            jump day1_dildo_no_lick


label day1_black_dildo_lick:
    $ em_kinks_rec_anal += 1
    $ mc_kinks_give_anal += 1
    $ mem_short_emily += 1
    $ mc_cuckpoints += 1

    scene bg 00_46B with Dissolve(1.0)
    call wait_for_click

    em "AHHHHHHHH "
    em "WHAT are you doing? "
    em "OHHHH "
    em "Don't stop.. "

    "You keep licking her while just fucking her with half of the tip "
    "You can feel her starting to shake more and breathing more heavily "

    em "I I Imm clooseee "
    em "MOOOOOOREEEE "

    "You press your tongue much harder and manage to get the tip in while simultaneously pressing the dildo head inside her "
    "The dildo is going in surprisingly easy. But you are being very careful because you are really hoping to fuck her tonight and not hurting or pissing her off "

    scene bg 00_47B with Dissolve(1.0)
    call wait_for_click

    em "I'm .. I'mmmmmmmmmmmm "
    em "AAAAUUU NAAAA AHHHHHHHHHHHHHHHHHHHHHHHHHHHHH "
    em "GGGGGGGGGAAAA OHHHHH!!!! "

    mc_thoughts "Did she just squirt?? "
    mc_thoughts "I didn't think it was possible in real life! They only do it in porn movies! "

    show bg black with Dissolve(1.0)


label day1_black_dildo_turn_around:
    show emily sex_01 at top with Dissolve(1.0)

    "Panting* "

    em "That was amazing! "
    em "I've never felt anything like that.. "
    em "I need more babe..  "
    em "You have to go deeper now! "

    show emily sex_02B at top with Dissolve(1.0)

    "She lays back and spreads her legs. You slowly press the dildo head inside her wet soft hole again "

    em "Ah GOD YES "
    em "FUCK "
    em "YES "

    show emily sex_03B at top with Dissolve(1.0)

    em "Ohhh"

    show emily sex_04B at top with Dissolve(1.0)

    em "HNNGGGGGGGGGHHHHHHHHHHH "
    em "OHHHHHH YEEEEEEEEEEEE FFFUUUUUCCCKK "

    mc "Wow baby. This is amazing, you are amazing! "

    "Dildo plops out.. "
    "Heavy panting... "

    em "Oh my god...  "
    em "I cant' think straight right now.. "

    show emily sex_05 at top with Dissolve(1.0)

    "Neither can you.. "
    "You are so horny your body moves almost by itself  "
    "You get down to your knees and position yourself between her shaking hips "

    mc_thoughts "I'm so horny it hurts. Look at that sexy pussy. It's still open, that dildo stretched her out more than she's used too"
    mc_thoughts "I need to feel that wet sloppy pussy right now! "

    jump day1_sex_starts


label day1_white_dildo:
    show bg 00_40A with Dissolve(1.0)

    em "OH MY GOD! "
    em "It's so BIG! "
    em "I've never seen.. No one has this size "
    em "Are you trying to kill me? "


    show bg 00_41A with Dissolve(1.0)

    mc "I thought you would like it "
    mc "It would be so hot to see you with it! "

    em "I.... I'm speechless "
    em "But that wine and movie really got me into mood. I'm already dripping! "


    show bg 00_42A with Dissolve(1.0)

    em "Oh my god! "
    em "Hihi "
    em "Look at the size difference... "

    mc "Ahh "

    em "I want to try it, We have to try it! "
    em "Follow me babe "


    scene bg 00_43 with Dissolve(1.0)
    call wait_for_click


    show bg 00_44 with Dissolve(1.0)

    em "I think im ready for this big boy now "
    em "Put it inside me babe "
    em "But take it slow! "


    scene bg 00_45A with Dissolve(1.0)
    call wait_for_click

    mc_thoughts "Wow. I've never seen her like this. This horny! "
    mc_thoughts "She's whimpering and shaking and so wet. And it's not even inside her yet. Just resting against her wet opening  "
    mc_thoughts "I'm just going to move it in circles around her for a few seconds. I want to make her crazy! "

    em "F FF FUCK ME! "
    em "please! Use it.. "
    em "Now! "

    mc_thoughts "That didn't take long! "
    mc_thoughts "Should i lick her ass while pressing the dildo in just a little bit? "

    menu:
        # Port note: Changed to pink to keep it consistent with
        # the cuck/kink = pink rule and with the black dildo branch
        "Lick her butt [pink]":
            jump day1_white_dildo_lick
        "Eew no way! [red]":
            jump day1_dildo_no_lick


label day1_white_dildo_lick:
    $ em_kinks_rec_anal += 1
    $ mc_kinks_give_anal += 1
    $ mc_cuckpoints += 1

    scene bg 00_46A with Dissolve(1.0)
    call wait_for_click

    em "AHHHHHHHH "
    em "WHAT are you doing? "
    em "OHHHH "
    em "Don't stop.. "

    "You keep licking her while just fucking her with half of the tip "
    "You can feel her starting to shake more and breathing more heavily "

    em "Press h h harder with the dildo "

    "You press your tongue much harder and manage to get the tip in while simultaneously pressing the dildo head inside her.. "


    scene bg 00_47A with Dissolve(1.0)
    call wait_for_click

    em "MORE\nHARDER HARDER\nMORE MOOOREEEE"

    mc_thoughts "This is so fucking hot! "
    mc_thoughts "I need to feel her warm pussy soon "

    show bg black with Dissolve(1.0)


label day1_white_dildo_turn_around:
    show emily sex_01 at top with Dissolve(1.0)

    "Panting* "

    em "I've never felt anything like this.. "
    em "I want more! "
    em "I need more now babe..  "
    em "Please go deeper now! "

    "She lays back and spreads her legs. You slowly press the dildo head inside her wet soft pussy again "

    show emily sex_02A at top with Dissolve(1.0)

    em "Ah GOD YES"
    em "YES"

    show emily sex_03A at top with Dissolve(1.0)

    call wait_for_click

    show emily sex_04A at top with Dissolve(1.0)

    em "HNNGGGGGGGGGHHHHHHHHHHH "
    em "OHHHHHH YEEEEEEEEEEEE "

    mc "Wow baby. This is amazing, you are amazing! "

    "Dildo plops out.. "
    "Heavy panting... "

    em "Oh my god...  "
    em "I can't think straight right now.. "

    show emily sex_05 at top with Dissolve(1.0)

    "The smell of sex is driving you mad "
    "You stand up on your knees and get closer to her "
    "You need that long lost pussy right now! "

    mc_thoughts "I'm so horny it hurts. Look at that sexy pussy. It's still open, that dildo stretched her out more than she's used too.. "


label day1_sex_starts:
    show emily sex_06 at top with Dissolve(1.0)

    "You rub your dick against her pussy "

    em "Wha what's happen "
    em "Oh "
    em "Go on babe, you deserve it. You have been so good to me "

    "That's all the encouragement you need! "
    "In one fast motion you lay down and slam it as deep as you can inside her "

    show emily sex_07 at top with Dissolve(1.0)

    "Her pussy is so wet and too stretched out right now for you to feel much at all But it's so long since you were last inside her, and everything you have witnessed today makes this the best feeling ever "
    "You haven't even started moving yet., Just enjoying the moment "

    em "Uh oh.. "
    em "Babe.. "
    em "I can't even feel you right now.. "
    em "I feel nothing down there... "

    "Those words sends a tingling shockwave down your back. All the way down to your dick. "
    "It makes you loose your strenght for a moment and you almost fell down on her while you let out a big moan thinking you are going to cum only from her words "

    "Emily looks at you and says "
    em "You liked that didn't you? When I talk...  "
    em "dirty like that to you "

    menu:
        "Y yyeah i think i almost came [pink]":
            jump day1_sex_sph_yes
        "No i dont think i liked that [red]":
            jump day1_sex_sph_no


label day1_sex_sph_yes:
    $ mc_kinks_sph += 1
    $ em_kinks_sph += 1
    $ mc_cuckpoints += 1

    em "Oh yeah?"
    em "I knew it!"
    em "Your penis is so tiny"

    mc "Cock.."

    # Port note:
    # This check was originally just > 1 but there is only 1 black point
    # for Emily at this stage. There are a few solutions:
    # 1: Just change to > 0
    # 2: Award an Emily black kink point for the black dildo
    # 3: Change to > 0 and check for dildo color
    # I went with 3 because it takes the dildo choice into account
    # (which I think makes sense) while not potentially affecting other
    # future black kink checks.
    if em_kinks_black > 0 and inventory_dildo == "black":
        jump day1_sex_black_sph

    em "Your cock is so tiny. It's worthless."
    em "It's pathetic. I can't even feel it! You are so pathetic!"
    em "I'm only letting your sorry tiny pathetic cock inside because i felt sorry for you"

    mc "Ahhh gaaad Ohhh. I i can't, I'm going to"

    "Emily presses her legs against your butt to push you deeper"

    "You have not moved anything, but you are going to cum right now"

    # Port note: Since Emily later complains if MC comes inside her despite
    # telling him not to I added these two lines from the non-SPH
    # branch for consistency
    em "What?? Already?"
    em "Get it out! "

    jump day1_sex_end


label day1_sex_sph_no:
    $ mc_cuckpoints -= 2

    em "Do NOT lie to me!!"

    mc "I i i..."

    em "Because you twitched and I think you were going to cum right then and there!"

    mc "Hnggg"

    em "You aren't even moving baby..."
    em "SHOVE THAT TINY DICK INSIDE NOW!"

    mc "Ahhh gaaad Ohhh. I i cant, I'm going to"

    "Emily presses her legs against your butt to push you deeper"
    "You have not moved anything, but you are going to cum right now"

    em "What?? Already?"
    em "Get it out! "

    jump day1_sex_end


label day1_sex_black_sph:
    $ em_kinks_black += 1

    em "Your tiny white cock is worthless babe"
    em "It's pathetic. I can't even feel it! You are so pathetic!"
    em "You are not a real man. I need a big black man as a boyfriend"
    em "I'm only letting your sorry tiny pathetic cock inside because I feel sorry for you"
    em "And"
    em "For finding me that huge black guy who fucked me senseless. He made me his bitch"

    mc "Ahhh gaaad Ohhh. I i cant, i I'm going to"

    "Emily presses her legs against your butt to push you deeper"

    "You have not moved anything, but you are going to cum right now"

    em "What?? Already?"
    em "Get out! "
    em "I only want black cum inside me!!!!"

    mc "Ahhhhh gaaaadddd"

label day1_sex_end:

    mc "I hhnnnggytyyuuu"
    mc "I'm cum cuming haaaa"

    mc "What? Already? You didn't even move anyth..."

    menu:
        "Cum inside her [red]":
            jump day1_sex_cum_inside
        "Cum outside [pink]":
            jump day1_sex_cum_outside


label day1_sex_cum_inside:
    $ mc_cuckpoints -= 1
    show emily sex_08A at top with Dissolve(1.0)

    mc "Ahhhhhh uhhhhhh"

    "You have no time to reach before your balls start emptying inside her. Seconds after you being empty your cock just falls out from the warm,sticky and wet heaven"

    em "That's.. I had no idea guys could even cum without moving.."
    em "Oh no. Shit!"
    em "Damn it!"
    em "I TOLD YOU NOT TOO!!!"
    em "This is a unsafe period for me!"
    em "We can't afford to have any babies now! We need to, we need...."

    mc "I'm sorry baby"
    mc "We can talk about it later, i can't keep my eyes open anymore. I'm so empty and satisfied. I've never felt this good"
    mc "Sorry"

    em "Ok..."
    em "But you need to start listening to me"
    em "No means no!"
    em "Got it?"

    mc "Yes, I'm sorry I just couldn't hold it anymore"

    em "..."
    em "It's ok, but start listening to me"

    hide emily with Dissolve(1.0)
    pause 1.0

    if mem_short_emily == 2:
        jump day1_sex_smoking

    jump day1_end

label day1_sex_cum_outside:
    $ mc_cuckpoints += 1
    show emily sex_08B at top with Dissolve(1.0)

    "Shakingly you quickly pull out. There's no time to aim before you explode over her breasts"

    mc "Ahhhhhh uhhhhhh"

    em "Oh wow.. That's the quickest I've ever seen"
    em "I don't think you even moved inside me?"

    mc "Sorry baby. You just make me feel too good! "
    mc "I'm spent. I have to close my eyes and rest"
    mc "Sorry"
    mc "Love you"
    mc "Goodnight"

    em "Don't worry!"
    em "You did good..."
    em "Goodnight babe"

    hide emily with Dissolve(1.0)
    pause 1.0

    if mem_short_emily == 2:
        jump day1_sex_smoking

    jump day1_end


label day1_sex_smoking:
    $ em_kinks_smoking += 1
    scene bg black with Dissolve(1.0)
    "5 minutes later"

    show bg 00_48 with Dissolve(1.0)

    em "I can't sleep!"
    em "It's so long since I felt anything like that.."
    em "I feel so.... "
    em "Empty.. Open.. and relaxed. I think I really needed this"
    em "I know i have quit smoking.."
    em "But I really need one now"

    mc "It's okey baby. Just don't set the bed on fire hehe.."

    em "Don't you trust me?"

    mc "I trust you baby!"

    em "Good! "
    em "And I know you do.."
    em "Sweet dreams my little guy!"

    "Kisses*"

    call wait_for_click


label day1_end:
    jump day2_start