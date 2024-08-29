<template>
	<div :class="[paddings.get(content.size)]">
		<div class="image">
			<ElementMedia :medium="content.images[0]"></ElementMedia>
		</div>
		<!-- <div v-if="content.credit" class="bot times">
			<div v-if="content.credit" class="credit times">{{ content.credit }}</div>
			<div v-if="content.title" class="title times-italic">
				{{ content.title
				}}<span v-if="content.year" class="year times">
					,{{ content.year }}</span
				>
			</div>
			<div v-if="content.medium" class="medium">{{ content.medium }}</div>
			<div v-if="content.worksize" class="size">{{ content.worksize }}</div>
			<div v-if="content.price" class="price">{{ content.price }}</div>
		</div> -->
	</div>
</template>

<script setup>
	const props = defineProps({
		content: Object,
	})

	const paddings = new Map([
		['S', 'padding-s'],
		['M', 'padding-m'],
		['L', undefined],
	])
</script>

<style lang="postcss" scoped>
	.image-block {
		position: relative;
		display: flex;
		flex-direction: column;
		gap: var(--space-s);
		& > .bot {
			margin-top: var(--space-s);
			& > *:not(.name, .title) {
				font-family: inherit;
			}

			& > * {
				text-align: center;
				max-width: 67ch;
				margin: 0 auto;
			}
			& > .title {
				text-transform: uppercase;
			}
		}
		& > .credit {
			text-align: center;
			white-space: pre-wrap;
			max-width: 70ch;
			margin: 0 auto;
		}
		&.padding-s {
			& > .image {
				padding: 0 25vw;
			}
		}

		&.padding-m {
			& > .image {
				padding: 0 10vw;
			}
		}

		@media screen and (max-width: 600px) {
			&.padding-m {
				& > .image {
					padding: 0;
				}
			}

			&.padding-s {
				& > .image {
					padding: 0;
				}
			}
		}
	}
</style>
