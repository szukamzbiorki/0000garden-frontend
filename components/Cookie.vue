<template>
	<transition name="fade">
		<div v-if="session.cookie" class="cookie-wrapper">
			<div class="cookie">
				<div class="text">
					Garden uses cookies and similar technologies to provide you with a better
					experience. I feel sick. Quite literally. I feel my body is processing
					something. Possibly there is an underlying psychological thing that I haven't
					worked through yet. Anyway, I feel like I am becoming stupid. All I do is sit
					behind this desk. The only interaction I have is with my computer. I don't know.
					I can't even call it interaction. Further details can be found in the privacy
					information.
				</div>
				<div class="buttons">
					<div @click="update({ cookie: false })" class="close">Accept</div>
					<div @click="update({ cookie: false })" class="close">Reject</div>
				</div>
			</div>
		</div>
	</transition>
</template>

<script setup>
	const { session, update } = await useSession()
	await update({ cookie: true })
	console.log(session)
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
			width: calc(100vw - 2 * var(--space-m));
			padding: var(--space-m);
			display: flex;
			flex-direction: row;
			align-items: center;
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
