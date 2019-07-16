import os

MONGO_DBNAME = 'theTopShelf'
MONGO_URI =os.environ.get("MONGO_URI")
SECRET_KEY  = os.urandom(32)




