// Función para abrir la ventana emergente
function abrirVentanaEmergente(ventana) {
  if (ventana == 1){
    var ventanaEmergente = document.getElementById('ventanaEmergenteAgregar');
  }
  if (ventana == 2){
    var ventanaEmergente = document.getElementById('ventanaEmergenteModificar');
  }
  if (ventana == 3) {
    var ventanaEmergente = document.getElementById('ventanaEmergenteEliminar')
  }
    ventanaEmergente.style.display = 'block';
    ventanaEmergente.style.opacity = '1'; /* Cambiamos la opacidad a 1 para hacerla completamente visible */
    ventanaEmergente.style.pointerEvents = 'auto'; /* Hacemos clicables los elementos dentro de la ventana emergente */
}
  
  // Función para cerrar la ventana emergente
function cerrarVentanaEmergente(ventana) {
  if (ventana == 1){
    var ventanaEmergente = document.getElementById('ventanaEmergenteAgregar');
  }
  if (ventana == 2){
    var ventanaEmergente = document.getElementById('ventanaEmergenteModificar');
  }
  if (ventana == 3) {
    var ventanaEmergente = document.getElementById('ventanaEmergenteEliminar');
  }
    ventanaEmergente.style.opacity = '0'; /* Cambiamos la opacidad a 0 para hacerla completamente transparente */
    ventanaEmergente.style.pointerEvents = 'none'; /* Evitamos que los elementos dentro de la ventana emergente sean clicables */
    setTimeout(function () {
      ventanaEmergente.style.display = 'none'; /* Después de la transición, ocultamos la ventana emergente */
    }, 300); /* Esperamos 300ms para ocultarla después de que termine la transición de 0.3 segundos */
}



  