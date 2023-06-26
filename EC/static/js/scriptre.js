window.onload = function() {
    // Obtener los elementos del formulario
    var matriculaInput = document.getElementById('Matricula');
    var institucionInput = document.getElementById('Institucion');
    var procedenciaRadios = document.getElementsByName('procedencia');
    var labelMatricula = document.getElementById('labelMatricula');
    var labelInstitucion = document.getElementById('labelInstitucion');
    var carreraInput = document.getElementById("Carrera");
    var labelCarrera = document.getElementById('labelCarrera')
    institucionInput.classList.add('hidden');
    labelInstitucion.classList.add('hidden');
    matriculaInput.classList.add('hidden');
    labelMatricula.classList.add('hidden');
    carreraInput.classList.add('hidden');
    labelCarrera.classList.add('hidden');
    institucionInput.classList.remove('required');
    matriculaInput.classList.remove('required');
  
    // Función para mostrar u ocultar los campos según la selección del radio
    function mostrarCampos() {
      if (procedenciaRadios[0].checked || procedenciaRadios[1].checked) {
        institucionInput.classList.add('hidden');
        labelInstitucion.classList.add('hidden');
        institucionInput.classList.remove('required');
        carreraInput.classList.remove('hidden');
        labelCarrera.classList.remove('hidden');


        matriculaInput.classList.remove('hidden');
        labelMatricula.classList.remove('hidden');
        matriculaInput.classList.add('required');

      } else {
        matriculaInput.classList.add('hidden');
        labelMatricula.classList.add('hidden');
        matriculaInput.classList.remove('required');
        carreraInput.classList.remove('hidden');
        labelCarrera.classList.remove('hidden');


        institucionInput.classList.remove('hidden');
        labelInstitucion.classList.remove('hidden');
        institucionInput.classList.add('required');

      }
    }
  
    // Asignar evento onclick a los radios para llamar a la función mostrarCampos
    for (var i = 0; i < procedenciaRadios.length; i++) {
      procedenciaRadios[i].onclick = mostrarCampos;
    }
};