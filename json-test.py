# JSON test

import json

print("JSON test - reading file.json")

with open("file.json", "r") as json_file:
    json_contents = json_file.read()
    json_file.close()

print("Contents of file.json - " + json_contents)

json_object = json.loads(json_contents)

print("JSON value of num-1 - " + str(json_object["num-1"]))
print("JSON value of str-1 - " + json_object["str-1"])
print("JSON values in array-1 - " + str(json_object["array-1"][0]) + ", " + json_object["array-1"][1] + ", " + str(json_object["array-1"][2]))
