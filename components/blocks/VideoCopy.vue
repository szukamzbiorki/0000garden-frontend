<script setup>
	import { useCurrentElement } from '@vueuse/core'
	import Hls from 'hls.js'

	const props = defineProps({
		caption: {
			type: String,
			default: '',
		},
		showCaption: {
			type: Boolean,
			default: false,
		},
		src: {
			type: String,
			default: '',
		},
		ratio: {
			type: Array,
			default: [],
		},
		mobile: {
			type: Object,
			default: () => {},
		},
		theme: {
			type: String,
			default: '',
		},
		poster: {
			type: Object,
			default: {},
		},
		autoplay: {
			type: Boolean,
			default: false,
		},
	})

	const video = ref()
	const el = useCurrentElement()
	let hls

	const src = computed(() => props.src)
	// !mq.m && props.mobile?.src ? props.mobile.src : props.src

	const ratio = computed(() =>
		!mq.m && props.mobile?.ratio.length ? props.mobile.ratio : props.ratio
	)

	const { playing, muted } = useMediaControls(video)
	const firstPlaying = ref(false)

	const { height: windowHeight } = useWindowSize()
	const progressPercentage = ref(0)

	const { stop } = useIntersectionObserver(
		el,
		([{ isIntersecting }]) => {
			if (isIntersecting) {
				if (hls) {
					hls.startLoad()
				} else if (video.value?.src !== src.value) {
					video.value.src = src.value
				}
			}

			if (video?.value) {
				playing.value = isIntersecting
				if (playing.value) {
					firstPlaying.value = true
				}
			}
		},
		{ rootMargin: `${windowHeight.value}px 0px ${windowHeight.value}px 0px` }
	)

	onMounted(() => {
		if (props.autoplay) {
			muted.value = true
			video.value.loop = 'loop'
			video.value.muted = true
		}
		initVideo(props.src)
		addVideoListeners()
	})

	onUnmounted(() => {
		if (hls) {
			hls.destroy()
		}
		stop()
		removeVideoListeners()
	})

	const addVideoListeners = () => {
		if (video.value) {
			video.value.addEventListener('timeupdate', updateProgress)
		}
	}

	const removeVideoListeners = () => {
		if (video.value) {
			video.value.removeEventListener('timeupdate', updateProgress)
		}
	}

	const updateProgress = () => {
		if (video.value) {
			progressPercentage.value = (video.value.currentTime / video.value.duration) * 100
		}
	}

	const seekVideo = (event) => {
		if (video.value) {
			const rect = event.target.getBoundingClientRect()
			const clickX = event.clientX - rect.left
			const width = rect.width
			const percentage = clickX / width
			video.value.currentTime = percentage * video.value.duration
		}
	}

	const initVideo = (src) => {
		if (!Hls.isSupported()) {
			video.value.src = src
		} else {
			if (!hls) {
				hls = new Hls({
					autoStartLoad: false,
					startLevel: 5,
				})
			} else {
				hls.stopLoad()
			}
			if (hls) {
				hls.startLoad()
			} else if (video.value?.src !== src.value) {
				video.value.src = src.value
			}
			hls.loadSource(src)
			hls.attachMedia(video.value)

			if (video?.value) {
				if (playing.value) {
					firstPlaying.value = true
				}
			}
		}
	}
</script>

<template>
	<div class="video-wrapper" :title="''">
		<div class="controls">
			<div @click="playing = !playing" class="play">
				{{ playing ? 'Pause' : 'Play' }}
			</div>
			<div @click="muted = !muted" class="mute">
				{{ muted ? 'Unmute' : 'Mute' }}
			</div>
		</div>
		<div :class="['video-container']">
			<video ref="video" playsinline />
			<div class="progress-bar" @click="seekVideo">
				<div class="progress" :style="{ width: `${progressPercentage}%` }"></div>
			</div>
		</div>
	</div>
</template>

<style lang="postcss" scoped>
	.video-wrapper {
		position: relative;
		& > .controls {
			position: absolute;
			top: -1rem;
			width: calc(100vw - 2 * var(--space-m));
			display: flex;
			flex-direction: row;
			justify-content: space-between;
			color: var(--lightgrey);
			& > * {
				cursor: pointer;
			}
		}
	}
	.video-container {
		position: relative;
		background-color: white;

		&:not(.autoplay) > * {
			cursor: pointer;
		}
		& > * {
			width: 100%;
			height: 100vh;
			object-fit: cover;
		}

		.progress-bar {
			position: absolute;
			bottom: 0;
			left: 0;
			right: 0;
			height: 5px;
			background-color: rgba(255, 255, 255, 0.3);
			cursor: pointer;
			width: calc(100vw - 2 * var(--space-m));
		}

		.progress {
			height: 100%;
			background-color: #414141;
			width: 0;
			transition: width 0.1s ease;
		}
	}

	.poster {
		position: relative;
		z-index: 1;
	}
</style>
