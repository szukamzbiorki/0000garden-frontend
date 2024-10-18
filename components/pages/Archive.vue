<template>
	<div class="archive">
		<div v-if="data.acres[0]" class="acres">
			<!-- <div class="title">Acre Archive</div> -->
			<div class="list">
				<component
					:to="'acre/' + acre.slug.current"
					:is="acre.upcoming ? 'div' : NuxtLink"
					v-for="(acre, i) in data.acres"
					class="item"
					:class="{ upcoming: acre.upcoming }"
				>
					<div class="no">{{ i + 1 }}</div>
					<div class="date">{{ formatDate(acre.date) }}</div>
					<div class="title">{{ acre.title }}</div>
					<div v-if="true" class="subject">{{ acre.subject }}</div>
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
				</component>
			</div>
		</div>
	</div>
</template>

<script setup>
	import 'animate.css'
	const query = groq`{
		'acres': *[_type == "acre"]{download{asset->}, ...}| order(orderRank),
		'mails': *[_type == "mail"]{download{asset->}, ...}| order(orderRank)
	}`
	const sanity = useSanity()
	const { data } = await useAsyncData(() => sanity.fetch(query))
	const { mobile } = useScreenSize()

	const NuxtLink = resolveComponent('NuxtLink')

	function formatDate(dateString) {
		const date = new Date(dateString)
		const day = String(date.getDate()).padStart(2, '0')
		const month = String(date.getMonth() + 1).padStart(2, '0')
		const year = date.getFullYear()

		return `${day}.${month}.${year}`
	}
</script>

<style scoped lang="postcss">
	.archive {
		width: var(--width-m);
		left: var(--space-m);
		top: 50vh;
		@media screen and (min-width: 640px) {
			transform: translateY(-50%);
		}
		@media screen and (max-width: 640px) {
			top: calc(var(--space-m) * 2 + 5rem);
		}
		& > .acres {
			& > .title {
				margin-bottom: var(--space-m);
			}
			& > .list {
				display: flex;
				flex-direction: column;
				& > .item {
					& > * {
						color: var(--darkgrey) !important;
					}
					border-bottom: var(--darkgrey) 1px solid;
					color: var(--darkgrey);
					&.upcoming {
						filter: blur(2px);
					}
					&:hover {
						color: var(--lightgrey) !important;
						border-bottom: var(--lightgrey) 1px solid !important;
						& > * {
							color: var(--lightgrey) !important;
						}
					}
					display: grid;
					grid-template-columns: repeat(12, 1fr);
					gap: var(--space-m);
					@media screen and (max-width: 640px) {
						grid-template-columns: repeat(4, 1fr);
						color: var(--lightgrey) !important;
						border-bottom: var(--lightgrey) 1px solid !important;
						gap: 0;
					}
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
						@media screen and (max-width: 640px) {
							grid-column: 1/-1;
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
						@media screen and (max-width: 640px) {
							grid-column: 1 / -1;
						}
					}
					& > .date {
						&::before {
							content: 'Date: ';
						}
						@media screen and (max-width: 640px) {
							grid-column: -2 / span 1;
							justify-self: end;
							&::before {
								content: '';
							}
						}
					}
				}
				& > a:visited {
					border-color: var(--darkergrey) !important;
					& > * {
						color: var(--darkergrey) !important;
					}
				}
			}
		}
	}
</style>
