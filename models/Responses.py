from tinydb import TinyDB, Query
import conf


class Responses(object):
    def __init__(self):
        #initializing the table on the db
        try:
            self.db = TinyDB(conf.DB_PATH)
            self.table = self.db.table('responses')
            self.ResponsesQuery = Query()
        except Exception as e:
            print(e)

    def find_response_by_action(self, incoming_action, botID):
        result = ""
        try:
            '''we are going to find the response acording to the bot 
            ID and the action triggered from the input text from the user'''
            result = self.table.search((self.ResponsesQuery.intext == incoming_action) & (self.ResponsesQuery.botID == botID))[0]

        except Exception as e:
            print(e)
            result= "error"

        return result
