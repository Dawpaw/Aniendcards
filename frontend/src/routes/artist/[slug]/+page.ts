import { error } from '@sveltejs/kit'; import type { PageLoad } from './$types';
export const load: PageLoad = async ({ params }) => {

    let artistId: number = Number(params.slug);
    if (isNaN(artistId)) {
        error(422, "422")
    }

    try {
        let artist = await fetchMedia(artistId);

        return { artist: artist };

    } catch (e) {
        throw e;
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
        error(response.status, `${response.status}`)
    }
    const artist = await response.json();
    return artist;
}