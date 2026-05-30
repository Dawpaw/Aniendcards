<script>
	import '../app.css';
	import Navbar from '$lib/components/Navbar.svelte';
	import Footer from '$lib/components/Footer.svelte';

	let { children } = $props();
</script>

<svelte:head>
	<title>Aniendcards</title>
	<meta name="description" content="A community database of anime endcard art" />
</svelte:head>

<div class="min-h-screen flex flex-col bg-[var(--color-cream)]">
	<Navbar />
	<main class="flex-1">
		{@render children()}
	</main>
	<Footer />
</div>
