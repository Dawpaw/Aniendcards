<script>
	let { data } = $props();

	const endcard = $derived(data.endcard);
	const media = $derived(data.media);
	const entry = $derived(data.entry);

	const mediaTitle = $derived(
		media
			? (media.titles.find((t) => t.language === 'english')?.title ??
			   media.titles.find((t) => t.language === 'romaji')?.title ??
			   media.titles[0]?.title ??
			   'Unknown')
			: null
	);
</script>

<svelte:head>
	<title>{mediaTitle ? `${mediaTitle} Ep. ${entry?.entry_number} Endcard` : 'Endcard'} — Aniendcards</title>
</svelte:head>

<div class="max-w-6xl mx-auto px-4 py-10">
	<div class="flex flex-col lg:flex-row gap-8">

		<!-- Image -->
		<div class="flex-1 min-w-0">
			<img
				src={endcard.img_url}
				alt={mediaTitle ?? 'Endcard'}
				class="w-full rounded-[var(--radius-card)] shadow-md object-contain max-h-[70vh]"
			/>
			{#if endcard.alt_img_url && endcard.alt_img_url !== endcard.img_url}
				<details class="mt-3">
					<summary class="text-sm text-[var(--color-ink-muted)] cursor-pointer select-none">Show alternate version</summary>
					<img
						src={endcard.alt_img_url}
						alt="Alternate version"
						class="mt-2 w-full rounded-[var(--radius-card)] shadow-sm object-contain"
					/>
				</details>
			{/if}
		</div>

		<!-- Info sidebar -->
		<aside class="lg:w-64 xl:w-72 shrink-0 flex flex-col gap-6">

			<!-- Artist -->
			<div>
				<h2 class="text-xs font-semibold uppercase tracking-widest text-[var(--color-ink-muted)] mb-2">Artist</h2>
				<p class="font-display font-semibold text-[var(--color-ink)]">{endcard.artist.username}</p>
				{#if endcard.artist.links && endcard.artist.links.length > 0}
					<div class="flex flex-col gap-1 mt-2">
						{#each endcard.artist.links as link}
							<a
								href={link.link}
								target="_blank"
								rel="noopener noreferrer"
								class="text-sm text-[var(--color-moss)] hover:underline truncate"
							>
								{new URL(link.link).hostname}
							</a>
						{/each}
					</div>
				{/if}
				<a
					href={endcard.source_url}
					target="_blank"
					rel="noopener noreferrer"
					class="inline-block mt-3 text-sm text-[var(--color-lavender)] hover:underline"
				>
					View source →
				</a>
			</div>

			<!-- Media -->
			{#if media}
				<div>
					<h2 class="text-xs font-semibold uppercase tracking-widest text-[var(--color-ink-muted)] mb-2">From</h2>
					<a href="/media/{media.id}" class="flex items-center gap-3 group">
						<img
							src={media.cover_image}
							alt={mediaTitle}
							class="w-10 h-14 object-cover rounded-md shadow-sm group-hover:opacity-80 transition-opacity"
						/>
						<div>
							<p class="font-display font-semibold text-[var(--color-ink)] leading-tight text-sm group-hover:underline">{mediaTitle}</p>
							{#if media.format}
								<p class="text-xs text-[var(--color-ink-muted)] mt-0.5">{media.format.replace('_', ' ')}</p>
							{/if}
						</div>
					</a>
				</div>
			{/if}

			<!-- Episode -->
			{#if entry}
				<div>
					<h2 class="text-xs font-semibold uppercase tracking-widest text-[var(--color-ink-muted)] mb-2">Episode</h2>
					<p class="text-[var(--color-ink)] font-medium">#{entry.entry_number}</p>
					{#if entry.description}
						<p class="text-sm text-[var(--color-ink-muted)] mt-1 leading-relaxed">{entry.description}</p>
					{/if}
				</div>
			{/if}

		</aside>
	</div>
</div>
