// Función para abrir la ventana emergente
function abrirVentanaEmergente(ventana) {
  // CURSOS
  if (ventana == 1){
    var ventanaEmergente = document.getElementById('ventanaEmergenteAgregar');
  }
  if (ventana == 2){
    var ventanaEmergente = document.getElementById('ventanaEmergenteModificar');
  }
  if (ventana == 3) {
    var ventanaEmergente = document.getElementById('ventanaEmergenteEliminar');
  }
  // CONFERENCIAS
  if(ventana == 4){ 
    var ventanaEmergente = document.getElementById('ventanaEmergenteAgregarConferencias');
  }
  if(ventana == 5){ 
    var ventanaEmergente = document.getElementById('ventanaEmergenteModificarConferencias');
  }
  if(ventana == 6){ 
    var ventanaEmergente = document.getElementById('ventanaEmergenteEliminarConferencias');
  }
  if(ventana == 7){ 
    var ventanaEmergente = document.getElementById('ventanaEmergenteAgregarTalleres');
  }
  if(ventana == 8){ 
    var ventanaEmergente = document.getElementById('ventanaEmergenteModificarTalleres');
  }
  if(ventana == 9){ 
    var ventanaEmergente = document.getElementById('ventanaEmergenteEliminarTalleres');
  }
  if (ventana === 10) {
    var ventanaEmergente = document.getElementById('ventanaEmergenteAgregarDiplomados');
  }
  if (ventana === 11) {
    var ventanaEmergente = document.getElementById('ventanaEmergenteModificarDiplomados');
  }
  if (ventana === 12) {
    var ventanaEmergente = document.getElementById('ventanaEmergenteEliminarDiplomados');
  }
  if (ventana === 13) {
    var ventanaEmergente = document.getElementById('ventanaEmergenteAgregarCongresos');
  }
  if (ventana === 14) {
    var ventanaEmergente = document.getElementById('ventanaEmergenteModificarCongresos');
  }
  if (ventana === 15) {
    var ventanaEmergente = document.getElementById('ventanaEmergenteEliminarCongresos');
  }
  if (ventana === 16) {
    var ventanaEmergente = document.getElementById('ventanaEmergenteAgregarCapacitaciones');
  }
  if (ventana === 17) {
    var ventanaEmergente = document.getElementById('ventanaEmergenteModificarCapacitaciones');
  }
  if (ventana === 18) {
    var ventanaEmergente = document.getElementById('ventanaEmergenteEliminarCapacitaciones');
  }
  ventanaEmergente.style.display = 'block';
  ventanaEmergente.style.opacity = '1'; /* Cambiamos la opacidad a 1 para hacerla completamente visible */
  ventanaEmergente.style.pointerEvents = 'auto'; /* Hacemos clicables los elementos dentro de la ventana emergente */
}
  
  // Función para cerrar la ventana emergente
function cerrarVentanaEmergente(ventana) {
  //CURSOS
  if (ventana == 1){
    var ventanaEmergente = document.getElementById('ventanaEmergenteAgregar');
  }
  if (ventana == 2){
    var ventanaEmergente = document.getElementById('ventanaEmergenteModificar');
  }
  if (ventana == 3) {
    var ventanaEmergente = document.getElementById('ventanaEmergenteEliminar');
  }
  // CONFERENCIAS
  if(ventana == 4){ 
    var ventanaEmergente = document.getElementById('ventanaEmergenteAgregarConferencias');
  }
  if(ventana == 5){ 
    var ventanaEmergente = document.getElementById('ventanaEmergenteModificarConferencias');
  }
  if(ventana == 6){ 
    var ventanaEmergente = document.getElementById('ventanaEmergenteEliminarConferencias');
  }
  if(ventana == 7){ 
    var ventanaEmergente = document.getElementById('ventanaEmergenteAgregarTalleres');
  }
  if(ventana == 8){ 
    var ventanaEmergente = document.getElementById('ventanaEmergenteModificarTalleres');
  }
  if(ventana == 9){ 
    var ventanaEmergente = document.getElementById('ventanaEmergenteEliminarTalleres');
  }
  if (ventana === 10) {
    var ventanaEmergente = document.getElementById('ventanaEmergenteAgregarDiplomados');
  }
  if (ventana === 11) {
    var ventanaEmergente = document.getElementById('ventanaEmergenteModificarDiplomados');
  }
  if (ventana === 12) {
    var ventanaEmergente = document.getElementById('ventanaEmergenteEliminarDiplomados');
  }
  if (ventana === 13) {
    var ventanaEmergente = document.getElementById('ventanaEmergenteAgregarCongresos');
  }
  if (ventana === 14) {
    var ventanaEmergente = document.getElementById('ventanaEmergenteModificarCongresos');
  }
  if (ventana === 15) {
    var ventanaEmergente = document.getElementById('ventanaEmergenteEliminarCongresos');
  }
  if (ventana === 16) {
    var ventanaEmergente = document.getElementById('ventanaEmergenteAgregarCapacitaciones');
  }
  if (ventana === 17) {
    var ventanaEmergente = document.getElementById('ventanaEmergenteModificarCapacitaciones');
  }
  if (ventana === 18) {
    var ventanaEmergente = document.getElementById('ventanaEmergenteEliminarCapacitaciones');
  }
    ventanaEmergente.style.opacity = '0'; /* Cambiamos la opacidad a 0 para hacerla completamente transparente */
    ventanaEmergente.style.pointerEvents = 'none'; /* Evitamos que los elementos dentro de la ventana emergente sean clicables */
    setTimeout(function () {
      ventanaEmergente.style.display = 'none'; /* Después de la transición, ocultamos la ventana emergente */
    }, 300); /* Esperamos 300ms para ocultarla después de que termine la transición de 0.3 segundos */
}



  