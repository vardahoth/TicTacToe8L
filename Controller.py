from PlayerFactory import PlayerFactory
from GameBoard import GameBoardMaster
from Player import Player
from UserInterface import *

class Controller:
    def __init__(self, interface): # Edited, doc strings needs updating
        """ (interfaceTypeObject) -> Global Variables
        
        Used for initializing objects for sequencial uses.
        
        >>>self.interface.DisplayWelcome()
        Displays the welcome message based on the type of interface being used.
        
        >>>self.Player.PlayerMove(gameBoard, firstPlayer, secondPlayer)
        Depending on the type of interface instantiated, the Player object
        will pass a message to the user interface asking to move on the interfaceType
        """
        self.interface = interface
        self.Player = Player(interface)
        self.PlayerFactory = PlayerFactory(interface)
        
    def StartGame(self):
        """ (None) -> bool
        
        Starts game on the interface it is handed to.
        
        >>>Main()
        True
        False
        """
        
        #Display welcome message with option to continue or quit
        if self.interface.DisplayWelcome() == False:
            return True
        
        #Get number of players, restart, or quit
        numPlayers = self.interface.GetNumPlayers() # (range(int(0 - 2))) or (str('R' or 'Q')) based on user input
        if numPlayers == 'R':
            return False
        elif numPlayers == 'Q':
            return True
        elif numPlayers == 0 or numPlayers == 1 or numPlayers == 2:
            players = self.PlayerFactory.GetPlayerTypes(numPlayers) # (['playerOneComputer', 'playerTwoComputer']) or (['playerOneHuman', 'playerTwoComputer']) or (['playerOneHuman', 'playerTwoHuman'])
        
        #Display to user the types of players
        playerVsPlayerMatchConfig = self.interface.DisplayAndGetPlayerTypes(players) # (str("Computer vs Computer")) or (str("Player vs Computer")) or (str("Player vs Player")
        
        #Assign PlayerOne and PlayerTwo as X or O
        playerOneX = self.PlayerFactory.SetPlayerOneX(players) # (True) or (False)
        playerTwoX = self.PlayerFactory.SetPlayerTwoX(playerOneX, players) # (True) or (False)
        
        #Assign first and second player as a string
        firstPlayerType = self.PlayerFactory.SetFirstPlayerType(players) # (str('playerOneComputer')) or (str('playerOneHuman')) or (str('playerTwoComputer')) or (str('playerTwoHuman'))
        secondPlayerType = self.PlayerFactory.SetSecondPlayerType(firstPlayerType, players) # (str('playerOneHuman')) or (str('playerTwoComputer')) or (str('playerTwoHuman'))
        
        #Initialize firstPlayer and secondPlayer as a list of configurations
        firstPlayer = self.PlayerFactory.SetPlayerConfig(firstPlayerType, playerOneX, playerTwoX) # [playerType, XorO] = ['playerOneComputer', True] or ['playerOneComputer', False] or ['playerOneHuman', True] or ['playerOneHuman', False] or ['playerTwoComputer', True] or ['playerTwoComputer', False] or ['playerTwoHuman', True] or ['playerTwoHuman', False]
        secondPlayer = self.PlayerFactory.SetPlayerConfig(secondPlayerType, playerOneX, playerTwoX) # [playerType, XorO] = ['playerOneComputer', True] or ['playerOneComputer', False] or ['playerOneHuman', True] or ['playerOneHuman', False] or ['playerTwoComputer', True] or ['playerTwoComputer', False] or ['playerTwoHuman', True] or ['playerTwoHuman', False]
        
        #User Confirms Game Settings
        userConfirmSettings = self.interface.ConfirmGameSettings(playerVsPlayerMatchConfig, firstPlayer, secondPlayer) # (str('Q' or 'R')) or (True) based on user input
        if userConfirmSettings == 'Q':
            return True
        elif userConfirmSettings == 'R':
            return False
            
        #Create New Game Board
        gameBoard = GameBoardMaster().CreateNewGameBoard() # [None, None, None, None, None, None, None, None, None]
        
        #Keeps track if game is still playable or is finished
        gameBoardStatus = 'Playable'
        
        #Start playing
        self.interface.DisplayBoard(gameBoard) # (None)
        while gameBoardStatus == 'Playable':
            if gameBoardStatus == 'Playable':
                firstPlayerMove = self.Player.PlayerMove(gameBoard, firstPlayer, secondPlayer) # (int(1, 2, 3, 4, 5, 6, 7, 8, or 9)) or (str('Quit', or 'Restart')) based on player input
                if firstPlayerMove == 'Quit':
                    return True
                elif firstPlayerMove == 'Restart':
                    return False
            gameBoard = GameBoardMaster().UpdateGameBoard(gameBoard, firstPlayerMove, firstPlayer[1]) # [slot, slot, slot, slot, slot, slot, slot, slot, slot] :: slot = (None) or (True) or (False)
            self.interface.DisplayBoard(gameBoard) # (None)
            gameBoardStatus = GameBoardMaster().CheckBoard(gameBoard, firstPlayer[1]) # 'Full', 'Winner', or 'Playable'
            if gameBoardStatus == 'Full':
                self.interface.DisplayGameDraw() # (None)
                playAgain = self.interface.AskUserPlayAgain() # (True) or (False)
                if playAgain == True:
                    return False
                elif playAgain == False:
                    return True
            elif gameBoardStatus == 'Winner':
                self.interface.DisplayGameWinner(firstPlayer[0], secondPlayer[0]) # (None)
                playAgain = self.interface.AskUserPlayAgain() # (True) or (False)
                if playAgain == True:
                    return False
                elif playAgain == False:
                    return True
            if gameBoardStatus == 'Playable':
                secondPlayerMove = self.Player.PlayerMove(gameBoard, secondPlayer, firstPlayer) # (int(1, 2, 3, 4, 5, 6, 7, 8, or 9)) or (str('Quit', or 'Restart')) based on player input
                if secondPlayerMove == 'Quit':
                    return True
                elif secondPlayerMove == 'Restart':
                    return False
            gameBoard = GameBoardMaster().UpdateGameBoard(gameBoard, secondPlayerMove, secondPlayer[1]) # [slot, slot, slot, slot, slot, slot, slot, slot, slot] :: slot = (None) or (True) or (False)
            self.interface.DisplayBoard(gameBoard) # (None)
            gameBoardStatus = GameBoardMaster().CheckBoard(gameBoard, secondPlayer[1]) # 'Full', 'Winner', or 'Playable'
            if gameBoardStatus == 'Full':
                self.interface.DisplayGameDraw() # (None)
                playAgain = self.interface.AskUserPlayAgain() # (True) or (False)
                if playAgain == True:
                    return False
                elif playAgain == False:
                    return True
            elif gameBoardStatus == 'Winner':
                self.interface.DisplayGameWinner(secondPlayer[0], firstPlayer[0]) # (None)
                playAgain = self.interface.AskUserPlayAgain() # (True) or (False)
                if playAgain == True:
                    return False
                elif playAgain == False:
                    return True
                    