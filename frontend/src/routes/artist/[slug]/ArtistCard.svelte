<script lang="ts">
    export let artist;
    import { getHostname } from "$lib/utils";
</script>

<div class="max-w-64 mt-8 ml-4">
    <p class="mb-4 font-bold text-2xl pt-2 text-center">{artist.username}</p>
    <div class="text-center">
        <div>
            <p class="font-semibold my-2">Links</p>
            {#each artist.links as links}
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
