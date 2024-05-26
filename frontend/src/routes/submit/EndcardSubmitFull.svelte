<script lang="ts">
    import { Title } from "@smui/paper";
    import Textfield from "@smui/textfield";
    import IconButton from "@smui/icon-button";
    import Snackbar, { Actions, Label } from "@smui/snackbar";
    import {
        submitArtist,
        getArtist,
        submitEndcard,
        submitEpisode,
    } from "./api";

    let snackbarWithClose: Snackbar;

    let mediaId: number = 0;

    let endcard = {
        img_url: "",
        alt_img_url: "",
        source_url: "",
        episode_id: 0,
        artist_id: 0,
    };

    let episode = {
        description: "",
        episode_number: 0,
    };

    let artist = {
        username: "",
    };

    async function submit(endcard: any, episode: any, artist: any) {
        // First create or find the artist
        try {
            artist = await getArtist(artist.username);
        } catch (error) {
            artist = await submitArtist(artist);
        }

        // Second create the episode
        episode = await submitEpisode(mediaId, episode);
        endcard.episode_id = episode.id;
        endcard.artist_id = artist.id;

        // Third create the endcard
        endcard = await submitEndcard(endcard);
    }
</script>

<Title>Media</Title>

<Textfield bind:value={mediaId} label="Media ID" type="number"></Textfield>

<Title>Endcard</Title>

<Textfield bind:value={endcard.img_url} type="url" label="Image Url"
></Textfield>

<Textfield
    bind:value={endcard.alt_img_url}
    type="url"
    label="Alternative Image Url"
></Textfield>

<Textfield bind:value={endcard.source_url} type="url" label="Source Url"
></Textfield>

<Title>Episode</Title>

<Textfield bind:value={episode.description} label="Description"></Textfield>

<Textfield
    bind:value={episode.episode_number}
    label="Episode Number"
    type="number"
></Textfield>

<Title>Artist</Title>
<Textfield bind:value={artist.username} label="Username"></Textfield>

<div style="flex items-center">
    <IconButton
        class="material-icons"
        on:click={async () => {
            await submit(endcard, episode, artist);
            snackbarWithClose.open();
        }}>send</IconButton
    >
</div>

<!-- TODO change this -->
<Snackbar bind:this={snackbarWithClose}>
    <Label>Submitted</Label>
    <Actions>
        <IconButton class="material-icons" title="Dismiss">close</IconButton>
    </Actions>
</Snackbar>
