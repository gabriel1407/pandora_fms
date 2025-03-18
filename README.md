# Prueba Técnica - Desarrollador Python (CLI, Multiprocesos, Multihilos, APIs)

## Descripción
Esta aplicación CLI obtiene información de fotos y sus respectivos álbumes desde la API pública JSONPlaceholder. Implementa tres modos de ejecución para realizar las solicitudes:

1. **Modo Secuencial:** Consulta cada foto y su álbum de forma secuencial.
2. **Modo Multihilos:** Usa `threading` para hacer las consultas de manera concurrente.
3. **Modo Multiprocesos:** Usa `multiprocessing` para procesar las solicitudes en paralelo.

## Instalación
Para ejecutar este proyecto, sigue estos pasos:

### **1. Clonar el repositorio**
```sh
git clone <URL_DEL_REPOSITORIO>
En este caso seria el de este mismo repositorio

cd <NOMBRE_DEL_REPOSITORIO>
```

### **2. Crear un entorno virtual (opcional pero recomendado)**
```sh
python -m venv env
source env/bin/activate  # Para macOS/Linux
env\Scripts\activate  # Para Windows
```

### **3. Instalar dependencias**
```sh
pip install -r requirements.txt
```

> Nota: Asegúrate de tener `Python 3.10+` instalado.

## Uso

Ejecutar el script con:

```sh
python script.py --mode <secuencial|multihilos|multiprocesos> --photos <cantidad_opcional>
```

Ejemplo:

```sh
python script.py --mode multihilos --photos 10
```

### Parámetros:
- `--mode`: Modo de ejecución (`secuencial`, `multihilos`, `multiprocesos`).
- `--photos`: Cantidad de fotos a obtener (opcional; si no se especifica, obtiene todas).

## Ejemplo de Salida

```sh
Modo de ejecución: multihilos
Foto ID: 1
Título: Accusamus Beatae Ad
URL: https://via.placeholder.com/600/92c952
Álbum ID: 1
Álbum Título: Quidem Molestiae Enim
Tiempo total de ejecución: 2.345 segundos
```

## Explicación de la Solución

La aplicación obtiene la lista de fotos y luego recupera la información de cada álbum correspondiente. Dependiendo del modo de ejecución:

- **Modo Secuencial:** Procesa una foto a la vez.
- **Modo Multihilos:** Crea un hilo por foto para hacer la consulta concurrentemente.
- **Modo Multiprocesos:** Usa un `Pool` de procesos para distribuir la carga.

### Problemas y Soluciones
- **Latencia de API:** En el modo secuencial, la consulta es más lenta debido a las múltiples solicitudes.
- **Limitaciones de CPU:** `threading` es eficiente para operaciones I/O, pero `multiprocessing` es mejor para tareas CPU-intensivas.

### Cuándo usar cada modo
- **Secuencial:** Cuando la cantidad de datos es pequeña o la API tiene límites de concurrencia.
- **Multihilos:** Cuando hay muchas consultas HTTP que pueden ejecutarse en paralelo.
- **Multiprocesos:** Cuando el procesamiento local de cada solicitud es intensivo y se quiere aprovechar múltiples núcleos de CPU.

## Puntos Extra Implementados
- **Manejo de errores con `logging`**.
- **Medición precisa del tiempo de ejecución**.

## Pruebas
Puedes comparar los tiempos de ejecución con:
```sh
python script.py --mode secuencial --photos 10
python script.py --mode multihilos --photos 10
python script.py --mode multiprocesos --photos 10
```

## Autor
Gabriel Carvajal
