<template>
	<div>
		<div ref="swipe" class="swiper">
			<div class="bar">
				<div v-if="content.images?.length > 1" class="counter">
					{{ slideNumber + '/' + content.images?.length }}
				</div>
			</div>
			<div class="swiper-wrapper">
				<div
					v-if="content.images?.length > 1"
					v-for="image in content.images"
					:key="image._id"
					class="swiper-slide"
				>
					<ElementMedia class="swiperimg" :medium="image"></ElementMedia>
				</div>
				<div v-else class="swiper-slide">
					<ElementMedia class="swiperimg" :medium="image"></ElementMedia>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
	const props = defineProps({
		content: Object,
	})

	import Swiper from 'swiper'
	import 'swiper/css'
	import 'swiper/css/navigation'
	import 'swiper/css/effect-fade'
	import { EffectFade } from 'swiper/modules'

	const swipe = ref(null)
	const swiper = ref()
	const slideNumber = ref(1)

	onMounted(() => {
		if (props.content?.images.length > 1) {
			swiper.value = new Swiper(swipe.value, {
				modules: [EffectFade],
				grabCursor: true,
				observer: true,
				observeParents: true,
				loop: true,
				slidesPerView: 'auto',
				autoHeight: true,
				effect: 'fade',
				fadeEffect: {
					crossFade: true,
				},
				on: {
					slideChange: (swiper) => {
						slideNumber.value = swiper.realIndex + 1
					},
				},
			})
		}
	})

	onUnmounted(() => {
		if (swiper.value) {
			swiper.value.destroy()
		}
	})
</script>

<style lang="postcss" scoped>
	.swiper {
		width: calc(100vw-2 * var(--space-m));
		& > .bar {
			width: calc(100vw-2 * var(--space-m));
			display: flex;
			flex-direction: row;
			justify-content: center;
		}
	}

	.swiper-wrapper {
		display: flex;
	}

	.swiper-slide {
		/* max-height: 70vh; */
		width: 100vw;
		margin-right: var(--space-m);
		@media screen and (max-width: 600px) {
			/* height: 65vw; */
		}

		& > .swiperimg {
			/* height: 70vh; */
			width: 100%;
			@media screen and (max-width: 600px) {
				/* height: 65vw; */
			}
		}
	}
</style>
