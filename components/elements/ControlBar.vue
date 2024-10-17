<template>
	<div class="controls">
		<div class="bar" :class="{ active: hash != 'signup' }">
			<div @click.prevent="hash = 'signup'" ref="signup" class="signup">SignUp</div>
			<div @click.prevent="hash = 'archive'" ref="archive" class="archive">Archive</div>
			<div class="slider"></div>
		</div>
	</div>
</template>

<script setup>
	const props = defineProps({
		active: Boolean,
	})

	const hash = ref('signup')

	const signup = useTemplateRef('signup')
	const archive = useTemplateRef('archive')

	const { width: signupWidth } = useElementSize(signup)
	const { width: archiveWidth } = useElementSize(archive)

	const sliderWidth = computed(() =>
		hash.value == 'signup' ? signupWidth.value + 'px' : archiveWidth.value + 'px'
	)
</script>

<style lang="postcss" scoped>
	.controls {
		position: fixed;
		top: var(--space-m);
		right: var(--space-m);
		width: fit-content;
		background-color: rgba(255, 255, 255, 0.679);
		color: var(--darkgrey);
		z-index: 100;
		padding: var(--space-s);
		border-radius: var(--border-radius);
		& > .bar {
			padding: 0 var(--space-s);
			display: flex;
			flex-direction: row;
			gap: var(--space-l);
			justify-content: space-between;
			& > .slider {
				position: fixed;
				background-color: pink;
				top: var(--space-m);
				right: var(--space-m);
				pointer-events: none;
				width: v-bind(sliderWidth);
				height: calc(1rem + 2 * var(--space-s));
				border-radius: var(--border-radius);
				background-color: rgba(150, 150, 150, 0.25);
				box-sizing: content-box;
				padding: 0 var(--space-m);
				z-index: 120;
				transition: width 0.6s ease, left 0.7s ease-in-out, right 0.5s ease;
			}
			&.active {
				& > .slider {
					left: calc(100vw - (3 * var(--space-m)) - v-bind(sliderWidth));
				}
			}
		}
	}
</style>
