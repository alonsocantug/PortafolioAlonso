---
page_title: Recordatorios por WhatsApp para una clínica — Caso de estudio
description: Sistema de recordatorios y solicitud de citas por WhatsApp para una clínica dermatológica, con revisión del contenido conversacional y de accesibilidad. Propuesta de piloto, probado con datos de ejemplo.
title: Recordatorios y solicitud de citas por WhatsApp para una clínica
summary: Un sistema que cada tarde avisa por WhatsApp a quien tiene cita al día siguiente y deja que el paciente confirme, reprograme o pida cita con botones. Lo propuse a una clínica dermatológica, lo construí con Make, Google Sheets y la plataforma oficial de WhatsApp, y revisé cada mensaje como lo vive el paciente.
tags: ["Propuesta a cliente real", "Individual", "Piloto sin arrancar"]
facts:
  - ["Rol", "Diseño de la conversación, construcción de la automatización, documentación y propuesta comercial"]
  - ["Herramientas", "WhatsApp Business Platform (Meta), Make, Google Sheets"]
  - ["Alcance", "Recordatorio diario con botones, menú, solicitud de cita, reprogramación, seguimiento, baja y aviso a recepción"]
  - ["Fuera de alcance", "Agenda con disponibilidad en tiempo real, asistente con IA e integración con software médico (se cotizan aparte)"]
note_label: Nota sobre el estado.
note: Lo construí y probé con el número de prueba de Meta, una agenda de ejemplo y mi propio teléfono. Todavía no hay pacientes reales ni métricas, así que no afirmo ninguna reducción de inasistencias. Los nombres, teléfonos y citas de las imágenes son ficticios. No publico el nombre de la clínica ni precios.
hero: wa-card
hero_alt: "Dos teléfonos con mensajes de ejemplo: un recordatorio con botones Confirmar y Reprogramar, y un menú con tres botones"
---

## Problema y objetivo

**El problema.** Cuando un paciente olvida su cita, la clínica pierde ese espacio y su ingreso. Además, recepción dedica tiempo cada día a llamar o escribir uno por uno para confirmar. Con 20 citas al día y 2 minutos por confirmación, son unos 40 minutos diarios, cerca de 3 horas a la semana (es un cálculo de ejemplo de la propuesta, no una medición de la clínica).

**El objetivo.** Que la agenda avise sola, que el paciente responda con un toque y que recepción se dedique a quien está en la clínica. El sistema no sustituye a recepción: le quita lo repetitivo y deja siempre una salida a una persona.

## Cómo funciona

Hay dos flujos. El primero corre una vez al día; el segundo responde cuando el paciente escribe.

![Diagrama con dos flujos: recordatorios diarios desde la agenda y respuestas a los mensajes del paciente](img:wa-flow)

**Recordatorios.** Cada tarde el sistema busca en la agenda las citas del día siguiente que no tengan recordatorio ni baja, envía una plantilla aprobada por Meta con nombre, fecha, hora y doctor, y anota en la agenda que ya avisó para no repetir el mensaje.

**Respuestas.** El paciente toca Confirmar o Reprogramar, o escribe a la clínica y recibe un menú con tres botones: solicitar cita, horarios y lugar, y recepción. Para solicitar cita elige servicio, día y turno con listas y botones. La solicitud queda en la hoja y recepción la confirma, porque el sistema todavía no aparta horarios por sí solo.

Así se ve en el chat del paciente, con datos ficticios. El texto de la baja es ilustrativo:

![Cuatro teléfonos con mensajes de ejemplo: recordatorio y confirmación, reprogramar con lista de fechas, solicitar cita y baja](img:wa-chats)

**Privacidad.** El mensaje solo lleva nombre, fecha, hora y doctor, nunca el motivo de la consulta, y la hoja que lee la automatización no tiene columnas de diagnóstico. Solo se escribe a quien dio su consentimiento, y quien escribe BAJA deja de recibir mensajes.

## Iteración del contenido conversacional

Con el sistema funcionando, revisé cada mensaje como lo vive el paciente, de principio a fin. Encontré cuatro problemas que podían causar errores reales y varios de tono y claridad. Los corregí y los probé con mensajes reales a mi propio teléfono.

| Mensaje | Antes | Después | Por qué |
|---|---|---|---|
| Reprogramar desde el recordatorio | "Cancelamos tu cita de mañana" | "Sin problema, Sofía. Ya avisamos a recepción que necesitas cambiar tu cita. ¿Qué día te queda mejor?", con la lista de fechas | El texto decía "cancelamos" cuando el paciente pidió reprogramar, y la agenda decía otra cosa |
| Seguimiento con historial | "Tu última cita fue el 16/10/2026", aunque esa cita era al día siguiente | Toma la última cita pasada y la muestra con día | Un dato incorrecto en un mensaje de salud resta confianza en todo el sistema |
| Seguimiento sin historial | No llegaba ningún mensaje | "No encontramos citas anteriores con este número. ¿Es tu primera vez con nosotros?", con dos botones | Un silencio se percibe como falla. Cada camino debe terminar en una respuesta y una salida |
| Lista de fechas | 16/10/2026, 17/10/2026… | Viernes 16 de oct., sin domingos ni días sin consulta | Las personas piensan en "el viernes", y ofrecer días sin consulta genera solicitudes imposibles |
| Menú principal | "Escribe 1 para agendar o 2 para hablar con recepción" | Tres botones: Solicitar cita, Horarios y lugar, Recepción | Era el único paso donde había que escribir. Se agregó la pregunta más frecuente |
| Hablar con recepción | "En un momento te atiende alguien" | "Te contactarán por este medio en horario de atención" | "En un momento" es una promesa que no se cumple de noche |
| Nombre del paciente | El del perfil de WhatsApp | El de la agenda | Un familiar puede agendar con su número, y el nombre del perfil puede ser un apodo |

## Revisión de accesibilidad

En una segunda ronda revisé cómo se escucha cada mensaje con un lector de pantalla, cómo lo lee una persona mayor y qué tan claro es sin depender de los emojis.

- **Fechas.** En las listas, "Viernes 16 de oct." en lugar de "Vie 16/10", que el lector leía como "dieciséis diagonal diez". En los mensajes, el mes completo, porque ahí no hay límite de caracteres.
- **Horas.** Formato de 12 horas ("4:00 p.m."), que es como la mayoría de las personas en México dice la hora, sobre todo las mayores.
- **Confirmaciones.** Con etiquetas y punto final (Día, Hora, Doctor) para que el lector haga pausas.
- **Emojis.** Cada uno va junto a una palabra que dice lo mismo. Quité las flechas de emoji de las fechas de Seguimiento, que el lector anunciaba como "botón retroceder".
- **Botones de horario.** Solo "Mañana" y "Tarde", con los rangos escritos en el mensaje.
- **Solicitud de cita.** El mensaje aclara que es una solicitud y todavía no una cita confirmada, para que nadie llegue a una cita que no existe.

## Decisiones de diseño

- **Listas y botones en lugar de formularios.** El formulario nativo de WhatsApp (Flows) fue bloqueado por Meta en la cuenta de prueba. Listas y botones dan una experiencia parecida y funcionan en cualquier cuenta.
- **Cada respuesta lleva su contexto.** El identificador de cada opción guarda lo que el paciente ya eligió, así el sistema no necesita recordar la conversación ni volver a preguntar.
- **Pedir el mínimo de datos.** Teléfono y nombre llegan solos con el mensaje; el resto lo completa recepción al confirmar.
- **Siempre una salida a una persona.** Todos los caminos ofrecen hablar con recepción.
- **Tuteo.** Evalué cambiar a "usted" para pacientes mayores y mantuve el tuteo como decisión de marca. Cambiarlo implica una plantilla nueva aprobada por Meta, así que queda por confirmar con la clínica.

## Propuesta y documentación

Preparé la propuesta de piloto para la clínica y tres documentos para poder repetir el trabajo con otro cliente:

1. **Requisitos del cliente.** Lista de lo que la clínica debe tener antes de empezar: responsable, cuentas, número, datos del negocio, pago, consentimiento de pacientes y agenda.
2. **Lista de implementación.** Pasos en orden, en 15 fases, con una tabla de errores conocidos y su solución, que armé con los fallos que me encontré al construirlo.
3. **Cómo explicárselo al cliente.** Guía sin tecnicismos: qué gana, qué pone y cuánto cuesta cada parte, y qué no conviene prometer, por ejemplo un porcentaje de reducción de ausencias o una fecha de arranque antes de tener aprobaciones de Meta.

La propuesta separa lo que incluye de lo que se cotiza aparte, y propone un piloto de tres meses en el que la clínica comparte métricas a los 30 y 90 días. Como el piloto todavía no arranca, esas métricas no existen.

## Qué no sé todavía

- **Si funciona con pacientes reales.** Todo se probó con el número de prueba de Meta. Falta dar de alta un número real y verificar el negocio, y la tarifa por mensaje vigente para México.
- **Cuánto reduce las inasistencias.** Por eso el piloto mide primero las inasistencias del último mes y las compara a los 30 y 90 días.
- **Qué prefiere la clínica.** Tuteo o usted, y el horario, teléfono y dirección reales, que hoy son de ejemplo.
- **Qué pasa con una fecha real de Seguimiento que cae en domingo.** La regla está hecha y falta probarla.
