<script>
	let { media } = $props();

	const title = $derived(
		media.titles.find((t) => t.language === 'english')?.title ??
		media.titles.find((t) => t.language === 'romaji')?.title ??
		media.titles[0]?.title ??
		'Unknown'
	);
</script>

<a
	href="/media/{media.id}"
	class="group block rounded-[var(--radius-card)] overflow-hidden bg-white shadow-sm hover:shadow-md transition-shadow"
>
	<div class="aspect-[3/4] overflow-hidden bg-[var(--color-sakura-light)]">
		<img
			src={media.cover_image}
			alt={title}
			class="w-full h-full object-cover transition-transform duration-300 group-hover:scale-105"
			loading="lazy"
		/>
	</div>
	<div class="p-3">
		<p class="text-sm font-semibold text-[var(--color-ink)] leading-tight line-clamp-2 font-display">{title}</p>
		{#if media.format}
			<p class="text-xs text-[var(--color-ink-muted)] mt-1">{media.format.replace('_', ' ')}</p>
		{/if}
	</div>
</a>
