import os

MONGO_DBNAME = 'theTopShelf'
# MONGO_URI =os.environ.get("MONGO_URI")
MONGO_URI = "mongodb+srv://root:jk6200dl@myfirstcluster-fdipx.mongodb.net/theTopShelf?retryWrites=true&w=majority"
SECRET_KEY  = os.urandom(32)




