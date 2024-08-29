<template>
	<div class="-type-l" :class="[content.font]">
		{{ content.content }}
	</div>
</template>

<script setup>
	const props = defineProps({
		content: Object,
	})
</script>

<style lang="postcss" scoped>
	.bigtext-block {
		hyphens: none;
		padding: 0 var(--space-m);
	}
</style>
