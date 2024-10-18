<template>
	<div class="signup">
		<ElementsVideo :theme="'fullscreen'" :src="data.home.background.src"></ElementsVideo>
		<div class="content">
			<div class="middle">
				<div class="logo">
					<img class="logo-img" src="/assets/garden-logo.svg" alt="" srcset="" />
				</div>

				<div class="container">
					<TransitionGroup name="signup">
						<form v-if="true" class="input" @submit.prevent="handleSubmit">
							<input
								class="text"
								type="email"
								name="email"
								placeholder="Enter your e-mail address here"
								required
							/>
							<div class="button">
								<input class="btn" type="submit" value="Enter mailinglist" />
							</div>
						</form>
						<div v-if="false" class="success">
							You successfully signed up for the Garden Newsletter
						</div>
						<div v-if="false" class="error">
							There was an error while signing up for the Garden Newsletter
						</div>
					</TransitionGroup>
				</div>
			</div>
			<Cookie></Cookie>
		</div>
	</div>
</template>

<script setup>
	import 'animate.css'

	const query = groq`{
		'home': *[_type == "home"]{background->}[0]
	}`
	const sanity = useSanity()
	const { data } = await useAsyncData(() => sanity.fetch(query))

	async function handleSubmit(e) {
		const email = e.target.email.value
		const requestOptions = {
			method: 'POST',
			body: { email },
		}
		const { response } = await $fetch('/api/submit', requestOptions)
		console.log(response)
	}
</script>

<style scoped lang="postcss">
	.signup-enter-active,
	.signup-leave-active {
		transition: all 0.5s ease;
	}
	.signup-enter-from,
	.signup-leave-to {
		opacity: 0;
	}
	.content {
		& > * {
			position: absolute;
		}
		& > .middle {
			top: 50vh;
			left: 50vw;
			transform: translate(-50%, -50%);
			display: flex;
			flex-direction: column;
			gap: var(--space-xl);
			user-select: none;

			@media screen and (max-width: 640px) {
				width: var(--width-m);
			}

			& > .logo {
				& > * {
					height: 3.5rem;
					pointer-events: none;
				}
			}
			& > .container {
				display: grid;
				& > .success,
				.error {
					grid-area: 1/1;
					background-color: rgba(255, 255, 255, 0.25);
					padding: 2px var(--space-m);
					color: white;
					border-radius: var(--border-radius);
					&:hover {
					}
					&:focus {
						border-bottom: white 2px solid;
						background-color: rgba(255, 255, 255, 0.45);
					}
				}
				& > .input {
					display: flex;
					flex-direction: row;
					gap: var(--space-m);

					

					@media screen and (max-width: 640px) {
						flex-direction: column;
						width: 100%;
					}
					& > .text {
						min-width: 20vw;
					}
					& > .button {
						mix-blend-mode: difference;
						& > * {
							@media screen and (max-width: 640px) {
								width: 100%;
							}
						}
					}
				}
			}
		}
	}
</style>
