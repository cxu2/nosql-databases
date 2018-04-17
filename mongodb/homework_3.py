from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://localhost")
db = client.movie

# Part A
db.movies.update_many(
    {"rated": "NOT RATED", "genres": "Drama"},
    {"$set": {"rated": "Pending rating"}}
)

# Part B
db.movies.insert_one(
    { "title" : "The Shape of Water",
      "year" : 2017,
      "countries" : ["USA"],
      "genres" : ["Adventure", 
                  "Drama",
                  "Fantasy",
                  "Horror",
                  "Romance",
                  "Thriller"
                 ],
      "directors" : ["Guillermo del Toro"],
      "imdb" : { "id" : 5580390,
                 "rating" : 7.5,
                 "votes" : 194478
               }
    }        
)

# Part C
cursor1 = db.movies.aggregate(
    [ 
        { "$match" : { "genres" : "Drama" } },
        { "$group" : { "_id" : "Drama", "count" : { "$sum" : 1 } } }
    ]
)

for document in cursor1:
    pprint(document)

# Part D
# I am just using "countries" : "China" here instead of ["China"] to match any movie that has "China" in countries
cursor2 = db.movies.aggregate(
    [
        { "$match" : { "countries" : "China", "rated" : "Pending rating" } },
        { "$group" : { "_id" : { "country" : "China", "rating" : "Pending rating" }, "count" : { "$sum" : 1 } } }
    ]
)

for document in cursor2:
    pprint(document)

# Part E
db.teams.insert([
    { "name" : "Houston Rockets", "wins" : 65, "loses" : 17 },
    { "name" : "Toronto Raptors", "wins" : 59, "loses" : 23 }
])

db.allstars.insert([
    { "names" : ["Stephen Curry", "Kevin Durant", "Klay Thompson", "Draymond Green"], "team" : "Golden State Warriors" },
    { "names" : ["Demar DeRozan", "Kyle Lowry"], "team" : "Toronto Raptors" },
    { "names" : ["James Harden"], "team" : "Houston Rockets" }
])

cursor3 = db.teams.aggregate([
    { "$lookup" : { "from" : "allstars", "localField" : "name", "foreignField" : "team", "as" : "allstars"} }    
])

for document in cursor3:
    pprint(document)
