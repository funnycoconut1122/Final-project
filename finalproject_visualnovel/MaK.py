import pygame
import copy
from button import Button  
from dialogue import DialogueSystem

pygame.init()


# ASK THE PLAYER FOR NAME AND USE IT FOR LATER DIALOGUES
player_name = ""

def get_player_name(screen, font):
    input_box = pygame.Rect(250, 250, 300, 40)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = True
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        if len(text) < 20:
                            text += event.unicode

        screen.fill((0, 0, 0))
        prompt = font.render("Your chosen name is:", True, (255, 255, 255))
        screen.blit(prompt, (input_box.x, input_box.y - 40))
        txt_surface = font.render(text, True, color)
        width = max(300, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.display.flip()
    return text


#THE GAME WINDOW
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Monster and Knight")
clock = pygame.time.Clock()

#MENU BG
background_surf = pygame.image.load("assets/menubg.jpg").convert()

# SCENES DATA (I lost track of the scenes' order...)
scenes = [
    {       
        "background": "assets/blackoutbg.jpg",
        "dialogues": [
            {"speaker": "narrator", "text": "..."}
        ]
    },



    # INTRO SCENE, NARRATOR.
    {
        "background": "assets/introbg.jpg",
        "dialogues": [
            {"speaker": "narrator", "text": "Once upon a time, a person who turned themselves into a monster by sheer force of self-hatred and distrust against humanity was coerced into imprisoning themselves in the damp and repulsive depths of a dungeon by other humans, incurring incessant physical and psychological torture from the bewitchment of the self-inflicted sufferings."},
            {"speaker": "narrator", "text": "Despite countless attempts to call for help, no one was willing to stay and help the self-deprecating monster. One day, that person decided to cry for help one last time as a last resort before letting go of reality."},
            {"speaker": "narrator", "text": "To their surprise and bewilderment, a knight from a distant land heard it while falling trees and decided to find and rescue them, clueless about the peculiar encounter about to transpire."}
        ]
    },



    { "background": "assets/blackoutbg.jpg",
        "dialogues": [
            {"speaker": "narrator", "text": "..."}
        ]
    },


    # CHAPTER I : THE PRINCE FINDING AND ENTERING THE DUNGEON 
    # SCENE 1: KNIGHT NOTICES THE SCREAM
    {
        "background": "assets/bgscene1.jpg",
        "character1": {
            "image": "assets/knightnoticing.png",
            "color": (0, 136, 122)  # Teal color for character 1
        },
        "dialogues": [
            {"speaker": "character1", "text": "Where could that blood-curdling scream originate from?"},
            {"speaker": "narrator", "text": "The knight wonders while searching steadfastly for the scream, for fear that someone is in danger."},
            {"speaker": "narrator", "text": "He has been trying for the whole day, but his effort was in vain..."},
        ]
    },


    #SCENE 2: KNIGHT FOUND THE ENTRANCE TO THE DUNGEON
    {
        "background": "assets/trapdoor.png", 
        "dialogues": [
            {"speaker": "narrator", "text": "Suddenly, he grazes past an odd trapdoor on the forest’s ground. Having lost all hope, he decided to go at it one last time, still hellbent on finding the origin of that unknown yet heart-wrenching outcry."},
            {"speaker": "narrator", "text": "At last, he opened the trapdoor and delved into oblivion armed with an axe and a torch."},
        ]
    },



    {
        "background": "assets/blackoutbg.jpg",
        "dialogues": [
            {"speaker": "narrator", "text": "..."},
            {"speaker": "narrator", "text": "The knight lights up his torch for a better look at the place."},
        ]
    },



    # SCENE 3,4: KNIGHT ENTERS THE DUNGEON
    {
        "background": "assets/bgscene3.jpg",
        "dialogues": [
            {"speaker": "narrator", "text": "The trapdoor leads to a ginormous dungeon. The dungeon reeks of stench and is infested with insects of all sorts, enough to scare off the squeamish."},
            {"speaker": "narrator", "text": "Nevertheless, the knight does not even bat an eye at the creepy crawlies and continues to power through the seemingly pitch-black halls of the dungeon."},
            {"speaker": "narrator", "text": "He seems wary, though, not because of the unwelcoming atmosphere of the dungeon, but because of the fact that someone is being ensnared and persecuted in this hell of a place."},
            {"speaker": "narrator", "text": "Nonetheless, he pressed on with his heroic journey."}
        ]
    },



    {
        "background": "assets/blackoutbg.jpg",
        "dialogues": [
            {"speaker": "narrator", "text": "..."}
        ]
    },
   


    # CHAPTER II : ENCOUNTER ENEMIES AND FIGHT
    # SCENE 5: KNIGHT ENCOUNTERS MOBS
    { 
        "background": "assets/monsterafar.jpg", 
        "dialogues" : [
            {"speaker": "narrator", "text": "After walking for a while, the knight sees something lurking in the dark. Without hesitation, he positioned himself and surreptitiously approached the creature while wielding an axe in his right hand."},
        ]
    },
    # SCENE 6: INSPECTION
    { 
        "background": "assets/monsterafar.jpg", 
        "character1": {
            "image": "assets/knightapproach.png",
            "color": (0, 136, 122)  # Teal color for character 1
        },
        "dialogues": [
            {"speaker": "narrator", "text": "Upon closer inspection, there is a host of those creatures roaming around the dungeon’s chambers, perhaps they are guarding something..."},
            {"speaker": "character1", "text": "I won’t be able to defend myself against these creatures; they surely outnumber me."},
            {"speaker": "narrator", "text": "The knight reckons."},
        ]
    },
    # SCENE 7: KNIGHT DISTRACTING MOBS
    { 
        "background": "assets/monsterafar.jpg", 
        "dialogues": [
            {"speaker": "narrator", "text": "Then, he makes a daring yet compulsory choice to sneak past them using a beetle as a distraction."},
            {"speaker": "narrator", "text": "He picks up a beetle on the ground and flings it into the middle of the hallway, where the abhorrent beasts gather. As the knight expected, it caught their attention, and they all flocked to one place, allowing him to escape with flying colors."},
        ]
    },
    # SCENE 9: KNIGHT RUSH THROUGH
    { 
        "background": "assets/rushingbg.jpg", 
        "dialogues": [
            {"speaker": "narrator", "text": "Unfortunately, the chambers ahead also contain more of those creatures, and while rushing past them, the knight inadvertently stirred up a storm and infuriated the creatures. At once, a troop of the mysterious creatures charges at him, prompting him to fight back vigorously."},
        ]
    },



    { 
        "background": "assets/blackoutbg.jpg",
        "dialogues": [
            {"speaker": "narrator", "text": "Suddenly, one of them struck him."}
        ]
    },



    # SCENE 10: KNIGHT STRUCK BY A MOB
    { 
        "background": "assets/fighting.png", 
        "character1": {
            "image": "assets/hit&exhaust.png",
            "color": (0, 136, 122)  # Teal color for character 1
        },
        "dialogues": [
            {"speaker": "narrator", "text": "..."},
            {"speaker": "character1", "text": "Kgh!"},
            {"speaker": "narrator", "text": "For a moment, he anticipated foreboding agony and pain coming rushing through his body, but contrary to his premonition, he felt nothing."},
            {"speaker": "narrator", "text": "Perplexed by the abnormal sensation, he halted his movements. To his amazement, the creatures’ hits were painless and swift, akin to gales blowing through."},
        ]
    },
    #SCENE 11: KNIGHT REALIZATION AND RUSHING TO THE DOOR
    { 
        "background": "assets/runningtodoor.jpg", 
        "dialogues": [
            {"speaker": "narrator", "text": "Having known the innocuous nature of the monsters, he ran towards the door at the end of the dungeon, busting through the wall of enemies in front of him."},
        ]
    },



    {
        "background": "assets/blackoutbg.jpg",
        "dialogues": [
            {"speaker": "narrator", "text": "..."}
        ]
    },



    # CHAPTER III : REACH THE CHAMBER AND MEET THE MONSTER
    # SCENE 12: AT THE DOOR
    {
        "background": "assets/doortochamber.jpg",
        "character1": {
            "image": "assets/hit&exhaust.png",
            "color": (0, 136, 122)  # Teal color for character 1
        },
        "dialogues": [
            {"speaker": "narrator", "text": "*thuds*"},
            {"speaker": "character1", "text": "That was absurd! *Huff huff* How was that even possible?"},
            {"speaker": "narrator", "text": "The knight is hyperventilating while resting at the doors."},
        ]
    },
    {
        "background": "assets/doortochamber.jpg",
        "character1": {
            "image": "assets/knightapproach.png",
            "color": (0, 136, 122)  # Teal color for character 1
        },
        "dialogues": [
            {"speaker": "character1", "text": "Is this the final room of the dungeon?..."},
            {"speaker": "narrator", "text": "The knight asks while glancing at the doors."},
            {"speaker": "narrator", "text": "When the knight fully recovers, he stands up and tries to figure out how to creak open the gigantic door. Surprisingly, after one single push..."},
        ]
    },
    {
        "background": "assets/doortochamber.jpg",
        "character1": {
            "image": "assets/knightscratch.png",
            "color": (0, 136, 122)  # Teal color for character 1
        },
        "dialogues": [
            {"speaker": "character1", "text": "Huh, the door is easier to open than I thought..."},
            {"speaker": "narrator", "text": "The knight said to himself while remaining cautious of the loosely closed doors."},
            {"speaker": "narrator", "text": "After a moment of contemplation, the knight slowly steps inside the ultimate chamber."},
        ]
    },



    {
        "background": "assets/blackoutbg.jpg",
        "dialogues": [
            {"speaker": "narrator", "text": "..."},
            {"speaker": "narrator", "text": "..."},
            {"speaker": "narrator", "text": "There in the dimly lit chamber lies the repugnant “monster” lying insensately and quietly on the cold, hard cobblestone ground."}   
        ]
    },



    # SCENE 13: FIRST MEET AND SELF-INTRODUCTION
    {
        "background": "assets/chamber(nomonster).jpg", 
        "dialogues": [
            {"speaker": "narrator", "text": "Rather than revolting upon seeing such a vile creature, the knight advanced toward the monster and hastily checked for verbal and vital responses."}
        ]
    },
    # SCENE 14: WAKING UP THE MONSTER
    { 
        "background": "assets/chamber(nomonster).jpg",
        "character1": {
            "image": "assets/knightconverse.png",
            "color": (0, 136, 122)  # Teal color for character 1
        },
        "character2": {
            "image": "assets/humansurprised.png", 
            "pos": (0, 0),
            "color": (224, 102, 102) # Red color for character 2
        },
        "dialogues": [
            {"speaker": "character1", "text": "Hey, are you ok? Were you the one who screamed for help?"},
            {"speaker": "narrator", "text": "The knight’s motions wake the monster up, and they push the knight away while quickly reverting into the chamber’s corner, trembling."},
            {"speaker": "character2", "text": "WHO...Oh, someone actually came? You...you’re not here to do bad things, right? You don’t look like a felon or anything of that sort..."},
            {"speaker": "narrator", "text": "The monster struggles to enunciate properly, but the words are still audible. Still trembling in the corner, they wait patiently for the knight’s response."},
        ]
    },
    { 
        "background": "assets/chamber(nomonster).jpg",
        "character1": {
            "image": "assets/knightneutral.png",
            "color": (0, 136, 122)  # Teal color for character 1
        },
        "dialogues": [
            {"speaker": "character1", "text": "Absolutely not, I heard a scream while hunting nearby and thought someone might be in great danger, so I went on a lookout and found you lying dormant on the ground in this dungeon."},
        ]
    },
    { 
        "background": "assets/chamber(nomonster).jpg",
        "character2": {
            "image": "assets/humansad.png", 
            "pos":(0, 0),
            "color": (224, 102, 102) # Red color for character 2
        },
        "dialogues": [
            {"speaker": "narrator", "text": "The monster replied in a jabbering manner."},
            {"speaker": "character2", "text": "Don’t mind that...I just did that for...fun. Even if you were to stay, you would eventually be grossed out or give up entirely anyway."},
            {"speaker": "narrator", "text": "The knight chose to stay mute so as not to invoke any unnecessary hostility or potential fallouts at the moment."},
            {"speaker": "narrator", "text": "They then sit in silence, and the already gloomy and sorrowful atmosphere gets even heavier after that conversation."},

        ]
    },



    { 
        "background": "assets/blackoutbg.jpg",
        "dialogues": [
            {"speaker": "narrator", "text": "..."},
        ]
    },



    { 
        "background": "assets/chamber(nomonster).jpg",
        "character1": {
            "image": "assets/knightscratch.png",
            "color": (0, 136, 122)  # Teal color for character 1
        },
        "character2": {
            "image": "assets/humansad.png", 
            "pos": (0, 0),
            "color": (224, 102, 102) # Red color for character 2
        },
        "dialogues": [
            {"speaker": "character1", "text": "Why do you think so? You seem like a normal person to me."},
            {"speaker": "narrator", "text": "The knight asks in a confusing tone."},
            {"speaker": "character2", "text": "Because I am conspicuously a monster, and everyone detests nefarious and ugly creatures like me...So what can make you different from them?"},
            {"speaker": "narrator", "text": "The knight realizes that ordinary conversation will not resolve this internal and external conflict."},
            {"speaker": "narrator", "text": "Therefore, he came up with another strategy..."},
        ]
    },
    # SCENE 15: SELF-INTRO AND TALK
    { 
        "background": "assets/chamber(nomonster).jpg",
        "character1": {
            "image": "assets/knightconverse.png",
            "color": (0, 136, 122)  # Teal color for character 1
        },
        "character2": {
            "image": "assets/humansad.png", 
            "pos": (0, 0),
            "color": (224, 102, 102) # Red color for character 2
        },
        "dialogues": [
            {"speaker": "narrator", "text": "Noticing the vibe is off, the knight breaks the ice by abruptly asking for the person’s name."},
            {"speaker": "character1", "text": "What should I call you, may I ask?"},
            {"speaker": "narrator", "text": "The monster hesitates slightly before mumbling timidly."},
            {"speaker": "character2", "text": "Thia, please..."},
            {"speaker": "narrator", "text": "The knight sits down, criss-cross-apple-sauce, and let out a faint chuckle."}
        ]
        
    },
    { 
        "background": "assets/chamber(nomonster).jpg",
        "character1": {
            "image": "assets/knightscratch.png",
            "color": (0, 136, 122)  # Teal color for character 1
        },
        "dialogues": [
            {"speaker": "character1", "text": "Nice to meet you, Thea! Call me [...]."},
            
        ]
    },
    { 
        "background": "assets/chamber(nomonster).jpg",
        "character1": {
            "image": "assets/knightconverse.png",
            "color": (0, 136, 122)  # Teal color for character 1
        },
        "character2": {
            "image": "assets/humansurprised.png", 
            "pos": (0, 0),
            "color": (224, 102, 102) # Red color for character 2
        },
        "dialogues": [
            {"speaker": "narrator", "text": "The tension simmers down as the monster gets more and more comfortable with the knight, until eventually, the monster slowly wriggles out of the corner and closer towards the knight."},
            {"speaker": "character2", "text": "You’re not afraid of my appearance or manners?..."},
            {"speaker": "narrator", "text": "The monster asks without looking at the knight directly, but at his wounds from body-slamming through the wave of mobs."},
        ]

    },
    { 
        "background": "assets/chamber(nomonster).jpg",
        "character1": {
            "image": "assets/knightscratch.png",
            "color": (0, 136, 122)  # Teal color for character 1
        },
        "character2": {
            "image": "assets/humansad.png", 
            "pos": (0, 0),
            "color": (224, 102, 102) # Red color for character 2
        },
        "dialogues": [
            {"speaker": "character1", "text": "Why should I be? You don’t look like you are going to ravage me or anything, or maybe you do want to, and I just don’t know. I don’t judge books by their covers, so don’t ask me those questions because I don’t have a definitive answer."},
            {"speaker": "narrator", "text": "The monster’s eyes widen as they say."},
            {"speaker": "character2", "text": "That...I didn’t expect to hear that. Thank you for not running off, [...]."},
        ]
    },
    { 
        "background": "assets/chamber(nomonster).jpg",
        "character1": {
            "image": "assets/knightneutral.png",
            "color": (0, 136, 122)  # Teal color for character 1
        },
        "character2": {
            "image": "assets/monsneutral.png", 
            "pos": (0, 0),
            "color": (102, 0, 0) # Red color for character 2
        },
        "dialogues": [
            {"speaker": "character1", "text": "..."},
            {"speaker": "character1", "text": "Why were you trapped in the first place, Thea?"},
            {"speaker": "narrator", "text": "The knight asks quizzically."},
            {"speaker": "character2", "text": "THEY...told me that creatures like me are dirtying and vandalizing society, so I shouldn’t stay alive any longer..."},
            {"speaker": "narrator", "text": "The monster mumbles."},

        ]
    },
    { 
        "background": "assets/chamber(nomonster).jpg",
        "character1": {
            "image": "assets/knightneutral.png",
            "color": (0, 136, 122)  # Teal color for character 1
        },
        "dialogues": [
            {"speaker": "character1", "text": "So you ran here and locked yourself in?"},
            {"speaker": "narrator", "text": "The monster slightly nods, as if they don’t want to admit it."},
            {"speaker": "character1", "text": "Who are...'they' exactly?"},
    
        ]
    },
    { 
        "background": "assets/chamber(nomonster).jpg",
        "character2": {
            "image": "assets/monslookdown.png", 
            "pos": (0, 0),
            "color": (204, 0, 0) # Red color for character 2
        },
        "dialogues": [
            {"speaker": "narrator", "text": "A ray of light emanates from the monster’s eyes."},
            {"speaker": "character2", "text": "Your kind..."},
        ]
    },
    { 
        "background": "assets/chamber(nomonster).jpg",
        "character1": {
            "image": "assets/knightconverse.png",
            "color": (0, 136, 122)  # Teal color for character 1
        },
        "character2": {
            "image": "assets/humansad.png", 
            "pos": (0, 0),
            "color": (224, 102, 102) # Red color for character 2
        },
        "dialogues": [
            {"speaker": "narrator", "text": "The knight, unwavered by the hostility of the monster’s cynicism, asks tentatively"},
            {"speaker": "character1", "text": "So...Why didn’t you go on a riot and slaughter them all?"},
            {"speaker": "character2", "text": "I can’t...Then I’m the same as those people, maybe I’m already grotesque like them, and I didn’t realize…"},
            {"speaker": "narrator", "text": "The monster shakily replies, their voice quivering."},
            {"speaker": "character1", "text": "Then go on, kill them all if you think you’re gross like them, you have no reason to hold back if you’re one of them, start with m-"},
            {"speaker": "narrator", "text": "The knight urges."},
        ]
    },
    # SCENE 19: MONSTER SURRENDERING
    { 
        "background": "assets/chamber(nomonster).jpg",
        "character1": {
            "image": "assets/knightscratch.png",
            "color": (0, 136, 122)  # Teal color for character 1
        },
        "character2": {
            "image": "assets/mons360.png", 
            "pos": (0, 0),
            "color": (224, 102, 102) # Red color for character 2
        },
        "dialogues": [
            {"speaker": "character2", "text": "Please stop, I’m already exhausted with life, why did you even come here just to leave? I...don’t need help anymore, you can go and pity someone else."},
            {"speaker": "narrator", "text": "The monster interrupts the knight’s sentence, lying back down on the ground."},
            {"speaker": "character2", "text": "I was about to give up on everything anyway..."},
            {"speaker": "narrator", "text": "The monster sussurates."},
            {"speaker": "narrator", "text": "..."},
            {"speaker": "narrator", "text": "After a brief moment of silence, the knight says,"},
            {"speaker": "character1", "text": "I don’t think you’re abnormal or gross...Think of them as your signature or specialty rather than blemishes or flaws."}
        ]
    },
    { 
        "background": "assets/chamber(nomonster).jpg",
        "character1": {
            "image": "assets/knightconverse.png",
            "color": (0, 136, 122)  # Teal color for character 1
        },
        "dialogues": [
            {"speaker": "character1", "text": "You breathing, moving, blinking, drinking, and masticating food constitutes life itself, Thea."},
            {"speaker": "narrator", "text": "The knight gets closer to the soullessly unbothered monster lying on the ground."},
            {"speaker": "narrator", "text": "The monster remains still. However, the knight’s determination to revive this self-proclaimed “monster” hasn’t died down, more fiery even."},           
        ]
    },



    { 
        "background": "assets/blackoutbg.jpg",
        "dialogues": [
            {"speaker": "narrator", "text": "..."},
            {"speaker": "narrator", "text": "..."},
        ]
    },


    
    { 
        "background": "assets/chamber(nomonster).jpg", 
        "character1": {
            "image": "assets/knightscratch.png",
            "color": (0, 136, 122)  # Teal color for character 1
        },
        "character2": {
            "image": "assets/monshuman.png", 
            "pos": (0, 0),
            "color": (224, 102, 102) # Red color for character 2
        },
        "dialogues": [
            {"speaker": "narrator", "text": "The knight towers over the monster and gently nudges them, asking."},
            {"speaker": "character1", "text": "How about we live together once you’re out of here, Thea?..."},
            {"speaker": "character2", "text": "You love burdening yourself, don’t you, big guy?"},
            {"speaker": "narrator", "text": "The monster is unconvinced by the knight’s offer."},
        ]
    },
    { 
        "background": "assets/chamber(nomonster).jpg",
        "character1": {
            "image": "assets/knightconverse.png",
            "color": (0, 136, 122)  # Teal color for character 1
        },
        "character2": {
            "image": "assets/humansad.png", 
            "pos": (0, 0),
            "color": (224, 102, 102) # Red color for character 2
        },
        "dialogues": [
            {"speaker": "character1", "text": "No...I want to help you get better, please accept my request, Thea."},
            {"speaker": "narrator", "text": "The knight insists."},
            {"speaker": "character2", "text": "Why...are you helping a stranger like me? You’re wasting your time, [...]"},
        ]
    },
    { 
        "background": "assets/chamber(nomonster).jpg",
        "character1": {
            "image": "assets/hit&exhaust.png",
            "color": (0, 136, 122)  # Teal color for character 1
        },
        "dialogues": [
            {"speaker": "character1", "text": "Because I believe you deserve better, you’re just living your life and being yourself, why do you have to be punished for being yourself?"},           
        ]
    },
    # SCENE 21: LETTING OUT FEELINGS
    { 
        "background": "assets/lamentrain.png", 
        "dialogues": [
            {"speaker": "narrator", "text": "The monster’s body vibrates slightly before springing up to hug the knight while sobbing out all of their frustration and depression."},
            {"speaker": "narrator", "text": "The knight immediately embraced the monster while patting them on the back as a means of consolation."},
            {"speaker": "narrator", "text": "The monster’s tears wet the knight’s shirt, but he doesn’t mind it at all."},
            {"speaker": "narrator", "text": "The atmosphere was heavy at first, but brightened up in the aftermath of a rain."},
            {"speaker": "narrator", "text": "Indeed, there was a rain in the dungeon, a rain whose constituents were chronic lamentation and sorrow."},
        ]
    },



    { 
        "background": "assets/blackoutbg.jpg",
        "dialogues": [
            {"speaker": "narrator", "text": "It all ends now..."},
            {"speaker": "narrator", "text": "..."},
            {"speaker": "narrator", "text": "..."},
            {"speaker": "narrator", "text": "..."}
        ]
    },
    


    # SCENE SECOND TO LAST: LEAVING THE DUNGEON
    { 
        "background": "assets/chamber(nomonster).jpg",
        "character1": {
            "image": "assets/knightreachingout.png",
            "color": (0, 136, 122)  # Teal color for character 1
        },
        "character2": {
            "image": "assets/humansmile.png", 
            "pos": (0, 0),
            "color": (224, 102, 102),
        },
        "dialogues": [
            {"speaker": "character1", "text": "So, shall we go, Thea?"},
            {"speaker": "narrator", "text": "The knight reaches out his hand to the person sitting on the ground."},
            {"speaker": "character2", "text": "Yeah, let’s get out of this place...together!"},
        ]    
    },
    { 
        "background": "assets/chamber(nomonster).jpg",
        "character1": {
            "image": "assets/knightconverse.png",
            "color": (0, 136, 122),
        },
        "character2": {
            "image": "assets/humansurprised.png", 
            "pos": (0, 0),
            "color": (224, 102, 102),
        },
        "dialogues": [
            {"speaker": "narrator", "text": "The person takes the knight’s hand and tries to gain momentum to stand up."},
            {"speaker": "character2", "text": "Woooah!"},
            {"speaker": "narrator", "text": "The knight cushions the wobbly person with his arm and says,"},
            {"speaker": "character1", "text": "You haven’t walked in a while, no?"},
        ]
    },
    { 
        "background": "assets/cushion.png",
        "character1": {
            "image": "assets/knightreachingout.png",
            "color": (0, 136, 122),
        },
        "character2": {
            "image": "assets/humanshy.png", 
            "pos": (0, 0),
            "color": (224, 102, 102),
        },
        "dialogues": [
            {"speaker": "narrator", "text": "..."},
            {"speaker": "character2", "text": "Yeah, sorry, I can’t even walk properly..."},
            {"speaker": "narrator", "text": "The person flusters."},
            {"speaker": "character1", "text": "Are you fine with me carrying you, Thea?"},
            {"speaker": "character2", "text": "What? Won’t that make the journey out more strenuous for you? I can still crawl..."}
        ]
    },
    { 
        "background": "assets/cushion.png",
        "character1": {
            "image": "assets/knightconverse.png",
            "color": (0, 136, 122),
        },
        "character2": {
            "image": "assets/humansurprised.png", 
            "pos": (0, 0),
            "color": (224, 102, 102),
        },
        "dialogues": [
            {"speaker": "character1", "text": "No, no you won’t crawl."},
            {"speaker": "narrator", "text": "Then the knight picks the person up and runs to the exit in a heartbeat."},
            {"speaker": "character2", "text": "Hey, wait!..."}
        ]
    },



    { 
        "background": "assets/blackoutbg.jpg",
        "dialogues": [
            {"speaker": "narrator", "text": "Surprisingly, there were no abnormal monsters obstructing them on their way out."},
            {"speaker": "narrator", "text": "As if they had evaporated out of existence...As if they never even existed in the first place."}
        ]
    },



    # FINAL CUTSCENE
    { 
        "background": "assets/finalscene.png", 
        "character1": {
            "image": "assets/knightnoticing.png",
            "color": (0, 136, 122)
        },
        "character2": {
            "image": "assets/humanshy.png", 
            "pos": (0, 0),
            "color": (224, 102, 102),
        },
        "dialogues": [
            {"speaker": "character1", "text": "Are you cold?"},
            {"speaker": "character2", "text": "No, you’re warm..."},
            {"speaker": "character1", "text": "Do you like living in a cottage, Thea?"},
        ]
    },
    { 
        "background": "assets/finalscene.png",
        "character2": {
            "image": "assets/humansmile.png",
            "pos": (0, 0),
            "color": (224, 102, 102),
        },
        "dialogues": [
            {"speaker": "character2", "text": "I like living anywhere that has you in it."},
            {"speaker": "narrator", "text": "And they live together happily until the end of time. The end."}
        ]
    }
]






# GOING THROUGH ALL THE SCENES
def play_scenes():
    global player_name
    scenes_copy = copy.deepcopy(scenes)
    font = pygame.font.Font("NightmarePills.ttf", 18)
    narrator_color = (255, 255, 255)  # Default narrator color
    for i, scene in enumerate(scenes_copy):
        #RESIZE THE BGS
        background_surf = pygame.image.load(scene["background"]).convert()
        background_surf = pygame.transform.scale(background_surf, (800, 500))
        
        # CREATE A DIALOGUE BOX
        box_width, box_height = 700, 120
        box_x = (800 - box_width) // 2
        box_y = 370

        # Load character 1 if present
        char1_surf = char1_pos = char1_color = None
        if "character1" in scene:
            char1 = scene["character1"]
            # Resize the character sprite to (200, 200) pixels (adjust as needed)
            original_surf = pygame.image.load(char1["image"]).convert_alpha()
            char1_surf = pygame.transform.scale(original_surf, (750, 470))
            # Place character to the left of the dialogue box
            char1_pos = (box_x, box_y - 340)  # 10px gap, adjust as needed
            char1_color = char1["color"]

        # Load character 2 if present
        char2_surf = char2_pos = char2_color = None
        if "character2" in scene:
            char2 = scene["character2"]
            char2_surf = pygame.image.load(char2["image"]).convert_alpha()
            char2_pos = char2["pos"]
            char2_color = char2["color"]

        # Narrator color (can be global or per scene)
        if "narrator" in scene and "color" in scene["narrator"]:
            narrator_color = scene["narrator"]["color"]


        dialogue_system = DialogueSystem(scene["dialogues"])
        scene_running = True
        while scene_running:
            screen.blit(background_surf, (0, 0))

            current_dialogue = dialogue_system.get_current_dialogue()
            # Pick color based on speaker, fallback to white
            if isinstance(current_dialogue, dict):
                speaker = current_dialogue.get("speaker")
                if speaker == "character1" and char1_color:
                    color = char1_color
                elif speaker == "character2" and char2_color:
                    color = char2_color
                elif speaker == "narrator":
                    color = narrator_color
                else:
                    color = (255, 255, 255)
                text = current_dialogue.get("text", "")
            else:
                color = (255, 255, 255)
                text = current_dialogue

            # Only draw characters if the speaker is NOT the narrator
            if isinstance(current_dialogue, dict) and speaker != "narrator":
                if speaker == "character1" and char1_surf:
                    screen.blit(char1_surf, char1_pos)
                if speaker == "character2" and char2_surf:
                    screen.blit(char2_surf, char2_pos)
           
            
            #ASK FOR PLAYER NAME AT [...] PRESENT
            if ( 
                isinstance(current_dialogue, dict)
                and "Call me [...]" in current_dialogue.get("text", "")
                and player_name == ""
            ):
                player_name = get_player_name(screen, font)

            # REPLACE [...] WITH PLAYER_NAME FOR ALL DIALOGUES
            if isinstance(current_dialogue, dict):
                text = current_dialogue.get("text", "")
                text = text.replace("[...]", player_name)
            else:
                text = current_dialogue


            # Now draw the dialogue box ON TOP of the characters
            dialogue_box = pygame.Surface((box_width, box_height), pygame.SRCALPHA)
            dialogue_box.fill((0, 0, 0, 180))  # Semi-transparent black
            screen.blit(dialogue_box, (box_x, box_y))

            # Draw wrapped text inside the dialogue box
            text_rect = pygame.Rect(box_x + 20, box_y + 10, box_width - 40, box_height - 20)
            draw_text_wrapped(screen, text, font, color, text_rect, font.get_height() + 4)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dialogue_system.advance()
            if dialogue_system.current_index >= len(scene["dialogues"]):
                scene_running = False  # Exit the scene loop

            pygame.display.update()
            clock.tick(60)



# MAIN MENU
def menu():
    while True:
        screen.blit(background_surf, (0, 0))
        mouse_pos = pygame.mouse.get_pos()
        
        # GAME TITLE
        title_text = pygame.font.Font("Frozito.ttf", 60).render("Monster and Knight", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(400, 100))
        screen.blit(title_text, title_rect)

        # CONTINUE BUTTON
        continue_button = Button((300, 200), "Continue", pygame.font.Font("Frozito.ttf", 40), (255, 255, 255), (255, 255, 255))
        continue_button.draw(screen)

        # CREDITS BUTTON
        credits_button = Button((300, 265), "Credits", pygame.font.Font("Frozito.ttf", 40), (255, 255, 255), (255, 255, 255))
        credits_button.draw(screen)
            
        # QUIT BUTTON
        quit_button = Button((300, 335), "Quit", pygame.font.Font("Frozito.ttf", 40), (255, 255, 255), (255, 255, 255))
        quit_button.draw(screen)
        if quit_button.check_for_input(mouse_pos) and pygame.mouse.get_pressed()[0]:
            pygame.quit()
            exit()

        for button in [continue_button, credits_button, quit_button]:
            button.update(mouse_pos)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continue_button.check_for_input(mouse_pos):
                    play_scenes()
                if credits_button.check_for_input(mouse_pos):
                    show_credits()
                if quit_button.check_for_input(mouse_pos):
                    pygame.quit()
                    exit()
        pygame.display.update()
        clock.tick(60)

def show_credits():
    while True:
        screen.fill((0, 0, 25))  # Clear the screen for credits
        credits_text1 = pygame.font.Font("Frozito.ttf", 40).render("Story and characters by me", True, (255, 255, 255))
        credits_rect1 = credits_text1.get_rect(center=(400, 200))

        credits_text2 = pygame.font.Font("Frozito.ttf", 40).render("Illustration by Thu", True, (255, 255, 255))
        credits_rect2 = credits_text2.get_rect(center=(400, 250))

        user_instruction = pygame.font.Font("Frozito.ttf", 30).render("Click to return to the menu", True, (0, 0, 100))
        user_instruction_rect = user_instruction.get_rect(center=(400, 300))

        social_text1 = pygame.font.Font("Frozito.ttf", 20).render("Facebook Anh Thu Nguyen Viet as illustrator", True, (0, 0, 200))
        social_rect1 = social_text1.get_rect(bottomleft=(10, 480))

        social_text2 = pygame.font.Font("Frozito.ttf", 20).render("Facebook Dux Thinh Tran as storywriter and programmer", True, (0, 0, 200))
        social_rect2 = social_text2.get_rect(bottomleft=(10, 500))


        screen.blit(credits_text1, credits_rect1)
        screen.blit(credits_text2, credits_rect2)
        screen.blit(user_instruction, user_instruction_rect)
        screen.blit(social_text1, social_rect1)
        screen.blit(social_text2, social_rect2)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return
        clock.tick(60)

def draw_text_wrapped(surface, text, font, color, rect, line_height):
    words = text.split(' ')
    lines = []
    current_line = ""
    for word in words:
        test_line = current_line + word + " "
        test_surface = font.render(test_line, True, color)
        if test_surface.get_width() > rect.width and current_line != "":
            lines.append(current_line)
            current_line = word + " "
        else:
            current_line = test_line
    lines.append(current_line)

    y = rect.top
    for line in lines:
        line_surface = font.render(line, True, color)
        surface.blit(line_surface, (rect.left, y))
        y += line_height

menu()



