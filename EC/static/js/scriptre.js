window.onload = function() {
    // Obtener los elementos del formulario
    var matriculaInput = document.getElementById('Matricula');
    var institucionInput = document.getElementById('Institucion');
    var procedenciaRadios = document.getElementsByName('procedencia');
    var tipoRadios = document.getElementsByName('tipoRegistro')
    var labelMatricula = document.getElementById('labelMatricula');
    var labelInstitucion = document.getElementById('labelInstitucion');
    var carreraInput = document.getElementById("Carrera");
    var labelCarrera = document.getElementById('labelCarrera')
    var selectorCursos = document.getElementById('selector-Cursos')
    var selectorConferencias = document.getElementById('selector-Conferencias')
    var selectorTalleres = document.getElementById('selector-Talleres')
    var selectorDiplomados = document.getElementById('selector-Diplomados')
    var selectorCongresos = document.getElementById('selector-Congresos')
    var selectorCapacitaciones = document.getElementById('selector-Capacitaciones')
    institucionInput.classList.add('hidden');
    labelInstitucion.classList.add('hidden');
    matriculaInput.classList.add('hidden');
    labelMatricula.classList.add('hidden');
    carreraInput.classList.add('hidden');
    labelCarrera.classList.add('hidden');
    institucionInput.classList.remove('required');
    matriculaInput.classList.remove('required');
    selectorCursos.classList.add('hidden');
    selectorConferencias.classList.add('hidden');
    selectorTalleres.classList.add('hidden');
    selectorDiplomados.classList.add('hidden');
    selectorCongresos.classList.add('hidden');
    selectorCapacitaciones.classList.add('hidden');
  
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
        institucionInput.value= "UPSIN";

      } else {
        matriculaInput.classList.add('hidden');
        labelMatricula.classList.add('hidden');
        matriculaInput.classList.remove('required');
        carreraInput.classList.remove('hidden');
        labelCarrera.classList.remove('hidden');
        institucionInput.value="";


        institucionInput.classList.remove('hidden');
        labelInstitucion.classList.remove('hidden');
        institucionInput.classList.add('required');

      }
    }
  
    // Asignar evento onclick a los radios para llamar a la función mostrarCampos
    for (var i = 0; i < procedenciaRadios.length; i++) {
      procedenciaRadios[i].onclick = mostrarCampos;
    }

    function mostrarSelector(selectorId) {
      var selectores = document.getElementsByClassName('selector-tipo');
      
      for (var i = 0; i < selectores.length; i++) {
        selectores[i].classList.add('hidden');
      }
      
      var selector = document.getElementById(selectorId);
      if (selector) {
        selector.classList.remove("hidden");
      }
    }

    for (var i = 0; i < tipoRadios.length; i++) {
      tipoRadios[i].onclick = mostrarSelector;
    }
};