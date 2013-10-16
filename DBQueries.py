def getCallsList(c):
    """ Return the name, duration and start date of the conversations
        """
    c.execute('SELECT dispname, call_duration, start_timestamp FROM CallMembers GROUP BY call_db_id')
    calls = c.fetchall()
    return [[0 if value is None else value for value in sublist] for sublist in calls]
    
def getChatList(c, minMessages):
    """Return the list of chats
        [topic, id]
        """
    c.execute('SELECT displayname, id FROM Conversations WHERE id IN (SELECT convo_id c FROM Messages GROUP BY convo_id HAVING  COUNT(*) > ?)', [minMessages])
    chatsList = c.fetchall();
    return chatsList

def getMessagesInChat(c, ChatSelectedId):
    """ Return the list of messages from the selected Chat:
        [author, timestamp, body]
        """
    c.execute ('SELECT from_dispname, timestamp, body_xml FROM Messages WHERE convo_id=?', [str(ChatSelectedId)])
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
    c.execute('SELECT from_dispname, COUNT(*) FROM Messages WHERE convo_id=? GROUP BY author ORDER BY COUNT(*) DESC', [ChatSelectedId])
    return c.fetchall()

def getFirstAndLastMessageInChat(c, ChatSelectedId):
    """ Get the first and the last message of the conversation
        [firstMsgTimestamp, lastMsgTimestamp]
        """
    edgedsTimestamp = [0,0]
    c.execute ('SELECT timestamp FROM Messages WHERE convo_id=? ORDER BY timestamp ASC LIMIT 1', [str(ChatSelectedId)])
    edgedsTimestamp[0] = c.fetchone()[0]
    c.execute ('SELECT timestamp FROM Messages WHERE convo_id=? ORDER BY timestamp DESC LIMIT 1', [str(ChatSelectedId)])
    edgedsTimestamp[1] = c.fetchone()[0]
    return edgedsTimestamp