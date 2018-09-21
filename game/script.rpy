# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define FC = Character("Crush", color="#FFFFFF")
define MC = Character("MC", color="#AEFFFF")
define CF = Character("ChildFriend", color="#99FFFF")
define TC = Character("TeacherClub", color="#55FFFF")

#image logo = "renpy logo.png"
#image eileen happy = "eileen_happy_blue_dress.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg bedroom

    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    FC "You've created a new Ren'Py game."

    FC "Once you add a story, pictures, and music, you can release it to the world!"

    scene bg bedroom

    "Eating breakfast to go to school. Monologue here"

    scene bg roadToSchool

    "on my way to school"

    show CF happy greet

    "choices: join childhood friend"

    menu:

        "Go greet FC":
            jump FC

        "Continue walking to school with CF":
            jump CF

    label FC:

        show FC happy smile

        "talk with FC"

        jump merge

    label CF:

        show CF happy smile

        "talk with CF"

        jump merge

    label merge:

    scene bg lockers

    "choices: "

    menu:

        "Place the letter in the shoebox":
            jump lockersPlace

        "Do it later":
            jump lockersLater

        "Decide against it":
            jump lockersNah

    scene bg homeroom

    "choices: "

    menu:

        "Place the letter in the shoebox":
            jump lockersPlace

        "Do it later":
            jump lockersLater


    scene bg classroom1





    scene bg cafeteria

    "choices: "

    menu:

        "Look for FC":
            jump lockersPlace

        "Decide against it":
            jump lockersNah



    scene bg clubRoom

    "choices: "

    menu:

        "Talk to CT":
            jump lockersPlace

        "Decide against it":
            jump lockersNah

    scene bg confessCherryBlossom

    "confession Talk"

    scene bg credits

    "neat"

    # This ends the game.

    return
