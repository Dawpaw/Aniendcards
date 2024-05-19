<script lang="ts">
    import Card, { Content, PrimaryAction, Media } from "@smui/card";
    import { onMount } from "svelte";

    import EndcardCardLazy from "./EndcardCardLazy.svelte";

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
    The best Endcards in town
</h1>

<div class="container m-auto grid grid-cols-4">
    {#each endcards as endcard}
        <EndcardCardLazy {endcard} />
    {/each}
</div>
