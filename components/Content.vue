<script setup>
	const props = defineProps({
		sections: Array,
	})

	const components = new Map([
		['smalltext', resolveComponent('LazyBlocksText')],
		['bigtext', resolveComponent('LazyBlocksTextBig')],
		['bigimg', resolveComponent('LazyBlocksCarousel')],
		['video', resolveComponent('LazyBlocksVideo')],
	])

	const naming = new Map([
		['smalltext', 'text'],
		['bigtext', 'bigtext'],
		['bigimg', 'image'],
		['video', 'video'],
	])
</script>

<template>
	<div class="blocks">
		<component
			v-for="(comp, i) in sections"
			:is="components.get(comp._type)"
			:content="comp"
			:class="[
				`${naming.get(comp._type)}-block`,
				{ ['first-block']: i === 0, ['last-block']: i === sections.length - 1 },
			]"
		></component>
	</div>
</template>

<style lang="postcss" scoped>
	.blocks {
		/* max-width: 100vw;
		display: flex;
		flex-direction: column;
		gap: 4vw;
		@media screen and (max-width: 600px) {
			gap: 6vw;
		}
		& > * {
			max-width: 100vw;
		}

		& > .last-block {
			margin-bottom: 0 !important;
		} */
	}
</style>
