<template>
	<div class="controls">
		<div class="bar" :class="{ active: active }">
			<div @click.prevent="setActive(false)" ref="signup" class="signup">Newsletter</div>
			<div @click.prevent="setActive(true)" ref="archive" class="archive">Archive</div>
			<div class="slider"></div>
		</div>
	</div>
</template>

<script setup>
	const active = useActive()

	const signup = useTemplateRef('signup')
	const archive = useTemplateRef('archive')

	const { width: signupWidth } = useElementSize(signup)
	const { width: archiveWidth } = useElementSize(archive)
	const archiveWidthPx = computed(() => archiveWidth.value + 'px')

	function setActive(state) {
		active.value = state
	}

	const sliderWidth = computed(() =>
		active.value == false ? signupWidth.value + 'px' : archiveWidth.value + 'px'
	)
</script>

<style lang="postcss" scoped>
	.controls {
		position: fixed !important;
		top: var(--space-l);
		right: var(--space-m);
		width: fit-content;
		background-color: var(--transparent-grey);
		z-index: 100;
		padding: var(--space-s);
		border-radius: var(--border-radius);
		cursor: pointer;
		user-select: none;
		@media screen and (max-width: 640px) {
			/* font-size: var(--type-s); */
		}
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

			/* @media screen and (max-width: 640px) {
				gap: var(--space-m);
				flex-direction: column;
			} */
			& > .slider {
				position: fixed;
				background-color: pink;
				top: var(--space-l);
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
