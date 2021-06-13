import json
from os import name

def checkKey(dict, key):
      
    if key in dict.keys():
        print("Present, ", end =" ")
        print("value =", dict[key])
        return True
    else:
        print("Not present")
        return False

dataset = json.load(open("data.json"))
data_of_all_facilities = json.load(open("facilities_koeln.geojson"))
new_dataset = []
new_dataset = dataset
print(dataset)
for key, data in dataset.items():
    for facility in data_of_all_facilities["features"]:
        if key == facility["properties"]["@id"]:
            if checkKey(facility["properties"], "name"):
                print(facility["properties"]["name"])
                facility_name = {}
                facility_name["name"] = facility["properties"]["name"]
                facility_name["relations"] = data
                dataset[key] = facility_name
            else:
                facility_info = {}
                facility_info["relations"] = data
                dataset[key] = facility_info

print(new_dataset)
with open("new_dataset.json", "w") as data_dumped:
    json.dump(new_dataset, data_dumped)
