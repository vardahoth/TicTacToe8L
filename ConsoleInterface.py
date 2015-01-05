import os
import msvcrt as inputKey

class ConsoleInputMessages:
    def DisplayWelcomeWithInput(self):
        ConsoleOutputMessages().DisplayWelcome()
        print "Any Key = Continue"
        print "Q = Quit"
        print "Please press Any Key to continue, or Q to quit:"
        continueOrQuit = inputKey.getche().upper()
        if continueOrQuit == 'Q':
            print '\n'
            print '\nExiting Game...'
            return False
        os.system('cls')
        return True
    
    def SetNumPlayers(self):
        ConsoleOutputMessages().PrintAskUserNumPlayers()
        while True:
            numOfPlayers = inputKey.getche().upper()
            if numOfPlayers == '0' or numOfPlayers == '1' or numOfPlayers == '2':
                print '\n'
                return int(numOfPlayers)
            elif numOfPlayers == 'R':
                print '\n'
                print '\nRestarting Game...\n\nPress any key to continue'
                inputKey.getche()
                return str(numOfPlayers)
            elif numOfPlayers == 'Q':
                print '\n'
                print '\nExiting Game...'
                return str(numOfPlayers)
            print "\nInputError: Please enter 0, 1, 2, r, or q:"
    
    def PrintandSetPlayerTypes(self, players):
        if players == ['playerOneComputer', 'playerTwoComputer']:
            print "You have selected Computer vs Computer\n\nPress any key to continue"
            inputKey.getche()
            os.system('cls')
            return "Computer vs Computer"
        elif players == ['playerOneHuman', 'playerTwoComputer']:
            print "You have selected Player vs Computer\n\nPress any key to continue"
            inputKey.getche()
            os.system('cls')
            return "Player vs Computer"
        elif players == ['playerOneHuman', 'playerTwoHuman']:
            print "You have selected Player vs Player\n\nPress any key to continue"
            inputKey.getche()
            os.system('cls')
            return "Player vs Player"
    
    def SetPlayerOneX(self):
        ConsoleOutputMessages().PrintAskPlayerOneToBeXorO()
        print "Input letter (X or O): "
        while True:
            XorO = inputKey.getche().upper()
            if XorO == 'X':
                print '\n'
                return True
            elif XorO == 'O':
                print '\n'
                return False
            print '\nInputError: Please enter X or O:'
    
    def PrintPlayersXandO(self, playerOneX, players):
        """ (bool, list['string1', 'string2']) -> None 
        
        Displays which typeOfPlayer is X and which typeOfPlayer is O.
        
        ['string1', 'string2'] Must be one of the following:
        ['playerOneComputer', 'playerTwoComputer']
        ['playerOneHuman', 'playerTwoComputer']
        ['playerOneHuman', 'playerTwoHuman']
        
        >>>DisplayPlayersXandO(True, ['playerOneComputer', 'playerTwoComputer'])
        "Computer Player 1 is X"
        "Computer Player 2 is O"
        
        "Press any key to continue"
        clear screen
        
        >>>DisplayPlayersXandO(False, ['playerOneComputer', 'playerTwoComputer'])
        "Computer Player 1 is O"
        "Computer Player 2 is X"
        
        "Press any key to continue"
        clear screen
        
        >>>DisplayPlayersXandO(True, ['playerOneHuman', 'playerTwoComputer'])
        "You are X"
        "Computer is O"
        
        "Press any key to continue"
        clear screen
        
        >>>DisplayPlayersXandO(False, ['playerOneHuman', 'playerTwoComputer'])
        "You are O"
        "Computer is X"
        
        "Press any key to continue"
        clear screen
        
        >>>DisplayPlayersXandO(True, ['playerOneHuman', 'playerTwoHuman'])
        "Player 1 is X"
        "Player 2 is O"
        
        "Press any key to continue"
        clear screen
        
        >>>DisplayPlayersXandO(False, ['playerOneHuman', 'playerTwoHuman'])
        "Player 1 is O"
        "Player 2 is X"
        
        "Press any key to continue"
        clear screen
        """
        if playerOneX == True and players == ['playerOneComputer', 'playerTwoComputer']:
            print "Computer Player 1 is X"
            print "Computer Player 2 is O\n\nPress any key to continue"
            inputKey.getche()
            os.system('cls')
        elif playerOneX == False and players == ['playerOneComputer', 'playerTwoComputer']:
            print "Computer Player 1 is O"
            print "Computer Player 2 is X\n\nPress any key to continue"
            inputKey.getche()
            os.system('cls')
        elif playerOneX == True and players == ['playerOneHuman', 'playerTwoComputer']:
            print "You are X"
            print "Computer is O\n\nPress any key to continue"
            inputKey.getche()
            os.system('cls')
        elif playerOneX == False and players == ['playerOneHuman', 'playerTwoComputer']:
            print "You are O"
            print "Computer is X\n\nPress any key to continue"
            inputKey.getche()
            os.system('cls')
        elif playerOneX == True and players == ['playerOneHuman', 'playerTwoHuman']:
            print "Player 1 is X"
            print "Player 2 is O\n\nPress any key to continue"
            inputKey.getche()
            os.system('cls')
        elif playerOneX == False and players == ['playerOneHuman', 'playerTwoHuman']:
            print "Player 1 is O"
            print "Player 2 is X\n\nPress any key to continue"
            inputKey.getche()
            os.system('cls')
            
    def SetFirstPlayerType(self, players):
        ConsoleOutputMessages().PrintAskPlayerWhoIsFirst(players)
        print "Input number (1 or 2): "
        while True:
            firstPlayer = inputKey.getche()
            if firstPlayer == '1':
                print '\n'
                return players[0]
            elif firstPlayer == '2':
                print '\n'
                return players[1]
            print '\nInputError: Please enter 1 or 2:'
            
    def PrintFirstAndSecondPlayers(self, firstPlayerType, secondPlayerType):
        if firstPlayerType == 'playerOneComputer' and secondPlayerType == 'playerTwoComputer':
            print "Computer Player 1 will go first"
            print "Computer Player 2 will go second\n\nPress any key to Start Playing"
            inputKey.getche()
            os.system('cls')
            return None
        elif firstPlayerType == 'playerTwoComputer' and secondPlayerType == 'playerOneComputer':
            print "Computer Player 2 will go first"
            print "Computer Player 1 will go second\n\nPress any key to Start Playing"
            inputKey.getche()
            os.system('cls')
            return None
        elif firstPlayerType == 'playerOneHuman' and secondPlayerType == 'playerTwoComputer':
            print "You will go first"
            print "Computer will go second\n\nPress any key to Start Playing"
            inputKey.getche()
            os.system('cls')
            return None
        elif firstPlayerType == 'playerTwoComputer' and secondPlayerType == 'playerOneHuman':
            print "Computer will go first"
            print "You will go second\n\nPress any key to Start Playing"
            inputKey.getche()
            os.system('cls')
            return None
        elif firstPlayerType == 'playerOneHuman' and secondPlayerType == 'playerTwoHuman':
            print "Player 1 will go first"
            print "Player 2 will go second\n\nPress any key to Start Playing"
            inputKey.getche()
            os.system('cls')
            return None
        elif firstPlayerType == 'playerTwoHuman' and secondPlayerType == 'playerOneHuman':
            print "Player 2 will go first"
            print "Player 1 will go second\n\nPress any key to Start Playing"
            inputKey.getche()
            os.system('cls')
            return None
    
    def ConfirmGameSettings(self, playerVsPlayerMatchConfig, firstPlayer, secondPlayer):
        print "Players = " + str(playerVsPlayerMatchConfig)
        if firstPlayer[0] == 'playerOneComputer' and secondPlayer[0] == 'playerTwoComputer':
            print "First Player is Computer Player 1"
            print "Second Player is Computer Player 2"
        elif firstPlayer[0] == 'playerTwoComputer' and secondPlayer[0] == 'playerOneComputer':
            print "First Player is Computer Player 2"
            print "Second Player is Computer Player 1"
        elif firstPlayer[0] == 'playerOneHuman' and secondPlayer[0] == 'playerTwoComputer':
            print "First Player is You"
            print "Second Player is Computer"
        elif firstPlayer[0] == 'playerTwoComputer' and secondPlayer[0] == 'playerOneHuman':
            print "First Player is Computer"
            print "Second Player is You"
        elif firstPlayer[0] == 'playerOneHuman' and secondPlayer[0] == 'playerTwoHuman':
            print "First Player is Player 1"
            print "Second Player is Player 2"
        elif firstPlayer[0] == 'playerTwoHuman' and secondPlayer[0] == 'playerOneHuman':
            print "First Player is Player 2"
            print "Second Player is Player 1"
        if firstPlayer[1] == True:
            print "First Player = X"
            print "Second Player = O"
        else:
            print "First Player = O"
            print "Second Player = X"
        print '\n'
        ConsoleOutputMessages().PrintBoardInstructions()
        print "\nPress any key to start the game, or (Q = Quit, R = Restart)"
        playerConfirmation = inputKey.getche().upper()
        print '\n'
        if playerConfirmation == 'Q':
            print "Exiting Game..."
            return playerConfirmation
        elif playerConfirmation == 'R':
            return playerConfirmation
        return True
        
    
    def SetPlayerMove(self, gameBoard):
        playerMove = raw_input()
        try:
            return int(playerMove)
        except ValueError:
            if playerMove.upper() == 'R':
                return playerMove.upper()
            elif playerMove.upper() == 'Q':
                return playerMove.upper()
        
    def MessageUserPlayAgain(self):
        print "Would you like to play again?\n(Y = Yes, N = No): "
        while True:
            yesOrNo = raw_input().upper()
            if yesOrNo == 'Y' or yesOrNo == 'YES':
                return True
            elif yesOrNo == 'N' or yesOrNo == 'NO':
                return False
            print "Error: " + str(yesOrNo) + " is not a valid input.\nPlease enter Y or N to play again:"
            
        
class ConsoleOutputMessages:
    def DisplayWelcome(self):
        os.system('cls')
        print """\
**************************************************************
******************** Welcome to TicTacToe ********************
**************************************************************
Copyright (c) 2014 James C. Page
All Rights Reserved
 
This product is protected by copyright and distributed under
licenses restricting copying, distribution and decompilation.
"""

    def PrintAskUserNumPlayers(self):
        print "0. Computer vs Computer\n1. Player vs Computer\n2. Player vs Player\nR = Restarts Game\nQ = Quits Game"
        print "Input key (0, 1, 2, r, or q): "
        
    def PrintAskPlayerOneToBeXorO(self):
        print "Do you want Player 1 to be X or O?"
        
    def PrintAskPlayerWhoIsFirst(self, players):
        print "Who do you want to go first?"
        if players == ['playerOneHuman', 'playerTwoComputer']:
            print "1. You go first"
            print "2. Computer goes first"
        elif players == ['playerOneHuman', 'playerTwoHuman']:
            print "1. Player 1 goes first"
            print "2. Player 2 goes first"
            
    def PrintBoardInstructions(self):
        print """\
Instructions: To select a slot on the board, input the number corresponding to the slot.
-------------
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
-------------
        """
    
    def PrintGameBoard(self, gameBoard):
        """
        PrintGameBoard([0, 1, 2, 3, 4, 5, 6, 7, 8]) -> None
        -------------
        |   |   |   |
        -------------
        |   |   |   |
        -------------
        |   |   |   |
        -------------
        
        """
        os.system('cls')
        modularNewLineCounter = 1
        GameBoardDisplayerString = ''
        GameBoardDisplayer = []
        print "-------------"
        for slot in gameBoard:
            if slot == None:
                slot = ' '
            elif slot == True:
                slot = 'X'
            elif slot == False:
                slot = 'O'
            GameBoardDisplayerString += "| " + str(slot) + " "
            if modularNewLineCounter % 3 == 0:
                GameBoardDisplayerString += "|"
                print GameBoardDisplayerString
                print "-------------"
                GameBoardDisplayerString = ''
                modularNewLineCounter = 0
            modularNewLineCounter += 1
        print '\n'
    def PrintAskPlayerMove(self, playerTypeMove, otherPlayerType, availablePicks):
        if playerTypeMove == 'playerOneComputer' and otherPlayerType == 'playerTwoComputer':
            print "Computer Player 1's turn to move\n"
        elif playerTypeMove == 'playerTwoComputer' and otherPlayerType == 'playerOneComputer':
            print "Computer Player 2's turn to move\n"
        elif playerTypeMove == 'playerOneHuman' and otherPlayerType == 'playerTwoComputer':
            print "Your move\n"
        elif playerTypeMove == 'playerTwoComputer' and otherPlayerType == 'playerOneHuman':
            print "Computer is deciding where to move...\n"
        elif playerTypeMove == 'playerOneHuman' and otherPlayerType == 'playerTwoHuman':
            print "Player 1's turn to move\n"
        elif playerTypeMove == 'playerTwoHuman' and otherPlayerType == 'playerOneHuman':
            print "Player 2's turn to move\n"
        if playerTypeMove == 'playerOneHuman' or playerTypeMove == 'playerTwoHuman':
            print "Input a number " + str(availablePicks) + "\nOr the letters Q or R(Q = Quits Game, R = Restart Game)"
        
    def PrintSlotTakenError(self, availablePicks, playerMove):
        print "Error: " + str(playerMove) + " is already taken"
        print "Please pick one of the following numbers " + str(availablePicks) + ":"
        
    def PrintInvalidSlotError(self, availablePicks, playerMove):
        print "Error: " + str(playerMove) + " is not a valid move"
        print "Please pick one of the following numbers " + str(availablePicks) + ":"
        
    def PrintGameDraw(self):
        print """\
******************
* Game is a draw *
******************
        """
        
    def PrintGameWinner(self, winner, loser):
        if winner == 'playerOneComputer' and loser == 'playerTwoComputer':
            print """\
**************************
* Computer Player 1 Wins *
**************************
            """
        elif winner == 'playerTwoComputer' and loser == 'playerOneComputer':
            print """\
**************************
* Computer Player 2 Wins *
**************************
            """
        elif winner == 'playerOneHuman' and loser == 'playerTwoComputer':
            print """\
***********
* You win *
***********
            """
        elif winner == 'playerTwoComputer' and loser == 'playerOneHuman':
            print """\
*****************
* Computer wins *
*****************
            """
        elif winner == 'playerOneHuman' and loser == 'playerTwoHuman':
            print """\
*****************
* Player 1 wins *
*****************
            """
        elif winner == 'playerTwoHuman' and loser == 'playerOneHuman':
            print """\
*****************
* Player 2 wins *
*****************
            """
            