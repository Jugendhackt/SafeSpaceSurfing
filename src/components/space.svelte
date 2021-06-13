<script>
import L,{La} from "leaflet";
import { getContext } from "svelte";

let mymap = getContext("leafletMapInstance")

let rawjson = {
    "type": "FeatureCollection",
    "features": []
}
L.Icon.Default.prototype.options.imagePath = "/static/icons/"
L.Icon.Default.prototype.options.iconUrl = "marker-icon.png"
L.Icon.Default.prototype.options.shadowUrl = "marker-shadow.png"

/*
mymap.on('zoom',()=>{
    console.log(mymap.getZoom()); 
})
*/
var admin_level = 6
var rel_id = 62578

fetch(`http://127.0.0.1:5000/api/v1/facilities/${admin_level}/relation/${rel_id}`)
.then(data => data.json())
.then(data => {
    data.forEach(async (space)=>{
    const osmId = space["osm_id"].split("/")
    fetch(`https://overpass-api.de/api/interpreter?data=[out:json][timeout:25];${osmId[0]}(${osmId[1]});out%20geom;`)
    .then(data => data.json())
    .then(data => data["elements"][0])
    .then(data =>{
            switch (data["type"]) {
                case "node":
                    var out_geo = {
                        "type": "Feature",
                        "properties": data["tags"],
                        "geometry": {
                            "type": "Point",
                            "coordinates": [data["lon"],data["lat"]] 
                        },
                    }
                    break
                
                case "way":
                    var coords = []
                    data["geometry"].forEach((p)=>{
                        coords.push([p["lon"],p["lat"]])
                    })
                    console.log(coords);
                    var out_geo = {
                        "type": "Feature",
                        "properties": data["tags"],
                        "geometry": {
                            "type": "Polygon",
                            "coordinates": [coords]
                        },
                        "id":data["id"]
                    }
                    break
                default:
                    break;
            }
        L.geoJson(rawjson).addTo(mymap)
        console.log({"Out":out_geo});
        rawjson["features"].push(out_geo)
    }) 
})
})

var geojsonFeature = {
    "type": "Feature",
    "properties": {
        "name": "Coors Field",
        "amenity": "Baseball Stadium",
        "popupContent": "This is where the Rockies play!"
    },
    "geometry": {
        "type": "Point",
        "coordinates": [-104.99404, 39.75621]
    }
};


console.log( geojsonFeature);
console.log( rawjson["features"]);


</script>

<style>

</style>

