import { api } from '$lib/api.js';

export async function load() {
	const [endcards, allMedia] = await Promise.all([api.getAllEndcards(), api.getAllMedia()]);

	const endcardMediaMap = buildEndcardMediaMap(allMedia);

	return { endcards, endcardMediaMap };
}

function buildEndcardMediaMap(allMedia) {
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
