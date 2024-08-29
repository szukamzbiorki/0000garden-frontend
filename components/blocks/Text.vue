<template>
	<div class="text-block" :class="[content.font, content.align]">
		<p class="-type-m block" v-for="block in content.contentblocks">
			{{ block.content }}
		</p>
	</div>
</template>

<script setup>
	const props = defineProps({
		content: Object,
	})
</script>

<style lang="postcss" scoped>
	.text-block {
		& > .block {
			max-width: calc(100vw / 12 * 5);
			text-wrap: wrap;
			font-family: inherit;
			margin-bottom: 1rem;
		}

		@media screen and (max-width: 600px) {
			& > .block {
				max-width: calc(100vw - 2 * var(--space-m));
				text-wrap: wrap;
				font-family: inherit;
			}
		}
	}
</style>
