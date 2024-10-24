<template>
	<transition name="fade">
		<div v-show="cookie !== 'hide'" class="cookie-wrapper">
			<div class="cookie">
				<div class="text">
					<SanityContent :blocks="data.home.cookie" :serializers="customSerializers" />
				</div>
				<div class="buttons">
					<div @click="handleClick" class="close">Accept</div>
					<div @click="handleClick" class="close">Reject</div>
				</div>
			</div>
		</div>
	</transition>
</template>

<script setup>
	const query = groq`{
		'home': *[_type == "home"]{cookie, ...}[0]
	}`
	const sanity = useSanity()
	const { data } = await useAsyncData(() => sanity.fetch(query))

	const cookie = useCookie('garden-cookies', { sameSite: 'strict', maxAge: 60 * 60 * 5 })

	function handleClick() {
		cookie.value = 'hide'
	}

	const customSerializers = {
		marks: {
			link: (value) => {
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
</script>

<style lang="postcss" scoped>
	.cookie-wrapper {
		position: fixed;
		top: 0;
		left: 0;
		width: 100vw;
		height: 100vh;
		backdrop-filter: blur(4px);
		z-index: 500;
		& > .cookie {
			position: absolute;
			background-color: var(--darkgrey);
			color: white !important;
			bottom: var(--space-m) !important;
			left: var(--space-m);
			bottom: var(--space-m) !important;
			width: var(--width-m);
			padding: var(--space-m);
			display: flex;
			flex-direction: row;
			align-items: center;
			justify-content: space-between;
			gap: var(--space-l);
			border-radius: var(--border-radius);
			@media screen and (max-width: 660px) {
				bottom: initial !important;
				top: var(--space-m);
				flex-direction: column-reverse;
				gap: var(--space-m);
			}
			& > .buttons {
				display: flex;
				flex-direction: row;
				gap: var(--space-s);
				@media screen and (max-width: 660px) {
					width: 100%;
				}
				& > .close {
					@media screen and (max-width: 660px) {
						flex-grow: 2;
					}
					background-color: white;
					padding: var(--space-s) var(--space-l);
					height: fit-content;
					color: var(--darkgrey);
					cursor: pointer;
					border-radius: var(--border-radius);
				}
			}
		}
	}
</style>
