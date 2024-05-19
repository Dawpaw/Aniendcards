<script lang="ts">
    import Card, { Content, PrimaryAction, Media } from "@smui/card";

    export let endcard;
    export let episodeNumber: number | null = null;
    export let episodeDescription: string | null = null;

    let clicked = 0;
</script>

<div class="max-w-96 mt-8 ml-4">
    <Card>
        <div class="p4 mx-4">
            {#if episodeNumber !== null}
                <h2 class="mb-4 font-bold text-2xl pt-2">
                    Episode {episodeNumber} - {episodeDescription}
                </h2>
            {/if}
        </div>
        <PrimaryAction on:click={() => clicked++}>
            <Media
                style="background-image:url({endcard.img_url})"
                aspectRatio="16x9"
            />
        </PrimaryAction>
    </Card>
</div>
