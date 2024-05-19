<script lang="ts">
    import Card, { Content, PrimaryAction, Media } from "@smui/card";

    export let endcard;

    let clicked = 0;
</script>

<div class="max-w-96 mt-8 ml-4">
    <Card>
        <div class="p4 mx-4">
            <a href="/anime/{endcard.episode.media_id}">
                <h2 class="mb-4 font-bold text-2xl pt-2 text-black">
                    {endcard.episode.media.title_romaji}
                </h2>
            </a>
            <h3 class="text-gray-500 mb-6 font-bold">
                {endcard.artist.username}
            </h3>
        </div>
        <PrimaryAction on:click={() => clicked++}>
            <Media
                style="background-image:url({endcard.img_url})"
                aspectRatio="16x9"
            />
            <Content class="">Episode {endcard.episode.episode_number}</Content>
            <Content class="">{endcard.episode.description}</Content>
        </PrimaryAction>
    </Card>
</div>
