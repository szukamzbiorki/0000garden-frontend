<script setup lang="ts">
	import Hls from 'hls.js'

	const {
		src,
		theme = 'default',
		ratio = {},
	} = defineProps<{ src: string; theme?: string; ratio?: Object }>()

	let hls

	const videoEl = useTemplateRef('videoEl')

	function init() {
		if (videoEl.value) {
			if (!Hls.isSupported()) {
				videoEl.value.src = src
			} else {
				hls = new Hls()
				hls.loadSource(src)
				hls.attachMedia(videoEl.value)
			}
		}
	}

	const { playing, muted, currentTime, duration } = useMediaControls(videoEl)

	const progress = computed(() => currentTime.value / duration.value)

	const visible = useElementVisibility(videoEl)

	const ratioReady = computed(() => {
		if ('width' in ratio && 'height' in ratio) {
			return `${ratio.width}/${ratio.height}`
		}
	})

	watch(
		visible,
		(v) => {
			muted.value = true
			// if (theme != 'fullscreen') {
			playing.value = v
			// }
		},
		{ immediate: true }
	)

	onMounted(() => {
		init()
	})

	function seek(event: MouseEvent) {
		if (videoEl.value) {
			const target = event.target as Element
			const { left, width } = target.getBoundingClientRect()
			const clickX = event.clientX - left
			const percentage = clickX / width
			videoEl.value.currentTime = percentage * videoEl.value.duration
		}
	}

	function handleClick() {
		if (theme == 'default') {
			playing.value = !playing.value
		}
	}
</script>

<template>
	<div
		class="video"
		:class="[theme]"
		:style="{ '--progress': `${progress * 100}%`, '--ratio': `${ratioReady}` }"
	>
		<div v-if="theme == 'default'" class="controls">
			<div @click="playing = !playing">
				{{ playing ? 'Pause' : 'Play' }}
			</div>
			<div @click="muted = !muted">
				{{ muted ? 'Unmute' : 'Mute' }}
			</div>
		</div>
		<video
			ref="videoEl"
			:src
			playsinline
			title=""
			@click="handleClick()"
			loop="true"
			class="vid"
		/>
		<div v-if="theme == 'default'" class="progress" @click="seek" />
	</div>
</template>

<style lang="postcss" scoped>
	.video {
		&.fullscreen {
			background-color: white;

			&:not(.autoplay) > * {
				cursor: pointer;
			}
			& > * {
				width: 100vw;
				height: 100vh;
				object-fit: cover;
			}
		}
	}
	.controls {
		display: grid;
		grid-auto-flow: column;
		gap: var(--space-m);
		justify-content: space-between;

		> * {
			cursor: pointer;
		}
	}
	.progress {
		cursor: pointer;
		transition: all ease 0.4s;
		height: 3px;
		background: linear-gradient(
			to right,
			var(--lightgrey) 0%,
			var(--lightgrey) var(--progress),
			black var(--progress),
			black 100%
		);
	}
	.vid {
		aspect-ratio: var(--ratio);
	}
</style>
