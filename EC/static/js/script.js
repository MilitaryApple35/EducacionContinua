const slider = document.querySelector('.slider');
const prevButton = document.querySelector('.prev-button');
const nextButton = document.querySelector('.next-button');

let translateValue = 0;
const slideWidth = slider.offsetWidth / 4;

prevButton.addEventListener('click', () => {
    if (translateValue < 0) {
        translateValue += slideWidth;
        slider.style.transform = `translateX(${translateValue}px)`;
    }
});

nextButton.addEventListener('click', () => {
    if (translateValue > -(slideWidth * (slider.childElementCount - 4))) {
        translateValue -= slideWidth;
        slider.style.transform = `translateX(${translateValue}px)`;
    }
});

function mostrarImagenCurso(imagenUrl) {
    var imagenCursoDiv = document.getElementById('imagen-curso');
    imagenCursoDiv.innerHTML = '<img src="' + imagenUrl + '" alt="Imagen del curso">';
}

