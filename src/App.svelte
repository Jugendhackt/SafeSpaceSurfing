<script>
	import Map from "./components/map.svelte";
	import Space from "./components/space.svelte";
</script>

<style>
	
</style>

<svelte:head>
	<link rel="stylesheet" href="/static/bundle.css">
	<link rel="stylesheet" href="/static/global.css">
</svelte:head>

<main>
	<Map>
		<Space></Space>
	</Map>
</main>