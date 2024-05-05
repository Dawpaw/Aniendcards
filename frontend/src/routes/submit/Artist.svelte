<script lang="ts">
    import { Title } from "@smui/paper";
    import Textfield from "@smui/textfield";
    import IconButton from "@smui/icon-button";

    let artist = {
        username: "",
    };
</script>

<Title>Artist</Title>
<Textfield bind:value={artist.username} label="Username"></Textfield>

<div style="flex items-center">
    <IconButton class="material-icons" on:click={() => console.log(artist)}
        >send</IconButton
    >
</div>
