function calcularPrecio(){
    var nombre = document.getElementById('nombre').value;
    var boleto = parseInt(document.getElementById('boleto').value);
    var precioUnitario = 100;

    var total = boleto * precioUnitario;

    document.getElementById('Precio').innerHTML = "Precio total para " + nombre +": $" + total;
}

function calcularCambio(){
    var totalPago = parseInt(document.getElementById('pago').value);
    var precioTotal = parseInt(document.getElementById('precioTotal').innerText);
    var metodoPago = document.querySelector('input[name="pago"]:checked').value;

    var cambio = totalPago - precioTotal;
    document.getElementById('Cambio').innerText = "Su cambio es $" + cambio + ". Pago realizado con " + metodoPago;
}
