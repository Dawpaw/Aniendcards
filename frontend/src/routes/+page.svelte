<script>
	import EndcardCard from '$lib/components/EndcardCard.svelte';
	import MediaCard from '$lib/components/MediaCard.svelte';

	let { data } = $props();
</script>

<svelte:head>
	<title>Aniendcards — Anime Endcard Database</title>
</svelte:head>

<!-- Hero -->
<section class="max-w-6xl mx-auto px-4 pt-14 pb-10">
	<h1 class="text-4xl sm:text-5xl font-display font-semibold text-[var(--color-ink)] leading-tight max-w-xl">
		Every <em>endcard</em>,<br />collected.
	</h1>
	<p class="mt-4 text-[var(--color-ink-muted)] text-lg max-w-md">
		A community database celebrating the artists behind anime ending card illustrations.
	</p>
</section>

<!-- Latest Endcards -->
<section class="max-w-6xl mx-auto px-4 pb-14">
	<h2 class="text-xl font-display font-semibold text-[var(--color-ink)] mb-5">Latest Endcards</h2>
	{#if data.endcards.length === 0}
		<p class="text-[var(--color-ink-muted)] text-sm">No endcards yet.</p>
	{:else}
		<div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-3 sm:gap-4">
			{#each data.endcards as endcard (endcard.id)}
				{@const info = data.endcardMediaMap[endcard.id]}
				<EndcardCard
					{endcard}
					mediaTitle={info?.mediaTitle ?? ''}
					entryNumber={info?.entryNumber ?? null}
				/>
			{/each}
		</div>
	{/if}
</section>

<!-- Divider -->
<div class="max-w-6xl mx-auto px-4">
	<hr class="border-[var(--color-border)]" />
</div>

<!-- Latest Media -->
<section class="max-w-6xl mx-auto px-4 py-14">
	<h2 class="text-xl font-display font-semibold text-[var(--color-ink)] mb-5">Latest Titles</h2>
	{#if data.media.length === 0}
		<p class="text-[var(--color-ink-muted)] text-sm">No media yet.</p>
	{:else}
		<div class="grid grid-cols-3 sm:grid-cols-4 lg:grid-cols-8 gap-3 sm:gap-4">
			{#each data.media as media (media.id)}
				<MediaCard {media} />
			{/each}
		</div>
	{/if}
</section>
