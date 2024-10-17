<template>
	<div>
		<div ref="swipe" class="swiper">
			<div v-if="content.images?.length > 1" class="bar">
				<div class="counter" @click="swiper.slideNext()">
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
					<ElementsVideo
						v-else
						v-bind="{ ...image }"
						class="swiperimg vid"
					></ElementsVideo>
				</div>
				<div v-else class="swiper-slide">
					<ElementMedia
						v-if="content.images[0]?._type == 'image'"
						class="swiperimg img"
						:medium="content.images[0]"
					></ElementMedia>
					<ElementsVideo
						v-else
						v-bind="{ ...content.images[0] }"
						class="swiperimg vid"
					></ElementsVideo>
				</div>
			</div>
		</div>
		<div v-if="content.caption" class="caption">
			<SanityContent :blocks="content.caption" :serializers="customSerializers" />
		</div>
	</div>
</template>

<script setup>
	const props = defineProps({
		content: Object,
	})

	console.log('this is content', props.content)

	const customSerializers = {
		marks: {
			link: (value) => {
				console.log(value)
				const isExternal = value.href && !value.href.startsWith('/')

				if (isExternal) {
					return h(
						'a',
						{
							href: value.href || '#', // Fallback URL
							target: value.target, // Open external links in a new tab
							rel: isExternal ? 'noopener noreferrer' : null, // Security for external links
							class: 'inline-link',
						},
						[
							value.textcontent, // Render the children (text inside the link)
						]
					)
				} else {
					const linkH = resolveComponent('NuxtLink')
					return h(
						linkH,
						{
							to: value.href || '#', // Fallback URL
							target: value.target, // Open external links in a new tab
							rel: isExternal ? 'noopener noreferrer' : null, // Security for external links
							class: 'inline-link',
						},
						() => value.textcontent
					)
				}
			},
		},
	}

	console.log(props.content.images.length)

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
				grabCursor: false,
				observer: true,
				observeParents: true,
				loop: true,
				slidesPerView: 'auto',
				autoHeight: true,
				effect: 'fade',
				preventClicks: true,
				preventClicksPropagation: true,
				speed: 400,
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
	.caption {
		padding-top: var(--space-s);
		text-align: right;
		font-size: var(--type-s);
		line-height: var(--type-s-leading);
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
			cursor: normal;
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
