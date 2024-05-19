import { error } from '@sveltejs/kit'; import type { PageLoad } from './$types';
export const load: PageLoad = async ({ params }) => {

    let artistId: number = Number(params.slug);
    if (isNaN(artistId)) {
        error(422, 'Invalid ID type')
    }

    try {
        let artist = await fetchMedia(artistId);

        return { artist: artist };

    } catch (e) {
        error(404, 'Not found'); // TODO change this
    }
};


async function fetchMedia(artistId: number) {
    const response = await fetch(
        `http://127.0.0.1:8000/artist/${artistId}`,
        {
            headers: {
                accept: "application/json",
            },
        },
    );

    if (!response.ok) {
        throw new Error("Error getting media");
    }
    const artist = await response.json();
    return artist;
}