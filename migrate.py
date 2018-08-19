from tinydb import TinyDB
import conf

db = TinyDB(conf.DB_PATH)
db.purge()
table = db.table('responses')
table.insert({'intext': "Schedule", "outtext": "Nuestro horario es de 6AM a 7PM", "botID":conf.YOUR_BOT_ID})
table.insert({'intext': "Products", "outtext": "Puedo ofrecerte: Bocinas, Televisores, Muebles...", "botID":conf.YOUR_BOT_ID})
table.insert({'intext': "conversation_start", "outtext": "Hola buen dia, como te va?", "botID":conf.YOUR_BOT_ID})