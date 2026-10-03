---
page_title: Firmia — Caso de estudio
description: Concepto de SaaS B2B para carpintería y obra con presupuestos interactivos que el cliente revisa y firma desde cualquier dispositivo. Landing, vista previa del presupuesto y flujo móvil.
title: Firmia
summary: Un concepto de SaaS B2B que reemplaza los presupuestos en PDF por un presupuesto interactivo que el cliente revisa y firma de conformidad desde cualquier dispositivo. Diseñé la landing, una vista previa interactiva del presupuesto y un flujo móvil de 7 pantallas.
tags: ["Proyecto de portafolio", "Concepto", "Individual"]
facts:
  - ["Rol", "UX/UI: estructura de la página, contenido, interfaz, componentes y revisión de contraste"]
  - ["Herramientas", "Figma"]
  - ["Alcance", "Landing de escritorio (1440 px) con 5 secciones y un kit de 7 componentes con estado hover. Como extensión, un flujo móvil de 7 pantallas para iPhone 16 con prototipo"]
  - ["Fuera de alcance", "Investigación con usuarios y pruebas de usabilidad"]
note_label: Nota sobre el método.
note: Es un ejercicio de diseño de interfaz sobre un concepto, sin cliente real ni investigación con usuarios. Las cifras de la landing (90%, 0 y 24/7), el folio, los montos y los datos de contacto son de ejemplo y no son resultados medidos.
hero: fi-case
hero_alt: "Cuatro pantallas móviles de Firmia: mis presupuestos, resumen, firma de conformidad y confirmación"
prototype: "https://www.figma.com/proto/QuFyeK4A08L6gaJjd4IzQT/Firmia-UX-UI?node-id=31-247&p=f&scaling=scale-down&content-scaling=fixed&page-id=29%3A212&starting-point-node-id=31%3A247&show-proto-sidebar=1"
---

## Problema y objetivo

**Hipótesis del concepto.** Quien cotiza obra o carpintería suele mandar un PDF estático que el cliente tiene que abrir, revisar y responder por otro canal. El problema que plantea Firmia es poder revisar, ajustar y aprobar un presupuesto desde cualquier lugar y desde cualquier dispositivo, sin depender de archivos sueltos. Es una hipótesis de diseño: no la validé con entrevistas.

**Objetivo.** Diseñar una página que explique el producto en segundos y una vista previa de presupuesto clara, donde el cliente vea materiales, mano de obra, tiempos, anticipo e IVA, y pueda aceptar y firmar, pedir ajustes o descargar una copia.

**Alcance del producto.** El concepto contempla compartir el presupuesto por mensajería como WhatsApp. Esa parte no está diseñada en este archivo.

## Diseño

La landing sigue un orden pensado para que alguien del oficio entienda el producto sin leer de más: promesa, beneficios, evidencia y proceso.

**1. Hero.** Un titular con la promesa ("Presupuestos de obra y carpintería aprobados al instante"), una frase que explica el cambio frente al PDF y dos acciones con jerarquía clara: "Ver un presupuesto en vivo" como acción principal y "Cómo funciona" como secundaria. La tarjeta inclinada de la derecha muestra un presupuesto real del mismo folio que aparece más abajo.

![Hero de la landing de Firmia con titular, dos acciones y tarjeta de presupuesto](img:fi-hero)

**2. Beneficios.** Seis tarjetas con icono, título corto y una frase: materiales al detalle, firma de conformidad inmediata, tiempos de entrega claros, historial de proyectos, accesibilidad y uso en obra y taller. Las tarjetas se leen en cualquier orden.

![Sección de beneficios con seis tarjetas](img:fi-features)

**3. Cómo funciona.** Tres pasos numerados que siguen el recorrido real: levantamiento y presupuesto, revisión por cliente y arquitecto, y firma de conformidad.

![Sección Cómo funciona con tres pasos numerados](img:fi-how)

**Decisiones de estilo.** Un hero oscuro con acentos ámbar y marrón cálido que remiten a la madera, y secciones claras para el contenido denso. Los botones principales miden 56 px de alto para que sean fáciles de tocar y de ver.

## Vista previa interactiva del presupuesto

Es la pieza central del proyecto: una tarjeta que reemplaza al PDF y que el cliente puede revisar antes de decidir.

![Vista previa del presupuesto Fabricación e Instalación de Cocina Integral en Encino con desglose, anticipo, total y tres acciones](img:fi-preview)

**Qué ve el cliente, en orden.**

1. El proyecto, el folio, quien lo emite y el estado ("Pendiente de aprobación").
2. Quién es el cliente, dónde es la obra y quién es el arquitecto responsable.
3. El desglose en dos bloques: materiales y herrajes, y mano de obra y taller, con cantidad, precio unitario y subtotal.
4. Los tiempos de entrega (12 días hábiles de fabricación y 3 de instalación) y las condiciones de anticipo (60% para iniciar y 40% contra entrega).
5. El resumen: subtotal de materiales ($58,280.00), subtotal de mano de obra ($16,320.00), subtotal general ($74,600.00), IVA del 16% ($11,936.00) y total del proyecto ($86,536.00).
6. Tres acciones: aceptar y firmar conformidad, solicitar ajustes o descargar una copia.

**Decisiones de diseño.**

- Los números se alinean a la derecha y los subtotales van en negritas, para comparar de un vistazo.
- El total está separado y es el texto más grande del resumen, porque es lo primero que busca quien decide.
- La acción principal es "Aceptar y firmar" en color sólido; "Solicitar ajustes" tiene borde y "Descargar copia" es la menos prominente, para que una duda no obligue a aceptar.
- Una nota debajo explica qué queda registrado al aceptar: la firma, la fecha y las condiciones de anticipo.

**Cuentas verificadas.** Revisé todas las líneas: materiales $58,280 + mano de obra $16,320 = $74,600; más IVA de $11,936 da $86,536. El folio, los montos y los nombres son de ejemplo.

## Extensión móvil: flujo del cliente

Después de la landing diseñé, como ejercicio, las pantallas móviles del recorrido del cliente, que el caso original había dejado fuera. Es una extensión: no la validé con usuarios ni con una prueba de usabilidad.

**Qué diseñé.** Siete pantallas para iPhone 16 (393 × 852 px): inicio con "Mis presupuestos", acceso desde el enlace, resumen, desglose, solicitar ajustes, firma de conformidad y confirmación. El prototipo en Figma tiene dos entradas: el enlace directo que recibe el cliente y el inicio de la app.

[Ver el prototipo navegable en Figma](https://www.figma.com/proto/QuFyeK4A08L6gaJjd4IzQT/Firmia-UX-UI?node-id=31-247&p=f&scaling=scale-down&content-scaling=fixed&page-id=29%3A212&starting-point-node-id=31%3A247&show-proto-sidebar=1)

![Pantallas móviles de Firmia: inicio, acceso, resumen y desglose](img:fi-movil-a)

![Pantallas móviles de Firmia: solicitar ajustes, firma y confirmación](img:fi-movil-b)

**Decisiones de diseño.**

- Un camino lineal en lugar de un menú: el cliente llega con un enlace, revisa y firma. El menú inferior solo aparece en el inicio; dentro del flujo no hay, para que nada compita con la acción principal.
- Una acción principal por pantalla (botón sólido) y una secundaria con borde. Pedir ajustes está siempre a un toque, para que una duda no obligue a firmar.
- Flecha de regresar y un indicador "Paso 1 de 3" en resumen, desglose y firma, porque lo que se firma es un compromiso con dinero.
- En la firma, una casilla que repite el folio y el total, para que quien firma vea exactamente qué acepta.
- Áreas táctiles de al menos 44 px y márgenes de seguridad del iPhone 16 (59 px arriba y 34 px abajo).
- A diferencia del kit de la landing, el sistema móvil tiene variables y estilos de texto con nombre propio, y componentes reutilizables: botones, estados, filas de concepto, barra superior, progreso y menú inferior.

**Accesibilidad.** Medí el contraste de los pares principales: texto secundario #6B645F sobre #FAFAF9, 5.56:1; blanco sobre el botón #92400E, 7.09:1; etiqueta "Pendiente", 8.15:1; "Firmado", 6.49:1; anillo de foco, 6.79:1. Con #6B645F queda resuelto el gris que fallaba en la landing. Diseñé estados de foco en las opciones y la casilla. No probé con lector de pantalla ni con el orden de foco real, y solo diseñé un tamaño de pantalla.

**Datos de ejemplo.** Los conceptos del desglose, el anticipo del 60% ($51,921.60 sobre un total de $86,536) y el presupuesto "Closet vestidor" son de ejemplo, igual que en la landing.

## Accesibilidad

Medí el contraste de los pares de color principales contra WCAG 2.1 AA (mínimo 4.5:1 para texto normal).

| Par | Razón | Resultado |
|---|---|---|
| Texto oscuro sobre el botón ámbar del hero (#1C1917 sobre #D97706) | 5.49:1 | Cumple |
| Blanco sobre "Solicitar demo" (#FFFFFF sobre #92400E) | 7.09:1 | Cumple |
| Estadísticas amarillas sobre el hero (#FBBF24 sobre #1C1917) | 10.48:1 | Cumple |
| Gris claro sobre el hero (#A8A29E sobre #1C1917) | 6.93:1 | Cumple |
| Gris secundario sobre blanco (#78716C sobre #FFFFFF) | 4.80:1 | Cumple |
| Gris secundario sobre #FAFAF9 | 4.59:1 | Cumple |
| Gris secundario sobre #F5F5F4 | 4.40:1 | No cumple en texto pequeño |
| Etiqueta "Pendiente" (#78350F sobre #FEF3C7) | 8.15:1 | Cumple |

**Lo que encontré.** El gris secundario (#78716C) cae a 4.40:1 sobre el fondo #F5F5F4 de la sección de la vista previa. La corrección es oscurecerlo a #6B645F, que da 5.33:1 sobre ese fondo y 5.81:1 sobre blanco. En la extensión móvil ya uso #6B645F; en la landing queda como mejora pendiente en el archivo.

**Lo que no medí.** No revisé todos los textos; hay textos de 11 px en los detalles y el pie que conviene revisar aparte. En la landing tampoco diseñé estados de foco ni la navegación por teclado, aunque la menciona como beneficio; los estados de foco sí los diseñé después en la extensión móvil.

## Aprendizajes y qué haría distinto

- **Revisar mis propios números.** Al auditar el proyecto encontré que el hero mostraba un total distinto al de la vista previa para el mismo folio, y que la suma del hero no cuadraba. Lo corregí para que ambas tarjetas muestren $86,536.00. Aprendí que en un producto de dinero la consistencia de las cifras es parte de la confianza.
- **Prometer solo lo que diseñé.** La landing dice que es responsiva y accesible por teclado, pero en el diseño original solo existía la versión de escritorio y no había estados de foco. Después diseñé el flujo móvil y los estados de foco, pero la landing sigue sin versión móvil. Lo que haría distinto: diseñar primero la versión móvil, porque el producto promete uso en obra, y los estados de foco, y solo después escribir la promesa.
- **Hablar con quien cotiza.** Planteé el problema como hipótesis. La siguiente vez entrevistaría a carpinteros y contratistas para saber cómo cotizan y cobran hoy, y qué les hace falta para firmar desde obra, antes de dibujar la primera pantalla.
- **Cifras de ejemplo, etiquetadas.** Las estadísticas del hero (90%, 0 y 24/7) son de ejemplo. En un caso real las reemplazaría por datos medidos o las quitaría.
- **Un sistema más completo.** El kit de la landing tiene siete componentes con estado hover. Le faltan estados de foco, deshabilitado y error, y variables de color con nombres propios en lugar de los automáticos; el sistema móvil ya resuelve parte de eso.
