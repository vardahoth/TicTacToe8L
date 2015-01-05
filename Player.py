import time
import random
import re
from GameBoard import GameBoardMaster

class Player:
    def __init__(self, PlayerInterface):
        """ (interfaceTypeClass) -> interfaceTypeObject
        
        Used for initializing the type of interface used as an object
        
        >>>self.PlayerInterface.DisplayAskPlayerMove(playerMovingStatus[0], otherPlayerStatus[0], availablePicks)
        Displays the message asking the user to move for the playerType with a list of available moves,
        on the interfaceTypeObject being used.
        
        >>>self.PlayerInterface.GetPlayerToMove(gameBoard, firstPlayer, secondPlayer)
        Talks to the interfaceTypeObject which will be responsible
        for getting the user input and returning the move to make on the game board
        """
        self.PlayerInterface = PlayerInterface
    
    def PlayerMove(self, gameBoard, playerMovingStatus, otherPlayerStatus):
        """ (list[9elements], playerMovingStatus['string', bool], otherPlayerStatus['string', bool]) -> int or 'string'
        
        Function determines if the moving player is (human or computer) and (X or O)
        If player is human, Function will call HumanPlayerMove function.
        If player is computer, function will call ComputerPlayerMove function.
        Based on human player input, the function can return an int with a range(1 - 9),
        or return a string('Restart' or 'Quit') for restarting the game, or quitting the game.
        The computer player should ONLY return an int with a range (1 - 9).
        
        If this function returns an int,
        it should only return an int pointing to the element(None) on the gameboard(list[int - 1])
        (arg1) should be the current status of the gameboard list[]
        (arg2) should be the status of the player who is moving.
        For Example: ['playerOneHuman', True] or ['playerTwoComputer', False]
        (arg3) should be the status of the other player who is not moving.
        for example: ['playerTwoComputer', False] or ['playerOneHuman', True]
        
        >>>PlayerMove([None, None, True, False, True, None, False, None, None], ['playerOneHuman', True], ['playerTwoComputer', False])
        1
        2
        6
        8
        9
        'Restart'
        'Quit'
        
        >>>PlayerMove([None, False, None, True, None, True, None, None, False], ['playerTwoComputer', True], ['playerOneHuman', False])
        1
        3
        5
        7
        8
        """
        if re.search('.*Human.*', playerMovingStatus[0]):
            playerMove = self.HumanPlayerMove(gameBoard, playerMovingStatus, otherPlayerStatus) # int(1, 2, 3, 4, 5, 6, 7, 8, or 9), or str('Quit', or 'Restart') based on player input
        elif re.search('.*Computer.*', playerMovingStatus[0]):
            playerMove = self.ComputerPlayerMove(gameBoard, playerMovingStatus, otherPlayerStatus) # int(1, 2, 3, 4, 5, 6, 7, 8, or 9)
        return playerMove # int(1, 2, 3, 4, 5, 6, 7, 8, or 9), or str('Quit', or 'Restart') based on player input
        
    def HumanPlayerMove(self, gameBoard, playerMovingStatus, otherPlayerStatus):
        """ (list[9elements], playerMovingStatus['string', bool], otherPlayerStatus['string', bool]) -> int or 'string'
        
        Function can return an int with a range(1 - 9),
        or return a string('Restart' or 'Quit') for restarting the game, or quitting the game.
        
        If this function returns an int,
        and it should only return an int pointing to the element(None) on the gameboard(list[int - 1])
        (arg1) should be the current status of the gameboard list[]
        (arg2) should be the status of the player who is moving.
        (arg2[0]) should contain 'Human' somewhere in the string
        For Example: ['playerOneHuman', True] or ['playerTwoHuman', False]
        (arg3) should be the status of the other player who is not moving.
        for example: ['playerTwoComputer', False] or ['playerOneHuman', True]
        
        >>>HumanPlayerMove([None, None, True, False, True, None, False, None, None], ['playerOneHuman', True], ['playerTwoComputer', False])
        1
        2
        6
        8
        9
        'Restart'
        'Quit'
        """
        playerQuitGame = 'Q'
        playerRestartGame = 'R'
        quitGame = 'Quit'
        restartGame = 'Restart'
        availablePicks = GameBoardMaster().GetGameBoardUnusedSlots(gameBoard) # int([availableSlots++]) :: availableSlots++ = elements(can be more than 1) with the value of None
        self.PlayerInterface.DisplayAskPlayerMove(playerMovingStatus[0], otherPlayerStatus[0], availablePicks) # (None)
        playerMove = self.PlayerInterface.GetPlayerToMove(gameBoard) # int(1, 2, 3, 4, 5, 6, 7, 8, or 9), or str('Quit', or 'Restart') based on player input
        while playerMove not in availablePicks and playerMove != playerQuitGame and playerMove != playerRestartGame:
            if playerMove not in range(1, 10):
                self.PlayerInterface.DisplayInvalidSlotError(availablePicks, playerMove) # (None)
                playerMove = self.PlayerInterface.GetPlayerToMove(gameBoard) # int(1, 2, 3, 4, 5, 6, 7, 8, or 9), or str('Quit', or 'Restart') based on player input
            elif playerMove in range(1, 10):
                self.PlayerInterface.DisplaySlotTakenError(availablePicks, playerMove) # (None)
                playerMove = self.PlayerInterface.GetPlayerToMove(gameBoard) # int(1, 2, 3, 4, 5, 6, 7, 8, or 9), or str('Quit', or 'Restart') based on player input
        if playerMove == playerQuitGame:
            return quitGame # str('Quit')
        elif playerMove == playerRestartGame:
            return restartGame # str('Restart')
        return playerMove # int(1, 2, 3, 4, 5, 6, 7, 8, or 9) based on player input
        
    def ComputerPlayerMove(self, gameBoard, playerMovingStatus, otherPlayerStatus):
        """ (list[9elements], playerMovingStatus['string', bool], otherPlayerStatus['string', bool]) -> int or 'string'
        
        Function can return an int with a range(1 - 9).
        
        If this function returns an int,
        and it should only return an int pointing to the element(None) on the gameboard(list[int - 1])
        (arg1) should be the current status of the gameboard list[]
        (arg2) should be the status of the player who is moving.
        (arg2[0]) should contain 'Computer' somewhere in the string
        For Example: ['playerOneComputer', True] or ['playerTwoComputer', False]
        (arg3) should be the status of the other player who is not moving.
        for example: ['playerOneHuman', False] or ['playerTwoComputer', True]
        
        >>>ComputerPlayerMove([True, False, None, None, False, None, None, None, True], ['playerTwoComputer', True], ['playerOneHuman', False])
        3
        4
        6
        7
        8
        """
        computerDecisionTime = random.randint(1, 3) # int(range(1 - 3))
        availablePicks = GameBoardMaster().GetGameBoardUnusedSlots(gameBoard) # int([availableSlots++]) :: availableSlots++ = elements(can be more than 1) with the value of None
        self.PlayerInterface.DisplayAskPlayerMove(playerMovingStatus[0], otherPlayerStatus[0], availablePicks) # (None)
        time.sleep(computerDecisionTime) # (None)
        computerMove = random.choice(availablePicks) # int(random(1, 2, 3, 4, 5, 6, 7, 8, or 9))
        return computerMove # int(random(1, 2, 3, 4, 5, 6, 7, 8, or 9))
        