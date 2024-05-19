<script lang="ts">
    import type { PageData } from "./$types";

    import EndcardCard from "../../EndcardCard.svelte";
    import ArtistCard from "./ArtistCard.svelte";

    export let data: PageData;
</script>

<div class="grid grid-cols-5 gap-3">
    <div class="pl-2">
        <ArtistCard artist={data.artist} />
    </div>

    <div class="col-span-4 pr-4">
        <div class="container m-auto grid grid-cols-4">
            {#each data.artist.endcards as endcard}
                <EndcardCard {endcard} />
            {/each}
        </div>
    </div>
</div>
