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
  
    // Limpiar cualquier contenido anterior
    imagenCursoDiv.innerHTML = '';
  
    // Crear un elemento de imagen y establecer la URL y atributo alt
    var imagenCurso = document.createElement('img');
    imagenCurso.src = imagenUrl;
    imagenCurso.alt = 'Imagen del curso';
  
    // Establecer estilos para ajustar la altura y centrar horizontalmente la imagen
    imagenCurso.style.maxHeight = '100%';
    imagenCurso.style.maxWidth = '100%'
    imagenCurso.style.display = 'block';
    imagenCurso.style.margin = '0 auto';
  
    // Agregar la imagen al div contenedor
    imagenCursoDiv.appendChild(imagenCurso);
  
    // Centrar la imagen verticalmente
    imagenCursoDiv.style.display = 'flex';
    imagenCursoDiv.style.justifyContent = 'center';
    imagenCursoDiv.style.alignItems = 'center';
  }
  
