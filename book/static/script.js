const imageList = [
	'2024WW01.jpg', '2024WW02.jpg', '2024WW03.jpg', '2024WW04.jpg', '2024WW05.jpg',
	'2024WW06.jpg', '2024WW07.jpg', '2024WW08.jpg', '2024WW09.jpg', '2024WW10.jpg',
	'2024WW11.jpg', '2024WW12.jpg', '2024WW13.jpg', '2024WW14.jpg', '2024WW15.jpg',
	'2024WW16.jpg', '2024WW17.jpg', '2024WW18.jpg', '2024WW19.jpg', '2024WW20.jpg', '2009View.jpg'
];

const slider = document.querySelector('.picture__slider');

window.addEventListener('load', displayImage);

const sliderOne = document.createElement('div');
sliderOne.classList.add('sliderOne');
sliderOne.style.backgroundImage = `url(/static/assets/images/${imageList[0]})`
slider.appendChild(sliderOne);

const sliderTwo = document.createElement('div');
sliderTwo.classList.add('sliderTwo');
sliderTwo.style.backgroundImage = `url(/static/assets/images/${imageList[1]})`
slider.appendChild(sliderTwo);


function crossOver() {
	setTimeout(()=>{
		sliderOne.style.opacity = 1
		sliderTwo.style.opacity = 0
	}, 5000)
	setTimeout(()=>{
		i = Math.floor(Math.random() * (imageList.length - 1))
		sliderTwo.style.backgroundImage = `url(/static/assets/images/${imageList[i]})`;
	}, 6000)

	setTimeout(()=>{
		sliderOne.style.opacity = 0
		sliderTwo.style.opacity = 1
	}, 10000)
	setTimeout(()=>{
		i = Math.floor(Math.random() * (imageList.length - 1))
		sliderOne.style.backgroundImage = `url(/static/assets/images/${imageList[i+1]})`;
	}, 11000)
} 

function displayImage() {
	setInterval(() => {
		crossOver(); 
	}, 11000);

}
