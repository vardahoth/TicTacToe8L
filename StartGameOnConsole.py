import os
from Controller import Controller
from UserInterface import ConsoleInterface

class StartGameOnConsole:
    def Main(self):
        """ (None) -> bool
        
        Starts game on windows cmd console.
        If crllr object returns False, the game will restart.
        if ctrllr object returns True, the game will exit.
        
        >>>Main()
        None
        """
        finished = False
        os.system('cls')
        interface = ConsoleInterface() # Class
        ctrllr = Controller(interface) # Object
        while finished == False:
            finished = ctrllr.StartGame() # (True) or (False)

#Starts the program
StartGameOnConsole().Main() # None
