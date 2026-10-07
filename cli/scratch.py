## Reading a CSV by column name

import csv

# with open("data.csv", "r") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(row["score"])
    
## argparse (readin things typed after the command)
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("path")
args = parser.parse_args()
print(args.path)

