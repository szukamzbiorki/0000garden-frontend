<script setup>
	const props = defineProps({
		sections: Array,
	})

	const components = new Map([
		['smalltext', resolveComponent('LazyBlocksText')],
		['bigtext', resolveComponent('LazyBlocksTextBig')],
		['bigimg', resolveComponent('LazyBlocksCarousel')],
		['video', resolveComponent('LazyBlocksVideoCopy')],
	])

	const naming = new Map([
		['smalltext', 'text'],
		['bigtext', 'bigtext'],
		['bigimg', 'image'],
		['video', 'video'],
	])
</script>

<template>
	<div class="content">
		<div class="blocks">
			<component
				v-for="(comp, i) in sections"
				:is="components.get(comp._type)"
				v-bind="comp._type == 'video' ? { ...comp } : { content: comp }"
				:class="[
					`${naming.get(comp._type)}-block`,
					{
						['first-block']: i === 0,
						['last-block']: i === sections.length - 1,
					},
				]"
			></component>
		</div>
		<NuxtLink to="/" class="back">Back to Overview</NuxtLink>
	</div>
</template>

<style lang="postcss" scoped>
	.blocks {
		& > *:not(.first-block) {
			margin-top: 2rem;
			&.image-block,
			.video-block {
				margin-top: 1rem;
			}
		}
	}
	.back {
		display: block;
		text-align: center;
		width: calc(100vw - 2 * var(--space-m));
		margin: var(--space-l) 0;
	}
</style>
