<script>
	let { data } = $props();

	const media = $derived(data.media);

	const title = $derived(
		media.titles.find((t) => t.language === 'english')?.title ??
		media.titles.find((t) => t.language === 'romaji')?.title ??
		media.titles[0]?.title ??
		'Unknown'
	);

	const altTitles = $derived(media.titles.filter((t) => t.title !== title));
</script>

<svelte:head>
	<title>{title} — Aniendcards</title>
</svelte:head>

<div class="max-w-6xl mx-auto px-4 py-10">

	<!-- Media header -->
	<div class="flex flex-col sm:flex-row gap-6 mb-10">
		<img
			src={media.cover_image}
			alt={title}
			class="w-32 sm:w-40 rounded-[var(--radius-card)] shadow-md object-cover self-start"
		/>
		<div class="flex-1 min-w-0">
			<h1 class="text-3xl font-display font-semibold text-[var(--color-ink)] leading-tight">{title}</h1>
			{#if altTitles.length > 0}
				<p class="text-sm text-[var(--color-ink-muted)] mt-1">
					{altTitles.map((t) => t.title).join(' · ')}
				</p>
			{/if}
			<div class="flex flex-wrap gap-2 mt-3">
				{#if media.format}
					<span class="text-xs px-2 py-1 rounded-full bg-[var(--color-sakura-light)] text-[var(--color-ink)]">
						{media.format.replace('_', ' ')}
					</span>
				{/if}
				{#if media.season && media.season_year}
					<span class="text-xs px-2 py-1 rounded-full bg-[var(--color-lavender-light)] text-[var(--color-ink)]">
						{media.season} {media.season_year}
					</span>
				{/if}
			</div>
			{#if media.description}
				<p class="mt-4 text-sm text-[var(--color-ink-muted)] leading-relaxed max-w-prose">{media.description}</p>
			{/if}
			{#if media.links && media.links.length > 0}
				<div class="flex flex-wrap gap-3 mt-4">
					{#each media.links as link}
						<a
							href={link.link}
							target="_blank"
							rel="noopener noreferrer"
							class="text-xs text-[var(--color-moss)] hover:underline"
						>
							{new URL(link.link).hostname}
						</a>
					{/each}
				</div>
			{/if}
		</div>
	</div>

	<!-- Entries table -->
	<h2 class="text-xl font-display font-semibold text-[var(--color-ink)] mb-4">Episodes & Endcards</h2>

	{#if !media.entries || media.entries.length === 0}
		<p class="text-[var(--color-ink-muted)] text-sm">No entries yet.</p>
	{:else}
		<div class="rounded-[var(--radius-card)] border border-[var(--color-border)] overflow-hidden">
			<table class="w-full text-sm">
				<thead class="bg-[var(--color-sakura-light)]">
					<tr>
						<th class="px-4 py-3 text-left font-semibold text-[var(--color-ink)] w-24">#</th>
						<th class="px-4 py-3 text-left font-semibold text-[var(--color-ink)]">Description</th>
						<th class="px-4 py-3 text-left font-semibold text-[var(--color-ink)]">Endcard(s)</th>
					</tr>
				</thead>
				<tbody>
					{#each media.entries as entry, i (entry.id)}
						<tr class="border-t border-[var(--color-border)] {i % 2 === 0 ? '' : 'bg-[var(--color-surface-raised)]'}">
							<td class="px-4 py-3 text-[var(--color-ink-muted)] font-mono">{entry.entry_number}</td>
							<td class="px-4 py-3 text-[var(--color-ink)]">{entry.description}</td>
							<td class="px-4 py-3">
								<div class="flex flex-wrap gap-2">
									{#each entry.endcards as endcard}
										<a href="/endcards/{endcard.id}" class="block">
											<img
												src={endcard.img_url_small}
												alt="Endcard"
												class="w-16 h-10 object-cover rounded-md hover:opacity-80 transition-opacity"
												loading="lazy"
											/>
										</a>
									{/each}
								</div>
							</td>
						</tr>
					{/each}
				</tbody>
			</table>
		</div>
	{/if}
</div>
