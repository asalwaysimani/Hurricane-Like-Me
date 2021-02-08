
define xyz = Character("Eileen", who_color = "#c8ffc8")

# Note: The code will not work with characters that were created
#       with the "kind" argument other than None, the default.

init -5 python:

    # Phone. This class includes all the methods
    # for controlling all the phone functions.
    class Phone():

        def __init__(self):

            self.phonebook = Phonebook()


        def addContact(self, character):
            
            if not type(character) == store.ADVCharacter:
                raise Exception("addContact() was not given a Character object, or not one created with \"kind = None\".")

            self.phonebook.addContact(character)

        def sendMessage(self, character, what):
            pass


    # Point of the phonebook as a standalone class
    # is to make a list that can be indexed by 
    # Ren'Py Characters for easier functionality.
    # This is only found inside a Phone object.
    class Phonebook():

        def __init__():

            self.

        def addContact(character):
            
            if character.name


    # A record about a person and their messages.
    # These are only found inside a Phonebook object.
    class Contact():
        
        def __init__(self):
            pass


    ###############################################################

    phone = Phone()