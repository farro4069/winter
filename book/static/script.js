const imageList = ['P1060594.JPG', 'P1060596.JPG', 'P1060603.JPG', 
	'P1060607.JPG', 'P1060609.JPG', 'P1060616.JPG', 'P1060617.JPG', 
	'P1060624.JPG', 'P1060631.JPG', 'P1060640.JPG', 'P1060643.JPG', 
	'P1060652.JPG', 'P1060661.JPG', 'P1060673.JPG', 'P1060676.JPG', 
	'P1060677.JPG', 'P1060679.JPG', 'P1060680.JPG', 'P1060683.JPG', 
	'P1060687.JPG', 'P1060699.JPG', 'P1060704.JPG', 'IMG_2A938F34D1CE-1.jpeg', 'IMG_7DB1492C659F-1.jpeg', 
	'IMG_7B91457FCB9E-1.jpeg', 'IMG_183F1421DF22-1.jpeg', 'IMG_CE1F459DD930-1.jpeg', 
	'return-break.jpg', 'return-descent.jpg', 'tranquil-view.jpg', 'woodford.jpg', 'carpark-depart.jpg', 'carpark-post.jpg', 'carpark-post2.jpg', 'samford.jpg', 'tranquil-buffet.jpg', 'mt-mee.jpg'];

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
