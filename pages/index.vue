<template>
	<div class="page">
		<div class="archive" :class="{ scaled }">
			<div class="emails">
				<div class="title">Email Archive</div>
				<div class="list">
					<NuxtLink
						:to="'email/' + acre.slug.current"
						v-for="(acre, i) in data.mails"
						class="item"
					>
						<div class="no">{{ i + 1 }}</div>
						<div v-if="!mobile" class="date">{{ formatDate(acre.date) }}</div>
						<div class="title">{{ acre.title }}</div>
						<div v-if="!mobile" class="subject">{{ acre.subject }}</div>
						<a v-if="!mobile" download :href="acre.download.asset.url" class="dl">{{
							acre.download.asset.originalFilename
						}}</a>
					</NuxtLink>
				</div>
			</div>
			<div class="acres">
				<div class="title">Acre Archive</div>
				<div class="list">
					<NuxtLink
						:to="'acre/' + acre.slug.current"
						v-for="(acre, i) in data.acres"
						class="item"
					>
						<div class="no">{{ i + 1 }}</div>
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
					</NuxtLink>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
	import 'animate.css'
	const query = groq`{
		'acres': *[_type == "acre"]{download{asset->}, ...},
		'mails': *[_type == "mail"]{download{asset->}, ...}
	}`
	const sanity = useSanity()
	const { data } = await useAsyncData(() => sanity.fetch(query))
	const { mobile } = useScreenSize()
	const scaled = ref(false)

	console.log(data.value.acres)

	function formatDate(dateString) {
		const date = new Date(dateString)

		// Extract day, month, and year
		const day = String(date.getDate()).padStart(2, '0') // Pad single digit day with leading zero
		const month = String(date.getMonth() + 1).padStart(2, '0') // Pad single digit month with leading zero
		const year = date.getFullYear()

		return `${day}.${month}.${year}`
	}

	const { y } = useWindowScroll()

	const header = ref(null)
	const h = useElementSize(header)

	const passed = ref(false)

	const active = ref(false)

	onMounted(() => {
		setTimeout(() => {
			passed.value = true
		}, 3500)
	})

	watch(y, (newY) => {
		if (newY > 0) {
			active.value = true
		}
	})

	const showImage = computed(() => {
		return active.value || passed.value
	})

	definePageMeta({
		name: 'indexah',
	})
</script>

<style scoped lang="postcss">
	.page {
		& > * {
			position: absolute;
			top: calc(6rem + 2 * var(--space-m));
			left: var(--space-m);
		}
		& > .archive {
			width: calc(100vw - 2 * var(--space-m));
			display: flex;
			flex-direction: column;
			gap: var(--space-xl);
			transition: all 0.3s ease;
			transform-origin: top left;
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
					padding-left: var(--space-m);

					& > .item {
						border-bottom: var(--darkgrey) 1px solid;
						color: var(--darkgrey);
						& > * {
							color: var(--darkgrey) !important;
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
							grid-column: span 3;
							&::before {
								content: 'Download: ';
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
		}
	}
</style>
