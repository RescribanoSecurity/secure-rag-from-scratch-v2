# 🔐 Secure RAG v2 – RAG con Enfoque Security-First

Secure RAG v2 es un sistema **RAG con enfoque security-first**, construido como laboratorio de aprendizaje y arquitectura de referencia para aplicaciones con LLMs.

---

## 🎯 Objetivos del Proyecto

- Construir un RAG desde cero con mentalidad de producción
- Separar claramente seguridad de entrada y salida
- Aplicar defensa en profundidad
- Alinear el sistema con OWASP LLM Top 10

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

---

## 🔐 Modelo de Seguridad

### Seguridad de Entrada
Detecta intención explícitamente maliciosa.

### Seguridad de Salida
Previene fugas de PII y secretos mediante redacción o bloqueo.

---

## 📜 Licencia

MIT
