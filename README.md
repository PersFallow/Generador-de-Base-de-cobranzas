# Generador-de-Base-de-cobranzas
Automatización ETL de bases de cobranzas con Python

Desarrollé una herramienta ETL en Python para automatizar la consolidación, normalización y validación de bases de cobranzas de la empresa en la que trabajé en uno de mis ultimas relaciones laborales, procesando volúmenes de entre 2 y 8 millones de clientes. La solución reemplazó tareas manuales realizadas en Excel, optimizando el procesamiento de grandes volúmenes de información. Dado ciertos requerimientos, se solicita crear un programa que reciba un archivo de texto csv y genere una base de cobranzas.
- El formato de las fechas debe ser ser modificado
- el orden de las columnas debe ser modificado
- Cada cliente puede aparecer un máximo de dos veces
- Se desea arreglar el formato de los numeros

Eso nos lleva a esta mini aplicación que hice para automatizar estos mismos procesos.
Adicional: Este código no está patentado ni licenciado bajo ninguna NDA 
Para usarlo debes droppear las bases de cobranza en la carpeta de bases, y el programa te devolverá la base unificada.

Para el tipo de archivos que recibiamos, este código cumple perfectamente lo solicitado, obviamente puede variar dependiendo de las necesidades del negocio en caso de que nos envien otro tipos de bases.
