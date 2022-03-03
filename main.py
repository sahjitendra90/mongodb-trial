#you can then connect to your MongoDB database server via the MongoClient.
# For example:
from pymongo import MongoClient
client = MongoClient()


#In this case, we will need a slack database, and a collection called messages.
# We can use the following code to connect:
db = client["slack"]
msg_collection = db["messages"]

# Note however that MongoDB works in lazy mode, and will not create the database
# or collection until you actually insert your first document.
# Create a message dict

message = {
    "channel": "dev",
    "author": "cerami",
    "text": "Hello, world!"
}

# To insert new records, you specify your record as a Python dict, and then use the
# insert_one() or insert_many() methods.
# For example, let's define a new message for our Slack code:
# We can then use the insert_one() method:
result = msg_collection.insert_one(message)
print(result.inserted_id)



# import pprint
# pp = pprint.PrettyPrinter(indent=4)
# for doc in msg_collection.find():
#     pp.pprint(doc)

