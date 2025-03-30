<a name="readme-top"></a>
<div align="center">

# Tarea 1 de INF331 - Pruebas de Software

Esta aplicación permite gestionar el inventario de productos en la bodega de un negocio, facilitando operaciones de CRUD, control de stock, búsqueda y generación de reportes. Además, incluye autenticación para un acceso seguro. El desarrollo se organizó con Slack y GitHub, con manejo de excepciones mediante `try-catch-finally` y monitoreo de errores con Sentry.

</div>

<details>
<summary>Tabla de contenidos</summary>

- [Tareas de INF331 - Pruebas de Software](#tareas-de-inf331---pruebas-de-software)
- [Grupo de Trabajo](#-grupo-de-trabajo)
- [Requerimiento Especificado](#requerimiento-especificado)
- [Preguntas](#preguntas)
- [Instalación](#instalación)
- [¿Cómo usar?](#cómo-usar)
- [¿Cómo contribuir?](#cómo-contribuir)
- [Licencia](#licencia)

</details>

## 💼 Grupo de trabajo
- Valentina Castillo  - ROL: 202021006-3
- Javier Hormaechea - ROL: 202003017-0

## Requerimiento Especificado
El sistema debe ser una aplicación que se utilice a través de la **consola**, el cual permite la gestión del inventario de productos en la bodega de un negocio. Todos estos datos se deben almacenar en una base de datos, y se deben contar con las siguientes funcionalidades:
### 1. CRUD de Productos:
El sistema debe permitir a los usuarios:
1. Crear un producto ingresando los siguientes datos: Nombre, descripción, cantidad disponible (número entero), precio unitario (valor decimal) y categoría.
2. Consultar productos mostrando una lista con todos los productos registrados en la base de datos.
3. Actualizar productos permitiendo modificar los campos de un producto existente mediante su SKU.
4. Eliminar productos usando su nombre como identificador.

### 2. Gestión de Stock:
1. El usuario podrá actualizar la cantidad de un producto ingresando dirctamente el nuevo valor en la base de datos.
2. La actualización se hará mediante el nombre del producto.
3. Se debe validar que la cantidad sea un número positivo.

### 3. Filtrado y Búsqueda
1. El sistema debe permitir filtrar por categoría: mostrar solo los productos de una categoría específica.
2. El sistema debe permitir realizar una búsqueda por nombre, para mostrar todos los datos realizado a dicho producto.

### 4. Gestión de Reportes
1. Se debe mostrar un resumen del inventario, incluyendo: Número total de productos ingresados, valor total del inventario y una lista de los producos agotados.
2. El reporte igual debe mostrarse por consola.

### 5. Autenticación
1. El sistema requerirá un nombre de usuario y contraseña para acceder.
2. Solo usuarios autenticados podrán realizar operaciones en el inventario.
3. Se validará la combinación de usuario y contraseña con una base de datos de usuarios.

## Preguntas

### 1. ¿Cómo especificarías mejor el requerimiento? (Validación)
Para asegurarnos que que realmente estemos resolviendo el problema correcto, se pueden realizar las siguientes acciones:
- Revisar con el cliente si los requisitos definidos cumplen con la necesidad.
- Validación de Requisitos: aclarar ambigüedades y suposiciones (en este caso en especifico, a través del Foro de la Tarea).
- Pruebas Funcionales: Se realizan pruebas para verificar que el software realiza sus funciones de acuerdo con los requisitos especificados.

### 2. ¿Cómo asegurarías que el programa cumpla el requerimiento? (Verificación)
Para asegurarnos si estamos resolviendo correctamente el problema, se pueden realizar las siguientes acciones:
- Revisión de Código y Software: Se analiza el sistema en busca de defectos.
- Verificación de Diseño: Se revisa la arquitectura y el diseño del software para asegurarse de que cumple con los requisitos y está bien estructurado.
- Pruebas de Unidad e Integración.

### 3. Sobre la organización y el flujo del trabajo del proyecto
Para la organización del proyecto, se utilizó **Slack** como la principal herramienta de comunicación. Se creó un espacio de trabajo dedicado para coordinar las tareas y discutir avances. Además, se integró Slack con GitHub para recibir notificaciones automáticas sobre cambios en el repositorio, lo que facilitó el seguimiento del desarrollo. También se elaboró una lista de tareas para registrar y monitorear las actividades pendientes, asegurando así un flujo de trabajo estructurado y eficiente. 

En cuanto al manejo de errores, se implementó el método `try-catch-finally` para gestionar excepciones y garantizar un control adecuado de fallos en la ejecución del código. Adicionalmente, se integró **Sentry** como herramienta de monitoreo para registrar y analizar logs de errores, lo que permite detectar y resolver problemas de manera más rápida y eficiente.

#### Gestión del Código Fuente
Para administrar el código fuente de este proyecto, se optó por elegir el enfoque de **Trunk-Based Development (TBD)**.  Esta elección se debe a que somos un equipo de dos personas y este modelo permite:

- Una integración rápida de cambios.
- Menos conflictos en fusiones, ya que las ramas son de corta duración.
- La colaboración es más fluida, a través de revisiones ágiles y entrega continua.

#### Aspectos de Administración
**1. Ramas**
- Para cada funcionalidad o tarea que implique cambios complejos, se creará una nueva rama. Por ejemplo: Por ejemplo: `feature-agregar-productos`
- Para cambios pequeños y ajustes menores (como la actualización de `README.md`), se permite trabajar directamente en `main`.

**2. Protección de Ramas**
- Se prohíbe hacer `push` directo a `main` para cambios complejos.
- Los cambios deben ser fusionados mediante Pull Requests (PRs).
- No se permiten `force pushes`.
- Cada PR debe ser revisado por el otro miembro del equipo.

### 4. Evidencias de flujo de trabajo y configuraciones realizadas

#### 4.1. Integración de GitHub con Slack:

![image](https://github.com/user-attachments/assets/1f39bd33-add7-4ebb-9834-2c12b1bb696d)

#### 4.2. Organización de Tareas con Slack:
![image](https://github.com/user-attachments/assets/6d7dc5d3-27bf-4938-bbdb-cae19d1b8060)

#### 4.3. Evidencia de Trunk-Based Development (TBD)
![image](https://github.com/user-attachments/assets/9480e13e-b5e1-4811-8a61-60a36668b739)

#### 4.4. Integración de Sentry
![image](https://github.com/user-attachments/assets/4a039dee-0841-41bc-820c-8932d59ed16c)

### 5. Sobre los problemas encontrados

## Instalación
Para instalar y ejecutar el proyecto, sigue estos pasos:
1. Descargar el código fuente o clonar el repositorio con el siguiente comando:
```
git clone https://github.com/valnhe/Tareas-Pruebas-de-Software.git
cd tu-repo
```
2. Instalar Python
Asegúrate de tener Python 3 instalado en tu sistema. Puedes verificarlo con:
```
python3 --version
```

## ¿Cómo usar?
Para ejecutar el probrama, usa el siguiente comando desde la raíz del proyecto:
```
python src/app.py
```
### Primer uso
1. Registrarse o iniciar sesión.
2. Después de registrarse o iniciar sesión, se entrará entrará automáticamente al menú principal para gestionar la base de datos.
   - **Nota**: La base de datos ya contiene datos preexistentes del repositorio, por lo que se puede comenzar a trabajar directamente.
     
## ¿Cómo contribuir?

Si tienes alguna sugerencia que podría mejorar el proyecto, por favor haz un [_fork_](https://github.com/valnhe/Tareas-Pruebas-de-Software/fork) del repositorio y crea una [_pull request_](https://github.com/valnhe/Tareas-Pruebas-de-Software/pulls). O simplemente puedes crear una [_issue_](https://github.com/valnhe/Tareas-Pruebas-de-Software/issues) y lo estaremos leyendo 😊.
Aquí tienes una guía rápida:

1. Haz un [_fork_](https://github.com/valnhe/Tareas-Pruebas-de-Software/fork) del Proyecto
2. Clona tu [_fork_](https://github.com/valnhe/Tareas-Pruebas-de-Software/fork) (`git clone <URL del fork>`)
3. Añade el repositorio original como remoto (`git remote add upstream <URL del repositorio original>`)
4. Crea tu Rama de Funcionalidad (`git switch -c feature-CaracteristicaIncreible`)
5. Realiza tus Cambios (`git commit -m 'Add: alguna CaracterísticaIncreible'`)
6. Haz Push a la Rama (`git push origin feature-CaracteristicaIncreible`)
7. Abre una [_pull request_](https://github.com/valnhe/Tareas-Pruebas-de-Software/pulls)

## Licencia
 Por favor, revise [este link](https://github.com/valnhe/Tareas-Pruebas-de-Software/blob/main/LICENSE).
