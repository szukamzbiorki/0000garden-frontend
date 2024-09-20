<template>
	<transition name="fade">
		<div v-if="session.cookie" class="cookie">
			<div class="text">
				Garden uses cookies and similar technologies to provide you with a better
				experience. I feel sick. Quite literally. I feel my body is processing something.
				Possibly there is an underlying psychological thing that I haven't worked through
				yet. Anyway, I feel like I am becoming stupid. All I do is sit behind this desk.
				The only interaction I have is with my computer. I don't know. I can't even call
				it interaction. Further details can be found in the privacy information.
			</div>
			<div @click="update({ cookie: false })" class="close">Accept</div>
		</div>
	</transition>
</template>

<script setup>
	const { session, update } = await useSession()
	await update({ cookie: true })
	console.log(session)
</script>

<style lang="postcss" scoped>
	.cookie {
		background-color: var(--grey);
		color: white !important;
		bottom: var(--space-m);
		left: var(--space-m);
		top: initial !important;
		width: calc(100vw - 2 * var(--space-m));
		padding: var(--space-m);
		display: flex;
		flex-direction: row;
		gap: var(--space-l);
		& > .close {
			background-color: white;
			padding: var(--space-s) var(--space-l);
			height: fit-content;
			color: var(--grey);
			cursor: pointer;
		}
	}
</style>
