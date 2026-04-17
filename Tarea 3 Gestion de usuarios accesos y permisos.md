TAREA 3: Gestión de usuarios, accesos y permisos (SaaS / cuentas) 
Parte A. Elige 1 escenario (obligatorio) 
● Alta de empleado nuevo 
Parte B. Define el “perfil del usuario” 
Perfil del usuario:Juan Perez Gomez,  
Área: Marketing  
Rol: Diseñador gráfico JR,  
Permisos: Editor/Creador (Escritura) Solo lectura, sin permisos de administrador 
Herramientas requeridas: - - - - - 
Correo electrónico institucional (Gmail / Google Workspace) 
Acceso a Drive/Sharepoint  
Microsoft Teams 
Canva  
Suite de Adobe 
Parte C. Flujo de atención (como mesa de servicio) 
Explica en bullets: 
1. Recepción de solicitud (ticket) para alta de empleado: -Nombre de empleado: Juan Perez Gomez  -Puesto: Diseñador grafico JR -Departamento: Marketing -Fecha de ingreso: 20/03/2026 -Jefe directo: Marco Morales    
2. Validación / autorización (quién aprueba) 
Valida: Dayana Hernandez del departamento de RRHH 
3. Acción ejecutada (alta/cambio/baja) 
ALTA 
4. Confirmación con usuario 
Se envía correo de confirmación a: - - - 
RRHH 
Jefe directo 
(Opcional) Nuevo empleado 
El correo incluye: - 
Usuario/correo asignado - - 
Instrucciones de acceso 
Recomendación de cambio de contraseña 
Se solicita confirmación de correcto funcionamiento 
5. Documentación 
Se actualiza el ticket con: - 
Fecha y hora de creación del correo - - 
Responsable que ejecutó el alta 
Detalles de configuración aplicada 
Estado: Cerrado.

Parte D. Evidencia simulada -Capturas (mock) 
Crear perfil de nuevo usuario para windows.
Crear cuenta corporativa para el nuevo empleado. 
Checklist de pasos 
1. Validación de solicitud 
2. Creación de usuario en sistema 
3. Asignación de correo 
4. Configuración de permisos 
5. Notificación al usuario 
6. Documentación del ticket -Comandos 
Creación de usuario en AD: New-ADUser -Name "Juan Perez Gomez" -GivenName 
"Juan" -Surname "Perez Gomez" -Department "Marketing" -Enabled $true  
Asignacion a grupo: Add-ADGroupMember -Identity "Graphic Designer" -Members 
"Juan Perez Gomez" -Formato de ticket con campos: