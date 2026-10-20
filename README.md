# Practica u4s7 — Pulido Funcional, UX y Simulacro de Defensa

**Estudiante:** Alejandro Bojórquez Rodríguez  
**Asignatura:** Aplicaciones Web (APLICAWEB - 4to Semestre)  
**Proyecto Integrador:** Vitrina Web con CRUD y Autenticación de Usuarios

---

## 📌 Enlaces del Proyecto

* 📁 **Repositorio en GitHub:** [u4S7-bojorquez-rodriguez-alejandro](https://github.com/BojorquezRodriguez01/u4S7-bojorquez-rodriguez-alejandro.git)  
* 🌐 **Despliegue en Producción (Render):** [https://u4s7-bojorquez-rodriguez-alejandro.onrender.com](https://u4s7-bojorquez-rodriguez-alejandro.onrender.com)

---

## 🛠️ Mejoras e Implementaciones de la Semana

Esta versión *"feature-complete"* consolida el trabajo de las 6 semanas anteriores agregando capa de usabilidad, accesibilidad y experiencia de usuario (UX):

1. **Paginación con `Paginator`:** Listado segmentado en bloques de 5 registros para optimizar la navegación y la carga de datos.
2. **Búsqueda Dinámica:** Filtro por título mediante consultas case-insensitive (`icontains`) que preserva la búsqueda al cambiar de página (`?q=...&page=...`).
3. **Estados Vacíos Informativos:** Mensajes personalizados en la plantilla mediante `{% empty %}` diferenciando entre una lista sin registros y un resultado de búsqueda sin coincidencias.
4. **Diseño Responsivo e Inclusivo (UI Review):** 
   * Tabla adaptada para dispositivos móviles con `overflow-x-auto`.
   * Atributos de accesibilidad `aria-label` en controles de navegación y búsqueda.
   * Contraste y focos de teclado optimizados.

---

## 💻 Tecnologías Utilizadas

* **Lenguaje &
