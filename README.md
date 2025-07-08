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



