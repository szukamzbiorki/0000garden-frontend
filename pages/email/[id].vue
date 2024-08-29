<template>
	<div class="page">Email ID</div>
</template>

<script setup>
	// import 'animate.css'
	// const query = groq`{
	// 	'acres': *[_type == "acre"]{download{asset->}, ...},
	// 	'mails': *[_type == "mail"]{download{asset->}, ...}
	// }`
	// const sanity = useSanity()
	// const { data } = await useAsyncData(() => sanity.fetch(query))

	const route = useRoute()
	const query = groq`*[_type=="email" && slug.current==$id]{download{asset->}, ...}[0]`
	const sanity = useSanity()
	const {
		data: artist,
		pending,
		error,
	} = await useAsyncData('artist', () =>
		sanity.fetch(query, { id: route.params.id })
	)

	console.log(artist.value)

	const { mobile } = useScreenSize()
</script>

<style scoped lang="postcss"></style>
