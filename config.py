import os

MONGO_DBNAME = 'theTopShelf'
MONGO_URI = 'mongodb+srv://root:jk6200dl@myfirstcluster-fdipx.mongodb.net/theTopShelf?retryWrites=true&w=majority'

S3_BUCKET = "the-top-shelf"
S3_KEY = "AKIAIRUD7XQBDPAX3T6Q"
S3_SECRET = "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"
S3_LOCATION = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)

SECRET_KEY  = os.urandom(32)




