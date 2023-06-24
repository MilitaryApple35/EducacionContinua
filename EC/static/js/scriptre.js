window.onload = function() {
    // Obtener los elementos del formulario
    var matriculaInput = document.getElementById('Matricula');
    var institucionInput = document.getElementById('Institucion');
    var procedenciaRadios = document.getElementsByName('procedencia');
  
    // Función para mostrar u ocultar los campos según la selección del radio
    function mostrarCampos() {
      if (procedenciaRadios[0].checked || procedenciaRadios[1].checked) {
        matriculaInput.classList.remove('hidden');
        institucionInput.classList.add('hidden');
      } else {
        matriculaInput.classList.add('hidden');
        institucionInput.classList.remove('hidden');
      }
    }
  
    // Asignar evento onclick a los radios para llamar a la función mostrarCampos
    for (var i = 0; i < procedenciaRadios.length; i++) {
      procedenciaRadios[i].onclick = mostrarCampos;
    }
  };