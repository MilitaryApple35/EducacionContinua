let currentSlide = 0;
let visibleSlides = getVisibleSlides();
var imagenCursoDiv = document.getElementById('imagen-curso');
var sliderCursos = document.getElementById('sld-Cursos');
var sliderConferencias = document.getElementById('sld-Conferencias');
var sliderTalleres = document.getElementById('sld-Talleres');
var sliderDiplomados = document.getElementById('sld-Diplomados');
var sliderCongresos = document.getElementById('sld-Congresos');
var sliderCapacitaciones = document.getElementById('sld-Capacitaciones');

function showSlideForSlider(slides) {
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
  showSlideForSlider(slides);
}

function nextSlide(sliderId) {
  var slides = $('#' + sliderId + ' .box');
  currentSlide++;
  if (currentSlide + visibleSlides > slides.length) {
    currentSlide = slides.length - visibleSlides;
  }
  showSlideForSlider(slides);
}

function prevSlide(sliderId) {
  var slides = $('#' + sliderId + ' .box');
  currentSlide--;
  if (currentSlide < 0) {
    currentSlide = 0;
  }
  showSlideForSlider(slides);
}

// Actualizar el slider cuando cambia el tamaño de la ventana
window.addEventListener("resize", updateSlider);

// Llama a la función showSlide() al cargar la página para mostrar las opciones por defecto.


window.onload= function(){
  console.log("Window loaded");
  imagenCursoDiv.classList.add('hidden');
  sliderConferencias.classList.add('hidden');
  sliderTalleres.classList.add('hidden');
  sliderDiplomados.classList.add('hidden');
  sliderCongresos.classList.add('hidden');
  sliderCapacitaciones.classList.add('hidden');
  var slides = $('#sld-Cursos .box');
  showSlideForSlider(slides);
}

function botonCursos(){
  imagenCursoDiv.classList.add('hidden');
  sliderCursos.classList.remove('hidden');
  sliderConferencias.classList.add('hidden');
  sliderTalleres.classList.add('hidden');
  sliderDiplomados.classList.add('hidden');
  sliderCongresos.classList.add('hidden');
  sliderCapacitaciones.classList.add('hidden');
  var slides = $('#sld-Cursos .box');
  currentSlide = 0; 
  showSlideForSlider(slides);
}

function botonConferencias(){
    imagenCursoDiv.classList.add('hidden');
    sliderCursos.classList.add('hidden');
    sliderConferencias.classList.remove('hidden');
    sliderTalleres.classList.add('hidden');
    sliderDiplomados.classList.add('hidden');
    sliderCongresos.classList.add('hidden');
    sliderCapacitaciones.classList.add('hidden');
    var slides = $('#sld-Conferencias .box');
    currentSlide = 0; 
    showSlideForSlider(slides);
  }
  function botonTalleres(){
    imagenCursoDiv.classList.add('hidden');
    sliderCursos.classList.add('hidden');
    sliderConferencias.classList.add('hidden');
    sliderTalleres.classList.remove('hidden');
    sliderDiplomados.classList.add('hidden');
    sliderCongresos.classList.add('hidden');
    sliderCapacitaciones.classList.add('hidden');
    var slides = $('#sld-Talleres .box');
    currentSlide = 0; 
    showSlideForSlider(slides);
  }
  function botonDiplomados(){
    imagenCursoDiv.classList.add('hidden');
    sliderCursos.classList.add('hidden');
    sliderConferencias.classList.add('hidden');
    sliderTalleres.classList.add('hidden');
    sliderDiplomados.classList.remove('hidden');
    sliderCongresos.classList.add('hidden');
    sliderCapacitaciones.classList.add('hidden');
    var slides = $('#sld-Diplomados .box');
    currentSlide = 0; 
    showSlideForSlider(slides);
  }
  function botonCongresos(){
    imagenCursoDiv.classList.add('hidden');
    sliderCursos.classList.add('hidden');
    sliderConferencias.classList.add('hidden');
    sliderTalleres.classList.add('hidden');
    sliderDiplomados.classList.add('hidden');
    sliderCongresos.classList.remove('hidden');
    sliderCapacitaciones.classList.add('hidden');
    var slides = $('#sld-Congresos .box');
    currentSlide = 0; 
    showSlideForSlider(slides);
  }
  function botonCapacitaciones(){
    imagenCursoDiv.classList.add('hidden');
    sliderCursos.classList.add('hidden');
    sliderConferencias.classList.add('hidden');
    sliderTalleres.classList.add('hidden');
    sliderDiplomados.classList.add('hidden');
    sliderCongresos.classList.add('hidden');
    sliderCapacitaciones.classList.remove('hidden');
    var slides = $('#sld-Capacitaciones .box');
    currentSlide = 0; 
    showSlideForSlider(slides);
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
  
