<script setup lang="ts">
	import Hls from 'hls.js'

	const { src, theme = 'default' } = defineProps<{ src: string; theme?: string }>()

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

	watch(
		visible,
		(v) => {
			muted.value = true
			playing.value = v
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
</script>

<template>
	<div class="video" :style="{ '--progress': `${progress * 100}%` }">
		<div class="controls">
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
			@click="playing = !playing"
			:loop="theme === 'homepage'"
		/>
		<div class="progress" @click="seek" />
	</div>
</template>

<style lang="postcss" scoped>
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
		height: 20px;
		background: linear-gradient(
			to right,
			var(--lightgrey) 0%,
			var(--lightgrey) var(--progress),
			black var(--progress),
			black 100%
		);
	}
</style>
