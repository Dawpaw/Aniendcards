<script lang="ts">
    import { Title } from "@smui/paper";
    import Textfield from "@smui/textfield";
    import IconButton from "@smui/icon-button";

    let endcard = {
        img_url: "",
        alt_img_url: "",
        source_url: "",
        episode_id: 0,
        artist_id: 0,
    };
</script>

<Title>Endcard</Title>

<Textfield bind:value={endcard.img_url} type="url" label="Image Url"
></Textfield>

<Textfield
    bind:value={endcard.alt_img_url}
    type="url"
    label="Alternative Image Url"
></Textfield>

<Textfield bind:value={endcard.source_url} type="url" label="Source Url"
></Textfield>

<Textfield bind:value={endcard.episode_id} label="Episode ID" type="number"
></Textfield>

<Textfield bind:value={endcard.artist_id} label="Artist ID" type="number"
></Textfield>

<div style="flex items-center">
    <IconButton class="material-icons" on:click={() => console.log(endcard)}
        >send</IconButton
    >
</div>
