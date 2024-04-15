const hamburgerToggle = document.querySelector('.hamburger__toggle');
const hamburger = document.querySelector('.hamburger');
const navItems = document.querySelector('.nav__items');


hamburgerToggle.addEventListener('click', (e) => {
	hamburger.classList.toggle('active');
	navItems.classList.toggle('active');
})

