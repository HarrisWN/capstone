import pandas as pd
from pathlib import Path
from base import Base
from to_mongo import ToMongo
import pymongo


# folder_dir = f"{Path(__file__).parents[0]}\\data"

# Base().df.to_csv(f"{folder_dir}\\covid_folder_doc.csv", index=False)
# print("Saved New Covid data to CSV file")


# ToMongo().drop_collectin_dynamic()
# print("All items have been dropped")
# ToMongo().upload_one_by_one()
# print("Collection updated with new data")

# df = pd.read_csv(f"{folder_dir}\\covid_folder_doc.csv", low_memory=False)
# print("Dataframe object created")


# Create a base instance and save the data to a CSV file
folder_dir = f"{Path(__file__).resolve().parents[0]}/data"
base_instance = Base()
base_instance.df.to_csv(f"{folder_dir}/covid_folder_doc.csv", index=False)
print("Saved New Covid data to CSV file")

# Create a ToMongo instance and perform operations
mongo_instance = ToMongo()
mongo_instance.drop_collection_dynamic()
print("All items have been dropped")
mongo_instance.upload_one_by_one()
print("Collection updated with new data")

# Read the data from the CSV file into a DataFrame
df = pd.read_csv(f"{folder_dir}/covid_folder_doc.csv", low_memory=False)
print("Dataframe object created")
