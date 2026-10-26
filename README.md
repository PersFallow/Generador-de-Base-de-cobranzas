# Generador-de-Base-de-cobranzas
ETL api

Para un proyecto de automatización en uno de mis ultimos trabajos: 
Dado ciertos requerimientos, se solicita crear un programa que reciba un archivo de texto csv y genere una base de cobranzas
- El formato de las fechas debe ser ser modificado
- el orden de las columnas debe ser modificado
- Un ID no debe estar repetido
- Se desea arreglar el formato de los numeros

Eso nos lleva a esta mini api que hice para automatizar procesos de una de las empresas en las que trabaje. 

Adicional: Este código no está patentado ni licenciado bajo ninguna NDA 

Para usarlo debes droppear las bases de cobranza en la carpeta de bases, y el programa te devolverá la base unificada.

Este programa fue creado para automatizar un proceso que en excel puede demorar varias horas debido a que excel no es tan bueno con el porcesamiento de grandes volumenes de datos
