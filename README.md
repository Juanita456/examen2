# Predicción de Cancelación de Reservas de Hotel 

Aplicación web desarrollada con **Flask** que utiliza un modelo de **Machine Learning (Random Forest)** para predecir si una reserva de hotel será cancelada o no.

---

## Características
- Interfaz web sencilla desarrollada con HTML y CSS.  
- Backend en Flask que carga el modelo entrenado (`modelo_rf.pkl` ).  
- Predicción basada en los siguientes campos:
  - Lead Time (días entre reserva y llegada)
  - ADR (Tarifa Promedio Diaria)
  - Total de Solicitudes Especiales
  - Cambios en la Reserva
  - Tipo de Depósito

---

## ⚙️ Instalación y Uso

### Clonar el repositorio
git clone https://github.com/tu_usuario/PrediccionReservasHotel.git

### Crear un entorno virtual 
python -m venv venv
venv\Scripts\activate

### Instalar dependencias
pip install -r requirements.txt
