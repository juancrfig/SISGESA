# SISGESA
Modernización del sistema de gestión de asistencia para ACME Education.

SISTEMA DE GESTION DE ASISTENCIA
--------------------------------
Nombre del software:  Sistema de Gestion de Asistencia Academica (SISGESA)

REQUERIMIENTOS:

1. Inicio de Sesión

   - Al iniciar el programa se solicita nombre de usuario y contraseña
   - Primera vez que se ejecute el programa la contraseña predefinida será "SISGESA" 
   - Guardar contraseña en un archivo y asegurarla mediante algoritmos de encriptación nativos de Python
   - Debe permitirse el cambio de contraseña desde el menú

2. Menú de Opciones

   - Registro de grupos
   - Registro de módulos
   - Registro de estudiantes
   - Registro de docentes
   - Registro de asistencia
   - Consultas de información
   - Generación de informes
   - Cambio de contraseña
   - Salida del sistema


3. Registro de Grupos

   Se debe permitir el registro de grupos de estudiantes. Cada grupo se identifica por un codigo, un nombre y una sigla

4. Registro de Modulos

   Ya que la institucion ofrece varios modulos, se debe poder registrar la informacion de cada modulo, que incluye su codigo, nombre y duracion en semanas

5. Registro de estudiantes

   El registro de estudiantes se realiza pidiendo codigo, nombre, sexo y edad

6. Asignacion de Estudiantes a Grupos y Módulos

   Los estudiantes se asignarán a un único grupo y podrán matricularse entre 1-3 modulos
   El sistema debe permitir asociar a los estudiantes con sus respectivos grupos y modulos

7. Registro de docentes

   Los docentes deben ser registrados en el sistema, identificados por su cédula y nombre. Un docente puede impartir hasta tres módulos diferentes. 

8. Registro de Asistencia

   El sistema debe permitir registrar la asistencia de los estudiantes. Los datos que se reciben serán:
   - Codigo Estudiante
   - Codigo Modulo
   - Fecha y hora de entrada
   - Fecha y hora de salida

9. Consultas por codigo

   Las consultas se realizarán exclusivamente utilizando los códigos de los grupos, módulos, estudiantes y docentes
   El sistema debe permitir:
   - Consultar los estudiantes matriculados en un grupo
   - Consultar los estudiantes inscritos en un módulo
   - Consultar los docentes que imparten un módulo
   - Consultar los estudiantes a cargo de un docente en un módulo

10. Informes de Asistencia

   El sistema debe generar informes con los siguientes datos: 
   - Estudiantes que han llegado tarde a un módulo en un mes específico
   - Estudiantes que se retiraron antes de la finalización de una sesión en un mes específico
   - Estudiantes que no han faltado a ningún módulo durante un mes
   - Porcentaje de asistencia por módulo, calculado como la proporción de estudiantes que asistieron al inicio de clase respecto al total de estudiantes matriculados

11. Persistencia de Datos

   Todos los datos relacionados con estudiantes, grupos, módulos y docentes deben ser almacenados de manera persistente en archivos

12. Formato de Salida

   Los informes generados por el sistema deben ser legibles y estar bien formateados en la consola. El uso de tablas o listas numeradas será fundamental para garantizar la claridad de la información

13. Manejo de Errores y Validación de Datos

    El sistema debe manejar correctamente entradas inválidas tanto en el menú como en las diversas funcionalidades. Debe guiar al usuario para que ingrese opciones o datos correctos. 
    El manejo de errores debe implementarse de forma robusta para asegurar que el programa no se interrumpa inesperadamente. 

14. Cambio de Contraseña y Seguridad

    La contraseña actualizada debe ser encriptada utilizando el algoritmo SHA-256 antes de ser almacenada en el archivo correspondiente
    En cada nuevo inicio del programa, el sistema debe solicitar la contraseña encriptada y verificarla antes de permitir el acceso al menú principal

15. Salida del Sistema

   El programa debe permitir al usuario salir de manera segura, asegurándose de que toda la información se guarde correctamente antes de finalizar la ejecución


--------------------------------------------------------

RESTRICCIONES TECNICAS

   - Usar lo visto en el modulo 2
   - No instalar modulos adicionales
   - Implementar la persistencia de datos mediante JSON
