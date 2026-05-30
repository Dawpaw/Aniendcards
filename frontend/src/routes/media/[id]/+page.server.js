import { api } from '$lib/api.js';
import { error } from '@sveltejs/kit';

export async function load({ params }) {
	const id = Number(params.id);
	if (isNaN(id)) error(404, 'Not found');

	const media = await api.getMediaById(id);
	return { media };
}
