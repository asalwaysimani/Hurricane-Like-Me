
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

        def sendMessage(self, character, what, say = True):
            
            if not character in self.phonebook.keys():

                if type(character) == store.ADVCharacter:
                    raise Exception("Trying to send a message to a Character that hasn't been added into Contacts.")
                else:
                    raise Exception("sendMessage was not Given a Character object.")

            self.phonebook[character].messageSent(character, what, say = say)


    # A record about a person and their messages.
    # These are only found inside a Phonebook object.
    class Contact():
        
        def __init__(self, character, name = None, image = None, messageSound = None):

            # Character from which this Contact was created.
            self.boundCharacter = character

            # By default, the phone will use given Character's name.
            # However, this can be changed by giving the "name" argument.
            # Useful for giving nicknames, for example:
            # You can then send messages to the "Boyfriend" character, but
            # the phone can view it as messages from "Honey <3"
            self.name = character.name if name == None else name

            # Image of the contact in the phone book.
            # Should be of pre-given dimensions.
            self.image = image

            # Sound that plays when receiving a message from
            # this contact.
            self.messageSound = messageSound

            # Stores messages with this Contact.
            self.messages = []

        def messageSent(self, who, what, sound = True, say = True):

            self.messages.append( [who, what] )

            if say:
                renpy.say(who, what)

            # if sound:
            #     renpy.play.sound()


    ###############################################################

# Has to be default, otherwise it will not participate in rollback.
default phone = Phone()