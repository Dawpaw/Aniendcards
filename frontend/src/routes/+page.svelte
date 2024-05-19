<script lang="ts">
    import Card, { Content, PrimaryAction, Media } from "@smui/card";
    import { onMount } from "svelte";

    let clicked = 0;
    let endcards: any[] = [];

    async function fetchEndcards() {
        const response = await fetch(
            "http://127.0.0.1:8000/endcards/?skip=0&limit=100",
            {
                headers: {
                    accept: "application/json",
                },
            },
        );

        if (!response.ok) {
            throw new Error("Can't get Endcards");
        }
        const endcards = await response.json();
        return endcards;
    }

    onMount(async () => {
        endcards = await fetchEndcards();
    });
</script>

<h1
    class="mb-4 text-4xl text-center font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl dark:text-white"
>
    The best endcards in town
</h1>

<div class="container m-auto grid grid-cols-4">
    {#each endcards as endcard}
        <div class="max-w-96 mt-8 ml-4">
            <Card>
                <div class="p4 mx-4">
                    <h2 class="mb-4 font-bold text-2xl pt-2">
                        {endcard.episode.media.title_romaji}
                    </h2>
                    <h3 class="text-gray-500 mb-6 font-bold">
                        {endcard.artist.username}
                    </h3>
                </div>
                <PrimaryAction on:click={() => clicked++}>
                    <Media
                        style="background-image:url({endcard.img_url})"
                        aspectRatio="16x9"
                    />
                    <Content class=""
                        >Episode {endcard.episode.episode_number}</Content
                    >
                    <Content class="">{endcard.episode.description}</Content>
                </PrimaryAction>
            </Card>
        </div>
    {/each}
</div>
