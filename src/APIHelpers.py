import os
import json
class APIHelpers:

    def save_pretty_json(self, response_data, filepath):
        with open(filepath, "w") as file:
            json.dump(response_data, file, indent=2)

    def compare_jsons(self,json_path1, json_path2):
        try:
            with open(json_path2, 'r') as f2:
                data2 = json.load(f2)
            print("Comparison done")
            return json_path1 == data2
        except json.JSONDecodeError:
            print("Error: One or both files are not valid JSON.")
            return False
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False
