import { error } from '@sveltejs/kit'; import type { PageLoad } from './$types';
export const load: PageLoad = async ({ params }) => {

    let animeId: number = Number(params.slug);
    if (isNaN(animeId)) {
        error(422, "422")
    }

    try {
        let media = await fetchMedia(animeId);

        return { media: media };

    } catch (e) {
        throw e;
    }
};


async function fetchMedia(mediaId: number) {
    const response = await fetch(
        `http://127.0.0.1:8000/media/${mediaId}`,
        {
            headers: {
                accept: "application/json",
            },
        },
    );

    if (!response.ok) {
        error(response.status, `${response.status}`)
    }
    const media = await response.json();
    return media;
}