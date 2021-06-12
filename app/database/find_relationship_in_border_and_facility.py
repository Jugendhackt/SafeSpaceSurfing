import json
import shapely
import shapely.geometry

fs = json.load(open("facility_to_compare.json"))
bs = json.load(open("bounds_koeln.geojson"))

fg = [(shapely.geometry.shape(f["geometry"]), f["properties"]["@id"]) for f in fs]
bg = [(shapely.geometry.shape(f["geometry"]), f["properties"]["@id"], f["properties"]["admin_level"]) for f in bs["features"] if "admin_level" in f["properties"]]

fm = {}
for f in fg:
	for b in bg:
		if b[0].contains(f[0]):
			if f[1] not in fm:
				fm[f[1]] = {}
			fm[f[1]][b[2]] = b[1]

with open("data.json", "w") as data_dumped:
    json.dump(fm, data_dumped)

