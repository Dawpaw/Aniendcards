<script>
	import MediaCard from '$lib/components/MediaCard.svelte';

	let { data } = $props();
</script>

<svelte:head>
	<title>Anime & Manga — Aniendcards</title>
</svelte:head>

<div class="max-w-6xl mx-auto px-4 py-10">
	<h1 class="text-3xl font-display font-semibold text-[var(--color-ink)] mb-8">Anime & Manga</h1>

	{#if data.media.length === 0}
		<p class="text-[var(--color-ink-muted)]">No titles in the database yet.</p>
	{:else}
		<div class="grid grid-cols-3 sm:grid-cols-4 md:grid-cols-5 lg:grid-cols-7 gap-3 sm:gap-4">
			{#each data.media as media (media.id)}
				<MediaCard {media} />
			{/each}
		</div>
	{/if}
</div>
