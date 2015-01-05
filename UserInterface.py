from ConsoleInterface import *

class ConsoleInterface:
    def DisplayWelcome(self):
        """ (None) -> bool
        
        Function is responsible for displaying the welcome message to the user.
        Function gives the user the option to continue or quit.
        Returns False if the user quits, or True if the user continues.
        
        >>>DisplayWelcome()
        True
        False
        """
        return ConsoleInputMessages().DisplayWelcomeWithInput() # (True) or (False)
        
    def GetNumPlayers(self):
        """ (None) -> int or 'string'
        
        Function returns the number of players (0 - 2) as an integer based on user input.
        or
        Function returns 'R' or 'Q' (for restart or quit) based on user input
        
        >>>GetNumPlayers()
        0
        1
        2
        'R'
        'Q'
        """
        return ConsoleInputMessages().SetNumPlayers() # (range(int(0 - 2))) or (str('R' or 'Q')) based on user input
    
    def DisplayAndGetPlayerTypes(self, players):
        """ (list['string1', 'string2']) -> "string"
        
        
        Displays to the user what if the players are human players or computer players.
        Returns a string showing the "typeOfPlayer vs typeOfPlayer".
        
        ['string1', 'string2'] Must be one of the following:
        ['playerOneComputer', 'playerTwoComputer']
        ['playerOneHuman', 'playerTwoComputer']
        ['playerOneHuman', 'playerTwoHuman']
        
        >>>DisplayAndGetPlayerTypes(['playerOneComputer', 'playerTwoComputer'])
        "Computer vs Computer"
        
        >>>DisplayAndGetPlayerTypes(['playerOneHuman', 'playerTwoComputer'])
        "Player vs Computer"
        
        >>>DisplayAndGetPlayerTypes(['playerOneHuman', 'playerTwoHuman'])
        "Player vs Player"
        """
        return ConsoleInputMessages().PrintandSetPlayerTypes(players) # (str("Computer vs Computer")) or (str("Player vs Computer")) or (str("Player vs Player")
    
    def GetPlayerOneX(self):
        """ (None) -> bool 
        
        Returns True if and only if the user for player 1 wants to be X.
        Returns False if and only if the user for player 1 wants to be O.
        
        >>>GetPlayerOneX()
        True
        False
        """
        return ConsoleInputMessages().SetPlayerOneX() # (True) or (False)
        
    def DisplayPlayersXandO(self, playerOneX, Players):
        """ (bool, list['string1', 'string2']) -> None 
        
        Displays which typeOfPlayer is X and which typeOfPlayer is O.
        
        ['string1', 'string2'] Must be one of the following:
        ['playerOneComputer', 'playerTwoComputer']
        ['playerOneHuman', 'playerTwoComputer']
        ['playerOneHuman', 'playerTwoHuman']
        
        >>>DisplayPlayersXandO(True, ['playerOneComputer', 'playerTwoComputer'])
        None
        """
        return ConsoleInputMessages().PrintPlayersXandO(playerOneX, Players) # (None)
    
    def GetFirstPlayerType(self, players):
        """ (list['string1', 'string2']) -> 'string'
        
        Function returns the first player as playerType
        based on user input from a list of 2 playerTypes in the arg.
        
        ['string1', 'string2'] Must be one of the following:
        ['playerOneHuman', 'playerTwoComputer']
        ['playerOneHuman', 'playerTwoHuman']
        
        >>>GetFirstPlayerType(['playerOneHuman', 'playerTwoComputer'])
        'playerOneHuman'
        'playerTwoComputer'
        
        >>>GetFirstPlayerType(['playerOneHuman', 'playerTwoHuman'])
        'playerOneHuman'
        'playerTwoHuman'
        """
        return ConsoleInputMessages().SetFirstPlayerType(players) # (str('playerOneHuman')) or (str('playerTwoComputer')) or (str('playerTwoHuman')) based on user input
    
    def DisplayFirstAndSecondPlayers(self, firstPlayerType, secondPlayerType):
        """ ('string1', 'string2') -> None
        
        Function returns displays to the user the which playerType is the first player
        and which playerType is the second player
        
        ('string1', 'string2') Must be the order of ('firstPlayerType', 'secondPlayerType') of the following:
        'playerOneComputer'
        'playerTwoComputer'
        'playerOneHuman'
        'playerTwoHuman'
        
        >>>DisplayFirstAndSecondPlayers('playerOneComputer', 'playerTwoComputer')
        None
        
        >>>DisplayFirstAndSecondPlayers('playerTwoComputer', 'playerOneComputer')
        None
        """
        return ConsoleInputMessages().PrintFirstAndSecondPlayers(firstPlayerType, secondPlayerType) # (None)
    
    def ConfirmGameSettings(self, playerVsPlayerMatchConfig, firstPlayer, secondPlayer):
        """ ('string', list['string', bool], list['string', bool]) -> 'string' or bool(True)
        
        Function displays settings of the game,
        then asks user to confirm the settings of the game to start game, restart game, or quit.
        
        (arg1) Must be the one of the following strings:
        'Computer vs Computer'
        'Player vs Computer'
        'Player vs Player'
        
        (arg2) Must resemble the first player with one of the following lists('playerType', playerIsX):
        ['playerOneComputer', 'True']
        ['playerOneComputer', 'False']
        ['playerTwoComputer', 'True']
        ['playerTwoComputer', 'False']
        ['playerOneHuman', 'True']
        ['playerOneHuman', 'False']
        ['playerTwoHuman', 'True']
        ['playerTwoHuman', 'False']
        
        (arg3) Must resemble the second player with one of the following lists('playerType', playerIsX):
        ['playerOneComputer', 'True']
        ['playerOneComputer', 'False']
        ['playerTwoComputer', 'True']
        ['playerTwoComputer', 'False']
        ['playerOneHuman', 'True']
        ['playerOneHuman', 'False']
        ['playerTwoHuman', 'True']
        ['playerTwoHuman', 'False']
        
        >>>ConfirmGameSettings('Computer vs Computer', ['playerOneComputer', 'True'], ['playerTwoComputer', 'False'])
        True
        'R'
        'Q'
        
        >>>ConfirmGameSettings('Player vs Computer', ['playerOneHuman', 'False'], ['playerTwoComputer', 'True'])
        True
        'R'
        'Q'
        """
        return ConsoleInputMessages().ConfirmGameSettings(playerVsPlayerMatchConfig, firstPlayer, secondPlayer) # (str('Q' or 'R')) or (True) based on user input
        
    def DisplayBoard(self, gameBoard):
        """ (list[9elements]) -> None
        
        Function displays what the current tic tac toe board looks like to the user.
        
        Each element of list[element, element, element, element, element, element, element, element, element]
        must be one of the following:
        'True'
        'False'
        'None'
        
        >>>DisplayBoard([None, None, None, None, None, None, None, None, None])
        None
        
        >>>DisplayBoard([None, False, None, False, True, None, None, True, None])
        None
        """
        return ConsoleOutputMessages().PrintGameBoard(gameBoard) # (None)
        
    def DisplayAskPlayerMove(self, playerTypeMove, otherPlayerType, availablePicks):
        """ ('sring1', 'string2', list[elements]) -> None
        
        Function displays to the user who's turn it is to move.
        The display is based upon what type of players are playing, and which players turn it is.
        Function also displays a list of the available moves left to choose from.
        
        (arg1) Must be one of the following strings of the players turn to move:
        'playerOneComputer'
        'playerTwoComputer'
        'playerOneHuman'
        'playerTwoHuman'
        
        (arg2) Must be one of the following strings of the players turn not to move:
        'playerOneComputer'
        'playerTwoComputer'
        'playerOneHuman'
        'playerTwoHuman'
        
        (arg3) Must be a list of integers resembling None in the list(gameBoard[9elements] + 1)
        for example:
        if gameboard[None, False, None, False, True, None, None, True, None]:
            availablePicks[1, 3, 6, 7, 9]
            
        >>>DisplayAskPlayerMove('playerOneComputer', 'playerTwoComputer', availablePicks[1, 3, 6, 7, 9])
        None
        
        >>>DisplayAskPlayerMove('playerTwoComputer', 'playerOneHuman', availablePicks[2, 3, 4, 5, 6, 7, 9])
        None
        """
        return ConsoleOutputMessages().PrintAskPlayerMove(playerTypeMove, otherPlayerType, availablePicks) # (None)
        
    def GetPlayerToMove(self, gameBoard):
        """ (list[9elements]) -> int or 'string'
        
        Function returns input from user.
        Function must return a integer between 1-9, or a string of ('R' or 'Q')
        
        GetPlayerToMove(gameBoard[None, False, None, False, True, None, None, True, None])
        1
        3
        6
        7
        9
        'R'
        'Q'
        """
        return ConsoleInputMessages().SetPlayerMove(gameBoard) # (range(int(1 - 9))) or (str('R' or 'Q')) based on user input
        
    def DisplayInvalidSlotError(self, availablePicks, playerMove):
        """ (list[elements], int) -> None
        
        Function displays error message (move out of range(1 - 9)) to the user of the move he/she picked,
        and the available slots he/she should have pick from
        
        DisplayInvalidSlotError(availablePicks[1, 3, 6, 7, 9], 10)
        None
        """
        return ConsoleOutputMessages().PrintInvalidSlotError(availablePicks, playerMove) #None
    
    def DisplaySlotTakenError(self, availablePicks, playerMove):
        """ (list[elements], int) -> None
        
        Function displays error message (slot already taken) to the user of the move he/she picked,
        and the available slots he/she should have pick from
        
        DisplaySlotTakenError(availablePicks[1, 3, 6, 7, 9], 2)
        None
        """
        return ConsoleOutputMessages().PrintSlotTakenError(availablePicks, playerMove) #None
    
    def DisplayGameDraw(self):
        """ (None) -> None
        
        Function displays a message to the user showing the game has ended in a draw.
        
        DisplayGameDraw()
        None
        """
        return ConsoleOutputMessages().PrintGameDraw() #None
        
    def DisplayGameWinner(self, winner, loser):
        """ ('string1', 'string2') -> None
        
        Function displays a message to the user showing the winner of the game.
        
        (arg1) Must be a string with the playerType who won the game
        (arg2) Must be a string with the playerType who lost the game
        
        DisplayGameWinner('playerOneHuman', 'playerTwoComputer')
        None
        """
        return ConsoleOutputMessages().PrintGameWinner(winner, loser) #None
    
    def AskUserPlayAgain(self):
        """ (None) -> None
        
        Function displays a message to the user asking them if they want to play again.
        Based on user input, function returns True if the user wants to play again,
        or function returns False if the user does not want to play again.
        
        AskUserPlayAgain()
        None
        """
        return ConsoleInputMessages().MessageUserPlayAgain() # True or False based on user input
    
class WindowInterface:
    def DisplayWelcome(self):
        """ (None) -> bool
        
        Function is responsible for displaying the welcome message to the user.
        Function gives the user the option to continue or quit.
        Returns False if the user quits, or True if the user continues.
        
        >>>DisplayWelcome()
        True
        False
        """
        raise NotImplementedError('This interface has not yet been implemented') # (True) or (False)
        
    def GetNumPlayers(self):
        """ (None) -> int or 'string'
        
        Function returns the number of players (0 - 2) as an integer based on user input.
        or
        Function returns 'R' or 'Q' (for restart or quit) based on user input
        
        >>>GetNumPlayers()
        0
        1
        2
        'R'
        'Q'
        """
        raise NotImplementedError('This interface has not yet been implemented') # (range(int(0 - 2))) or (str('R' or 'Q')) based on user input
    
    def DisplayAndGetPlayerTypes(self, players):
        """ (list['string1', 'string2']) -> "string"
        
        
        Displays to the user what if the players are human players or computer players.
        Returns a string showing the "typeOfPlayer vs typeOfPlayer".
        
        ['string1', 'string2'] Must be one of the following:
        ['playerOneComputer', 'playerTwoComputer']
        ['playerOneHuman', 'playerTwoComputer']
        ['playerOneHuman', 'playerTwoHuman']
        
        >>>DisplayAndGetPlayerTypes(['playerOneComputer', 'playerTwoComputer'])
        "Computer vs Computer"
        
        >>>DisplayAndGetPlayerTypes(['playerOneHuman', 'playerTwoComputer'])
        "Player vs Computer"
        
        >>>DisplayAndGetPlayerTypes(['playerOneHuman', 'playerTwoHuman'])
        "Player vs Player"
        """
        raise NotImplementedError('This interface has not yet been implemented') # (str("Computer vs Computer")) or (str("Player vs Computer")) or (str("Player vs Player")
    
    def GetPlayerOneX(self):
        """ (None) -> bool 
        
        Returns True if and only if the user for player 1 wants to be X.
        Returns False if and only if the user for player 1 wants to be O.
        
        >>>GetPlayerOneX()
        True
        False
        """
        raise NotImplementedError('This interface has not yet been implemented') # (True) or (False)
        
    def DisplayPlayersXandO(self, playerOneX, Players):
        """ (bool, list['string1', 'string2']) -> None 
        
        Displays which typeOfPlayer is X and which typeOfPlayer is O.
        
        ['string1', 'string2'] Must be one of the following:
        ['playerOneComputer', 'playerTwoComputer']
        ['playerOneHuman', 'playerTwoComputer']
        ['playerOneHuman', 'playerTwoHuman']
        
        >>>DisplayPlayersXandO(True, ['playerOneComputer', 'playerTwoComputer'])
        None
        """
        raise NotImplementedError('This interface has not yet been implemented') # (None)
    
    def GetFirstPlayerType(self, players):
        """ (list['string1', 'string2']) -> 'string'
        
        Function returns the first player as playerType
        based on user input from a list of 2 playerTypes in the arg.
        
        ['string1', 'string2'] Must be one of the following:
        ['playerOneHuman', 'playerTwoComputer']
        ['playerOneHuman', 'playerTwoHuman']
        
        >>>GetFirstPlayerType(['playerOneHuman', 'playerTwoComputer'])
        'playerOneHuman'
        'playerTwoComputer'
        
        >>>GetFirstPlayerType(['playerOneHuman', 'playerTwoHuman'])
        'playerOneHuman'
        'playerTwoHuman'
        """
        raise NotImplementedError('This interface has not yet been implemented') # (str('playerOneHuman')) or (str('playerTwoComputer')) or (str('playerTwoHuman')) based on user input
    
    def DisplayFirstAndSecondPlayers(self, firstPlayerType, secondPlayerType):
        """ ('string1', 'string2') -> None
        
        Function returns displays to the user the which playerType is the first player
        and which playerType is the second player
        
        ('string1', 'string2') Must be the order of ('firstPlayerType', 'secondPlayerType') of the following:
        'playerOneComputer'
        'playerTwoComputer'
        'playerOneHuman'
        'playerTwoHuman'
        
        >>>DisplayFirstAndSecondPlayers('playerOneComputer', 'playerTwoComputer')
        None
        
        >>>DisplayFirstAndSecondPlayers('playerTwoComputer', 'playerOneComputer')
        None
        """
        raise NotImplementedError('This interface has not yet been implemented') # (None)
    
    def ConfirmGameSettings(self, playerVsPlayerType, firstPlayer, secondPlayer):
        """ ('string', list['string', bool], list['string', bool]) -> 'string' or bool(True)
        
        Function displays settings of the game,
        then asks user to confirm the settings of the game to start game, restart game, or quit.
        
        (arg1) Must be the one of the following strings:
        'Computer vs Computer'
        'Player vs Computer'
        'Player vs Player'
        
        (arg2) Must resemble the first player with one of the following lists('playerType', playerIsX):
        ['playerOneComputer', 'True']
        ['playerOneComputer', 'False']
        ['playerTwoComputer', 'True']
        ['playerTwoComputer', 'False']
        ['playerOneHuman', 'True']
        ['playerOneHuman', 'False']
        ['playerTwoHuman', 'True']
        ['playerTwoHuman', 'False']
        
        (arg3) Must resemble the second player with one of the following lists('playerType', playerIsX):
        ['playerOneComputer', 'True']
        ['playerOneComputer', 'False']
        ['playerTwoComputer', 'True']
        ['playerTwoComputer', 'False']
        ['playerOneHuman', 'True']
        ['playerOneHuman', 'False']
        ['playerTwoHuman', 'True']
        ['playerTwoHuman', 'False']
        
        >>>ConfirmGameSettings('Computer vs Computer', ['playerOneComputer', 'True'], ['playerTwoComputer', 'False'])
        True
        'R'
        'Q'
        
        >>>ConfirmGameSettings('Player vs Computer', ['playerOneHuman', 'False'], ['playerTwoComputer', 'True'])
        True
        'R'
        'Q'
        """
        raise NotImplementedError('This interface has not yet been implemented') # (str('Q' or 'R')) or (True) based on user input
        
    def DisplayBoard(self, gameBoard):
        """ (list[9elements]) -> None
        
        Function displays what the current tic tac toe board looks like to the user.
        
        Each element of list[element, element, element, element, element, element, element, element, element]
        must be one of the following:
        'True'
        'False'
        'None'
        
        >>>DisplayBoard([None, None, None, None, None, None, None, None, None])
        None
        
        >>>DisplayBoard([None, False, None, False, True, None, None, True, None])
        None
        """
        raise NotImplementedError('This interface has not yet been implemented') # (None)
        
    def DisplayAskPlayerMove(self, playerTypeMove, otherPlayerType, availablePicks):
        """ ('sring1', 'string2', list[elements]) -> None
        
        Function displays to the user who's turn it is to move.
        The display is based upon what type of players are playing, and which players turn it is.
        Function also displays a list of the available moves left to choose from.
        
        (arg1) Must be one of the following strings of the players turn to move:
        'playerOneComputer'
        'playerTwoComputer'
        'playerOneHuman'
        'playerTwoHuman'
        
        (arg2) Must be one of the following strings of the players turn not to move:
        'playerOneComputer'
        'playerTwoComputer'
        'playerOneHuman'
        'playerTwoHuman'
        
        (arg3) Must be a list of integers resembling None in the list(gameBoard[9elements] + 1)
        for example:
        if gameboard[None, False, None, False, True, None, None, True, None]:
            availablePicks[1, 3, 6, 7, 9]
            
        >>>DisplayAskPlayerMove('playerOneComputer', 'playerTwoComputer', availablePicks[1, 3, 6, 7, 9])
        None
        
        >>>DisplayAskPlayerMove('playerTwoComputer', 'playerOneHuman', availablePicks[2, 3, 4, 5, 6, 7, 9])
        None
        """
        raise NotImplementedError('This interface has not yet been implemented') # (None)
        
    def GetPlayerToMove(self, gameBoard):
        """ (list[9elements]) -> int or 'string'
        
        Function returns input from user.
        Function must return a integer between 1-9, or a string of ('R' or 'Q')
        
        GetPlayerToMove(gameBoard[None, False, None, False, True, None, None, True, None])
        1
        3
        6
        7
        9
        'R'
        'Q'
        """
        raise NotImplementedError('This interface has not yet been implemented') # (range(int(1 - 9))) or (str('R' or 'Q')) based on user input
        
    def DisplayInvalidSlotError(self, availablePicks, playerMove):
        """ (list[elements], int) -> None
        
        Function displays error message (move out of range(1 - 9)) to the user of the move he/she picked,
        and the available slots he/she should have pick from
        
        DisplayInvalidSlotError(availablePicks[1, 3, 6, 7, 9], 10)
        None
        """
        raise NotImplementedError('This interface has not yet been implemented') #None
    
    def DisplaySlotTakenError(self, availablePicks, playerMove):
        """ (list[elements], int) -> None
        
        Function displays error message (slot already taken) to the user of the move he/she picked,
        and the available slots he/she should have pick from
        
        DisplaySlotTakenError(availablePicks[1, 3, 6, 7, 9], 2)
        None
        """
        raise NotImplementedError('This interface has not yet been implemented') #None
    
    def DisplayGameDraw(self):
        """ (None) -> None
        
        Function displays a message to the user showing the game has ended in a draw.
        
        DisplayGameDraw()
        None
        """
        raise NotImplementedError('This interface has not yet been implemented') #None
        
    def DisplayGameWinner(self, winner, loser):
        """ ('string1', 'string2') -> None
        
        Function displays a message to the user showing the winner of the game.
        
        (arg1) Must be a string with the playerType who won the game
        (arg2) Must be a string with the playerType who lost the game
        
        DisplayGameWinner('playerOneHuman', 'playerTwoComputer')
        None
        """
        raise NotImplementedError('This interface has not yet been implemented') #None
    
    def AskUserPlayAgain(self):
        """ (None) -> None
        
        Function displays a message to the user asking them if they want to play again.
        Based on user input, function returns True if the user wants to play again,
        or function returns False if the user does not want to play again.
        
        AskUserPlayAgain()
        None
        """
        raise NotImplementedError('This interface has not yet been implemented') # True or False based on user input
        
class WebInterface:
    def DisplayWelcome(self):
        """ (None) -> bool
        
        Function is responsible for displaying the welcome message to the user.
        Function gives the user the option to continue or quit.
        Returns False if the user quits, or True if the user continues.
        
        >>>DisplayWelcome()
        True
        False
        """
        raise NotImplementedError('This interface has not yet been implemented') # (True) or (False)
        
    def GetNumPlayers(self):
        """ (None) -> int or 'string'
        
        Function returns the number of players (0 - 2) as an integer based on user input.
        or
        Function returns 'R' or 'Q' (for restart or quit) based on user input
        
        >>>GetNumPlayers()
        0
        1
        2
        'R'
        'Q'
        """
        raise NotImplementedError('This interface has not yet been implemented') # (range(int(0 - 2))) or (str('R' or 'Q')) based on user input
    
    def DisplayAndGetPlayerTypes(self, players):
        """ (list['string1', 'string2']) -> "string"
        
        
        Displays to the user what if the players are human players or computer players.
        Returns a string showing the "typeOfPlayer vs typeOfPlayer".
        
        ['string1', 'string2'] Must be one of the following:
        ['playerOneComputer', 'playerTwoComputer']
        ['playerOneHuman', 'playerTwoComputer']
        ['playerOneHuman', 'playerTwoHuman']
        
        >>>DisplayAndGetPlayerTypes(['playerOneComputer', 'playerTwoComputer'])
        "Computer vs Computer"
        
        >>>DisplayAndGetPlayerTypes(['playerOneHuman', 'playerTwoComputer'])
        "Player vs Computer"
        
        >>>DisplayAndGetPlayerTypes(['playerOneHuman', 'playerTwoHuman'])
        "Player vs Player"
        """
        raise NotImplementedError('This interface has not yet been implemented') # (str("Computer vs Computer")) or (str("Player vs Computer")) or (str("Player vs Player")
    
    def GetPlayerOneX(self):
        """ (None) -> bool 
        
        Returns True if and only if the user for player 1 wants to be X.
        Returns False if and only if the user for player 1 wants to be O.
        
        >>>GetPlayerOneX()
        True
        False
        """
        raise NotImplementedError('This interface has not yet been implemented') # (True) or (False)
        
    def DisplayPlayersXandO(self, playerOneX, Players):
        """ (bool, list['string1', 'string2']) -> None 
        
        Displays which typeOfPlayer is X and which typeOfPlayer is O.
        
        ['string1', 'string2'] Must be one of the following:
        ['playerOneComputer', 'playerTwoComputer']
        ['playerOneHuman', 'playerTwoComputer']
        ['playerOneHuman', 'playerTwoHuman']
        
        >>>DisplayPlayersXandO(True, ['playerOneComputer', 'playerTwoComputer'])
        None
        """
        raise NotImplementedError('This interface has not yet been implemented') # (None)
    
    def GetFirstPlayerType(self, players):
        """ (list['string1', 'string2']) -> 'string'
        
        Function returns the first player as playerType
        based on user input from a list of 2 playerTypes in the arg.
        
        ['string1', 'string2'] Must be one of the following:
        ['playerOneHuman', 'playerTwoComputer']
        ['playerOneHuman', 'playerTwoHuman']
        
        >>>GetFirstPlayerType(['playerOneHuman', 'playerTwoComputer'])
        'playerOneHuman'
        'playerTwoComputer'
        
        >>>GetFirstPlayerType(['playerOneHuman', 'playerTwoHuman'])
        'playerOneHuman'
        'playerTwoHuman'
        """
        raise NotImplementedError('This interface has not yet been implemented') # (str('playerOneHuman')) or (str('playerTwoComputer')) or (str('playerTwoHuman')) based on user input
    
    def DisplayFirstAndSecondPlayers(self, firstPlayerType, secondPlayerType):
        """ ('string1', 'string2') -> None
        
        Function returns displays to the user the which playerType is the first player
        and which playerType is the second player
        
        ('string1', 'string2') Must be the order of ('firstPlayerType', 'secondPlayerType') of the following:
        'playerOneComputer'
        'playerTwoComputer'
        'playerOneHuman'
        'playerTwoHuman'
        
        >>>DisplayFirstAndSecondPlayers('playerOneComputer', 'playerTwoComputer')
        None
        
        >>>DisplayFirstAndSecondPlayers('playerTwoComputer', 'playerOneComputer')
        None
        """
        raise NotImplementedError('This interface has not yet been implemented') # (None)
    
    def ConfirmGameSettings(self, playerVsPlayerType, firstPlayer, secondPlayer):
        """ ('string', list['string', bool], list['string', bool]) -> 'string' or bool(True)
        
        Function displays settings of the game,
        then asks user to confirm the settings of the game to start game, restart game, or quit.
        
        (arg1) Must be the one of the following strings:
        'Computer vs Computer'
        'Player vs Computer'
        'Player vs Player'
        
        (arg2) Must resemble the first player with one of the following lists('playerType', playerIsX):
        ['playerOneComputer', 'True']
        ['playerOneComputer', 'False']
        ['playerTwoComputer', 'True']
        ['playerTwoComputer', 'False']
        ['playerOneHuman', 'True']
        ['playerOneHuman', 'False']
        ['playerTwoHuman', 'True']
        ['playerTwoHuman', 'False']
        
        (arg3) Must resemble the second player with one of the following lists('playerType', playerIsX):
        ['playerOneComputer', 'True']
        ['playerOneComputer', 'False']
        ['playerTwoComputer', 'True']
        ['playerTwoComputer', 'False']
        ['playerOneHuman', 'True']
        ['playerOneHuman', 'False']
        ['playerTwoHuman', 'True']
        ['playerTwoHuman', 'False']
        
        >>>ConfirmGameSettings('Computer vs Computer', ['playerOneComputer', 'True'], ['playerTwoComputer', 'False'])
        True
        'R'
        'Q'
        
        >>>ConfirmGameSettings('Player vs Computer', ['playerOneHuman', 'False'], ['playerTwoComputer', 'True'])
        True
        'R'
        'Q'
        """
        raise NotImplementedError('This interface has not yet been implemented') # (str('Q' or 'R')) or (True) based on user input
        
    def DisplayBoard(self, gameBoard):
        """ (list[9elements]) -> None
        
        Function displays what the current tic tac toe board looks like to the user.
        
        Each element of list[element, element, element, element, element, element, element, element, element]
        must be one of the following:
        'True'
        'False'
        'None'
        
        >>>DisplayBoard([None, None, None, None, None, None, None, None, None])
        None
        
        >>>DisplayBoard([None, False, None, False, True, None, None, True, None])
        None
        """
        raise NotImplementedError('This interface has not yet been implemented') # (None)
        
    def DisplayAskPlayerMove(self, playerTypeMove, otherPlayerType, availablePicks):
        """ ('sring1', 'string2', list[elements]) -> None
        
        Function displays to the user who's turn it is to move.
        The display is based upon what type of players are playing, and which players turn it is.
        Function also displays a list of the available moves left to choose from.
        
        (arg1) Must be one of the following strings of the players turn to move:
        'playerOneComputer'
        'playerTwoComputer'
        'playerOneHuman'
        'playerTwoHuman'
        
        (arg2) Must be one of the following strings of the players turn not to move:
        'playerOneComputer'
        'playerTwoComputer'
        'playerOneHuman'
        'playerTwoHuman'
        
        (arg3) Must be a list of integers resembling None in the list(gameBoard[9elements] + 1)
        for example:
        if gameboard[None, False, None, False, True, None, None, True, None]:
            availablePicks[1, 3, 6, 7, 9]
            
        >>>DisplayAskPlayerMove('playerOneComputer', 'playerTwoComputer', availablePicks[1, 3, 6, 7, 9])
        None
        
        >>>DisplayAskPlayerMove('playerTwoComputer', 'playerOneHuman', availablePicks[2, 3, 4, 5, 6, 7, 9])
        None
        """
        raise NotImplementedError('This interface has not yet been implemented') # (None)
        
    def GetPlayerToMove(self, gameBoard):
        """ (list[9elements]) -> int or 'string'
        
        Function returns input from user.
        Function must return a integer between 1-9, or a string of ('R' or 'Q')
        
        GetPlayerToMove(gameBoard[None, False, None, False, True, None, None, True, None])
        1
        3
        6
        7
        9
        'R'
        'Q'
        """
        raise NotImplementedError('This interface has not yet been implemented') # (range(int(1 - 9))) or (str('R' or 'Q')) based on user input
        
    def DisplayInvalidSlotError(self, availablePicks, playerMove):
        """ (list[elements], int) -> None
        
        Function displays error message (move out of range(1 - 9)) to the user of the move he/she picked,
        and the available slots he/she should have pick from
        
        DisplayInvalidSlotError(availablePicks[1, 3, 6, 7, 9], 10)
        None
        """
        raise NotImplementedError('This interface has not yet been implemented') #None
    
    def DisplaySlotTakenError(self, availablePicks, playerMove):
        """ (list[elements], int) -> None
        
        Function displays error message (slot already taken) to the user of the move he/she picked,
        and the available slots he/she should have pick from
        
        DisplaySlotTakenError(availablePicks[1, 3, 6, 7, 9], 2)
        None
        """
        raise NotImplementedError('This interface has not yet been implemented') #None
    
    def DisplayGameDraw(self):
        """ (None) -> None
        
        Function displays a message to the user showing the game has ended in a draw.
        
        DisplayGameDraw()
        None
        """
        raise NotImplementedError('This interface has not yet been implemented') #None
        
    def DisplayGameWinner(self, winner, loser):
        """ ('string1', 'string2') -> None
        
        Function displays a message to the user showing the winner of the game.
        
        (arg1) Must be a string with the playerType who won the game
        (arg2) Must be a string with the playerType who lost the game
        
        DisplayGameWinner('playerOneHuman', 'playerTwoComputer')
        None
        """
        raise NotImplementedError('This interface has not yet been implemented') #None
    
    def AskUserPlayAgain(self):
        """ (None) -> None
        
        Function displays a message to the user asking them if they want to play again.
        Based on user input, function returns True if the user wants to play again,
        or function returns False if the user does not want to play again.
        
        AskUserPlayAgain()
        None
        """
        raise NotImplementedError('This interface has not yet been implemented') # True or False based on user input
        