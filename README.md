<a name="readme-top"></a>
<div align="center">

# Tarea 1 de INF331 - Pruebas de Software

Esta aplicación permite gestionar el inventario de productos en la bodega de un negocio, facilitando operaciones de CRUD, control de stock, búsqueda y generación de reportes. Además, incluye autenticación para un acceso seguro. El desarrollo se organizó con Slack y GitHub, con manejo de excepciones mediante `try-catch-finally` y monitoreo de errores con Sentry.

</div>

<details>
<summary>Tabla de contenidos</summary>

- [Tareas de INF331 - Pruebas de Software](#tareas-de-inf331---pruebas-de-software)
- [Grupo de Trabajo](#-grupo-de-trabajo)
- [Preguntas](#preguntas)
- [Instalación](#instalación)
- [¿Cómo usar?](#cómo-usar)
- [¿Cómo contribuir?](#cómo-contribuir)
- [Licencia](#licencia)

</details>

## 💼 Grupo de trabajo
- Valentina Castillo  - ROL: 202021006-3
- Javier Hormaechea - ROL: 202003017-0

## Preguntas

### 1. ¿Cómo especificarías mejor el requerimiento? (Validación)

### 2. ¿Cómo asegurarías que el programa cumpla el requerimiento? (Verificación)

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
blabla

## ¿Cómo usar?
blabla

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
 Por favor, revise [este link](LICENSE.md).
