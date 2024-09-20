<template>
	<div class="-type-m">
		{{ content.content }}
	</div>
</template>

<script setup>
	const props = defineProps({
		content: Object,
	})
</script>

<style lang="postcss" scoped>
	.specialtext-block {
		hyphens: none;
		color: var(--lightgrey);
	}
</style>
