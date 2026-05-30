import { api } from '$lib/api.js';

export async function load() {
	const media = await api.getAllMedia();
	return { media };
}
