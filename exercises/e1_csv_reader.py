import os
import csv

def load_users(filepath:str) -> dict:
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"CSV File not found : {filepath}")
    with open(file=filepath, mode='r', encoding='utf-8-sig') as file:
        read_csv = csv.DictReader(file)
        users = {row['id'] : row for row in read_csv}
        return users
    
if __name__ == "__main__":
  csv_path = "test_data/users.csv"
  data = load_users(csv_path)
  print(data)