function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}


async function logg() {
	while (true) {
		window.chatcheck(general, glob)
		sleep(1)
	}
}
logg()