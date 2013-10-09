import sqlite3
import datetime

import DBQueries

        
def conversationMenu():
        #Print the list of Chats:
        chatsList = 0 #printChatList(c)
        
        #Wait for the user to select a Chat
        convSelected = input("Select Chat: ")
        convSelectedInt = int(convSelected);
        convSelectedName = str(chatsList[convSelectedInt][0])
        convSelectedId = chatsList[convSelectedInt][1]
        print (convSelectedName)
        
        #Print the Chat menu
        convOptions = ['Print all messages', 'Get number of messages per user', 'Get most popular words']
        index = 0
        for option in convOptions:
            print (str(index) + ") " + option)
            index +=1
            
        optionSelected = input("Select Option: ")
        optionSelectedInt = int(optionSelected);
        print (" ")
        
        if optionSelectedInt == 0:
            #printMessagesInChat(convSelectedId)
            pass
        elif optionSelectedInt == 1:
            pass #printMessagesPerUserInChat(convSelectedId)
        elif optionSelectedInt == 2:
            pass
        
        input("Press any key to continue...")
        


def printMenuAndWaitResponse(optionList):
    """ Print the menu of options and return the choosen one by the user
        """
    index = 0
    for option in optionList:
        print (str(index) + ") " + option)
        index +=1
        
    while True:
        try:
            optionSelected = int(input("Select Option: "))
            if optionSelected < len(optionList):
                return optionSelected
            else:
                print('Option not available')
        except ValueError:
            print("Option not valid, please introduce a valid option")
            

def printCallsList(c):
    
    calls = DBQueries.getCallsList(c)
    for call in calls:
        duration = round(call[1]/60,1)
        time = datetime.datetime.fromtimestamp(call[2])
        print (call[0] + ": " + str(duration) + " min - " + str(time))
        
if __name__ == '__main__':
    
    conn = sqlite3.connect(r'main.db')
    c = conn.cursor()
    
    while 1:
        
        mainOptions = ['Conversations', 'Calls']
        optionSelected = printMenuAndWaitResponse(mainOptions)
        if optionSelected == 0:
            conversationMenu()
        elif optionSelected == 1:
            printCallsList(c)
 
    
        

    