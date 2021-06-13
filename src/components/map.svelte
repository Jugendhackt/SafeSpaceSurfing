<script>
    import L, { DomEvent } from "leaflet";
    import { setContext, getContext, onMount } from "svelte";

    let mymap;
    let mapContainer;
    
    mymap = L.map(L.DomUtil.create("div"),{
        center:[50.9290019,6.9582040],
        zoom: 10
    });
    
    setContext("leafletMapInstance",mymap);

    L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution:
        'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>',
    }).addTo(mymap);

    onMount(()=>{
        mapContainer.appendChild(mymap.getContainer());
        mymap.getContainer().style.width = '100%';
		mymap.getContainer().style.height = '100%';
		mymap.invalidateSize();
    })

</script>

<style>
    .map{
        height: 100vh;
        width: 100vw;
    }
</style>

<svelte:head>
    <link 
        rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css"
        integrity="sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A=="
        crossorigin=""
    />
</svelte:head>

<div class="map" bind:this={mapContainer}>
    <slot></slot>
</div>
