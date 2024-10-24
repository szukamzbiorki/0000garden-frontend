<script setup>
	const ready = ref(false)
	const { currentRoute: route } = useRouter()

	onMounted(async () => {
		await document.fonts.ready
		ready.value = true
	})
</script>

<template>
	<div :class="['layout', { ready }]">
		<header>
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
	img {
		width: initial;
	}
	header {
		& > * {
			position: fixed;
			z-index: 2;
			user-select: none;
		}
		& > .mailinglist {
			top: var(--space-m);
			right: var(--space-m);
		}
		& > .back {
			top: var(--space-l);
			left: var(--space-m);
			@media screen and (max-width: 640px) {
				left: initial;
				right: var(--space-m);
			}
		}

		& > .top {
			top: var(--space-l);
			left: 50vw;
			transform: translateX(-50%);
			display: flex;
			flex-direction: column;
			gap: var(--space-xl);
			@media screen and (max-width: 640px) {
				left: var(--space-m);
				transform: translateX(0%);
			}
			& > .logo {
				& > * {
					height: 3.5rem;
					pointer-events: none;
				}
			}
		}
	}
</style>
