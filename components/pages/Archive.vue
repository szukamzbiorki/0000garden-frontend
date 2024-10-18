<template>
	<div class="archive" :class="{ scaled }">
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
	const scaled = ref(false)

	const NuxtLink = resolveComponent('NuxtLink')

	function formatDate(dateString) {
		const date = new Date(dateString)
		const day = String(date.getDate()).padStart(2, '0') // Pad single digit day with leading zero
		const month = String(date.getMonth() + 1).padStart(2, '0') // Pad single digit month with leading zero
		const year = date.getFullYear()

		return `${day}.${month}.${year}`
	}
</script>

<style scoped lang="postcss">
	.page {
		& > * {
			position: absolute;
			top: calc(6rem + 2 * var(--space-m));
			left: var(--space-m);
		}
		& > .archive {
			width: var(--width-m);
			left: var(--space-m);
			display: flex;
			flex-direction: column;
			gap: var(--space-xl);
			transition: all 0.3s ease;
			transform-origin: top left;
			@media screen and (min-width: 640px) {
				top: 50vh !important;
				transform: translateY(-50%);
			}
			&.scaled {
				transform: scale(0.25);
			}
			& > * {
				& > .title {
					margin-bottom: var(--space-m);
				}
				& > .list {
					display: flex;
					flex-direction: column;
					/* padding-left: var(--space-m); */

					& > .item {
						border-bottom: var(--darkgrey) 1px solid;
						color: var(--darkgrey);
						& > * {
							color: var(--darkgrey) !important;
						}
						&.upcoming {
							filter: blur(2px);
						}
						&:hover {
							color: var(--lightgrey) !important;
							border-bottom: var(--lightgrey) 1px solid;
							& > * {
								color: var(--lightgrey) !important;
							}
						}
						display: grid;
						grid-template-columns: repeat(12, 1fr);
						@media screen and (max-width: 640px) {
							grid-template-columns: repeat(4, 1fr);
							color: var(--lightgrey) !important;
							border-bottom: var(--lightgrey) 1px solid !important;
							gap: 0;
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
	}
</style>
