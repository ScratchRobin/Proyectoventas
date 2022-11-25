print("****Bienvenidos**** ");
import time

name=str(input("Ingrese su nombre:"));
nac=int(input("Ingrese su nacimiento:"));
if(nac >= 2004):
    print("Lo sentimos ",name,"eres menor de edad");
    time.sleep(5);
    print("");
    print("Hasta pronto");
elif(nac<2004):
    print("-------------");
    print("//////Ventas del 2021//////");
    print("----------------");
    semana_1=float(input("Ingrese las ventas del primer semestre:"));
    seman_2=float(input("Ingrese  las ventas del segundo semestre:"));
    total=float(semana_1+seman_2);
    if(semana_1 > seman_2):
           mejor="1ro.(Primer semestre)";
    elif(seman_2 > semana_1):
           mejor="2do.(Segundo semestre)";
    else:
           mejor="las ventas semesstrales son iguales";

    if(total < 100000.00):
            medal="Bronce";
            prize="Un dia libre";

    elif (total < 500000.00):
             medal="Plata";
             prize="Un dia libre  y un bono  de Q250";

    elif (total < 1000000.00):
             medal = "oro";
             prize = "Un dia libre  y un bono  de Q500";
    else:
            medal="Diamante";
            prize="Dos dias de libres  y un bono de Q1000";

    print("");
    print("**************");
    print("*****RESUMEN DE REGISTRODE TODAS LAS VENTAS*****");
    print("Vendedor:",name);
    print("Ventas anuales:Q",total);
    print("Mejor semestre:",mejor);
    print("Medalla acreditada:",medal);
    print("Premio:",prize);
    time.sleep(5);
    print("");
    print("******Adios******");
    time.sleep(5);



