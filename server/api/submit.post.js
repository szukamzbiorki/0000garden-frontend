export default defineEventHandler(async (event) => {
	const body = await readBody(event)
	const BIN_MASTER = useRuntimeConfig().public.BIN_MASTER
	try {
		const response = await $fetch('https://api.jsonbin.io/v3/b', {
			method: 'POST',
			body: {
				email: body.email,
			},
			headers: {
				'Content-Type': 'application/json',
				'X-Master-Key': BIN_MASTER,
				'X-Bin-Name': body.email,
			},
		})
		return response
	} catch (error) {
		console.log('Error fetching data:', error.message, error.stack)
		return { error: 'Failed to fetch data' }
	}
})
