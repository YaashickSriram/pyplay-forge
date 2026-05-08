import json

def find_null_values_path(data : dict, path = ""):
   result = []
   if isinstance(data, dict):
      for key, val in data.items():
         current_path = f"{path}.{key}" if path else key
         if val == None:
            result.append(current_path)
         elif isinstance(val, dict):
            print(f"recursing into {current_path}, value = {val}")
            result.extend(find_null_values_path(val, current_path))
   return result

if __name__ == "__main__":
   json_file_path = "test_data/sample.json"
   with open(json_file_path, 'r') as f:
      data = json.load(f)
      null_keys = find_null_values_path(data, )
      print(null_keys)