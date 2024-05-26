import { error } from '@sveltejs/kit';

export async function submitArtist(artist: any) {
    let response = await fetch("http://127.0.0.1:8000/artist", {
        method: "POST",
        body: JSON.stringify(artist),
        headers: {
            "Content-type": "application/json; charset=UTF-8",
        },
    });

    if (response.ok) {
        return await response.json();
    }

    return
}

export async function submitEpisode(mediaId: number, episode: any) {
    let response = await fetch(`http://127.0.0.1:8000/media/${mediaId}/episodes`, {
        method: "POST",
        body: JSON.stringify(episode),
        headers: {
            "Content-type": "application/json; charset=UTF-8",
        },
    });

    if (response.ok) {
        return await response.json();
    }

    return
}

export async function submitEndcard(endcard: any) {
    let response = await fetch("http://127.0.0.1:8000/endcards", {
        method: "POST",
        body: JSON.stringify(endcard),
        headers: {
            "Content-type": "application/json; charset=UTF-8",
        },
    });

    if (response.ok) {
        return await response.json();
    }

    return
}

export async function getArtist(username: string) {
    const response = await fetch(
        `http://127.0.0.1:8000/artist/?username=${username}`,
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

