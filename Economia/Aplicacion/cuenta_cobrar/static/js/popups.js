const registro = document.getElementById("insertar");

function abrir_modal(url){
    (registro).load(url,function(){
        (this).modal('show');
    });
}