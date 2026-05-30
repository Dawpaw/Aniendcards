import { api } from '$lib/api.js';
import { error } from '@sveltejs/kit';

export async function load({ params }) {
	const id = Number(params.id);
	if (isNaN(id)) error(404, 'Not found');

	const [endcard, allMedia] = await Promise.all([api.getEndcardById(id), api.getAllMedia()]);

	// Find which media/entry this endcard belongs to
	let mediaRef = null;
	let entryRef = null;
	for (const media of allMedia) {
		for (const entry of media.entries ?? []) {
			if (entry.endcards.some((e) => e.id === id)) {
				mediaRef = media;
				entryRef = entry;
				break;
			}
		}
		if (mediaRef) break;
	}

	return { endcard, media: mediaRef, entry: entryRef };
}
