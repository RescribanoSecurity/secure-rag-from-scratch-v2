# 🔐 Secure RAG v2  
### Retrieval-Augmented Generation con enfoque Security-First

Secure RAG v2 es un **sistema RAG completo con enfoque security-first**, construido como **laboratorio práctico** y **arquitectura de referencia** para diseñar aplicaciones con LLMs defendibles.

Este proyecto evita deliberadamente los “happy-path demos”.  
Su objetivo principal es explorar **cómo deben diseñarse, aplicarse, probarse y exponerse los controles de seguridad** en sistemas RAG modernos.

---

## 📌 Qué es este proyecto (y qué no es)

**Este proyecto es:**
- Una implementación RAG centrada en seguridad
- Construida desde cero con decisiones explícitas
- Testeable, auditable y explicable
- Alineada con OWASP LLM Top 10
- Un laboratorio que documenta errores y aprendizajes

**Este proyecto NO es:**
- Un producto listo para producción
- Un framework o SDK
- Un tutorial genérico de RAG
- Una demo optimizada para benchmarks

---

## 🎯 Objetivos del Proyecto

- Construir un RAG desde cero con mentalidad de producción
- Aplicar **defensa en profundidad** a sistemas con LLMs
- Separar claramente **seguridad de entrada y de salida**
- Hacer visibles y auditables las decisiones de seguridad
- Validar el comportamiento mediante pruebas y evidencia
- Alinear controles con **OWASP LLM Top 10**

---

## 🧱 Arquitectura (v2)

```
Usuario
  ↓
[ UI Streamlit ]
  ↓
[ API FastAPI ]
  ↓
[ Seguridad de Entrada ]
  ↓
[ Recuperación Vectorial (Qdrant) ]
  ↓
[ Generación de Respuesta ]
  ↓
[ Seguridad de Salida v2 ]
  ↓
Usuario
```


**Principios clave:**
- La seguridad es modular y desacoplada
- Ningún control vive solo en la UI
- Todas las decisiones se devuelven estructuradas
- Existe trazabilidad por petición

---

## 🔐 Modelo de Seguridad

### 🛡️ Seguridad de Entrada (v2)

Analiza las **consultas del usuario** antes de cualquier recuperación o generación.

**Capacidades:**
- Detección de prompt injection
- Intentos de override de instrucciones
- Patrones de bypass de seguridad
- Intención de exfiltración de datos

**Acciones:**
- `allow`
- `warn`
- `block`

Las peticiones bloqueadas no continúan el pipeline.

---

### 🔒 Seguridad de Salida (v2)

Analiza el **contenido generado** antes de devolverlo al usuario.

**Amenazas mitigadas:**
- Fugas de PII
- Exposición accidental de secretos
- Respuestas inseguras del modelo

**Acciones:**
- `allow`
- `warn`
- `redact`
- `block`

Cada decisión incluye:
- puntuación de riesgo
- hallazgos
- acción aplicada

---

## 🧪 Escenarios End-to-End

| Escenario | Resultado |
|---------|----------|
| Entrada y salida limpias | ✅ ALLOW |
| Prompt injection | ⛔ BLOCK (Entrada) |
| PII en la salida | ✂️ REDACT |
| Secreto en la salida | ⛔ BLOCK |

---

## 🧾 Auditoría y Trazabilidad

- Cada petición incluye `request_id`
- Decisiones devueltas como metadatos
- Diseñado para futura integración con SIEM
- Lógica determinista y testeable

---

## 🧪 Testing y Validación

- Tests unitarios de seguridad
- Tests de integración del pipeline
- Validación manual vía Streamlit
- Evidencia visual en: docs/screenshots/v2/


---

## 📊 OWASP LLM Top 10 – Estado

| Riesgo | Estado |
|------|-------|
| Prompt Injection | ✅ |
| Data Leakage | ✅ |
| Excessive Agency | ⚠️ Parcial |
| Overreliance | ⚠️ Parcial |
| Otros | 🚧 Planificados |

---

## 🚧 Qué NO está implementado (todavía)

De forma explícita:
- Autenticación e identidad
- Logs persistentes
- Multi-LLM
- IAM cloud
- Policy engines automáticos
- Rate limiting avanzado

---

## 📑 Documentación y Presentaciones

Presentaciones técnicas y capturas disponibles vía GitHub Pages:

- `/docs/presentations/`
- `/docs/screenshots/`

---

## 📜 Licencia

MIT
