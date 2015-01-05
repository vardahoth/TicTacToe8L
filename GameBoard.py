
class GameBoardMaster:
    def CreateNewGameBoard(self):
        return [None] * 9 # [None, None, None, None, None, None, None, None, None]
        
    def GetGameBoardUnusedSlots(self, gameBoard):
        availablePicks = []
        availableGameBoardIndex = 1
        for slot in gameBoard:
            if slot == None:
                availablePicks.append(availableGameBoardIndex)
                availableGameBoardIndex += 1
            else:
                availableGameBoardIndex += 1
        return availablePicks
        
    def UpdateGameBoard(self, gameBoard, playerMove, playerXorO):
        """ (list[9elements], int, bool) -> 1 element changed(None to Bool) in list
        
        Function updates an element in the gameboard list from [None] to [True or False]
        Element chosen is based on the (int(arg2) - 1) given.
        Value of True or False is based on the (bool(arg3)) given.
        
        (arg1) Must be the gameBoard list[9elements]
        (arg2) Must be an integer between 1 - 9
        (arg3) Must be a boolean of True or False
        
        >>>UpdateGameBoard([True, None, True, False, None, None, False, None, None], 2, True)
        [True, True, True, False, None, None, False, None, None]
        
        >>>UpdateGameBoard([True, None, True, False, None, None, False, None, None], 8, False)
        [True, None, True, False, None, None, False, False, None]
        """
        gameBoard[int(playerMove) - 1] = playerXorO # (playerMove = (int(range(1 - 9)))), (playerXorO = (True) or (False)) :: Updates element(None) in gameBoard[playerMove - 1] with (element(True)) or (element(False))
        return gameBoard # [slot, slot, slot, slot, slot, slot, slot, slot, slot] : slot = (None) or (True) or (False)
        
    def CheckBoard(self, gameBoard, playerXorO):
        """ (list[9elements], int) -> 'string'
        
        Function checks the game board to see if there is:
        A winner
        gameBoard is full
        or gameboard is still able to play
        
        (arg1) Must be the gameBoard list[9elements]
        (arg2) Must be a boolean of True or False
        
        >>>CheckBoard([True, False, True, False, True, True, False, True, False], True)
        'Full'
        
        >>>CheckBoard([False, False, False, True, None, None, False, None, None], False)
        'Winner'
        
        >>>CheckBoard([True, None, True, False, None, None, False, None, None], False)
        'Playable'
        """
        if self.CheckWinningBoard(gameBoard, playerXorO) == True:
            return 'Winner'
        elif self.CheckFullBoard(gameBoard) == True:
            return 'Full'
        return 'Playable'
        
    def CheckWinningBoard(self, gameBoard, playerXorO):
        """ (list[9elements], int) -> bool
        
        Function checks the game board to see if there is a winner
        Function returns True if the winner is found.
        Function returns False if the winner is not found.
        
        (arg1) Must be the gameBoard list[9elements]
        (arg2) Must be a boolean of True or False
        
        >>>CheckWinningBoard([True, False, True, False, True, True, True, False, False], True)
        True
        
        >>>CheckWinningBoard([False, False, False, True, None, None, False, None, None], False)
        True
        
        >>>CheckWinningBoard([True, None, True, False, None, None, False, None, None], False)
        False
        """
        winningGameBoardRows = [
            gameBoard[0:3],
            gameBoard[3:6],
            gameBoard[6:9],
            [gameBoard[0], gameBoard[3], gameBoard[6]],
            [gameBoard[1], gameBoard[4], gameBoard[7]],
            [gameBoard[2], gameBoard[5], gameBoard[8]],
            [gameBoard[0], gameBoard[4], gameBoard[8]],
            [gameBoard[2], gameBoard[4], gameBoard[6]],
        ]
        for list in winningGameBoardRows:
            XorORowCounter = 0
            for element in list:
                if element == playerXorO:
                    XorORowCounter += 1
                if XorORowCounter == 3:
                    return True # Player winner has been found
        return False # Player winner has not yet been found
        
    def CheckFullBoard(self, gameBoard):
        """ (list[9elements]) -> bool
        
        Function checks the game board to see if there is a winner
        Function returns True if the an element(None) is not found in the gameboard.
        Function returns True if the an element(None) is found in the gameboard.
        
        (arg1) Must be the gameBoard list[9elements]
        
        >>>CheckFullBoard([True, False, True, False, True, True, False, True, False], True)
        True
        
        >>>CheckFullBoard([True, None, True, False, None, None, False, None, None], False)
        False
        """
        if None in gameBoard:
            return False # gameBoared list[] still has 1 or more elements(None)
        return True # There is no more elements(None) in the gameBoard list[]
        