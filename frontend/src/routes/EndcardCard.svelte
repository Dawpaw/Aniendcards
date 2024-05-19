<script lang="ts">
    import Card, { Content, PrimaryAction, Media } from "@smui/card";

    export let endcard;
    export let episodeNumber: number;
    export let episodeDescription: string;

    let clicked = 0;
</script>

<div class="max-w-96 mt-8 ml-4">
    <Card>
        <div class="p4 mx-4">
            <h2 class="mb-4 font-bold text-2xl pt-2">
                Episode {episodeNumber} - {episodeDescription}
            </h2>
        </div>
        <PrimaryAction on:click={() => clicked++}>
            <Media
                style="background-image:url({endcard.img_url})"
                aspectRatio="16x9"
            />
        </PrimaryAction>
    </Card>
</div>
