from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Cargar modelo y columnas
model = joblib.load('modelo_rf.pkl')
columnas = joblib.load('columnas_modelo.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Capturar los datos del formulario
        lead_time = float(request.form['lead_time'])
        adr = float(request.form['adr'])
        total_of_special_requests = int(request.form['total_of_special_requests'])
        booking_changes = int(request.form['booking_changes'])
        deposit_type = request.form['deposit_type']  # texto

        # Crear DataFrame base
        data = {
            'lead_time': [lead_time],
            'adr': [adr],
            'total_of_special_requests': [total_of_special_requests],
            'booking_changes': [booking_changes],
            'deposit_type': [deposit_type]
        }

        df_input = pd.DataFrame(data)

        # One-hot encoding para deposit_type
        df_input = pd.get_dummies(df_input, columns=['deposit_type'])

        # Asegurar que tenga las mismas columnas que el modelo
        for col in columnas:
            if col not in df_input.columns:
                df_input[col] = 0
        df_input = df_input[columnas]

        # Predicción
        prediction = model.predict(df_input)[0]
        prob = model.predict_proba(df_input)[0][1]
        resultado = "Cancelará la reserva" if prediction == 1 else "No cancelará la reserva"

        return render_template('index.html', prediction=f"{resultado} (Probabilidad: {prob:.2f})")

    except Exception as e:
        return render_template('index.html', prediction=f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)