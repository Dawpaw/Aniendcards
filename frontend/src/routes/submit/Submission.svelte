<script lang="ts">
    import Paper, { Title, Content } from "@smui/paper";

    import Media from "./MediaSubmit.svelte";
    import Artist from "./Artist.svelte";
    import Episode from "./Episode.svelte";
    import EndcardSubmit from "./EndcardSubmit.svelte";

    export let typeSubmission: string;
</script>

<Paper class="grid grid-cols-1 gap-4 max-w-xl">
    {#if typeSubmission === "Media"}
        <Media />
    {:else if typeSubmission === "Episode"}
        <Episode />
    {:else if typeSubmission === "Endcard"}
        <EndcardSubmit />
    {:else if typeSubmission === "Artist"}
        <Artist />
    {/if}
</Paper>
