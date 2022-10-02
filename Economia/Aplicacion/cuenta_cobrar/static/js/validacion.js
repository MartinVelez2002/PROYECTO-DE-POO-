//////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////
/* Para calcular las cuotas mensuales */
const deuda =  document.getElementById("deu");
const plazo =  document.getElementById("mes");
const btnCal = document.getElementById("btnCalcular");
const captInt = document.getElementById("id_interes");




btnCal.addEventListener('click', () => {
    calcular(deuda.value, plazo.value, captInt.value);
});

function calcular(deuda, plazo, captInt) {
    let inter = captInt/100
    let cuota = deuda/plazo;
    let mensual = (((cuota * inter) + cuota).toFixed(2))
    let sal_int = (deuda * inter) + parseInt(deuda)

    document.registro.cuotamen.value = mensual;
    document.registro.saldo.value = sal_int;


};

///////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////



