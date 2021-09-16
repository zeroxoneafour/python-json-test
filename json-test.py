# JSON test

import json

print("JSON test - reading file.json")

json_file = open("file.json", "r")

print("Contents of file.json - " + json_file.read())

json_object = json.load(json_file)

print("JSON value of num-1 - " + json_object["num-1"])
print("JSON value of str-1 - " + json_object["str-1"])
print("JSON values in array-1 - " + json_object["array-1"][0] + ", " + json_object["array-1"][1] + ", " + json_object["array-1"][2])

json_file.close()
