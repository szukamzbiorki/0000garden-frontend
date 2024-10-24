<template>
	<NuxtLayout>
		<Transition name="gradient">
			<PagesSignUp v-show="!active"></PagesSignUp>
		</Transition>

		<PagesArchive :active="active" :route="route"></PagesArchive>
		<Transition name="fadebottom">
			<ElementsInfo
				v-if="!mobile && route.path == '/'"
				:tagline="data.home.tagline"
			></ElementsInfo>
		</Transition>
		<ElementsControlBar></ElementsControlBar>
		<NuxtPage></NuxtPage>
		<Cookie></Cookie>
	</NuxtLayout>
</template>

<script setup>
	const { mobile } = useScreenSize()
	const { currentRoute: route } = useRouter()
	const query = groq`{
	'home': *[_type == "home"]{tagline}[0]
	}`
	const sanity = useSanity()
	const { data } = await useAsyncData(() => sanity.fetch(query))
	const active = useActive()
</script>

<style lang="postcss" scoped>
	.layout {
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

		& > & > .left {
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
