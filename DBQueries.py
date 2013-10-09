def getCallsList(c):
    """ Return the name, duration and start date of the conversations
        """
    c.execute('SELECT dispname, call_duration, start_timestamp FROM CallMembers GROUP BY call_db_id')
    calls = c.fetchall()
    return [[0 if value is None else value for value in sublist] for sublist in calls]
    
def getChatList(c):
    """Return the list of chats
        [topic, id]
        """
    c.execute('SELECT topic, conv_dbid FROM Chats ORDER BY id')
    chatsList = c.fetchall();
    return chatsList

def getMessagesInChat(c, ChatSelectedId):
    """ Return the list of messages from the selected Chat:
        [author, id, body]
        """
    c.execute ('SELECT author, id, body_xml FROM Messages WHERE convo_id=?', [str(ChatSelectedId)])
    return c.fetchall()


def getUsersInChat(c, ChatSelectedId):
    """ Return the list of user of a chat:
        [name] 
        """
    c.execute ('Select identity FROM ChatMembers WHERE chatname= (SELECT identity FROM Chats WHERE id=?)', [ChatSelectedId])
    return c.fetchall()

    
def getMessagesPerUserInChat(c, ChatSelectedId):
    """ Get the number of messages per user of a chat
        [author, messages count]
        """
    c.execute('SELECT author, COUNT(*) FROM Messages WHERE convo_id=? GROUP BY author ORDER BY COUNT(*) DESC', [ChatSelectedId])
    return c.fetchall()