import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = "mongodb://myazurecosmosdblegolasproject:EcoxKxMrJqDi7ssaktaY3jGCIG7YXMPiR1SJ6e8WbCTNBlQsY7irUeYSsScK0HIiLh4fpPRLMyQYl1JG4v4EXQ==@myazurecosmosdblegolasproject.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@myazurecosmosdblegolasproject@"  # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url)
        database = client['legolasprojectdb']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)