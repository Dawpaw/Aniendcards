<script>
    import "../app.css";
    import Banner, { Label, Icon } from "@smui/banner";
    import Button from "@smui/button";
</script>

<Banner open autoClose={false}>
    <Icon slot="icon" class="material-icons" color="primary">tv</Icon>
    <Label slot="label"><div class="font-bold">AniEndcard</div></Label>
    <svelte:fragment slot="actions">
        <Button href="/" class="mx-8">Home</Button>
        <Button href="/submit" class="mx-8">Submit</Button>
    </svelte:fragment>
</Banner>

<slot />
