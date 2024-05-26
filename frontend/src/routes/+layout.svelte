<script>
    import "../app.css";
    import { goto } from "$app/navigation";
    import Banner, { Label, Icon } from "@smui/banner";
    import Button from "@smui/button";
</script>

<Banner open autoClose={false}>
    <Icon
        on:click={() => goto("/")}
        slot="icon"
        class="material-icons"
        color="primary">tv</Icon
    >
    <Label slot="label"
        ><a href="/"><div class="font-bold text-black">AniEndcard</div></a
        ></Label
    >
    <svelte:fragment slot="actions">
        <Button href="/" class="mx-8">Home</Button>
        <Button href="/submit" class="mx-8">Submit</Button>
    </svelte:fragment>
</Banner>

<slot />
