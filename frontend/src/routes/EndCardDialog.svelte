<script lang="ts">
    import { error } from "@sveltejs/kit";
    import { onMount } from "svelte";
    import Dialog, { Actions, Content, Header, Title } from "@smui/dialog";
    import IconButton from "@smui/icon-button";
    import yt_source from "$lib/assets/yt_source.webp";
    import yt_anime from "$lib/assets/yt_anime.webp";
    import yt_drawing from "$lib/assets/yt_drawing.webp";

    export let open: boolean;
    export let endcard: any = null;
    export let endcardId = null; // Change this when changing the backend

    async function fetchEndcard(endcardId: number) {
        const response = await fetch(
            `http://127.0.0.1:8000/endcards/${endcardId}`,
            {
                headers: {
                    accept: "application/json",
                },
            },
        );

        if (!response.ok) {
            error(response.status, `${response.status}`);
        }
        const endcard = await response.json();
        return endcard;
    }

    onMount(async () => {
        if (endcard !== null) {
            return;
        }
        if (endcardId !== null) {
            endcard = await fetchEndcard(endcardId);
        }
    });
</script>

{#if endcard}
    <Dialog bind:open fullscreen>
        <Header>
            <Title></Title>
            <IconButton action="close" class="material-icons">close</IconButton>
        </Header>
        <Content>
            <div class="m-auto grid grid-cols-5 gap-3">
                <div
                    class="col-span-4 align-middle flex justify-center items-center"
                >
                    <img src={endcard.img_url} alt="poster" />
                </div>
                <div class="grid grid-cols-1">
                    <div>
                        <p class="font-semibold my-2">Source</p>
                        <a
                            href={endcard.source_url}
                            class="font-normal hover:underline"
                            target="_blank"
                        >
                            <img
                                class="object-contain max-h-48 w-auto"
                                alt="Artist"
                                src={yt_source}
                            /></a
                        >
                    </div>

                    <div>
                        <p class="font-semibold my-2">Anime</p>
                        <a
                            href="/anime/{endcard.episode.media_id}"
                            class="font-normal hover:underline"
                            target="_blank"
                        >
                            <img
                                class="object-contain max-h-48 w-auto"
                                alt="Artist"
                                src={yt_anime}
                            /></a
                        >
                    </div>

                    <div>
                        <p class="font-semibold my-2">Artist</p>
                        <a
                            href="/artist/{endcard.artist_id}"
                            class="font-normal hover:underline"
                            target="_blank"
                        >
                            <img
                                class="object-contain max-h-48 w-auto"
                                alt="Artist"
                                src={yt_drawing}
                            />
                        </a>
                    </div>
                </div>
            </div>
        </Content>
    </Dialog>
{/if}
