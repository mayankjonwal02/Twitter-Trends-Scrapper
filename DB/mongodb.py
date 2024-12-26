from pymongo import MongoClient 
# import object id 
from bson.objectid import ObjectId



import datetime


def get_collection():

    try:

        connection_string = "mongodb+srv://jonwal1:jonwal1@trendsdb.jd8rl.mongodb.net/?retryWrites=true&w=majority&appName=TrendsDB"

        client = MongoClient(connection_string)

        db = client["TrendsDB"]
        collection = db["Trends"]

        return collection

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def create_unique_id():
    return datetime.datetime.now().strftime("%Y%m%d%H%M%S")
def get_all_trends(collection=None):

    if collection is None:
        collection = get_collection()

    if collection is not None:
        items = collection.find()
        trends_list = []
        for trend in items:
            trend["_id"] = str(trend["_id"])
            trends_list.append(trend)
        print(trends_list)  # Print the list of trends
        return trends_list

    return None

def add_trends(trends, collection=None):
    trends_simple = trends.copy()
    if collection is None:
        collection = get_collection()

    if collection is not None:
        id = ObjectId()
        trends["_id"] = id
        trends_simple["_id"] = str(id)
        print("id : {}".format(id))
        collection.insert_one(trends)
    
    print(trends_simple)

    return trends_simple


        