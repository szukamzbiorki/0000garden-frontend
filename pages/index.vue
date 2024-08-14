<template>
	<div class="wrapper">
		<div class="page">
			<a href="https://0001.garden" class="mailinglist">Mailinglist</a>
			<div class="top">
				<div class="logo">
					<img
						class="logo-img"
						src="/assets/garden-logo-ar.svg"
						alt=""
						srcset=""
					/>
				</div>
			</div>
			<div class="archive">
				<div class="emails">
					<div class="title">Email Archive</div>
					<div class="list">
						<div v-for="(acre, i) in data.mails" class="item">
							<div class="no">{{ i + 1 }}</div>
							<div class="date">{{ acre.date }}</div>
							<div class="title">{{ acre.title }}</div>
							<div class="subject">{{ acre.subject }}</div>
							<a download :href="acre.download.asset.url" class="dl">{{
								acre.download.asset.originalFilename
							}}</a>
						</div>
					</div>
				</div>
				<div class="acres">
					<div class="title">Acre Archive</div>
					<div class="list">
						<div v-for="(acre, i) in data.acres" class="item">
							<div class="no">{{ i + 1 }}</div>
							<div class="date">{{ acre.date }}</div>
							<div class="title">{{ acre.title }}</div>
							<div class="subject">{{ acre.subject }}</div>
							<a download :href="acre.download.asset.url" class="dl">{{
								acre.download.asset.originalFilename
							}}</a>
						</div>
					</div>
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

	console.log(data.value.acres)

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
		}
		& > .mailinglist {
			top: var(--space-m);
			right: var(--space-m);
		}
		& > .top {
			top: var(--space-m);
			left: 50vw;
			transform: translateX(-50%);
			display: flex;
			flex-direction: column;
			gap: var(--space-xl);
			& > .logo {
				& > * {
					height: 6rem;
				}
			}
		}
		& > .archive {
			top: calc(6rem + 2 * var(--space-m));
			left: 50vw;
			width: calc(100vw - 2 * var(--space-m));
			transform: translateX(-50%);
			display: flex;
			flex-direction: column;
			gap: var(--space-xl);
			& > * {
				& > .title {
					margin-bottom: var(--space-m);
				}
				& > .list {
					display: flex;
					flex-direction: column;
					padding-left: var(--space-m);
					& > .item {
						display: grid;
						grid-template-columns: repeat(12, 1fr);
						border-bottom: var(--grey) 1px solid;
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
