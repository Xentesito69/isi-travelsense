## KPIs (medibles en MVP)  
### Rendimiento de la IA:  
• Tiempo de respuesta del motor de IA: Tiempo transcurrido desde la petición del usuario 
hasta la generación del itinerario narrativo (Objetivo: < 3 segundos).  
• Tasa de Coherencia Contextual: % de planes generados que se ajustan correctamente al 
clima detectado (ej. que no sugiera senderismo si la API de clima devuelve lluvia).  
### Interacción y Valor:  
• Nº de planes generados por usuario: Mide el interés recurrente en la herramienta.  
• Nº de recomendaciones "Aceptadas": Cantidad de planes generados por la IA que el 
usuario decide guardar en favoritos (valida la calidad de la sugerencia).  
• Ratio de Conversión de Preferencias: % de usuarios que rellenan el campo de "intereses" 
para que la IA personalice el resultado.  
### Retención:  
• Nº de planes consultados post-generación: Usuarios que vuelven a entrar para ver un plan 
que la IA ya les guardó en la base de datos.  


## OKRs   
### O1 – Desarrollar un MVP potenciado por IA y totalmente integrado  
• KR1: Integrar con éxito las APIs de Google Maps, OpenWeather y un modelo de IA 
(OpenAI/Gemini).  
• KR2: Generar un itinerario narrativo y coherente mediante la IA que combine al menos 3 
puntos de interés por día.  
• KR3: Implementar la persistencia de usuarios e itinerarios "inteligentes" en la base de datos 
para su consulta posterior.  
### O2 – Optimizar la relevancia de las recomendaciones mediante razonamiento semántico  
• KR1: Desarrollar un motor de decisión híbrido donde la IA ajuste el "scoring" de los 
lugares basándose en la previsión meteorológica real.  
• KR2: Validar que el sistema filtra correctamente actividades según el contexto (ej. la IA debe 
descartar deporte al aire libre si la API de clima detecta lluvia).  
• KR3: Incluir una "explicación de la IA" en cada recomendación para aumentar la confianza 
del usuario.  
### O3 – Garantizar la calidad técnica y el despliegue del sistema  
• KR1: Configurar un pipeline de CI/CD que ejecute tests automáticos, incluyendo pruebas de 
validación de las respuestas de la IA (evitar alucinaciones).  
• KR2: Documentación técnica completa del diseño del prompt y la arquitectura de integración 
de sistemas.  
