<script lang="ts">
    import { Title } from "@smui/paper";
    import Textfield from "@smui/textfield";
    import Select, { Option } from "@smui/select";
    import IconButton from "@smui/icon-button";

    let media = {
        title_original: "",
        title_romaji: "",
        title_english: "",
        type: "ANIME",
        format: "TV",
        description: "",
        season: "WINTER",
        season_year: 0,
        episodes_count: 0,
        chapters_count: 0,
    };

    const mediaTypes = ["ANIME", "MANGA"];
    const mediaFormats = [
        "TV",
        "TV_SHORT",
        "MOVIE",
        "SPECIAL",
        "OVA",
        "ONA",
        "MUSIC",
        "MANGA",
        "NOVEL",
        "ONE_SHOT",
    ];

    const mediaSeasons = ["WINTER", "SPRING", "SUMMER", "FALL"];
</script>

<Title>Media</Title>
<Textfield bind:value={media.title_original} label="Original Title"></Textfield>
<Textfield bind:value={media.title_romaji} label="Original Romaji"></Textfield>
<Textfield bind:value={media.title_english} label="Original Title"></Textfield>

<Select
    key={(mediaType) => `${mediaType == null ? "ANIME" : mediaType}`}
    bind:value={media.type}
    label="Media Type"
>
    {#each mediaTypes as mediaType}
        <Option value={mediaType}>{mediaType}</Option>
    {/each}
</Select>

<Select
    key={(mediaFormat) => `${mediaFormat == null ? "TV" : mediaFormat}`}
    bind:value={media.format}
    label="Media Format"
>
    {#each mediaFormats as mediaFormat}
        <Option value={mediaFormat}>{mediaFormat}</Option>
    {/each}
</Select>

<Textfield bind:value={media.description} textarea label="Description"
></Textfield>

<Select
    key={(mediaSeason) => `${mediaSeason == null ? "WINTER" : mediaSeason}`}
    bind:value={media.season}
    label="Media Season"
>
    {#each mediaSeasons as mediaSeason}
        <Option value={mediaSeason}>{mediaSeason}</Option>
    {/each}
</Select>

<Textfield bind:value={media.season_year} label="Season Year" type="number"
></Textfield>

<Textfield bind:value={media.episodes_count} label="Episodes" type="number"
></Textfield>

<Textfield bind:value={media.chapters_count} label="Chapters" type="number"
></Textfield>

<div style="flex items-center">
    <IconButton class="material-icons" on:click={() => console.log(media)}
        >send</IconButton
    >
</div>
