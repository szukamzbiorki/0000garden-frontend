<template>
	<div>
		<div ref="swipe" class="swiper">
			<div class="bar">
				<div
					v-if="content.images?.length > 1"
					class="counter"
					@click="swiper.slideNext()"
				>
					{{ slideNumber + '/' + content.images?.length }}
				</div>
			</div>
			<div class="controls">
				<div class="left" @click="swiper.slidePrev()"></div>
				<div class="mid"></div>
				<div class="right" @click="swiper.slideNext()"></div>
			</div>
			<div class="swiper-wrapper">
				<div
					v-if="content.images?.length > 1"
					v-for="(image, i) in content.images"
					:key="image._id"
					class="swiper-slide"
				>
					<ElementMedia
						v-if="image?._type == 'image'"
						class="swiperimg"
						:medium="image"
					></ElementMedia>
					<BlocksVideoCopy
						v-else
						v-bind="{ ...image }"
						class="swiperimg"
					></BlocksVideoCopy>
				</div>
				<div v-else class="swiper-slide">
					<ElementMedia
						v-if="image?._type == 'image'"
						class="swiperimg"
						:medium="image"
					></ElementMedia>
					<BlocksVideoCopy
						v-else
						v-bind="{ ...image }"
						class="swiperimg"
					></BlocksVideoCopy>
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

	const components = new Map([
		['image', resolveComponent('LazyElementMedia')],
		['video', resolveComponent('LazyBlocksVideoCopy')],
	])

	const naming = new Map([
		['image', 'image'],
		['video', 'video'],
	])

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
			color: var(--lightgrey);
			& > .counter {
				cursor: pointer;
				user-select: none;
			}
		}
	}
	.controls {
		position: absolute;
		width: 100%;
		height: calc(100% - 2rem);
		bottom: 0;
		display: grid;
		grid-template-columns: repeat(6, 1fr);
		z-index: 6;
		pointer-events: none;
		@media screen and (max-width: 600px) {
			display: none;
		}

		& > .left {
			grid-column: 1/2;
			cursor: pointer;
			pointer-events: all;
		}

		& > .mid {
			grid-column: 2/6;
			cursor: grab;
			pointer-events: none;
		}

		& > .right {
			grid-column: 6/7;
			cursor: pointer;
			pointer-events: all;
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
