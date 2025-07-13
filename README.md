# Pasos


**Paso 1:**
Deberas crear un python virtual environment de la siguiente forma


```
python -m venv ./venv      
```

**Paso 2:**
Deberas activar el virtual environment con el siguiente comando:

Para PowerShell:
```bash
.venv/Scripts/Activate.ps1 
```



En caso de que no funcione el commando 

```bash
.\venv\Scripts\Activate.ps1
```


Corre este comadno en la terminal:
```bash
 Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

es posible que se deba a ha este error:
```bash 
+ .\venv\Scripts\Activate.ps1
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```

Nota: Despues de haber activbado el envrionemnt deberan correr pip install

Para correr la API
fastapi run main.py --reload


## Librerias 
pip install selenium






Project Description:
Necestio que seas un buen Project Manager y me ayudes a crear tareas con estiumaciones de tiempo para mi proyecto.



Este proyecto tiene como proposito conectarse a la API de canvas LSM para crear un aplicacion que permita
a los estudiantes descragar y acceders a los recursos de los cursos de una forma mas facil. El primero paso es sincronizar estos recursos con la aplicacion
para que el usuario pueda acceder a ellos sin ningun problema. 
Actualmente podrian existir aplicaciones similares sin embargo cada institucion tiene una CAVAS con configuraciones muy diferentes y por ello debemos crear esta API.

Para el front end tengo pensado usar Angular necesito evaluar cual se adaptaria mejor y que otras herramientas puede facilitarme el proceso de creacion de componentes para la app.

Por ahora la idea es que esto sea una web-app y desktop app.   

Por otra parte me estoy apoyando en gemini para generar compoenentes pero necesito saber que librerias de componentes totalmente graturias puedo incorporar a angular.


Neceisto crear una serie de tareas para comenzar este proyecto, hare uso de la metodologia Scrum entonces necesito estimacion de tiempo de cada tarea.
Neceisot que generes tambien una lista de herramientas que consideres aptas para este proyecto ya que debe ser una aplicacion escalable.

Para la API
Algunas de las librerias que usare son fastapi, canvassync, canvasapi


Estado del proyecto: Acutalmente he creado una API usando fastapi y tengo lista la estructura del proyecto sin embargo necesito todavia trabajar en los siguientes:
que tendran ofrecer funciones como obtener datos del estudiante, los cursos y mnodulos dentro de los curos que es donde se encuentran los archivos.

