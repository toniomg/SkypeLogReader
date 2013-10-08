import sqlite3

def printChatList(c):
    """Print the list of Chats stored in DB
        """

    c.execute('SELECT topic, conv_dbid FROM Chats ORDER BY id')
    chatsList = c.fetchall();
    
    index = 0;
    for chat in chatsList:
        print (str(index) + " " + str(chat[0]))
        index +=1
        
    return chatsList

def printMessagesInChat(ChatSelectedId):
    """ Print the list of messages from the selected Chat
        """
    
    #Print Messages in Chat selected
    c.execute ('SELECT author, id, body_xml FROM Messages WHERE convo_id=?', [str(ChatSelectedId)])
    messagesList = c.fetchall()
    print (messagesList)
    
    for author, idMessage, message in messagesList:
        print (author)
        print (message)
        print ("")
        
    return

def printUsersInChat(ChatSelectedId):
    
    #Get the users of that Chat
    c.execute ('Select identity FROM ChatMembers WHERE chatname= (SELECT identity FROM Chats WHERE id=?)', [ChatSelectedId])
    userList = c.fetchall()
    print (userList)
    
def printMessagesPerUserInChat(ChatSelectedId):
    
    c.execute('SELECT author, COUNT(*) FROM Messages WHERE convo_id=? GROUP BY author ORDER BY COUNT(*) DESC', [ChatSelectedId])
    messagesPerUser = c.fetchall()
    
    sumM = sum(messagesPerUser[i][1] for i in range(len(messagesPerUser)))
     
    print ('Total messages: ' + str(sumM))
    for name, messagesCount in messagesPerUser:
        print (str(name) + ': ' + str(messagesCount))
        

conn = sqlite3.connect(r'main.db')
c = conn.cursor()

while 1:
    
    #Print the list of Chats:
    chatsList = printChatList(c)
    
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
        printMessagesPerUserInChat(convSelectedId)
    elif optionSelectedInt == 2:
        pass
    
    raw_input("Press any key to continue...")
        

    