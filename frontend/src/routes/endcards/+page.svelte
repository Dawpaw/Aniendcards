<script>
	import EndcardCard from '$lib/components/EndcardCard.svelte';

	let { data } = $props();
</script>

<svelte:head>
	<title>Endcards — Aniendcards</title>
</svelte:head>

<div class="max-w-6xl mx-auto px-4 py-10">
	<h1 class="text-3xl font-display font-semibold text-[var(--color-ink)] mb-8">All Endcards</h1>

	{#if data.endcards.length === 0}
		<p class="text-[var(--color-ink-muted)]">No endcards in the database yet.</p>
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
</div>
