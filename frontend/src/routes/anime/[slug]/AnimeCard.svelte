<script lang="ts">
    export let media;
    import { getHostname } from "$lib/utils";
</script>

<div class="max-w-64 mt-8 ml-4">
    <p class="mb-4 font-bold text-2xl pt-2 text-center">{media.title_romaji}</p>
    <img
        src={media.cover_image}
        alt="poster"
        class="object-contain rounded-lg"
    />

    <div class="text-center">
        <p class="font-semibold my-2">Description</p>
        <p class="line-clamp-4 text-justify">{media.description}</p>
        <p class="font-semibold my-2">Premier</p>
        <p>{media.season} {media.season_year}</p>
        <p class="font-semibold my-2">Format</p>
        <p>{media.format}</p>
        <p class="font-semibold my-2">Episodes</p>
        <p>{media.episodes_count}</p>

        <div>
            <p class="font-semibold my-2">Links</p>
            {#each media.external_links as links}
                <div>
                    <a
                        href={links.link}
                        class="font-normal hover:underline"
                        target="_blank"
                    >
                        <div class="text-cool-blue">
                            {getHostname(links.link)}
                        </div></a
                    >
                </div>
            {/each}
        </div>
    </div>
</div>
