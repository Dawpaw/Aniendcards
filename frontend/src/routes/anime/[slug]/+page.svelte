<script lang="ts">
    import type { PageData } from "./$types";

    import EndcardCard from "../../EndcardCard.svelte";
    import AnimeCard from "./AnimeCard.svelte";

    export let data: PageData;
</script>

<div class="grid grid-cols-5 gap-3">
    <div class="pl-2">
        <AnimeCard media={data.media} />
    </div>

    <div class="col-span-4 pr-4">
        <div class="container m-auto grid grid-cols-4">
            {#each data.media.episodes as episode}
                {#each episode.endcards as endcard}
                    <EndcardCard
                        {endcard}
                        episodeNumber={episode.episode_number}
                        episodeDescription={episode.description}
                    />
                {/each}
            {/each}
        </div>
    </div>
</div>
