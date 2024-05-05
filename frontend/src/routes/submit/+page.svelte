<script lang="ts">
    import Tab, { Label } from "@smui/tab";
    import TabBar from "@smui/tab-bar";
    import Submission from "./Submission.svelte";
    let active: string = "Media";
</script>

<div>
    <TabBar
        tabs={["Media", "Episode", "Endcard", "Artist"]}
        class="mt-2"
        let:tab
        bind:active
    >
        <Tab {tab}>
            <Label>{tab}</Label>
        </Tab>
    </TabBar>
</div>

<Submission typeSubmission={active}></Submission>
