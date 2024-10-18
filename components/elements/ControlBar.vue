<template>
	<div class="controls">
		<div class="bar" :class="{ active: active }">
			<div @click.prevent="active = false" ref="signup" class="signup">Newsletter</div>
			<div @click.prevent="active = true" ref="archive" class="archive">Archive</div>
			<div class="slider"></div>
		</div>
	</div>
</template>

<script setup>
	const active = useActive()

	const hash = ref('signup')

	const signup = useTemplateRef('signup')
	const archive = useTemplateRef('archive')

	const { width: signupWidth } = useElementSize(signup)
	const { width: archiveWidth } = useElementSize(archive)
	const archiveWidthPx = computed(() => archiveWidth.value + 'px')

	const sliderWidth = computed(() =>
		active.value == false ? signupWidth.value + 'px' : archiveWidth.value + 'px'
	)
</script>

<style lang="postcss" scoped>
	.controls {
		position: fixed;
		top: var(--space-m);
		right: var(--space-m);
		width: fit-content;
		background-color: rgba(255, 255, 255, 0.679);

		z-index: 100;
		padding: var(--space-s);
		border-radius: var(--border-radius);
		cursor: pointer;
		user-select: none;
		& > .bar {
			padding: 0 var(--space-s);
			display: flex;
			flex-direction: row;
			gap: var(--space-l);
			justify-content: space-between;
			color: var(--darkgrey);
			transition: color 0.6s ease;
			&.active {
				color: white;
			}
			& > .slider {
				position: fixed;
				background-color: pink;
				top: calc(var(--space-m));
				right: calc((3 * var(--space-m)) + v-bind(archiveWidthPx) + 2px);
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
					right: var(--space-m);
				}
			}
		}
	}
</style>
