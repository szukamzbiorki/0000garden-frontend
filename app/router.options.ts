import type { RouterConfig } from '@nuxt/schema'

export default {
	// https://router.vuejs.org/api/interfaces/routeroptions.html#routes
	scrollBehavior(to, from, savedPosition) {
		if (savedPosition) {
			return savedPosition
		} else {
			return false
		}
		// if (savedPosition) {
		// 	return savedPosition
		// } else if (to.name === '/') {
		// 	return { top: 1 }
		// } else {
		// 	return false
		// }
	},
} satisfies RouterConfig
