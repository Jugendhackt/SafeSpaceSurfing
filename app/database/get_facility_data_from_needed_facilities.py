import json

facilities = json.load(open("default_facilities.json", "rt"))
all_facilities = json.load(open("facilities_koeln.geojson", "rt"))

new_object = []
i_newObject = 0



print(all_facilities["features"][1]["properties"])

for local_facility in facilities["Facilities"]:
    i_loop = 0
    for koeln_facility in all_facilities["features"]:
        i_loop = i_loop+1
        if koeln_facility["properties"]["@id"] == local_facility:
            print(local_facility + " found")
            new_object.append(all_facilities["features"][i_loop])
            i_newObject = 0

print(new_object)
with open("facility_to_compare.json", "w") as facilities_dumped:
    json.dump(new_object, facilities_dumped)
