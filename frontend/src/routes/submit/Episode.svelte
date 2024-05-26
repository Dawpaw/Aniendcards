<script lang="ts">
    import { Title } from "@smui/paper";
    import Textfield from "@smui/textfield";
    import IconButton from "@smui/icon-button";

    let episode = {
        description: "",
        episode_number: 0,
    };
</script>

<Title>Episode</Title>

<Textfield bind:value={episode.description} label="Description"></Textfield>

<Textfield
    bind:value={episode.episode_number}
    label="Episode Number"
    type="number"
></Textfield>

<div style="flex items-center">
    <IconButton class="material-icons" on:click={() => console.log(episode)}
        >send</IconButton
    >
</div>
