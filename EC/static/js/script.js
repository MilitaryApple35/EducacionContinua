let currentSlide = 0;
const slides = document.getElementsByClassName("box");
let visibleSlides = getVisibleSlides();


function showSlide() {
  for (let i = 0; i < slides.length; i++) {
    if (i < currentSlide || i >= currentSlide + visibleSlides) {
      slides[i].style.display = "none";
    } else {
      slides[i].style.display = "block";
    }
  }
}

function getVisibleSlides() {
  if (window.innerWidth >= 1200) {
    return 4;
  } else if (window.innerWidth >= 1024) {
    return 3;
  } else if (window.innerWidth >= 768) {
    return 2;
  } else {
    return 1;
  }
}

function updateSlider() {
  visibleSlides = getVisibleSlides();
  showSlide();
}

function nextSlide() {
  currentSlide++;
  if (currentSlide + visibleSlides > slides.length) {
    currentSlide = slides.length - visibleSlides;
  }
  showSlide();
}

function prevSlide() {
  currentSlide--;
  if (currentSlide < 0) {
    currentSlide = 0;
  }
  showSlide();
}

// Actualizar el slider cuando cambia el tamaño de la ventana
window.addEventListener("resize", updateSlider);

// Llama a la función showSlide() al cargar la página para mostrar las opciones por defecto.
showSlide();

window.onload= function(){
    var imagenCursoDiv = document.getElementById('imagen-curso');
    imagenCursoDiv.classList.add('hidden');
}

function mostrarImagenCurso(imagenUrl) {
    var imagenCursoDiv = document.getElementById('imagen-curso');
  
    // Limpiar cualquier contenido anterior
    imagenCursoDiv.innerHTML = '';
    imagenCursoDiv.classList.remove('hidden')
  
    // Crear un elemento de imagen y establecer la URL y atributo alt
    var imagenCurso = document.createElement('img');
    imagenCurso.src = imagenUrl;
    imagenCurso.alt = 'Imagen del curso';
  
    // Establecer estilos para ajustar la altura y centrar horizontalmente la imagen
    imagenCurso.style.maxHeight = '100%';
    imagenCurso.style.maxWidth = '100%';
    imagenCurso.style.display = 'block';
    imagenCurso.style.margin = '0 auto';
  
    // Agregar la imagen al div contenedor
    imagenCursoDiv.appendChild(imagenCurso);
  
    // Centrar la imagen verticalmente
    imagenCursoDiv.style.display = 'flex';
    imagenCursoDiv.style.justifyContent = 'center';
    imagenCursoDiv.style.alignItems = 'center';
  }
  
