import csv
from tqdm import tqdm
from sqlalchemy import engine, create_engine

engine = create_engine('mysql://pranav:password@localhost:3306/xo')
rows = engine.execute("SELECT * FROM data1")

with open("/home/pranav/Documents/Projects/xo_ai/dataset3.csv", "w") as file:
    writer = csv.writer(file)
    for row in tqdm(rows):
        writer.writerow(row)
