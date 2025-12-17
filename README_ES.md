# Secure RAG from Scratch – Versión 2 (Privado)

Este repositorio contiene la **evolución v2** del proyecto Secure RAG from Scratch.

La versión 2 tiene como objetivo transformar el baseline local de la v1 en una
**arquitectura modular, orientada a seguridad y con mentalidad productiva**,
manteniéndose local-first pero preparada para entornos cloud y empresariales.

Este repositorio es actualmente **privado** y se encuentra en desarrollo activo.

---

## Objetivos de la Versión 2

Los objetivos principales de la v2 son:

- Sustituir componentes “toy” por **infraestructura real**
- Introducir **límites arquitectónicos claros**
- Reforzar los controles de seguridad en todo el pipeline RAG
- Añadir **testing automatizado**, incluyendo pruebas de seguridad
- Preparar el sistema para futuras arquitecturas cloud y enterprise

---

## Diferencias Clave respecto a la Versión 1

| Área | v1 | v2 |
|----|----|----|
| Vector Store | En memoria | Qdrant (Docker) |
| Arquitectura | Monolítica | Modular |
| Seguridad | Entrada / Salida | Entrada, Recuperación, Salida, Políticas |
| Testing | Manual | Automatizado + tests de seguridad |
| Enfoque | Baseline de aprendizaje | Fundación productiva |

---

## Visión General de la Arquitectura (v2)

Secure RAG v2 se compone de las siguientes capas:

- **Capa de API** (FastAPI)
- **Core RAG** (ingesta, recuperación, construcción de prompts)
- **Abstracción de Vector Store**
- **Capa de Seguridad**
- **Auditoría y Observabilidad**
- **Framework de Testing**

Los controles de seguridad se implementan **fuera del LLM** y se aplican
en múltiples puntos del pipeline.

---

## Base de Datos Vectorial: Qdrant

La versión 2 introduce **Qdrant** como base de datos vectorial principal.

Características:

- Ejecución local mediante Docker
- Motor de búsqueda vectorial real
- Soporte de filtrado por metadata
- Compatible con despliegues cloud

El uso de una interfaz de vector store permite cambiar de implementación
sin afectar al core del sistema RAG.

---

## Modelo de Seguridad

La seguridad se trata como un **elemento de primer nivel**:

- Seguridad de entrada (detección de prompt injection)
- Seguridad en recuperación (control de fuentes y metadata)
- Seguridad de salida (detección de PII y datos sensibles)
- Auditoría estructurada con correlation IDs

---

## Estrategia de Testing

La versión 2 introduce testing automatizado:

- Tests unitarios de componentes clave
- Tests de integración (API y vector store)
- Suite de tests de seguridad simulando escenarios de ataque reales

El objetivo no es evaluar la calidad del modelo,
sino validar la **corrección de los controles de seguridad**.

---

## Estado del Desarrollo

La versión 2 se encuentra en desarrollo activo.

Próximos pasos previstos:

- Tests de integración con Qdrant
- Expansión del motor de políticas
- Rate limiting y control de abuso
- Threat modeling basado en OWASP LLM Top 10
- Patrones de despliegue cloud-ready
