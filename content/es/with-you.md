---
page_title: With You — Caso de estudio
description: App móvil de respiración guiada de 3 a 5 minutos para bajar la ansiedad. Proyecto de portafolio individual, de la investigación al sistema de diseño.
title: With You
summary: Una app móvil que lleva a una respiración guiada de 3 a 5 minutos para bajar la ansiedad. La diseñé de principio a fin, desde la investigación hasta el sistema de diseño.
tags: ["Proyecto de portafolio", "Individual", "App móvil"]
facts:
  - ["Rol", "UX/UI y Product Design de principio a fin: investigación, síntesis, flujos, wireframes, UI, prototipo, pruebas y sistema de diseño"]
  - ["Duración", "3 semanas"]
  - ["Herramientas", "Figma, FigJam, Maze"]
  - ["Investigación", "Revisión bibliográfica y 2 entrevistas simuladas; 2 personas ficticias"]
  - ["Pruebas", "3 usuarios simulados en Maze, 3 tareas"]
  - ["Sistema de diseño", "UI Kit de 44 componentes y Design System v1.1 con 48 variables, aplicados a las pantallas"]
note_label: Nota sobre el método.
note: Es un ejercicio de práctica sin cliente real. Las entrevistas, las personas (Sofía y Diego) y las pruebas de usabilidad en Maze se simularon para recorrer el proceso completo, por lo que sus resultados ilustran el método y no tienen valor estadístico. Las fotografías de las personas son ilustrativas. La interfaz, el prototipo y el sistema de diseño son trabajo real y se pueden revisar en Figma.
hero: wy-case
hero_alt: "Cinco pantallas de With You en teléfonos: bienvenida, inicio, respiración guiada, registro de ánimo y progreso"
embed: true
prototype: "https://www.figma.com/proto/ueVtfaqiM6nx04cCVxwbIT/With-you-app_Alonso-Cant%C3%BA?node-id=8735-3732&p=f&t=kgGgzBfNxlV73m9J-1&scaling=scale-down&content-scaling=fixed&page-id=194%3A839&starting-point-node-id=8735%3A3732"
---

## Problema y objetivo

Según la OMS, en 2023 había 470 millones de personas con un trastorno de ansiedad y 322 millones con depresión; casi 1 de cada 7 personas (1,200 millones) vivía con algún trastorno mental ([OMS, ficha sobre trastornos mentales, actualizada el 11 de septiembre de 2026](https://www.who.int/news-room/fact-sheets/detail/mental-disorders)).

En las dos entrevistas simuladas, las apps que ya habían probado fallaban por lo mismo: tenían demasiadas cosas, eran largas o estaban pensadas para meditar y no para calmarse rápido. Una persona también dudaba de si respiraba bien.

**Objetivo.** Diseñar una app móvil que ayude a reducir la ansiedad y el estrés con respiraciones guiadas, simples, rápidas y efectivas.

**Solución propuesta.** Respiraciones guiadas de 3 a 5 minutos, registro del estado emocional, seguimiento del progreso y una interfaz simple y amable.

## Investigación

*Entrevistas y personas de ejercicio, ver la nota sobre el método al inicio.*

**Revisión bibliográfica.** Revisé fuentes sobre ansiedad y respiración: la [OMS](https://www.who.int/news-room/fact-sheets/detail/mental-disorders) para el contexto, y tres estudios ([Balban et al., 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9873947), *Cell Reports Medicine*; [Luo et al., 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11897343), *Scientific Reports*; [Iwabe et al., 2025](https://www.frontiersin.org/articles/10.3389/fnhum.2025.1605862), *Frontiers in Human Neuroscience*). Tres ideas guiaron el diseño:

- La respiración lenta reduce la ansiedad: con ciclos de 6 segundos bajaron la ansiedad autorreportada y la activación (Luo et al., 2025), y con inhalación de 4 s y exhalación de 6 s bajó la ansiedad de estado (Iwabe et al., 2025).
- Sesiones breves pueden bastar: en un estudio con 108 personas, 5 minutos al día durante 28 días mejoraron el ánimo más que la meditación, y la práctica de respiración fue de unos 20 de los 28 días (Balban et al., 2023). Ese estudio no compara duraciones, así que los 3 a 5 minutos de With You son una decisión de diseño apoyada en las entrevistas.
- Esa práctica diaria mejoró el ánimo y redujo la ansiedad; en ese mismo estudio no cambió el sueño, así que la app no promete mejorar el sueño con la respiración (Balban et al., 2023).

**Entrevistas simuladas.** Dos jóvenes universitarios. Quise saber cómo manejan la ansiedad hoy, qué estrategias usan y qué esperarían de una app de bienestar.

| Tema | Sofía | Diego |
|---|---|---|
| Cuándo aparece | Varios trabajos a la vez o un examen importante | Entregas de la universidad mientras clientes esperan trabajo |
| Qué hace hoy | Música, TikTok; intenta respirar profundo sin saber si lo hace bien | Música o salir; sigue pensando en lo mismo |
| Apps previas | Dejó una porque tenía demasiadas cosas | Algunas eran largas o más de meditar que de calmarse rápido |
| Qué espera | Abrir la app y empezar sin configurar mucho | Que sea sencilla: abrir, respirar y volver a lo que hacía |
| Duración | Unos 5 minutos | Entre 3 y 5 minutos |
| Registro | Ver si mejora con el tiempo | Saber cuánto respiró y comparar la semana |

## Síntesis

**Insight principal.** Las personas necesitan recuperar la calma en pocos minutos sin interrumpir su rutina diaria.

De las dos entrevistas salieron cuatro hallazgos: buscan una forma rápida de calmarse, prefieren apps simples, consideran ideal que las sesiones duren de 3 a 5 minutos y les gusta llevar un registro de cómo se sienten.

**Dos personas ficticias**, construidas a partir de esas entrevistas simuladas:

- **Sofía**, estudiante universitaria. Siente ansiedad antes de exámenes y entregas. Quiere reducir la ansiedad y mejorar su concentración. Frustración: apps complejas y sesiones largas. *“Solo necesito algo que me ayude a calmarme cuando me siento abrumada.”*
- **Diego**, estudiante y diseñador freelance. Vive con exceso de entregas y le cuesta desconectarse al final del día. Quiere dormir mejor y encontrar momentos de calma sin alterar su rutina. *“Cuando me siento abrumado, necesito algo que me ayude a despejar mi mente rápidamente.”*

![Fichas de las personas Sofía y Diego con necesidad principal, objetivos y frustraciones](img:wy-personas-es)

Para cada persona armé un journey map que me mostró dónde se pierde la calma y dónde podría ayudar la app.

![Journey maps de Sofía y Diego: pasos, emoción y punto de dolor en cada etapa](img:wy-journey-es)

**Decisión clave.** Un acceso directo a la respiración guiada desde la pantalla principal, pensado para iniciar el ejercicio en menos de 4 toques. Es una meta de diseño, no una medición: con ella busco reducir la fricción y aumentar la probabilidad de que la persona termine la sesión.

| Hallazgo | Decisión de diseño |
|---|---|
| Buscan calmarse rápido | Botón “Respira ahora” en la pantalla principal |
| Prefieren apps simples | Cuatro pestañas (Inicio, Ejercicios, Mi progreso, Perfil) y una acción principal por pantalla |
| Sesiones de 3 a 5 minutos | Ejercicios cortos por categoría |
| Les gusta el registro | Registro del estado de ánimo y pantalla de progreso |

## Diseño

**Arquitectura de información.** La app tiene cuatro secciones: Inicio (“Respira ahora”, estado de ánimo del día, recomendaciones), Ejercicios (Ansiedad, Estrés, Concentración, Sueño y relajación), Seguimiento emocional (registrar el estado de ánimo, historial, estadísticas) y Perfil (datos, objetivos, configuración). En el mapa también aparece Ayuda, con consejos de bienestar y recursos de apoyo, que dejé fuera del prototipo como alcance futuro.

![Arquitectura de información de With You: Inicio, Ejercicios, Seguimiento emocional, Perfil y Ayuda con sus subsecciones](img:wy-ia-es)

**Flujos de usuario**, uno por persona:

1. **Sofía, ansiedad antes de un examen.** Abre With You, decide iniciar una sesión, elige alivio de ansiedad, completa la respiración guiada y registra su estado de ánimo. Si se siente mejor, vuelve a estudiar; si no, la app sugiere otra sesión o explorar otras herramientas.
2. **Diego, estrés tras un día agitado.** Abre With You, entra a Ejercicios, elige alivio de estrés, completa la sesión, registra su ánimo y revisa su progreso.

![Flujo de usuario de Sofía, de abrir la app a registrar su ánimo y decidir si repite la sesión](img:wy-flow-sofia-es)

![Flujo de usuario de Diego, de abrir la app a revisar su progreso](img:wy-flow-diego-es)

**Wireframes.** Cuatro pantallas de baja fidelidad me sirvieron para decidir la estructura antes del color: el flujo de navegación, el acceso rápido al ejercicio, la jerarquía de la información, el registro emocional, el temporizador visible en la sesión y el botón “Respira ahora” como acción principal.

![Cuatro wireframes de baja fidelidad: inicio, progreso y dos pasos de la respiración guiada](img:wy-wireframes)

**Alta fidelidad.** Cuatro pantallas móviles en español: Inicio (saludo, selector de estado de ánimo, ejercicios recomendados y “Respira ahora”), Ejercicios (cuatro categorías con duración), Mi progreso (sesiones completadas, días de racha, estado emocional promedio y sesiones de la semana) y Perfil.

![Pantallas de alta fidelidad: Inicio, Ejercicios y Mi progreso](img:wy-hifi)

**Prototipo.** [Ábrelo en Figma](https://www.figma.com/proto/ueVtfaqiM6nx04cCVxwbIT/With-you-app_Alonso-Cant%C3%BA?node-id=8735-3732&p=f&t=kgGgzBfNxlV73m9J-1&scaling=scale-down&content-scaling=fixed&page-id=194%3A839&starting-point-node-id=8735%3A3732) y recorre el flujo de respiración guiada.

## Prueba de usabilidad simulada

*Prueba de ejercicio con 3 usuarios ficticios en Maze, ver la nota sobre el método al inicio.*

| Tarea | Resultado |
|---|---|
| 1. Iniciar una sesión de respiración guiada | Los 3 encontraron el botón principal en unos 8 segundos |
| 2. Registrar su estado emocional al terminar | Los 3 completaron el registro sin ayuda; una persona sugirió marcar cuál se eligió |
| 3. Consultar el progreso de sus sesiones | Dos tardaron unos segundos en encontrar la sección y los 3 confundieron “Historial” |

**Hallazgos.** La navegación principal es intuitiva y “Respira ahora” destaca. El registro emocional es sencillo, aunque no queda claro cuál ícono se eligió. “Historial” confunde y las personas quieren ver su progreso con claridad.

**Cambios.**

1. “Mi historial” pasó a llamarse **“Mi progreso”**.
2. El botón **“Respira ahora”** se hizo más llamativo y ganó un fondo que resalta la emoción elegida.

![Pantalla de inicio antes (izquierda) y después (derecha) de la prueba: el botón Respira ahora gana fondo y el ánimo elegido se resalta](img:wy-cambios)

El hallazgo sobre el ícono elegido quedó sin resolver en esta versión; lo retomo en la auditoría del sistema de diseño.

## Design System

**v1.0, el UI Kit del proyecto.** Poppins para títulos e Inter para cuerpo, siete colores semánticos (Primary, Ansiedad, Estrés, Sueño, Concentración, Calma y Alerta), escala de radios, dos sombras y componentes como tarjeta de ejercicio, badges, barras de progreso, tab bar y avatar. Los colores estaban pintados a mano, sin variables de Figma.

![UI Kit v1.0: colores de acento Primary, Ansiedad, Estrés, Sueño y Concentración con sus códigos hexadecimales](img:wy-uikit)

**v1.1, auditoría posterior (septiembre de 2026).** Medí el contraste con WCAG 2.2 AA y encontré fallas que no vi al diseñar. Reconstruí el kit en [un archivo aparte de Figma](https://www.figma.com/design/GHPCtHubSztEL1khHyVq3t) con cuatro colecciones de variables, nueve estilos de texto, dos sombras y 11 componentes con estados (foco, presionado, deshabilitado). No se probó con usuarios.

**Aplicado a las pantallas (octubre de 2026).** Al llevar las pantallas a Hi-Fi v2 junté todo en el archivo del proyecto. El UI Kit creció a 44 componentes (70 contando sus variantes) en seis secciones, y la v1.1 pasó a una página "Design System" con 48 variables en cuatro colecciones. Corregí los colores en los estilos del UI Kit y en las variables del Design System con los mismos valores, así que las pantallas, el kit y el sistema coinciden. Estos son los cambios que medí sobre las pantallas:

| Elemento | Antes | Ahora |
|---|---|---|
| Botones, enlaces y pestaña activa | Blanco sobre #0EA5E9, 2.77:1 | #0369A1, 5.93:1 |
| Texto secundario | #717182, 4.51 a 4.79:1 | #5F6472, 5.56 a 5.91:1 |
| Botón de colgar | Blanco sobre #EF4444, 3.76:1 | #DC2626, 4.83:1 |
| Números del calendario sobre verde y naranja | Blanco, 2.54 y 2.80:1 | #111111, 7.44 y 6.74:1 |
| Cifras de progreso (12 y 5) | #10B981 y #F97316 sobre blanco, 2.54 y 2.80:1 | #047857 y #C2410C, 5.48 y 5.18:1 |

![Design System del proyecto: variables de color de texto, superficie, borde, acción, categorías, calma y pestañas, con sus códigos corregidos](img:wy-ds-color)

Otras correcciones de la v1.1 viven en los componentes del Design System y todavía no están en las pantallas: badges con colores de texto seguros (4.76 a 6.34:1), botones pequeños de 44 px, marca ✓ en el ánimo seleccionado y estados de foco, presionado y deshabilitado. La versión anterior de "Respira ahora" tenía 1.82 a 2.91:1 con texto blanco sobre degradado; en Hi-Fi v2 la sustituí por un hero con foto. Medí el texto blanco sobre la foto: el título y el subtítulo dan 7.15:1 o más en el peor punto, y a la etiqueta "Recomendado" le oscurecí el fondo porque bajaba a 3.52:1 en los reflejos claros y ahora da 11.12:1 como mínimo.

**UI Kit ampliado en el archivo del proyecto.** Tiene 15 estilos de color, 21 estilos de texto, dos sombras y cuatro radios (10, 14, 18 y 20 px). Sus seis secciones son navegación y encabezados, botones y formularios, tarjetas, listas y calendario, estado de ánimo, e iconos y respiración. Los componentes están vinculados a las pantallas del prototipo, como la tarjeta de ejercicio con miniatura, el hero de respiración con foto, el selector de ánimo y la fila de lista.

![Fundamentos del UI Kit: 15 estilos de color, estilos de texto en Poppins e Inter, dos sombras y cuatro radios](img:wy-kit-fund)

![Componentes de tarjetas: ejercicio, recomendados, ánimo promedio, progreso, objetivo, gráfica semanal, contenedor, miniatura y hero de respiración](img:wy-kit-cards)

![Componentes de estado de ánimo: emojis, mood tiles con estado seleccionado y selectores](img:wy-kit-mood)

![Componentes de botones y formularios: botón principal con estados, secundario y de peligro, interruptor, campo de texto y notas](img:wy-kit-forms)

![Componentes de navegación: barra superior, logo, pestaña, tab bar y menú de perfil](img:wy-kit-nav)

![Filas de lista y días de calendario con estado de ánimo, más ícono de cerebro, botón de pausa y play, avatar y emojis mini](img:wy-kit-lists)

## Aprendizajes y qué haría distinto

Diseñar With You me dejó cuatro aprendizajes y una lista clara de lo que haría distinto.

- **Diseñé bien el proceso, pero me faltó hablar con personas reales.** Practiqué cada etapa con entrevistas y pruebas simuladas y eso me enseñó a estructurar preguntas, sintetizar y convertir un hallazgo en un cambio. La siguiente vez haría una ronda real con unas 5 personas que vivan ansiedad, con guión, consentimiento y una plantilla de análisis, y compararía qué cambia frente a lo que yo había supuesto.
- **Auditar mi propio trabajo encontró lo que yo no vi.** "Respira ahora" tenía un contraste de 1.82 a 2.91:1 con texto blanco, muy por debajo del 4.5:1 de WCAG AA, aunque yo había puesto "accesible" como principio. La v1.1 lo corrigió a 4.93–7.88:1 y, ya en las pantallas finales, el azul principal pasó de 2.77 a 5.93:1. Ahora mido el contraste en el momento en que elijo un color, no al final.
- **El color y el emoji no bastan.** El selector de ánimo dependía de ellos; en el Design System agregué una marca ✓ al estado elegido y objetivos táctiles de 44 px, porque una persona en un momento de ansiedad necesita saber sin dudar qué eligió.
- **Un sistema de diseño sin variables no escala.** La v1.0 tenía los colores pintados a mano. El Design System del proyecto tiene 48 variables en 4 colecciones, 21 estilos de texto compartidos con el kit y 11 secciones de componentes con estados, y cada decisión de contraste queda documentada.
- **Lo que aún me falta.** Probar los colores corregidos con usuarios reales, llevar a las pantallas la marca ✓ y los objetivos de 44 px, reemplazar los iconos provisionales.
