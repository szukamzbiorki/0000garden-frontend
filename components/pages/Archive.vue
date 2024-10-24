<template>
	<div class="archive" :class="{ active: route.path != '/' }">
		<Transition name="fade">
			<div v-if="y < 1" class="acres">
				<div class="list">
					<TransitionGroup name="list">
						<component
							:to="'acre/' + acre.slug.current"
							:is="acre.upcoming ? 'div' : NuxtLink"
							v-for="(acre, i) in data.acres"
							:key="acre._id"
							class="item"
							:class="{ upcoming: acre.upcoming }"
							v-show="route.path == '/' || acre.slug.current == route.params.id"
						>
							<div class="no">{{ i + 1 }}</div>
							<div class="date">{{ formatDate(acre.date) }}</div>
							<div class="title">{{ acre.title }}</div>
							<div class="subject">{{ acre.subject }}</div>
							<a
								v-if="!mobile && acre.download?.asset.url"
								download
								:href="acre.download.asset.url"
								class="dl"
								>{{ acre.download.asset.originalFilename }}</a
							>
							<div v-if="acre.contributor" class="contributor">
								{{ acre.contributor }}
							</div>
						</component>
					</TransitionGroup>
				</div>
			</div>
		</Transition>
	</div>
</template>

<script setup>
	const query = groq`{
		'acres': *[_type == "acre"]{download{asset->}, ...}| order(orderRank)
	}`
	const sanity = useSanity()
	const { data } = await useAsyncData(() => sanity.fetch(query))
	const { mobile } = useScreenSize()

	const NuxtLink = resolveComponent('NuxtLink')
	const { y } = useWindowScroll()

	const props = defineProps({
		route: Object,
		active: Boolean,
	})

	function formatDate(dateString) {
		const date = new Date(dateString)
		return date
			.toLocaleDateString('en-GB', {
				day: '2-digit',
				month: '2-digit',
				year: 'numeric',
			})
			.replace(/\//g, '.')
	}
</script>

<style scoped lang="postcss">
	.archive {
		position: fixed !important;
		width: var(--width-m);
		left: var(--space-m);
		top: 50vh;
		transition: top 0.5s ease;
		&.active {
			top: calc(var(--space-m) * 2 + 7.2rem);
		}
		@media screen and (min-width: 640px) {
			transform: translateY(-50%);
		}
		@media screen and (max-width: 640px) {
			top: calc(var(--space-m) * 2 + 5rem);
		}
		& > .acres {
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
						color: var(--black);
						border-bottom: var(--black) 1px solid;
						user-select: none;
						& > * {
							color: var(--black) !important;
						}
					}
					&:hover:not(.upcoming) {
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
						@media screen and (max-width: 640px) {
							grid-column: -2 / span 1;
							/* grid-row: -2/-1; */
							justify-self: end;
							&::before {
								content: 'by ';
							}
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
