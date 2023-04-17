# Collecting-data-from-mongo-db-
Collecting data from  mongo_db and storing it in a dataframe
#Instlling pymongo
pip install pymongo

#Importing Libraries
from pymongo import MongoClient
import pandas as pd

#Connecting to mongo database using the connection string
client = MongoClient("mongodb+srv://debolamech:oluwatoyin@cluster0.leh48mn.mongodb.net/?retryWrites=true&w=majority")
db = client["student_db"]
student_record = db["student_record"]

def mongo(colections):
    result =list(colections.find({})) # Find and list the data in the collections,
    df = pd.DataFrame(result) # convert the result into a dataframe;
    df.to_csv("Project.csv")

    return df

mongo(student_record)

