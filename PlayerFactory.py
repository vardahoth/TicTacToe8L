import re

class PlayerFactory:
    def __init__(self, interface): # Edited, doc strings needs updating
        """ (None) -> Global Variables
        
        Initializes global variables for class PlayerFactor
        """
        self.interface = interface
        
        self.setPlayerTypes = {
            0 : self.SetPlayersCompVsComp,
            1 : self.SetPlayersHumanVsComp,
            2 : self.SetPlayersHumanVsHuman,
        }
        
    def GetPlayerTypes(self, numPlayers):
        """ (int) -> ['string1', 'string2']
        
        Returns the two types of players as computer or human.
        
        (arg1) Must be an integer with a range(0 - 2)
        
        >>>GetPlayerTypes(0)
        self.setPlayerTypes[0]()
        return ['playerOneComputer', 'playerTwoComputer']
        
        >>>GetPlayerTypes(1)
        self.setPlayerTypes[1]()
        return ['playerOneHuman', 'playerTwoComputer']
        
        >>>GetPlayerTypes(2)
        self.setPlayerTypes[2]()
        return ['playerOneHuman', 'playerTwoHuman']
        
        """
        players = self.setPlayerTypes[numPlayers]()
        return players # (['playerOneComputer', 'playerTwoComputer']) or (['playerOneHuman', 'playerTwoComputer']) or (['playerOneHuman', 'playerTwoHuman'])
    
    def SetPlayersCompVsComp(self):
        return ['playerOneComputer', 'playerTwoComputer']
    
    def SetPlayersHumanVsComp(self):
        return ['playerOneHuman', 'playerTwoComputer']
    
    def SetPlayersHumanVsHuman(self):
        return ['playerOneHuman', 'playerTwoHuman']
        
    def SetPlayerOneX(self, players): # Edited, doc strings needs updating
        """ (None) -> True
        
        If the game is set so it is Computer vs Computer,
        Function will return True, which assigns Computer Player 1 as X.
        
        (arg1) Must be an integer with a range(0 - 2)
        
        >>>SetPlayerOneX()
        True
        
        """
        if players == ['playerOneComputer', 'playerTwoComputer']:
            return True
        else:
            playerOneX = self.interface.GetPlayerOneX() # (True) or (False)
            return playerOneX
    
    def SetPlayerTwoX(self, playerOneX, players): # Edited, doc strings needs updating
        """ (bool) -> bool
        
        Returns the player one X as True, if and only if the argument player one is False.
        or
        Returns the player one X as False, if and only if the argument player one is True.
        
        >>>SetPlayerTwoX(True)
        False
        
        >>>SetPlayerTwoX(False)
        True
        """
        if players == ['playerOneComputer', 'playerTwoComputer']:
            return False
        elif playerOneX == True:
            self.interface.DisplayPlayersXandO(playerOneX, players) # (None)
            return False
        elif playerOneX == False:
            self.interface.DisplayPlayersXandO(playerOneX, players) # (None)
            return True
            
    def SetFirstPlayerType(self, players): # Edited, doc strings needs updating
        """ (['string1', 'string2']) -> 'string1'
        
        Function returns the first string from a list of two strings.
        It is recommended to use this function only for "Computer vs Computer",
        Since there is another function(GetFirstPlayerType(players)) that interacts with the interface,
        and gets player input to set the firstPlayerType
        
        >>>SetFirstPlayerType(['playerOneComputer', 'playerTwoComputer'])
        'playerOneComputer'
        """
        if players == ['playerOneComputer', 'playerTwoComputer']:
            return players[0] # (str('playerOneComputer'))
        else:
            firstPlayerType = self.interface.GetFirstPlayerType(players) # (str('playerOneHuman')) or (str('playerTwoComputer')) or (str('playerTwoHuman'))
            return firstPlayerType
        
    def SetSecondPlayerType(self, firstPlayerType, players): # Edited, doc strings needs updating
        """ ('string', ['string1', 'string2']) -> 'string'
        
        Function returns the second player, based upon who the first player is.
        
        (arg1) Must be the string that is equal to what the firstPlayerType is set to.
        For example:
            'playerOneHuman'
            'playerTwoComputer'
            'playerTwoHuman'
        (arg2) arg1 string must be in the list of arg2
        
        >>>SetSecondPlayerType(playerTwoComputer, ['playerOneHuman', 'playerTwoComputer'])
        'playerOneHuman'
        """
        if players == ['playerOneComputer', 'playerTwoComputer']:
            return players[1]
        elif firstPlayerType == players[0]:
            self.interface.DisplayFirstAndSecondPlayers(firstPlayerType, players[1]) # (None)
            return players[1] # (str('playerOneHuman')) or (str('playerTwoComputer')) or (str('playerTwoHuman'))
        elif firstPlayerType == players[1]:
            self.interface.DisplayFirstAndSecondPlayers(firstPlayerType, players[0]) # (None)
            return players[0] # (str('playerOneHuman')) or (str('playerTwoComputer')) or (str('playerTwoHuman'))
            
    def SetPlayerConfig(self, playerType, playerOneX, playerTwoX):
        if re.search('.*One.*', playerType):
            return [playerType, playerOneX] # ['playerOneComputer', True] or ['playerOneComputer', False] or ['playerOneHuman', True] or ['playerOneHuman', False]
        elif re.search('.*Two.*', playerType):
            return [playerType, playerTwoX] # ['playerTwoComputer', True] or ['playerTwoComputer', False] or ['playerTwoHuman', True] or ['playerTwoHuman', False]
            