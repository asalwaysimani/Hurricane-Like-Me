
define xyz = Character("Eileen", who_color = "#c8ffc8")

# Note: The code will not work with characters that were created
#       with the "kind" argument other than the default, None.

# Note: Contacts should be defined early.

init -5 python:

    # This is so that Contacts will be in the
    # same order everytime we open the phone.
    from collections import OrderedDict

    # Phone. This class includes all the methods
    # for controlling all the phone functions.
    class Phone():

        def __init__(self):

            # Keys are strings, names of Character objects.
            # Values are Contacts created based on Character objects.
            self.phonebook = OrderedDict()

        def addContact(self, character, **contactProperties):
            
            if not type(character) == store.ADVCharacter:
                raise Exception("addContact() was not given a Character object, or not one created with \"kind = None\".")

            if character in self.phonebook.keys():
                raise Exception("That Character is already in Contacts.")

            # Creates a new Contact object and maps it to this Character from both sides.
            self.phonebook[character] = Contact(character, **contactProperties)

            print("Phone: {} has been added into Contacts.".format(character.name))

        def sendMessage(self, contact, character, what, say = True):
            
            if not character in self.phonebook.keys():

                ### TO BE UPDATED
                if type(character) == store.ADVCharacter:
                    raise Exception("Trying to send a message to a Character that hasn't been added into Contacts.")
                else:
                    raise Exception("sendMessage was not Given a Character object.")

            self.phonebook[contact].messageSent(character, what, say = say)

        def showConversation(self, character):

            if not character in self.phonebook.keys():

                ### TO BE UPDATED ??? MAYBE ???
                if type(character) == store.ADVCharacter:
                    raise Exception("Trying to show messages with a Character that hasn't been added into Contacts.")
                else:
                    raise Exception("showConversation was not Given a Character object.")

            renpy.invoke_in_new_context( renpy.call_screen , "phoneConvoScreen", character )

        def getContact(self, character):

            if not character in self.phonebook.keys():
                raise Exception("That Character is not in the phonebook.")

            return self.phonebook[character]


    # A record about a person and their messages.
    # These are only found inside a Phonebook object.
    class Contact():
        
        def __init__(self, character, name = None, nameColor = None, textColor = None, image = None, messageSound = None):

            # Character from which this Contact was created.
            self.boundCharacter = character

            # By default, the phone will use given Character's name.
            # However, this can be changed by giving the "name" argument.
            # Useful for giving nicknames, for example:
            # You can then send messages to the "Boyfriend" character, but
            # the phone can view it as messages from "Honey <3"
            self.name = character.name if name == None else name

            self.nameColor = nameColor
            self.textColor = textColor

            # Image of the contact in the phone book.
            # Should be of pre-given dimensions.
            self.image = image

            # Sound that plays when receiving a message from
            # this contact.
            self.messageSound = messageSound

            # Stores messages with this Contact.
            self.messages = []

        def showPhoneConversation(self, character):

            renpy.invoke_in_new_context( renpy.call_screen , "phoneConvoScreen", character )


        def messageSent(self, character, what, sound = True, say = True):

            self.messages.append( [character, what] )

            if say:

                self.showPhoneConversation( self )

                # I would have to modify the Say screen and redirect it to 
                # phoneConvoScreen that way, which I do not want.
                #
                # renpy.say(character, what)

            # if sound:
            #     renpy.play.sound()


    ###############################################################

# Has to be default, otherwise it will not participate in rollback.
default phone = Phone()

screen phoneConvoScreen( contact ):

    default phoneScrollLock = False

    # It is a button because of the phoneScroll lock.
    # Otherwise it would be a frame.
    button:
        xsize 619
        ysize 1080
        align (0.5, 0.5)
        padding (98, 151, 49, 158)
        background "gui/Hurricane_Like_Me/Handphone/Handphone.png"

        hovered SetScreenVariable("phoneScrollLock", True)
        unhovered SetScreenVariable("phoneScrollLock", False)
        action NullAction()

        viewport:
            align (0.5, 0.5)
            # x is the total width minus the padding
            xsize 517
            # y is calculated from bottom padding, vbox spacing and textbox height
            ysize 730
            yinitial 1.0

            mousewheel True
                
            vbox:
                spacing 8

                for message in contact.messages:

                    # textbox
                    frame:
                        xsize 473
                        ysize 115 
                        background "gui/Hurricane_Like_Me/Handphone/eirtextbox.png"

                        # who
                        text message[0].name:
                            size 22
                            pos (120, 2)
                            color phone.phonebook[ message[0] ].nameColor

                        # what area
                        frame:
                            background None # Solid("f80")
                            pos (112, 35)
                            xsize 348
                            ysize 66

                            # what
                            text message[1]:
                                size 26
                                color phone.phonebook[ message[0] ].textColor


            # for message in phone.phonebook[who].messages:

            #     hbox:
            #         spacing 20
            #         text message[0]
            #         text message[1]

    # Moves forward
    key "dismiss" action Return()
    # Rolls back
    if not phoneScrollLock:
        key "rollback" action Rollback()