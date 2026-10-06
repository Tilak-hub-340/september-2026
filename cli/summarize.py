import csv
import argparse
# 1. read the path from the command line
# 2. load the score column from the CSV
# 3. compute count, mean, min, max
# 4. print the result

def load_csv(path):
    values = []
    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            number = float(row["score"])
            values.append(number)
    return values        

def summarize(values):
    count = len(values)
    mean = sum(values)/count
    return {"mean": mean, 
            "min": min(values), 
            "max":max(values),
            "count": count}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()
    values = load_csv(args.path)
    result = summarize(values)
    for key, value in result.items():
        print(f"{key}: {value}")




if __name__ == "__main__":
    main()
