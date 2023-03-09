const burgerMenu = document.querySelector('.navbar_burger'); //выбрать где именно нарисован бургер и скрыт.
const menuList = document.querySelector('.navbar_nav'); //родительский элемент листа меню
const body = document.querySelector('body'); //это просто body для фиксации
const links = document.querySelectorAll('navbar_nav-link'); // ссылки меню



burgerMenu.onclick = function showBurger() {
	this.classList.toggle('activeBurger');
	menuList.classList.toggle('activeBurger');
	body.classList.toggle('lockScroll');
};

const swiper = new Swiper('.swiper_slider-intro', {
	// Optional parameters
	direction: 'horizontal',
	loop: true,
	spaceBetween: 30,
	slidesPerView: 1,
	clickable: true,

	autoplay: {
		delay: 4000,
	},
	// If we need pagination
	pagination: {
		el: '.swiper-pagination',
		clickable: true,
	},

	// Navigation arrows
	navigation: {
		nextEl: '.swiper-button-next',
		prevEl: '.swiper-button-prev',
	},

	// And if we need scrollbar
	scrollbar: {
		el: '.swiper-scrollbar',
	},
});