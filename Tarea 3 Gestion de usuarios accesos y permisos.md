# TAREA 3: Gestión de usuarios, accesos y permisos (SaaS / cuentas)

---

## 🅰️ Parte A. Escenario
**Alta de empleado nuevo**

---

## 🅱️ Parte B. Perfil del usuario

- **Nombre:** Juan Pérez Gómez  
- **Área:** Marketing  
- **Rol:** Diseñador Gráfico Jr  
- **Permisos:**
  - Editor / Creador (escritura)
  - Solo lectura en recursos sensibles
  - Sin permisos de administrador  

- **Herramientas requeridas:**
  - Correo institucional (Google Workspace / Gmail)
  - Acceso a Drive / SharePoint  
  - Microsoft Teams  
  - Canva  
  - Suite de Adobe  

---

## 🅲 Parte C. Flujo de atención (Mesa de Servicio)

### 1. Recepción de solicitud (ticket)

Se recibe solicitud con la siguiente información:

- Nombre: Juan Pérez Gómez  
- Puesto: Diseñador Gráfico Jr  
- Departamento: Marketing  
- Fecha de ingreso: 20/03/2026  
- Jefe directo: Marco Morales  

---

### 2. Validación / autorización

- Aprobado por: **Dayana Hernández (RRHH)**  
- Se valida que la solicitud esté completa  

---

### 3. Acción ejecutada

- Tipo: **ALTA de usuario**
- Actividades:
  - Creación de cuenta en Active Directory  
  - Asignación de correo institucional  
  - Configuración de accesos  
  - Asignación a grupos  

---

### 4. Confirmación con usuario

Se envía correo a:

- RRHH  
- Jefe directo  
- (Opcional) Usuario  

**Incluye:**

- Usuario/correo asignado  
- Instrucciones de acceso  
- Cambio de contraseña recomendado  
- Validación de funcionamiento  

---

### 5. Documentación

Se actualiza el ticket con:

- Fecha y hora de creación  
- Responsable  
- Configuración aplicada  
- Evidencias  
- Estado: **Cerrado**  

---

## 🅳 Parte D. Evidencia simulada

### Checklist

- [x] Validación de solicitud  
- [x] Creación de usuario  
- [x] Asignación de correo  
- [x] Configuración de permisos  
- [x] Notificación  
- [x] Documentación  

---

## 💻 Comandos (simulación)

### Crear usuario en Active Directory

```powershell
New-ADUser -Name "Juan Perez Gomez" `
-GivenName "Juan" `
-Surname "Perez Gomez" `
-Department "Marketing" `
-Enabled $true