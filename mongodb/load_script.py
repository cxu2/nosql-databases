from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://localhost")
db = client.news

db.users.insert([
    { "credentials" : { "username" : "u1", "password" : "00" },
      "posts" : [ 1, 2, 3 ],
      "voted" : [ 1, 5, 8 ],
      "comments" : [ 1, 2, 3, 4 ]
    },
    { "credentials" : { "username" : "u2", "password" : "01" },
      "posts" : [ 4, 5, 6 ],
      "voted" : [ 1, 2, 5, 9 ],
      "comments" : [ 5, 6, 7, 8 ]
    },
    { "credentials" : { "username" : "u3", "password" : "10" },
      "posts" : [ 7, 8, 9 ],
      "voted" : [ 2, 3, 7 ],
      "comments" : [ 9, 10, 11, 12 ]
    }
])

db.board.insert([
    { 
      "id" : 1,
      "articles" : [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ],
      "jobs" : [ 1, 2, 3 ]
    }
])

db.job.insert([
    { "id" : 1, "title" : "google" },
    { "id" : 2, "title" : "facebook" },
    { "id" : 3, "title" : "amazon" }
])

db.article.insert([
    { "id" : 1, 
      "props" : { "points" : 5, "time": "05/05/18" }, 
      "comments" : [ 2, 5, 9 ],
      "title" : { "text" : "Gitea: Open source, self-hosted GitHub alternative", "url" : "https://gitea.io/en-US/" },
      "author" : "u1"
    },
    { "id" : 2, 
      "props" : { "points" : 3, "time": "05/05/18" }, 
      "comments" : [ 1, 6 ],
      "title" : { "text" : "Subscription Hell", "url" : "https://techcrunch.com/2018/05/06/subscription-hell/" },
      "author" : "u1"
    },
    { "id" : 3, 
      "props" : { "points" : 2, "time": "05/05/18" }, 
      "comments" : [],
      "title" : { "text" : "Researchers have developed a water-based battery to store solar and wind energy", "url" : "https://news.stanford.edu/2018/04/30/new-water-based-battery-offers-large-scale-energy-storage/" },
      "author" : "u1"
    },
    { "id" : 4, 
      "props" : { "points" : 4, "time": "05/06/18" }, 
      "comments" : [ 3, 10 ],
      "title" : { "text" : "California to become first U.S. state mandating solar on new homes", "url" : "https://www.ocregister.com/2018/05/04/california-to-become-first-u-s-state-mandating-solar-on-new-homes/" },
      "author" : "u2"
    },
    { "id" : 5, 
      "props" : { "points" : 3, "time": "05/04/18" }, 
      "comments" : [ 4 ],
      "title" : { "text" : "Origins of the finger command (1990)", "url" : "https://groups.google.com/forum/#!msg/alt.folklore.computers/IdFAN6HPw3k/Ci5BfN8i26AJ" },
      "author" : "u2"
    },
    { "id" : 6, 
      "props" : { "points" : 3, "time": "05/03/18" }, 
      "comments" : [ 7, 8 ],
      "title" : { "text" : "NASA advisers say SpaceX rocket technology could put lives at risk", "url" : "http://www.chicagotribune.com/news/nationworld/ct-nasa-spacex-rocket-elon-musk-20180505-story.html" },
      "author" : "u2"
    },
    { "id" : 7, 
      "props" : { "points" : 2, "time": "05/06/18" }, 
      "comments" : [],
      "title" : { "text" : "Cells Talk in a Language That Looks Like Viruses", "url" : "https://www.quantamagazine.org/cells-talk-in-a-language-that-looks-like-viruses-20180502/" },
      "author" : "u3"
    },
    { "id" : 8, 
      "props" : { "points" : 1, "time": "05/02/18" }, 
      "comments" : [ 11 ],
      "title" : { "text" : "How Harvey Karp Turned Baby Sleep into Big Business", "url" : "https://www.nytimes.com/2018/04/18/magazine/harvey-karp-baby-mogul.html" },
      "author" : "u3"
    },
    { "id" : 9, 
      "props" : { "points" : 1, "time": "05/01/18" }, 
      "comments" : [ 12 ],
      "title" : { "text" : "The Muse Is Hiring a PM for Data and Analytics", "url" : "https://www.themuse.com/jobs/themuse/product-manager-data-analytics-8fa79a" },
      "author" : "u3"
    },
])

db.comments.insert([
    { "id" : 1, "by" : "u1", "content" : "comment 1", "on" : 2 },
    { "id" : 2, "by" : "u1", "content" : "comment 2", "on" : 1 },
    { "id" : 3, "by" : "u1", "content" : "comment 3", "on" : 4 },
    { "id" : 4, "by" : "u1", "content" : "comment 4", "on" : 5 },
    { "id" : 5, "by" : "u2", "content" : "comment 5", "on" : 1 },
    { "id" : 6, "by" : "u2", "content" : "comment 6", "on" : 2 },
    { "id" : 7, "by" : "u2", "content" : "comment 7", "on" : 6 },
    { "id" : 8, "by" : "u2", "content" : "comment 8", "on" : 6 },
    { "id" : 9, "by" : "u3", "content" : "comment 9", "on" : 1 },
    { "id" : 10, "by" : "u3", "content" : "comment 10", "on" : 4 },
    { "id" : 11, "by" : "u3", "content" : "comment 11", "on" : 8 },
    { "id" : 12, "by" : "u3", "content" : "comment 12", "on" : 9 },
])
