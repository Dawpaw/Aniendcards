const BASE_URL = import.meta.env.VITE_API_URL ?? 'http://localhost:8000';

async function get(path) {
	const res = await fetch(`${BASE_URL}${path}`);
	if (!res.ok) throw new Error(`API error ${res.status}: ${path}`);
	return res.json();
}

export const api = {
	// Media
	getAllMedia: () => get('/media/'),
	getMediaByTitle: (title) => get(`/media/${encodeURIComponent(title)}`),
	getMediaById: (id) => get(`/media/id/${id}`),

	// Artists
	getAllArtists: () => get('/artists/'),
	getArtistByUsername: (username) => get(`/artist/${encodeURIComponent(username)}`),
	getArtistById: (id) => get(`/artist/id/${id}`),

	// Endcards
	getAllEndcards: () => get('/endcards/'),
	getEndcardById: (id) => get(`/endcard/${id}`)
};
