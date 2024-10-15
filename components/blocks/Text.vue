<template>
	<div class="text-block" :class="[content.font, content.align]">
		<SanityContent :blocks="content.content" :serializers="customSerializers" />
	</div>
</template>

<script setup>
	const props = defineProps({
		content: Object,
	})

	console.log(props.content)

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
</script>

<style lang="postcss">
	.text-block {
		& > p {
			max-width: calc(100vw / 12 * 5);
			text-wrap: wrap;
			font-family: inherit;
			margin-bottom: 1rem;
		}

		& > blockquote {
			max-width: calc(100vw / 12 * 5);
			text-wrap: wrap;
			font-family: inherit;
			margin-bottom: 1rem;
			padding-left: calc(100vw / 12 * 1);
			/* font-style: italic; */
		}
		@media screen and (max-width: 600px) {
			& > p,
			blockquote {
				max-width: var(--width-m);
				text-wrap: wrap;
				font-family: inherit;
			}
		}
	}
</style>
