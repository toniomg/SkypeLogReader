import sqlite3


def printConversationList(c):
    """Print the list of conversations stored in DB
        """

    c.execute('SELECT displayname, id FROM Conversations ORDER BY id')
    return c.fetchall();



conn = sqlite3.connect("C:\Users\Antonio\Desktop\main.db")
c = conn.cursor()

while 1:
    
    chatsList = printConversationList(c);
    
    index = 0;
    for title, idChat in chatsList:
        print str(index) + " " + str(title)
        index +=1

    optionSelected = raw_input("Select Chat: ")
    print str(chatsList[int(optionSelected)][0])
    
    #Print Messages in conversation selected
    c.execute ('SELECT author, id, body_xml FROM Messages WHERE convo_id=?', [str(chatsList[int(optionSelected)][1])])
    messagesList = c.fetchall()
    print messagesList
    
    for author, idMessage, message in messagesList:
        print author
        print message
        print ""
        
    raw_input("Press any key to continue")

    