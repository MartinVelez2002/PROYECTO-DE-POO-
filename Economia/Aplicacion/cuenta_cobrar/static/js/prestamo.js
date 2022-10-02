var btn = document.getElementById('btnCalcular')
btn.addEventListener('click',gen_table)

function gen_table(){
    document.getElementById("tab").innerHTML="";
    fechaInicio = new Date(document.getElementById('fecha').value);
    fechaInicio.setDate(fechaInicio.getDate() + 1) //Actual
    Primerafecha = new Date(fechaInicio);
    let n=Number(document.getElementById("deu").value);
    let n2=Number(document.getElementById("mes").value);
    let n3=Number(document.getElementById("id_interes").value);
    if(n>0){
        for(i=1;i<=n2;i++){
            let fe
            ca=n/n2;
            d1=ca.toFixed(2);
            i2=((n*n3)/100)/n2;
            d2=i2.toFixed(2);
            r=ca+i2;
            d3=r.toFixed(2);
            Primerafecha.setMonth(Primerafecha.getMonth()+1);
            fe = Primerafecha.toLocaleDateString();
            document.getElementById("tab").innerHTML=document.getElementById("tab").innerHTML+
                    `<tr>
                        <td> ${i}</td>
                        <td> ${d1}</td>
                        <td> ${d2}</td>
                        <td> ${d3}</td>
                        <td> ${fe} </td>
                    </tr>`;
        }
        n1=n.toFixed(2);
        t_i=i2*n2;
        d4=t_i.toFixed(2);
        t_p=r*n2;
        d5=t_p.toFixed(2);
        document.getElementById("t1").innerHTML=n1;
        document.getElementById("t2").innerHTML=d4;
        document.getElementById("t3").innerHTML=d5;
    }

}