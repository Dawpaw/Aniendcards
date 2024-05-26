<script lang="ts">
    import { page } from "$app/stores";
    import Button from "@smui/button";
    import { getReasonPhrase } from "http-status-codes";

    let getReason = (message: string) => {
        if (message == "Not Found") return "";
        return getReasonPhrase(message);
    };
</script>

<div class="flex justify-center">
    <div class="max-w-96 mt-8 ml-4 text-center">
        <div class="flex justify-center">
            <img
                src="https://files.catbox.moe/hr535a.jpg"
                alt="Not Found"
                class="object-contain rounded-lg"
            />
        </div>
        {#if $page.error}
            <div class="my-4 font-bold text-2xl pt-2">
                {$page.error.message}
                {getReason($page.error.message)}
            </div>
        {/if}
        <div class="text-gray-500 mb-6 font-semibold">
            No idea what you were looking for, but it won't work
        </div>
        <Button href="/" class="mx-8">Go back Home</Button>
    </div>
</div>
