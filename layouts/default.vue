<script setup>
	const ready = ref(false)
	const { currentRoute: route } = useRouter()

	// const { mobile } = useScreenSize()

	onMounted(async () => {
		await document.fonts.ready
		ready.value = true
	})
</script>

<template>
	<div :class="['layout', { ready }]">
		<header>
			<a href="https://0001.garden" class="mailinglist">Mailinglist</a>
			<Transition name="fade">
				<NuxtLink to="/" v-if="route.path != '/'" class="back">Back</NuxtLink>
			</Transition>
			<div class="top">
				<div class="logo" @click="scaled = !scaled">
					<img class="logo-img" src="/assets/garden-logo-ar.svg" alt="" srcset="" />
				</div>
			</div>
		</header>
		<slot />
	</div>
</template>

<style lang="postcss" scoped>
	header {
		& > * {
			position: fixed;
			z-index: 30;
			user-select: none;
		}
		& > .mailinglist {
			top: var(--space-m);
			right: var(--space-m);
		}
		& > .back {
			top: var(--space-m);
			left: var(--space-m);
		}
		& > .top {
			top: var(--space-m);
			left: 50vw;
			transform: translateX(-50%);
			display: flex;
			flex-direction: column;
			gap: var(--space-xl);
			& > .logo {
				& > * {
					height: 3.5rem;
					pointer-events: none;
				}
			}
		}
	}
</style>
