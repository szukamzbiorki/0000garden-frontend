<template>
	<div class="info">
		<div class="left" v-show="!mobile">
			<div class="additional">{{ tagline }}</div>
		</div>
		<div class="right" v-show="!mobile">
			<NuxtLink to="/info" class="additional">Additional Information</NuxtLink>
			<div class="additional">info@0000.garden</div>
			<div class="powered">
				Garden is powered by
				<NuxtLink to="https://00316.agency" class="additional">00316.agency</NuxtLink>
			</div>
		</div>
	</div>
</template>

<script setup>
	const { mobile } = useScreenSize()
	const props = defineProps({
		tagline: String,
	})
</script>

<style lang="postcss" scoped>
	.info {
		position: fixed;
		bottom: var(--space-m);
		right: var(--space-m);
		display: flex;
		flex-direction: row;
		justify-content: space-between;
		width: var(--width-m);
		font-size: var(--type-s);
		line-height: var(--type-s-leading);
		z-index: 33;
		& > div {
			&.right {
				display: flex;
				flex-direction: row;
				gap: var(--space-l);
			}
			color: var(--darkgrey);
			& a {
				color: var(--lightgrey);
			}
		}
	}
</style>
