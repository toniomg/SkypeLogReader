import sqlite3
import datetime

import DBQueries

minMessagesToDisplayConversation = 100
  
def conversationMenu(c):
        #Print the list of Chats:
        chatsList = DBQueries.getChatList(c, minMessagesToDisplayConversation)
        index = 0;
        for title, idChat in chatsList:
            print (str(index) + " " + str(title.encode('UTF-8') if title else "No name"))
            index +=1
        
        
        #Wait for the user to select a Chat
        convSelected = input("Select Chat: ")
        convSelectedInt = int(convSelected);
        convSelectedName = str(chatsList[convSelectedInt][0])
        convSelectedId = chatsList[convSelectedInt][1]
        print (convSelectedName)
        
        #Print the Chat menu
        convOptions = ['Print all messages', 'Statistics']
        index = 0
        for option in convOptions:
            print (str(index) + ") " + option)
            index +=1
            
        optionSelected = input("Select Option: ")
        optionSelectedInt = int(optionSelected);
        print (" ")
        
        if optionSelectedInt == 0:
            messages = DBQueries.getMessagesInChat(c, convSelectedId)
            print (messages)
        elif optionSelectedInt == 1:
            
            firstLastMsg = DBQueries.getFirstAndLastMessageInChat(c, convSelectedId)
            print ("First msg: " + datetime.date.fromtimestamp(firstLastMsg[0]).strftime('%d/%b/%Y'))
            print ("Last msg: " + datetime.date.fromtimestamp(firstLastMsg[1]).strftime('%d/%b/%Y'))
            print ("")
            
            userMessages = DBQueries.getMessagesPerUserInChat(c, convSelectedId)
            msgsTotal = sum(userMessages[i][1] for i in range(len(userMessages)))
            print("Total messages: " + str(msgsTotal))
            print("") 
            for author, msgCount in userMessages:
                print (author + ": " + str(msgCount) + " (" + str(round(msgCount/msgsTotal*100,1)) +  "%)")
            
            messages = DBQueries.getMessagesInChat(c, convSelectedId)
            daysOfWeekCount = [0]*7
            
            for author, timestamp, body in messages:
                msgDate = datetime.date.fromtimestamp(timestamp)
                daysOfWeekCount[msgDate.weekday()] += 1
            
            print("") 
            print("Monday: " + str(daysOfWeekCount[0]) + " (" + str(round(daysOfWeekCount[0]/len(messages)*100,1)) +  "%)")
            print("Tuesday: " + str(daysOfWeekCount[1]) + " (" + str(round(daysOfWeekCount[1]/len(messages)*100,1)) +  "%)")
            print("Wednesday: " + str(daysOfWeekCount[2])+ " (" + str(round(daysOfWeekCount[2]/len(messages)*100,1)) +  "%)")
            print("Thursday: " + str(daysOfWeekCount[3])+ " (" + str(round(daysOfWeekCount[3]/len(messages)*100,1)) +  "%)")
            print("Friday: " + str(daysOfWeekCount[4])+ " (" + str(round(daysOfWeekCount[4]/len(messages)*100,1)) +  "%)")
            print("Saturday: " + str(daysOfWeekCount[5])+ " (" + str(round(daysOfWeekCount[5]/len(messages)*100,1)) +  "%)")
            print("Sunday: " + str(daysOfWeekCount[6])+ " (" + str(round(daysOfWeekCount[6]/len(messages)*100,1)) +  "%)")
            print ("")
            
            
        
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
        mainOptions = ['Conversations (min ' + str(minMessagesToDisplayConversation) + ' messages)', 'Calls']
        optionSelected = printMenuAndWaitResponse(mainOptions)
        if optionSelected == 0:
            conversationMenu(c)
        elif optionSelected == 1:
            printCallsList(c)
 
    
        

    