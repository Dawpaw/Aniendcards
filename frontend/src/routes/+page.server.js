import { api } from '$lib/api.js';

export async function load() {
	const [endcards, allMedia] = await Promise.all([
		api.getAllEndcards(),
		api.getAllMedia()
	]);

	// Build a lookup for media title from endcard → entry → media
	// The endcard response has artist but not entry/media, so we derive from allMedia
	const endcardMediaMap = buildEndcardMediaMap(allMedia);

	return {
		// Latest 12 endcards
		endcards: endcards.slice(-12).reverse(),
		// Latest 8 media
		media: allMedia.slice(-8).reverse(),
		endcardMediaMap
	};
}

/**
 * Build a map of endcard_id → { mediaTitle, entryNumber }
 * by walking media → entries → endcards
 * @param {Array} allMedia
 */
function buildEndcardMediaMap(allMedia) {
	/** @type {Record<number, { mediaTitle: string, entryNumber: number }>} */
	const map = {};
	for (const media of allMedia) {
		const title =
			media.titles.find((t) => t.language === 'english')?.title ??
			media.titles.find((t) => t.language === 'romaji')?.title ??
			media.titles[0]?.title ??
			'Unknown';
		for (const entry of media.entries ?? []) {
			for (const endcard of entry.endcards ?? []) {
				map[endcard.id] = { mediaTitle: title, entryNumber: entry.entry_number };
			}
		}
	}
	return map;
}
