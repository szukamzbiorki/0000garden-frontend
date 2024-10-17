<template>
	<div class="page index" :class="[{ active: active }]">
		<PagesSignUp></PagesSignUp>
		<PagesArchive></PagesArchive>
		<Transition name="fade">
			<div class="info" v-show="active && !mobile">
				<NuxtLink to="/info" class="additional">Additional Information</NuxtLink>
				<div class="additional">info@0000.garden</div>
				<div class="powered">
					Garden is powered by
					<NuxtLink to="https://00316.agency" class="additional">00316.agency</NuxtLink>
				</div>
			</div>
		</Transition>
		<!-- <ElementsControlBar v-show="mobile" :active="active"></ElementsControlBar> -->
	</div>
</template>

<script setup>
	import 'animate.css'
	const { mobile } = useScreenSize()
	//tak

	const { y } = useWindowScroll()

	const header = ref(null)
	const h = useElementSize(header)

	const passed = ref(false)

	onMounted(() => {
		setTimeout(() => {
			passed.value = true
		}, 3500)
	})

	const active = computed(() => (y.value > 0 ? true : false))

	const showImage = computed(() => {
		return active.value || passed.value
	})

	definePageMeta({
		name: 'indexah',
	})
</script>

<style scoped lang="postcss">
	.page {
		@media screen and (min-width: 640px) {
			min-height: calc(100vh + 1px);
			&.active {
				& > .signup {
					opacity: 0;
					top: -80vh;
					pointer-events: none;
				}
				& > .archive {
					/* top: 10vh; */
					opacity: 1;
				}
			}

			& > * {
				position: absolute;
				transition: top ease 0.5s, opacity 0.5s ease;
			}
		}
		@media screen and (max-width: 640px) {
			&.index {
				max-height: 100vh;
				& > .archive {
					/* top: 10vh; */
					opacity: 1;
				}
			}
		}

		& > .archive {
			opacity: 0;
		}

		& > .info {
			bottom: var(--space-m);
			right: var(--space-m);
			display: flex;
			flex-direction: row;
			gap: var(--space-l);
			font-size: var(--type-s);
			line-height: var(--type-s-leading);
		}

		& > .signup {
			opacity: 1;
			top: 0;
			height: 100vh;
			z-index: 31;
			--scale: 1;
			mask-image: linear-gradient(
				to top,
				rgba(255, 255, 255, 0) calc(var(--scale) * 0%),
				rgba(255, 255, 255, 0.5) calc(var(--scale) * 25%),
				rgba(255, 255, 255, 1) calc(var(--scale) * 50%),
				rgba(255, 255, 255, 1) calc(var(--scale) * 100%)
			);
		}
	}
</style>
