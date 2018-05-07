# Put the use case you chose here. Then justify your database choice:
# Hackernews is chosen for use case and mongodb for database. 
# Since Mongodb provides model shemas which can be nested and of different data structures. 
# Queries are also easy to write with a bunch of useful operators.
#
# Explain what will happen if coffee is spilled on one of the servers in your cluster, causing it to go down.
# A mongodb server replica will come up in the place of the down server, which provides redundency and thus prevents data loss.
# When the down server comes back, it will become the backup server and get updates from the new leader server.
#
# What data is it not ok to lose in your app? What can you do in your commands to mitigate the risk of lost data?
# User credentials is the data that is sensitive and not ok to lose. So in command we need to make sure that each command is atomic so we don't get partial credencials or things like that 
#
from pymongo import MongoClient
from pprint import pprint
from datetime import datetime

client = MongoClient("mongodb://localhost")
db = client.news

# Action 1: User u1 publishes an article
board = db.board.find_one({ "id" : 1 })
new_id = max(board["articles"]) + 1

db.users.update_one(
    { "credentials.username" : "u1" },
    { "$push" : { "posts" : new_id } }
)

db.board.update_one(
    { "id" : 1 },
    { "$push" : { "articles" : new_id } }
)

db.article.insert_one(
    { "id" : new_id,
      "props" : { "points" : 0, "time" : str(datetime.now()) },
      "comments" : [],
      "title" : { "text" : "New Article added!", "url" : "" },
      "author" : "u1"
    }        
)

# Action 2: A user sees a list of the 5 highest-voted articles
cursor = db.article.aggregate([
    { "$sort" : { "props.points" : -1} },
    { "$limit" : 5 }
])

for i in cursor:
    pprint(i)

# Action 3: A user u1 upvotes article with id 1
u1 = db.users.find_one({ "credentials.username" : "u1" })
voted = u1["voted"]
if 2 not in voted:
    db.article.update_one(
        { "id" : 2 },
        { "$inc" : { "props.points" : 1 } }
    )
    db.users.update_one(
        { "credentials.username" : "u1" },
        { "$push" : { "voted" : 2 }}
    )

# Action 4: User u1 retrieves the vote for article with id 1
u1 = db.users.find_one({ "credentials.username" : "u1" })
voted = u1["voted"]
if 5 in voted:
    db.article.update_one(
        { "id" : 5 },
        { "$inc" : { "props.points" : -1 } }
    )
    db.users.update_one(
        { "credentials.username" : "u1" },
        { "$pull" : { "voted" : 5 }}
    )

# Action 5: A new job is posted
board = db.board.find_one({ "id" : 1 })
new_job_id = max(board["jobs"]) + 1

db.board.update_one(
    { "id" : 1 },
    { "$push" : { "jobs" : new_job_id } }
)

db.job.insert_one(
    { "id" : new_job_id,
      "title" : "new job title" 
    }
)

# Action 6: A user u1 comments on an article with id 5
cursor2 = db.comments.aggregate([
    { "$sort" : { "id" : -1} },
    { "$limit" : 1 }
])

new_comment_id = 0
for comment in cursor2:
    new_comment_id = comment["id"] + 1

db.comments.insert_one(
    { "id" : new_comment_id,
      "by" : "u1",
      "content": " u1 comment on article 5",
      "on" : 5 }
)

db.users.update_one(
    { "credentials.username" : "u1" },
    { "$push" : { "comments" : new_comment_id } }
)

db.article.update_one(
    { "id" : 5 },
    { "$push" : { "comments" : new_comment_id } }
)

# Action 7: get all article ids voted by user with id 1
u1_voted = db.users.find_one({ "credentials.username" : "u1" })["voted"]
print(u1_voted)

# Action 8: get all article ids commented by user with id 1
u1_commented = db.users.find_one({ "credentials.username" : "u1" })["comments"]
print(u1_commented)

