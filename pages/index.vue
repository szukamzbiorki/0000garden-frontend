<template>
	<div class="page" :class="[{ active: active }]">
		<PagesSignUp></PagesSignUp>
		<PagesArchive></PagesArchive>
	</div>
</template>

<script setup>
	import 'animate.css'
	const { mobile } = useScreenSize()

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

	// watch(y, (newY) => {
	// 	if (newY > 0) {
	// 		active.value = true
	// 	}
	// })

	const showImage = computed(() => {
		return active.value || passed.value
	})

	definePageMeta({
		name: 'indexah',
	})
</script>

<style scoped lang="postcss">
	.page {
		&.active {
			& > .signup {
				opacity: 0;
				top: -80vh;
				pointer-events: none;
			}
			& > .archive {
				top: 10vh;
				opacity: 1;
			}
		}
		& > * {
			position: absolute;
			transition: top ease 0.5s, opacity 0.5s ease;
		}

		& > .signup {
			opacity: 1;
			top: 0;
			height: 100vh;
			z-index: 60;
			/* mask-image: -webkit-gradient(
				linear,
				left 30%,
				left bottom,
				from(rgba(0, 0, 0, 1)),
				to(rgba(0, 0, 0, 0))
			); */
		}
		& > .archive {
			opacity: 0;
			top: 80vh;
			left: 0;
		}

		@media screen and (min-height: 650px) {
			min-height: calc(100vh + 1px);
		}
	}
</style>
