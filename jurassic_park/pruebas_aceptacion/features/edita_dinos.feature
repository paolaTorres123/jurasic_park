Característica: Editar dinosaurio
    Como usuario del sistema Jurassic Park
    Quiero modificar un dinosaurio del inventario
    Para tener actualizados los datos del dinosaurio en la lista de dinosaurios

    Escenario: Edición de datos correctos para el dinosaurio
        Dado que ingreso a la lista de dinosaurios existentes
        Y busco el dinosaurio por su nombre llamado "t-rex"
        Cuando presiono el botón editar
        Y modifico los datos de nombre a : "t-rex spike"
        Y presiono el botón guardar
        Entonces puedo ver la modificación que le hice al dinosaurio en su nombre por "t-rex spike" en la lista de dinosaurios