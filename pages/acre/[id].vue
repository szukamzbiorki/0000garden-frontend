<template>
	<div class="acre">
		<div class="content">
			<div class="bar">
				<div class="no">{{ 1 }}</div>
				<div v-if="!mobile" class="date">{{ formatDate(acre.date) }}</div>
				<div class="title">{{ acre.title }}</div>
				<div v-if="!mobile" class="subject">{{ acre.subject }}</div>
				<a
					v-if="!mobile && acre.download?.asset.url"
					download
					:href="acre.download.asset.url"
					class="dl"
					>{{ acre.download.asset.originalFilename }}</a
				>
				<div v-if="!mobile && acre.contributor" class="contributor">
					{{ acre.contributor }}
				</div>
			</div>
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

	const { mobile } = useScreenSize()
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
		top: calc(6rem + 2 * var(--space-m));

		& > .info {
			position: fixed;
			bottom: var(--space-m);
			right: var(--space-m);
			z-index: 70;
		}
		& > .content {
			width: var(--width-m);
			& > .bar {
				display: grid;
				grid-template-columns: repeat(12, 1fr);
				border-bottom: var(--lightgrey) 1px solid;
				@media screen and (max-width: 640px) {
					grid-template-columns: repeat(4, 1fr);
				}
				gap: var(--space-m);
				& > .no {
					&::before {
						content: 'Number: ';
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
					grid-column: span 3;
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
