<script>
	import { page } from '$app/stores';

	let menuOpen = $state(false);

	const links = [
		{ href: '/', label: 'Home' },
		{ href: '/media', label: 'Anime & Manga' },
		{ href: '/endcards', label: 'Endcards' }
	];
</script>

<nav class="sticky top-0 z-50 bg-white/80 backdrop-blur-md border-b border-[var(--color-border)]">
	<div class="max-w-6xl mx-auto px-4 h-14 flex items-center justify-between">
		<a href="/" class="font-display text-xl font-semibold text-[var(--color-ink)] tracking-tight">
			Ani<span class="text-[var(--color-sakura)]">endcards</span>
		</a>

		<!-- Desktop links -->
		<div class="hidden sm:flex items-center gap-6">
			{#each links as link}
				<a
					href={link.href}
					class="text-sm font-medium transition-colors
						{$page.url.pathname === link.href
						? 'text-[var(--color-ink)]'
						: 'text-[var(--color-ink-muted)] hover:text-[var(--color-ink)]'}"
				>
					{link.label}
				</a>
			{/each}
		</div>

		<!-- Mobile hamburger -->
		<button
			class="sm:hidden p-2 rounded-md text-[var(--color-ink-muted)]"
			onclick={() => (menuOpen = !menuOpen)}
			aria-label="Toggle menu"
		>
			<svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
				{#if menuOpen}
					<path d="M6 18L18 6M6 6l12 12" />
				{:else}
					<path d="M4 6h16M4 12h16M4 18h16" />
				{/if}
			</svg>
		</button>
	</div>

	<!-- Mobile menu -->
	{#if menuOpen}
		<div class="sm:hidden border-t border-[var(--color-border)] bg-white px-4 py-3 flex flex-col gap-3">
			{#each links as link}
				<a
					href={link.href}
					class="text-sm font-medium text-[var(--color-ink-muted)]"
					onclick={() => (menuOpen = false)}
				>
					{link.label}
				</a>
			{/each}
		</div>
	{/if}
</nav>
