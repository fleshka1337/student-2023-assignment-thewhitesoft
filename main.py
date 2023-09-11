import requests
import json
import os

url = "https://raw.githubusercontent.com/thewhitesoft/student-2023-assignment/main/data.json"
directory = os.path.dirname(os.path.realpath(__file__))
data_path = os.path.join(directory, "data.json")
replacement_path = os.path.join(directory, "replacement.json")
result_path = os.path.join(directory, "result.json")
dictionary = {}
final_result = []

with open(replacement_path, "r") as replacement_file:
    replacement_data = json.load(replacement_file)

data_response = requests.get("https://raw.githubusercontent.com/thewhitesoft/student-2023-assignment/main/data.json")
data1 = data_response.json()

for item in replacement_data:
    replacement = item.get("replacement")
    source = item.get("source")
    if replacement is not None:
        dictionary[replacement] = source

for message in data1:
    for replacement, source in dictionary.items():
        if source is not None:
            message = message.replace(replacement, source)
        else:
            message = message.replace(replacement, "")
    final_result.append(message)

question = input("Would you like to remove empty lines from the result? (yes / no): ").strip().lower()
if question == "yes":
    final_result = [line for line in final_result if line.strip()]

with open(result_path, "w") as result_file:
    json.dump(final_result, result_file, ensure_ascii=False, indent=4)

print("Result saved in result.json")