#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Importing Libraries
from pymongo import MongoClient
import pandas as pd


# In[3]:


#Connecting to mongo database using the connection string
client = MongoClient("mongodb+srv://debolamech:oluwatoyin@cluster0.leh48mn.mongodb.net/?retryWrites=true&w=majority")
db = client["student_db"]
student_record = db["student_record"]


# In[6]:


def mongo(colections):
    result =list(colections.find({})) # Find and list the data in the collections,
    df = pd.DataFrame(result) # convert the result into a dataframe;
    df.to_csv("Project.csv")

    return df


# In[7]:


mongo(student_record)


# In[ ]:




