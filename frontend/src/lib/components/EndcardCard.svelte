<script>
	let { endcard, mediaTitle = '', entryNumber = null } = $props();
</script>

<a
	href="/endcards/{endcard.id}"
	class="group relative block rounded-[var(--radius-card)] overflow-hidden aspect-video bg-[var(--color-lavender-light)] shadow-sm hover:shadow-md transition-shadow"
>
	<img
		src={endcard.img_url}
		alt={mediaTitle || 'Endcard'}
		class="w-full h-full object-cover transition-transform duration-300 group-hover:scale-105"
		loading="lazy"
	/>
	<div class="absolute inset-0 bg-gradient-to-t from-[var(--color-ink)]/70 to-transparent
		opacity-0 group-hover:opacity-100 transition-opacity duration-200 flex flex-col justify-end p-3">
		{#if mediaTitle}
			<p class="text-white text-sm font-semibold font-display leading-tight">{mediaTitle}</p>
		{/if}
		{#if entryNumber !== null}
			<p class="text-white/80 text-xs mt-0.5">Episode {entryNumber}</p>
		{/if}
	</div>
</a>
