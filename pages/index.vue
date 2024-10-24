<template>
	<div class="page index" :class="[{ active: active }]">
		<Transition name="gradient">
			<PagesSignUp v-show="!active"></PagesSignUp>
		</Transition>
		<PagesArchive></PagesArchive>
		<div class="info" v-show="!mobile">
			<NuxtLink to="/info" class="additional">Additional Information</NuxtLink>
			<div class="additional">info@0000.garden</div>
			<div class="powered">
				Garden is powered by
				<NuxtLink to="https://00316.agency" class="additional">00316.agency</NuxtLink>
			</div>
		</div>
		<div class="info left" v-show="!mobile">
			<div class="additional">{{ data.home.tagline }}</div>
		</div>
		<ElementsControlBar></ElementsControlBar>
	</div>
</template>

<script setup>
	import 'animate.css'
	const { mobile } = useScreenSize()

	const query = groq`{
		'home': *[_type == "home"]{tagline}[0]
	}`
	const sanity = useSanity()
	const { data } = await useAsyncData(() => sanity.fetch(query))

	const active = useActive()
</script>

<style scoped lang="postcss">
	.page {
		& > * {
			position: absolute;
		}
		@media screen and (max-width: 640px) {
			&.index {
				max-height: 100vh;
				& > .archive {
					opacity: 1;
				}
			}
		}

		& > .archive {
			opacity: 1;
		}

		& > .info {
			bottom: var(--space-m);
			right: var(--space-m);
			display: flex;
			flex-direction: row;
			gap: var(--space-l);
			font-size: var(--type-s);
			line-height: var(--type-s-leading);
			z-index: 33;
			color: var(--darkgrey);
			& a {
				color: var(--lightgrey);
			}
		}

		& > .left {
			right: initial;
			left: var(--space-m);
		}

		& > .signup {
			position: relative;
			opacity: 1;
			top: 0;
			height: 100vh;
			z-index: 31;
		}
	}
</style>
