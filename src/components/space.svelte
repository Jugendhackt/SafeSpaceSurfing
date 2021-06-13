<script>
import L,{La} from "leaflet";
import { getContext } from "svelte";

let mymap = getContext("leafletMapInstance");
const ids = ["node/1726779295","way/35004878","way/246625456","way/25270980","node/2443427813",
    "node/1962552448",
    "node/1023190054",
    "node/352702446"]
let rawjson = {
    "type": "FeatureCollection",
    "features": []
}
L.Icon.Default.prototype.options.imagePath = "/static/icons/"
L.Icon.Default.prototype.options.iconUrl = "marker-icon.png"
L.Icon.Default.prototype.options.shadowUrl = "marker-shadow.png"

ids.forEach(async (id)=>{
    const osmId = id.split("/")
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
                        //"bbox": data["bounds"].map(makeCoordsToPoint),
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


//L.marker([47.439278,9.529174]).addTo(mymap).bindPopup("Willkommen in Heiden!").openPopup();

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

