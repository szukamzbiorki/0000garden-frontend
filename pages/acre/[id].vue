<template>
	<div class="acre">
		<div class="content">
			<Content :sections="acre.blocks"></Content>
		</div>
		<div class="info" v-if="acre.contributor">
			<NuxtLink to="/info" class="additional"
				>Contributed by {{ acre.contributor }}</NuxtLink
			>
		</div>
	</div>
</template>

<script setup>
	const route = useRoute()
	const query = groq`*[_type=="acre" && slug.current==$id]{download{asset->}, blocks[]{
		_type == "video" => @->,
		_type != "video" => {
			images[]{
				_type == "video" => @->,
				_type != "video" => {
					...
				}
			},
			...
		}
	},
	...}[0]`
	const sanity = useSanity()
	const { data: acre } = await useAsyncData('acre', () =>
		sanity.fetch(query, { id: route.params.id })
	)

	
	function formatDate(dateString) {
		const date = new Date(dateString)

		// Extract day, month, and year
		const day = String(date.getDate()).padStart(2, '0') // Pad single digit day with leading zero
		const month = String(date.getMonth() + 1).padStart(2, '0') // Pad single digit month with leading zero
		const year = date.getFullYear()

		return `${day}.${month}.${year}`
	}
</script>

<style scoped lang="postcss">
	.acre {
		position: absolute;
		left: var(--space-m);
		top: calc(6rem + 5 * var(--space-m));

		& > .info {
			position: fixed;
			bottom: var(--space-m);
			right: var(--space-m);
			z-index: 70;
			font-size: var(--type-s);
			line-height: var(--type-s-leading);
		}
		& > .content {
			width: var(--width-m);
			& > .bar {
				display: grid;
				grid-template-columns: repeat(12, 1fr);
				border-bottom: var(--darkgrey) 1px solid;
				@media screen and (max-width: 640px) {
					grid-template-columns: repeat(4, 1fr);
				}
				gap: var(--space-m);
				& > .no {
					&::before {
						content: 'Project: ';
					}
				}
				& > .title {
					grid-column: span 3;
					&::before {
						content: 'Title: ';
					}
				}
				& > .dl {
					grid-column: span 2;
					&::before {
						content: 'Download: ';
					}
				}
				& > .contributor {
					grid-column: span 2;
					&::before {
						content: 'Contributor: ';
					}
				}
				& > .subject {
					grid-column: span 2;
					&::before {
						content: 'Subject: ';
					}
				}
				& > .date {
					&::before {
						content: 'Date: ';
					}
				}
			}
		}
	}
</style>
