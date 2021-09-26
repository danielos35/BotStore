import random 
# import random  allow import radoms values from a list o functions
saludos =('Bienvenido, ¿en que puedo ser de ayuda?', '¿Bienvenido a mi web, buscas alguna asesoria en especial?', 'Bienvenido a mi web, ¿Que puedo programar por ti?.')
skills = ('Data scientist junior (EAFIT)','Web Developer Junior(UPB-SENA-CESDE)')
servicio = ('pagina web','aplicación movil','otro')
print (random.choice(saludos))

def indu_saludo():
    global servicio
    for i, servicios in enumerate(servicio):
        print(i+1,'',servicio[i])
        
    servicio = input('Elige una de las opciones: ')
    if servicio == '1':
        print('¿Quieres conoces antes algunos de nuestros proyectos?')
        print('1. Si, conozcamos un poco')
        print('2. No, ya se que quiero hacer')
        mostrar = input('¿Que deseas resalizar?: ')
        if mostrar =='1':
            print('Bienvenido a nuestro portafolio')
        elif mostrar == '2':
            print('Cuentanos en detalle tu proyecto, para brindarte la mejor información')

       
        
def skill():
    global skills
    print('¿Quieres conocer un poco de mi formación academica?')
    print('Si, cuentame sobre ti.')
    print('No, quizas en una proxima ocasión.')
    eleccion =  input('Selecciona una opción')
    if eleccion.lower().strip()== 'si': #.lower convert the text in lowercase .strip clean the spae in the star an in the end
        for j, habilidad in enumerate(skills):
            print(j+1,'',habilidad)
skill()            
            