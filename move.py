import csv
from tqdm import tqdm
from sqlalchemy import engine, create_engine

engine = create_engine('mysql://pranav:password@localhost:3306/xo')


with open("dataset.csv", "r") as file:
    reader = csv.reader(file)
    for row in tqdm(reader):
        for i in range(9):
            row[i] = int(float(row[i]))
        row[9:] = [row[9:].index("1.0")]
        query = "INSERT INTO data VALUES ({},{},{},{},{},{},{},{},{},{})".format(*row)
        engine.execute(query)
