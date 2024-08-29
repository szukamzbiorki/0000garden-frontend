<template>
	<div
		class="imagebox"
		:data-format="orientation"
		:style="`aspect-ratio: ${ratio};`"
	>
		<transition mode="in-out" name="heart">
			<img
				v-show="imageloaded"
				@load="onloaded"
				:src="
					mobile
						? $urlFor(medium)
								.width(Math.floor(windowWidth * 4.5))
								.fit('crop')
								.url()
						: $urlFor(medium)
								.height(Math.floor(windowHeight * 1.5))
								.fit('crop')
								.url()
				"
				:data-format="orientation"
			/>
		</transition>
		<div
			class="grad"
			:style="`--bg: ${medium.asset.metadata?.palette.dominant.background}; --fg: ${medium.asset.metadata?.palette.lightVibrant.background};`"
		></div>
	</div>
</template>

<script setup>
	const { height: windowHeight, width: windowWidth } = useWindowSize()
	const { mobile } = useScreenSize()
	const imageloaded = ref(false)
	const format = ref('')

	const props = defineProps({
		medium: Object,
		size: {
			type: String,
			default: 'large',
		},
		caption: {
			type: String,
			default: '',
		},
		showCaption: {
			type: Boolean,
			default: false,
		},
		srcs: {
			type: Object,
			default: {},
		},
		url: {
			type: String,
			default: '',
		},
		w: {
			type: Number,
			default: () => {},
		},
		h: {
			type: Number,
			default: () => {},
		},
		alt: {
			type: String,
			default: '',
		},
		mobile: {
			type: Object,
			default: () => {},
		},
		theme: {
			type: String,
			default: '',
		},
		lazy: {
			type: Boolean,
			default: true,
		},
		ratio: {
			type: Array,
			default: [],
		},
	})

	let ratiodata
	let ratio
	let orientation

	if (props.medium.asset._ref) {
		ratiodata = props.medium.asset._ref.split(/(?:-|x)+/)
		ratio = ratiodata[2] + '/' + ratiodata[3]
		orientation = ratiodata[2] / ratiodata[3] > 1 ? 'landscape' : 'portrait'
	} else {
		ratiodata = props.medium.asset._id.split(/(?:-|x)+/)
		ratio = ratiodata[2] + '/' + ratiodata[3]
		orientation = ratiodata[2] / ratiodata[3] > 1 ? 'landscape' : 'portrait'
	}

	function onloaded() {
		imageloaded.value = true
	}
</script>

<style>
	.imagebox {
		display: grid;
		& > * {
			grid-area: 1/1;
			width: 100%;
			height: 100%;
			z-index: 2;
		}
	}
	.grad {
		background: linear-gradient(var(--fg), var(--bg));
		height: 100%;
		filter: blur(0);
		z-index: 1;
	}
</style>
