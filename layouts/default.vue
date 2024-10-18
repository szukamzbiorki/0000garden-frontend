<script setup>
	const ready = ref(false)
	const { currentRoute: route } = useRouter()

	// const { mobile } = useScreenSize()

	onMounted(async () => {
		await document.fonts.ready
		ready.value = true
	})
</script>

<template>
	<div :class="['layout', { ready }]">
		<header>
			<!-- <a href="https://0001.garden" class="mailinglist">Mailinglist</a> -->
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
		<svg style="display: none">
			<defs>
				<filter id="pixelate" x="0%" y="0%" width="100%" height="100%">
					<!--Thanks to Zoltan Fegyver for figuring out pixelation and producing the awesome pixelation map. -->
					<feGaussianBlur stdDeviation="2" in="SourceGraphic" result="smoothed" />
					<feImage
						width="15"
						height="15"
						xlink:href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAIAAAACDbGyAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAWSURBVAgdY1ywgOEDAwKxgJhIgFQ+AP/vCNK2s+8LAAAAAElFTkSuQmCC"
						result="displacement-map"
					/>
					<feTile in="displacement-map" result="pixelate-map" />
					<feDisplacementMap
						in="smoothed"
						in2="pixelate-map"
						xChannelSelector="R"
						yChannelSelector="G"
						scale="50"
						result="pre-final"
					/>
					<feComposite operator="in" in2="SourceGraphic" />
				</filter>
			</defs>
		</svg>
	</div>
</template>

<style lang="postcss" scoped>
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
