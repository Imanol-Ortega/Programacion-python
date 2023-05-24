nombre=''
apellido=''
curso=''
porasis=0
mod=0
punt = 100
punta = 0
porcentaje = False
puntaje = False

nombre = input('Ingrese su nombre: ')
apellido = input('\nIngrese su apellido: ')
curso = input('\nIngrese su curso.\n1.Primero.\n2.Segundo.\n3.Tercero\n4.Cuarto.\n')
porasis = int(input('\nIngrese su porcentaje de asistencia: '))
mod = int(input('\nIngrese su modalidad.\n1.presencial\n2.semi-presencial.\n3.virtual\n'))
punta = int(input('\nIngrese su puntaje en la materia de programacion: '))

if mod==1:
    if porasis>=80:
        porcentaje = True
    if punta>=80:
        puntaje = True
elif mod==2:
    if porasis>=50:
        porcentaje=True
    if punta>=85:
        puntaje = True
elif mod==3:
    porcentaje = True
    if punta>=90:
        puntaje = True


print('\nEl alumno',nombre,' ',apellido,' del curso ',curso)
if porcentaje == True:
    if puntaje == True:
        print(' aprobo la  materia de programacion')
    else:
        print(' no aprobo por no alcanzar el puntaje')
else:
    print(' no aprobo por no alcanzar la asistencia minima')        


