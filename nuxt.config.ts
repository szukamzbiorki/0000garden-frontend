// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
	devtools: { enabled: false },
	css: ['/assets/css/index.css'],
	app: {
		pageTransition: {
			name: 'pagetransition',
			mode: 'out-in',
		},
		head: {
			link: [
				{
					rel: 'stylesheet',
					href: 'https://use.typekit.net/jsn0klg.css',
				},
				{
					rel: 'icon',
					type: 'image/x-icon',
					href: '/favicon.ico',
				},
			],
			title: 'Garden Archive',
		},
	},
	sanity: {
		projectId: '9tabryc1',
		dataset: 'production',
	},
	modules: ['@nuxtjs/sanity', '@vueuse/nuxt', '@sidebase/nuxt-session'],
	ssr: false,
})
