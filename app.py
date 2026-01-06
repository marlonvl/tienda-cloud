from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# --- SIMULACIÓN DE BASE DE DATOS ---
# En un entorno real, estos datos vendrían de SQL o Firestore.
# Para esta práctica de CI/CD, los definimos aquí para facilitar el despliegue.
def obtener_productos():
    productos = [
        {
            "id": 1,
            "nombre": "MacBook Pro M3",
            "precio": 1499.00,
            # Imagen real de Unsplash
            "imagen": "https://images.unsplash.com/photo-1724859234679-8e4eb56eae0d?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "descripcion": "Potencia bruta para desarrolladores. Chip M3 Pro, 18GB de memoria unificada y hasta 18 horas de batería. Ideal para correr contenedores Docker sin despeinarse."
        },
        {
            "id": 2,
            "nombre": "Sony WH-1000XM5",
            "precio": 348.00,
            "imagen": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=800&q=80",
            "descripcion": "Cancelación de ruido líder en la industria. Perfectos para mantener el foco (Flow State) mientras programas tu pipeline de CI/CD."
        },
        {
            "id": 3,
            "nombre": "Keychron K2 Mecánico",
            "precio": 89.99,
            "imagen": "https://images.unsplash.com/photo-1708024593817-d9a26da9f977?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "descripcion": "Teclado mecánico inalámbrico 75% con switches Gateron Blue. Compacto, táctil y con el sonido satisfactorio que todo programador ama."
        },
        {
            "id": 4,
            "nombre": "Dell UltraSharp 38\"",
            "precio": 950.00,
            "imagen": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?auto=format&fit=crop&w=800&q=80",
            "descripcion": "Monitor curvo WQHD+. Espacio suficiente para tener VS Code, la terminal y la documentación de Google Cloud abiertos simultáneamente."
        },
        {
            "id": 5,
            "nombre": "Herman Miller Aeron",
            "precio": 1200.00,
            "imagen": "https://images.unsplash.com/photo-1505843490538-5133c6c7d0e1?auto=format&fit=crop&w=800&q=80",
            "descripcion": "La silla definitiva para ergonomía. Malla Pellicle transpirable y soporte lumbar ajustable PostureFit SL."
        },
        {
            "id": 6,
            "nombre": "Servidor Rack 2U",
            "precio": 2500.00,
            "imagen": "https://plus.unsplash.com/premium_photo-1682145189653-bb0b79db3415?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "descripcion": "Hardware dedicado para tu infraestructura on-premise. Doble procesador Xeon, 128GB RAM y bahías NVMe hot-swap."
        }
    ]
    return productos

@app.route('/')
def index():
    # Enviamos la fecha para verificar cuándo se hizo el último despliegue automático
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lista_productos = obtener_productos()
    
    return render_template('index.html', productos=lista_productos, fecha=fecha_actual)

if __name__ == '__main__':
    # '0.0.0.0' permite acceder desde fuera del contenedor
    app.run(host='0.0.0.0', port=5000, debug=True)
