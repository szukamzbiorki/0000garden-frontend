export default defineEventHandler(async (event) => {
	const body = await readBody(event)
	const BIN_MASTER = useRuntimeConfig().public.BIN_MASTER
	const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/

	// Check if the provided email matches the regex
	if (!emailRegex.test(body.email)) {
		return {
			error: true,
			message: 'Invalid email format',
			statusCode: 400,
		}
	}
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
		console.log('Response:', response)
		return response
	} catch (error) {
		console.log('Error fetching data:', error.message, error.stack)
		return {
			error: true,
			message: 'Failed to sign up',
			statusCode: 500,
		}
	}
})
