# Teoría Fundamental y Referencias Externas
## Conceptos para Resolver Ejercicios Python UD2 (E1-E37)

---

## 📚 Tabla de Contenidos
0. Punto de partida: conceptos fundamentales de IA (UD1)
1. Fundamentos de Programación (nombres, constantes, operadores)
2. Tipos de Datos en Python (conversión, entrada/salida y formato, cadenas a fondo)
3. Estructuras de Control (bucles anidados, patrones, problemas numéricos)
4. Funciones (argumentos, lambda, map/filter/reduce, recursión, ámbito)
5. Estructuras de Datos Complejas (listas a fondo, conjuntos, comprensiones, módulos, chuleta)
6. Conceptos Estadísticos
7. Librerías Científicas (NumPy, Pandas)
8. Visualización (Matplotlib)
9. Conceptos ETL y Análisis de Datos
10. Introducción a Machine Learning
11. Introducción a Big Data
12. Ecosistema de Librerías: PyTorch, scikit-learn y Seaborn
13. Crear Aplicaciones: Escritorio y Web (tkinter, Streamlit, Gradio...) y desplegar un modelo
14. Ampliación con materiales complementarios (IA vs ML vs DL vs GenAI, Pandas, pipeline ML, Seaborn, EDA, redes neuronales, IA generativa, hashing, automatización, testing y SQLite, algoritmia, banco de ejercicios, buenas prácticas y Python avanzado)
15. Referencias Externas (incluye IDEs locales y datasets recomendados)

---

## 0️⃣ PUNTO DE PARTIDA: CONCEPTOS FUNDAMENTALES DE IA (UD1)

Esta sección resume los conceptos de la **UD1 · Conceptos clave de la inteligencia artificial**, trabajados en el aula virtual (libro «UD1. Conceptos» y sus tareas) y en los capítulos 1–3 del libro de J. F. Puentes Calvo, *Tecnologías Inteligentes* (ed. 2025, CC BY-NC-ND 4.0). En la UD2 estos conceptos **se convierten en código**: cada apartado indica con qué parte de este documento conecta.

---

### 0.1 ¿Qué es la inteligencia? ¿Y la inteligencia artificial?

No hay una definición única: la inteligencia es un **constructo social** que cambia con la cultura y la época. Howard Gardner propone **inteligencias múltiples**: lingüística, lógico-matemática, espacial, musical, corporal, interpersonal, intrapersonal, naturalista y otras.

> **Definición de consenso** (libro, 1.1): «La inteligencia es la capacidad general para razonar, planificar, resolver problemas, pensar de manera abstracta, comprender ideas complejas, aprender rápidamente y, especialmente, **aprender de la experiencia**».

Esta definición da el **criterio para decidir si una máquina es inteligente** (0.5).

**¿Y la inteligencia artificial?** Es la rama de la informática que crea sistemas capaces de realizar tareas que normalmente requieren inteligencia humana: reconocer patrones e imágenes, aprender de la experiencia, resolver problemas, comprender el lenguaje y tomar decisiones.

| Característica clave | Qué significa | En un móvil con Face ID |
|----------------------|---------------|-------------------------|
| **Percepción** | Recibir información del entorno con sensores | La cámara y el sensor de profundidad captan la cara |
| **Razonamiento** | Analizar la información y decidir con lógica | ¿Coincide con la cara registrada? |
| **Aprendizaje** | Mejorar con la experiencia | Se adapta a gafas, barba o cambios de peinado |
| **Actuación** | Realizar acciones en el entorno | Desbloquea la pantalla |

### 0.2 Datos, información y conocimiento

| Nivel | Qué es | Ejemplo del semáforo | En Python |
|-------|--------|----------------------|-----------|
| **Dato** | Valor aislado, sin contexto | `"rojo"` | `color = "rojo"` |
| **Información** | Dato con contexto y significado | «El semáforo está en rojo» | `semaforo = {"estado": "rojo"}` |
| **Conocimiento** | Información que permite decidir o actuar | «Si está en rojo, me paro» | `if semaforo["estado"] == "rojo": parar()` |

**Aprender es encontrar patrones**: una fuente que emite siempre ceros no aporta información, y una secuencia totalmente aleatoria no permite predecir nada. La IA busca regularidades entre esos dos extremos.

**Sentidos y sensores**: la tecnología **amplía los sentidos** humanos e imita los de los animales. Los sensores son la puerta de entrada de los datos a un sistema de IA.

| Sentido | Sensor | Fenómeno físico | Dónde aparece |
|---------|--------|-----------------|---------------|
| Vista | Sensor de imagen CMOS | Efecto fotoeléctrico | Cámara del móvil (→ visión artificial) |
| Oído | Micrófono MEMS | Presión que deforma una membrana | Asistentes de voz (→ lenguaje natural) |
| Tacto | Pantalla capacitiva | Variación de capacidad eléctrica | Móvil, tableta |
| Equilibrio | Acelerómetro, giroscopio | Inercia de una masa microscópica | Girar la pantalla, pulseras de actividad |
| Ecolocalización (murciélago) | Ultrasonidos | Tiempo de ida y vuelta del eco | Sensor de aparcamiento |
| Magnetorrecepción (aves) | Magnetómetro (efecto Hall) | El campo magnético desvía cargas en movimiento | Brújula del móvil |
| Infrarrojos (serpientes) | Sensor PIR, cámara térmica | Radiación infrarroja de los cuerpos calientes | Detector de presencia |
| — | LiDAR | Tiempo de vuelo de pulsos láser | Coche autónomo, robot aspirador |
| — | Radar | Ondas de radio y efecto Doppler | Coche autónomo |

**Conexión con UD2**: los datos de los sensores llegan como números, listas y tablas. Leerlos, limpiarlos y convertirlos en información es justamente el **ETL** (sección 9). Una imagen es una **matriz NumPy** (sección 7).

### 0.3 Del sensor a la acción: el ciclo de un sistema de IA

**Sensorización ≠ percepción**:
- **Sensorizar** es adquirir datos del mundo físico. Por ejemplo, un termómetro que registra la temperatura cada hora.
- **Percibir** es organizar e interpretar esos datos para extraer significado. Por ejemplo, combinar la temperatura con la humedad y la presión para hacer un pronóstico.

Entre percibir y actuar hay pasos que no pueden faltar:

| Paso | Qué hace | En Python (UD2) |
|------|----------|-----------------|
| **Representación** | Transformar los datos para que la máquina los entienda: números, palabras, imágenes | Tipos de datos, listas, matrices NumPy (secciones 2, 5, 7) |
| **Procesamiento** | Organizarlos según el objetivo: tablas, grafos, ejes de coordenadas | DataFrames, diccionarios, grafos (7, 0.7) |
| **Razonamiento** | **Formalizar** el problema: identificar sus elementos, sus relaciones y las reglas | Condicionales y funciones (3, 4) |

**Formalizar es encontrar la estructura** común de problemas distintos:

```
«Los gatos son encantadores y Tip es un gato   → Tip es encantador»
«Las frutas son saludables y la manzana es fruta → la manzana es saludable»

Regla:  si un CONJUNTO tiene una PROPIEDAD y un ELEMENTO pertenece al conjunto,
        el elemento tiene la propiedad
```

```python
propiedades = {"gatos": "encantador", "frutas": "saludable"}
pertenece = {"Tip": "gatos", "manzana": "frutas"}

def deducir(elemento):
    conjunto = pertenece[elemento]
    return f"{elemento} es {propiedades[conjunto]}"

print(deducir("Tip"))       # Tip es encantador
print(deducir("manzana"))   # manzana es saludable
```

**Todo acaba en ceros y unos**: los circuitos solo distinguen dos estados, apagado (0, nivel bajo) y encendido (1, nivel alto). La **lógica formal** opera con verdadero (1) y falso (0). En Python son `True` y `False` con los operadores `and`, `or` y `not` (sección 2.3), y `bin(5)` muestra `'0b101'`.

**El ciclo percepción → procesamiento → actuación**:

```
1 PERCEPCIÓN    sensores recogen datos          cámara → imagen · micrófono → audio
2 PROCESAMIENTO el algoritmo decide             «¿gato o perro?» → 92 % gato
3 ACTUACIÓN     los actuadores ejecutan         pantalla muestra «Gato» · motor gira
        └──────────── el entorno cambia y se vuelve a percibir ◄──────────┘
```

**Ejemplo: robot que evita obstáculos**. Es automatización (una regla fija), pero muestra el ciclo completo:

```python
import random

def leer_ultrasonido():                 # SENSOR: distancia en cm (simulada)
    return random.randint(2, 400)

def decidir(distancia_cm):              # PROCESAMIENTO
    return "girar 90°" if distancia_cm < 20 else "avanzar"

def actuar(orden):                      # ACTUADOR: motores
    print("Motor:", orden)

for _ in range(5):                      # el ciclo se repite continuamente
    d = leer_ultrasonido()
    print(f"Distancia: {d} cm", end=" → ")
    actuar(decidir(d))
```

**Sensores y actuadores habituales**:

| Tipo | Ejemplos | Aplicación |
|------|----------|------------|
| Sensores visuales | Cámara RGB, sensor de profundidad (Kinect) | Reconocimiento facial, drones, videojuegos |
| Sensores de audio | Micrófono (unos 16 000 muestras/s para voz) | Alexa, Siri, dictado |
| Sensores de proximidad | Ultrasonidos (2 cm a 4 m), LDR (luz) | Robots aspiradores, brillo automático de la pantalla |
| Sensores de movimiento | Acelerómetro, giroscopio | Contar pasos, estabilizar la cámara, realidad virtual |
| Sensores ambientales | Temperatura, humedad, presión | Estaciones meteorológicas |
| Actuadores mecánicos | Motor DC (giro continuo), servomotor (0–180°), motor paso a paso | Ruedas, brazos robóticos, impresoras 3D |
| Actuadores lumínicos | LED RGB, pantalla LCD/OLED | Indicadores, móviles |
| Actuadores de sonido | Altavoz | Asistentes de voz, alarmas |

### 0.4 Breve historia de la IA: veranos e inviernos

```
1843      Ada Lovelace: la máquina analítica podría manipular símbolos, no solo números
1950      Alan Turing: «¿Pueden pensar las máquinas?» → Test de Turing
1956      Conferencia de Dartmouth (McCarthy, Minsky...): nace el término «inteligencia artificial»
           Optimismo: se cree que en 20 años habrá IA general (predicción fallida)
1966-74   ❄ PRIMER INVIERNO: máquinas lentas, conocimiento difícil de representar → menos fondos
1980-87   📈 SISTEMAS EXPERTOS: reglas extraídas de expertos (XCON configuraba ordenadores)
1987-93   ❄ SEGUNDO INVIERNO: sistemas expertos caros, difíciles de mantener, no aprenden
1995-2011 🚀 ERA DEL MACHINE LEARNING: de «programar reglas» a «aprender de datos»
          1997 Deep Blue gana a Kasparov · 2006 Hinton entrena redes profundas · 2011 Watson gana Jeopardy!
2012      🚀 ERA DEL DEEP LEARNING: una red convolucional arrasa en ImageNet (≈85 % frente a ≈74 %)
2016      AlphaGo vence al campeón mundial de Go (deep learning + búsqueda)
2017-18   Arquitectura Transformer → BERT y GPT revolucionan el lenguaje
2020      GPT-3: 175 000 millones de parámetros; hace tareas sin entrenamiento específico
2022      ChatGPT: un millón de usuarios en cinco días
2023-26   Modelos multimodales (GPT-4, Gemini, Claude...) y modelos especializados en medicina, biología, código
```

**Personas clave**: Ada Lovelace, Alan Turing, John McCarthy, Marvin Minsky, Norbert Wiener, Grace Hopper, Walter Pitts, Elaine Rich, Lotfi Zadeh, Judea Pearl, Fei-Fei Li, Cynthia Breazeal, Geoffrey Hinton, Yoshua Bengio, Yann LeCun, Kate Crawford, Cynthia Dwork, Karen Spärck Jones.

**¿Por qué el deep learning no triunfó hasta 2012 si las redes neuronales existen desde los años 50?** Faltaban datos masivos, GPU y capacidad de cálculo, y una forma eficiente de entrenar con *backpropagation*.

**Grandes modelos de lenguaje (LLM)**: son Transformers entrenados con enormes cantidades de texto, con miles de millones de parámetros, durante meses y en miles de GPU. Su tarea básica es **predecir la siguiente palabra** (14.8), pero de la escala **emergen** capacidades que nadie programó explícitamente. Si «entienden» de verdad es un debate abierto.

**Lección para la UD2**: la IA actual funciona porque se juntaron **datos** (Big Data, sección 11), **capacidad de cálculo** (GPU) y **algoritmos** (redes neuronales, 14.7). Python es el lenguaje que une las tres cosas.

### 0.5 ¿Qué es IA y qué no lo es?

**No son IA por sí mismos**: los algoritmos deterministas (ordenar, buscar), los programas con condiciones fijas, la automatización, la estadística y el análisis de datos, los sensores e IoT, los simuladores, las bases de datos y las redes de comunicación. **Pero un sistema de IA suele contener piezas de todos ellos.**

**IA frente a automatización**: la automatización ejecuta instrucciones predefinidas sin adaptarse. Una puerta que se abre con un sensor de movimiento (sensor + actuador) es automatización. Un sistema que **aprende a qué hora abrir** según el flujo de personas es IA.

**Criterio** (basado en la definición de 0.1): ¿**aprende** de la experiencia? ¿Se **adapta** a situaciones nuevas? ¿**Decide** según el contexto?

| Sistema | ¿IA? | Por qué |
|---------|------|---------|
| Termostato clásico (enciende por debajo de 20 °C) | No | Regla fija: `if temp < 20: encender()` |
| Termostato que aprende tus horarios | Sí | Aprende patrones de uso |
| Filtro antispam | Sí | Aprende de ejemplos y de lo que marcas como spam |
| Hoja de cálculo, calculadora | No | Cálculo determinista |
| Robot aspirador que mapea la casa | Sí | Agente: percibe, construye un mapa y decide |
| Recomendaciones de Netflix o Spotify | Sí | Modelo entrenado con el comportamiento de usuarios |
| Desbloqueo facial, teclado predictivo, ChatGPT | Sí | Modelos de visión y de lenguaje |
| Puerta automática, detector de humo, semáforo con temporizador | No | Sensor + umbral o temporizador |
| GPS calculando una ruta | Depende | Búsqueda en grafos (técnica clásica de IA) sin aprendizaje; si estima el tráfico con datos históricos, sí aprende |
| Corrector ortográfico | Depende | Con diccionario es una regla; si sugiere por contexto, usa un modelo |

**Conexión con UD2**: casi todo lo que programamos en E1–E37 es **programación determinista** (no IA). Es la base imprescindible: los modelos de IA (sección 10, UD5) se construyen encima de ella.

### 0.6 Tipos de IA: IA clásica, Machine Learning y Deep Learning

**IA clásica, ML y DL** (cada una contiene a la siguiente, 14.1):

| Aspecto | IA clásica | ML tradicional | Deep Learning |
|---------|-----------|----------------|---------------|
| Cómo funciona | Reglas explícitas escritas por personas | Aprende patrones de los datos | Aprende las características por sí mismo |
| Características | Definidas por humanos | Seleccionadas por humanos (*feature engineering*) | Descubiertas automáticamente |
| Datos necesarios | Pocos | Medianos | Muchos (millones) |
| Interpretabilidad | Alta | Media | Baja («caja negra») |
| Ejemplo | Diagnóstico con reglas SI-ENTONCES | Árbol de decisión para el spam | Red neuronal que reconoce caras |
| En el curso | Condicionales (sección 3) | scikit-learn (10, 14.4) | Keras/PyTorch (12, 14.7) |

**Spam con reglas frente a spam con ML**:

```python
# IA clásica: reglas escritas a mano
def es_spam_reglas(texto):
    return any(p in texto.lower() for p in ["gratis", "premio", "urgente"])

# Machine Learning: aprende de ejemplos etiquetados
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

correos = ["gana un premio gratis", "reunión de departamento mañana",
           "oferta urgente solo hoy", "apuntes de la UD2 adjuntos",
           "premio en efectivo ya", "horario del examen de Python"]
etiquetas = [1, 0, 1, 0, 1, 0]                  # 1 = spam
vectorizador = CountVectorizer()
modelo = MultinomialNB().fit(vectorizador.fit_transform(correos), etiquetas)

nuevo = ["has ganado un premio"]
print(es_spam_reglas(nuevo[0]), modelo.predict(vectorizador.transform(nuevo))[0])   # True 1
```

**ML tradicional** usa algoritmos como la regresión lineal, los árboles de decisión, SVM, *k-means* y *Naive Bayes*. Funciona mejor con datos en tabla y le cuesta trabajar con imágenes o texto sin procesar.

**Deep Learning**: las capas de la red aprenden de lo simple a lo complejo.

```
píxeles → capa 1: bordes → capa 2: texturas → capa 3: orejas, ojos → capa 4: «gato» → 97 % gato
```

Tipos de redes: **CNN** para imágenes, **RNN/LSTM** para secuencias y **Transformers** para lenguaje (14.7).

✓ Úsalo con datos complejos (imágenes, audio, vídeo), con millones de ejemplos y cuando no sabes qué características importan.
✗ Evítalo con pocos datos o cuando necesitas explicar cada decisión.

**La misma tarea en tres generaciones**:

| Sistema | IA clásica | ML tradicional | Deep Learning |
|---------|-----------|----------------|---------------|
| Recomendador | «Si género = acción y nota > 7 → recomendar» | «Usuarios parecidos a ti vieron esto» | Red que aprende preferencias complejas |
| Reconocimiento de voz | Patrones fonéticos (años 90) | Modelos estadísticos (2000s) | Redes LSTM/CNN: acentos, ruido, contexto (2015+) |
| Traducción | Frases predefinidas | Estadística: errores gramaticales | Transformers: casi como una persona |

Un **coche autónomo** las combina todas. Usa sensores (cámaras, LiDAR, radar), DL para ver señales y peatones, ML para predecir el movimiento de otros vehículos e IA clásica para reglas de seguridad inviolables.

**Otras clasificaciones**:

| Clasificación | Tipos | Ejemplo |
|---------------|-------|---------|
| **Según la tarea** | **Débil o estrecha**: hace bien una sola tarea · **Fuerte o general**: inteligencia comparable a la humana en todo | Todas las IA reales son débiles; la IA fuerte solo existe en la ficción (HAL 9000, Ex Machina) |
| **Según la escuela** | **Simbólica**: reglas y lógica escritas por personas · **Conexionista**: redes neuronales que aprenden de datos | Sistema experto médico · reconocimiento de imágenes |
| **Según lo que se le pide** | Predecir, detectar patrones, agrupar, reducir dimensiones, generar datos, optimizar acciones | Precio de una casa, clientes parecidos, imágenes nuevas |

**Tipos de aprendizaje** (amplía la sección 10):

| Tipo | Datos | Tarea | Ejemplo |
|------|-------|-------|---------|
| **Supervisado** | Con etiqueta (la respuesta correcta) | Regresión (número) o clasificación (categoría) | Perro o gato; precio de una casa |
| **No supervisado** | Sin etiqueta | Agrupamiento (*clustering*) | Agrupar clientes parecidos |
| **Por refuerzo** | Premios y castigos al interactuar | Optimizar acciones | Robot que aprende a andar, IA de videojuegos |

**Entrenar un modelo en 5 pasos** (ejemplo de perros y gatos):

```
1 RECOPILAR y revisar los datos       → Pandas: read_csv, isnull, drop_duplicates (E20-E22)
2 DIVIDIR: 80 % entrenamiento, 20 % prueba → train_test_split (14.4)
3 ENTRENAR (repetir durante varias épocas) → modelo.fit(X_train, y_train)
4 EVALUAR con datos que el modelo no ha visto → modelo.score(X_test, y_test)
5 DESPLEGAR y vigilar; si empeora, volver al paso 1 → apps (sección 13)
```

### 0.7 Algoritmos y resolución de problemas por búsqueda

**Algoritmo**: secuencia **finita** de pasos **ordenados** que resuelve un problema. Por ejemplo, la receta de la tortilla de patatas:
- **Entrada**: 3 huevos, 500 g de patatas, sal y aceite.
- **Proceso**: pelar y cortar las patatas, freírlas, batir los huevos, mezclar y cuajar.
- **Salida**: la tortilla.

Un algoritmo tiene entrada, proceso y salida, y es **repetible**: con los mismos pasos se obtiene el mismo resultado. En Python, un algoritmo se escribe como una **función** (sección 4):

```python
def tortilla(huevos, patatas_g):               # ENTRADA
    pasos = ["pelar y cortar", "freír 10 min", "batir huevos", "mezclar", "cuajar 3 min/lado"]
    for i, paso in enumerate(pasos, 1):        # PROCESO: pasos ordenados y finitos
        print(i, paso)
    return f"Tortilla de {huevos} huevos y {patatas_g} g de patata"   # SALIDA

print(tortilla(3, 500))
```

#### Resolver problemas buscando: el espacio de estados

Muchos problemas se resuelven **explorando estados**:

- **Estado**: una situación posible del problema (dónde está cada pieza).
- **Estado inicial** y **estado final** (objetivo).
- **Transiciones**: movimientos permitidos de un estado a otro.
- Todo junto forma un **grafo** G = (N, A): nodos (estados) y aristas (transiciones).

**Explosión combinatoria**: el número de estados crece muy deprisa. Con 3 reinas en 3×3 hay 84 colocaciones; con 4 reinas en 4×4, 1 820; con 10 reinas habría que explorar casi 10¹⁴, más de tres años a un millón por segundo. **La inteligencia está en explorar solo los caminos prometedores**: la **poda** descarta una rama en cuanto se ve que no lleva a una solución.

**Las N reinas en Python** (backtracking con poda: una reina por fila):

```python
def n_reinas(n, fila=0, cols=()):
    """Devuelve todas las soluciones: tuplas con la columna (1..n) de la reina de cada fila."""
    if fila == n:
        return [cols]
    soluciones = []
    for c in range(1, n + 1):
        # Poda: misma columna o misma diagonal que una reina ya colocada
        if all(c != cc and abs(c - cc) != fila - f for f, cc in enumerate(cols)):
            soluciones += n_reinas(n, fila + 1, cols + (c,))
    return soluciones

print(n_reinas(3))        # [] → no hay solución
print(n_reinas(4))        # [(2, 4, 1, 3), (3, 1, 4, 2)]
print(len(n_reinas(8)))   # 92
```

**Torres de Hanói** (recursión, 14.12): el mínimo de movimientos es 2ⁿ − 1.

```python
def hanoi(n, origen="A", destino="C", auxiliar="B"):
    if n == 0:
        return []
    return (hanoi(n - 1, origen, auxiliar, destino)
            + [(origen, destino)]
            + hanoi(n - 1, auxiliar, destino, origen))

print(len(hanoi(3)), hanoi(3))   # 7 movimientos
print(2 ** 64 - 1)               # 18446744073709551615 con 64 discos
```

**El pastor, el lobo, el cordero y el heno** como búsqueda en anchura (BFS). Un estado es lo que queda en la orilla de partida:

```python
from collections import deque

TODOS = frozenset("PLCH")                    # Pastor, Lobo, Cordero, Heno

def valido(orilla):
    for lado in (orilla, TODOS - orilla):    # comprobar ambas orillas
        if "P" not in lado and ({"L", "C"} <= lado or {"C", "H"} <= lado):
            return False
    return True

def sucesores(orilla):
    lado = orilla if "P" in orilla else TODOS - orilla   # donde está el pastor
    for acompañante in [None] + sorted(lado - {"P"}):
        viajan = {"P"} | ({acompañante} if acompañante else set())
        nueva = orilla - viajan if "P" in orilla else orilla | viajan
        if valido(nueva):
            yield frozenset(nueva)

def resolver(inicio=TODOS, objetivo=frozenset()):
    cola, padre = deque([inicio]), {inicio: None}
    while cola:
        estado = cola.popleft()
        if estado == objetivo:
            camino = []
            while estado is not None:
                camino.append("".join(sorted(estado)) or "∅")
                estado = padre[estado]
            return camino[::-1]
        for s in sucesores(estado):
            if s not in padre:
                padre[s] = estado
                cola.append(s)

print(" → ".join(resolver()))   # 8 estados = 7 viajes
```

**Otros problemas de búsqueda**:

- **GPS**: las ciudades son nodos y las carreteras aristas con distancia. El **algoritmo de Dijkstra** encuentra el camino más corto.
- **Problema del viajante (TSP)**: visitar todas las ciudades una vez por el camino más corto. Solo admite soluciones aproximadas en tiempo razonable.
- **Ajedrez**: imposible explorarlo entero. **Minimax** mira unas jugadas hacia delante: yo **maximizo** mi ventaja suponiendo que el rival la **minimizará**. Una **función de valoración** suma el valor de las piezas, y la **poda alfa-beta** recorta ramas.

```python
import heapq

def dijkstra(grafo, origen):
    dist = {origen: 0}
    cola = [(0, origen)]
    while cola:
        d, nodo = heapq.heappop(cola)
        if d > dist[nodo]:
            continue
        for vecino, km in grafo[nodo].items():
            if d + km < dist.get(vecino, float("inf")):
                dist[vecino] = d + km
                heapq.heappush(cola, (d + km, vecino))
    return dist

galicia = {   # distancias aproximadas por carretera (km)
    "A Coruña": {"Santiago": 73, "Lugo": 97, "Ferrol": 55},
    "Ferrol": {"A Coruña": 55},
    "Santiago": {"A Coruña": 73, "Pontevedra": 62, "Lugo": 103, "Ourense": 110},
    "Pontevedra": {"Santiago": 62, "Vigo": 27},
    "Vigo": {"Pontevedra": 27, "Ourense": 100},
    "Lugo": {"A Coruña": 97, "Santiago": 103, "Ourense": 96},
    "Ourense": {"Santiago": 110, "Vigo": 100, "Lugo": 96},
}
print(dijkstra(galicia, "Ferrol"))   # distancia mínima desde Ferrol a cada ciudad
```

```python
def minimax(nodo, maximizo):
    """Árbol de juego como listas anidadas; las hojas son la valoración de la posición."""
    if isinstance(nodo, (int, float)):
        return nodo
    valores = [minimax(hijo, not maximizo) for hijo in nodo]
    return max(valores) if maximizo else min(valores)

# Tengo 2 jugadas; el rival responde con 2 jugadas a cada una
arbol = [[3, 12], [2, 8]]
print(minimax(arbol, True))   # 3: la primera jugada garantiza al menos 3 aunque el rival juegue bien
```

### 0.8 Resolver problemas optimizando

**Optimizar** = buscar la mejor solución según una **función objetivo**, respetando unas **restricciones**.

**Problema de la fábrica** (libro): los productos A y B dan 3 € y 4 € de beneficio. A necesita 2 h de montaje y 1 h de embalaje; B, 1 h y 2 h. Hay 100 h de montaje y 80 h de embalaje.

```
Maximizar   Z = 3x + 4y
sujeto a    2x +  y ≤ 100   (montaje)
             x + 2y ≤  80   (embalaje)
             x, y ≥ 0
Vértices: (0,0) → 0 €   (50,0) → 150 €   (0,40) → 160 €   (40,20) → 200 € ← ÓPTIMO
```

```python
# Comprobación por fuerza bruta (en UD5 se usaría scipy.optimize.linprog)
mejor = max(((3*x + 4*y, x, y) for x in range(101) for y in range(81)
             if 2*x + y <= 100 and x + 2*y <= 80))
print(mejor)   # (200, 40, 20)
```

Cuando un problema es demasiado grande para resolverlo exactamente, se aceptan **soluciones subóptimas** («suficientemente buenas»). Hay métodos inspirados en la naturaleza: **algoritmos genéticos** y **enjambre de partículas**.

**Descenso del gradiente**: es como bajar una montaña con los ojos vendados notando solo la pendiente, y dar siempre un paso cuesta abajo. Puede quedarse atrapado en un **mínimo local**. **Entrenar una red neuronal es esto mismo**: buscar el punto más bajo de una «montaña de error» con millones de dimensiones. Ver el código en 14.7.

### 0.9 Agentes inteligentes

> **Agente inteligente**: entidad autónoma que **percibe** su entorno mediante **sensores** y **actúa** sobre él mediante **actuadores** para maximizar una **medida de rendimiento**, aprendiendo de la experiencia.

**Cinco componentes**: percepción · actuación · procesamiento de la información · representación del conocimiento · aprendizaje.

```
          ┌──────────────────── ENTORNO ◄───────────────────┐
          │                                                 │
          ▼                                                 │
   SENSORES (percepción) → PROCESAMIENTO + CONOCIMIENTO → ACTUADORES (actuación)
                                   ▲
                             APRENDIZAJE (mejora con la experiencia)
```

| Componente | Coche autónomo | Robot aspirador |
|------------|----------------|-----------------|
| Entorno | Carreteras, vehículos, peatones, señales, tiempo | Casa: suelos, muebles, obstáculos |
| Sensores | Cámaras, LiDAR, radar, ultrasonidos, GPS, acelerómetros | LiDAR, sensores de choque y de desnivel, odómetro |
| Actuadores | Motor, frenos, dirección, luces | Ruedas, cepillos, aspiración |
| Procesamiento | Detectar objetos, estimar distancias, planificar trayectoria | Construir el mapa (SLAM), planificar la ruta |
| Conocimiento | Mapa, normas de circulación, trayectorias previstas | Mapa de la casa, zonas ya limpias |
| Aprendizaje | Modelos entrenados con millones de km | Mejora el mapa en cada pasada |
| Medida de rendimiento | Llegar seguro, sin infracciones, rápido y con confort | Superficie limpia, tiempo, batería |

**Un agente en Python** (programación orientada a objetos y bucle percibir → decidir → actuar):

```python
import random

class Aspirador:
    """Agente reactivo simple para un mundo de dos casillas: A y B."""
    def __init__(self):
        self.posicion = "A"
        self.conocimiento = {}                  # lo que sabe de cada casilla

    def percibir(self, mundo):                  # sensor
        return self.posicion, mundo[self.posicion]

    def decidir(self, percepcion):              # procesamiento
        pos, estado = percepcion
        self.conocimiento[pos] = estado
        if estado == "sucio":
            return "aspirar"
        if self.conocimiento.get("A") == self.conocimiento.get("B") == "limpio":
            return "parar"
        return "derecha" if pos == "A" else "izquierda"

    def actuar(self, accion, mundo):            # actuadores
        if accion == "aspirar":
            mundo[self.posicion] = "limpio"
            self.conocimiento[self.posicion] = "limpio"
        elif accion == "derecha":
            self.posicion = "B"
        elif accion == "izquierda":
            self.posicion = "A"

mundo = {"A": random.choice(["sucio", "limpio"]), "B": random.choice(["sucio", "limpio"])}
agente = Aspirador()
for paso in range(10):
    accion = agente.decidir(agente.percibir(mundo))
    print(paso, agente.posicion, accion)
    if accion == "parar":
        break
    agente.actuar(accion, mundo)
```

Este agente **no aprende**: es un automatismo con memoria. Para que aprendiera, por ejemplo qué casilla se ensucia más para visitarla antes, haría falta un modelo de ML (UD5) o aprendizaje por refuerzo.

### 0.10 La IA en el mundo real y la ética

| Ámbito | Uso de la IA | Riesgo |
|--------|-------------|--------|
| Medicina | Detectar tumores en radiografías | Errores sin supervisión médica; privacidad de los datos |
| Transporte | Conducción autónoma, rutas, tráfico | Responsabilidad en caso de accidente |
| Finanzas | Detectar fraude, conceder créditos | Sesgos que discriminan a colectivos |
| Educación | Tutores personalizados | Dependencia; copiar sin aprender |
| Agricultura y ganadería | Riego inteligente, drones, vigilancia del ganado | Coste; brecha digital en el rural |
| Energía y medio ambiente | Predecir la producción eólica y la demanda | Consumo energético de los propios modelos |
| Medios y entretenimiento | Recomendadores, generación de contenido | Desinformación, *deepfakes*, burbujas de filtro |
| Recursos humanos | Filtrar currículos | Sesgos de género u origen heredados de los datos |

**Sesgo algorítmico**: un algoritmo trata injustamente a un grupo de personas sin que nadie lo haya programado así. Es el resultado de **datos históricos sesgados** que la IA aprende y **amplifica**.

> **Caso real: el reclutador de Amazon (2018).** Amazon entrenó una IA para filtrar currículos con los datos de quién había contratado en los diez años anteriores, mayoritariamente hombres en puestos técnicos. El sistema aprendió a **penalizar a las mujeres**: dos currículos idénticos podían puntuar distinto según el género. Amazon abandonó la herramienta.
>
> **Cómo evitarlo**: detectar sesgos antes de lanzar el sistema, usar datos diversos y auditar el modelo con regularidad.

```python
import pandas as pd
# Comprobar un sesgo en los datos ANTES de entrenar (Pandas, sección 7)
historico = pd.DataFrame({"genero": ["H"] * 80 + ["M"] * 20,
                          "contratado": [1] * 60 + [0] * 20 + [1] * 5 + [0] * 15})
print(historico.groupby("genero")["contratado"].mean())   # H 0.75 · M 0.25 → ¡datos sesgados!
```

**Privacidad**: los sistemas de recomendación de las redes sociales recogen lo que publicas, lo que miras sin interactuar (cuánto tiempo te detienes en una foto), cuándo te conectas, tu ubicación, tus amistades, tus compras, tus búsquedas e incluso tu cara. Con esos datos personalizan el contenido y la publicidad: **si el servicio es gratis, el producto eres tú**. Los riesgos son aceptar condiciones sin leerlas y que tu información quede centralizada en una sola empresa, expuesta a filtraciones.

**Regla de oro del curso**: **toda respuesta de una IA se comprueba en otra fuente**. Si al investigar aparece un concepto que no entiendes, pregúntalo; si la respuesta trae otro concepto nuevo, vuelve a preguntar (método «recursivo» del libro).

### 0.11 De la UD1 a la UD2: mapa de conexiones

| Concepto UD1 | Herramienta en UD2 | Sección |
|--------------|--------------------|---------|
| Dato, información, conocimiento | Variables, tipos, diccionarios, condicionales | 1, 2, 3, 5 |
| Algoritmo | Funciones, bucles, pseudocódigo | 3, 4, 14.12 |
| Espacio de estados, grafo | Listas, diccionarios, recursión, BFS | 5, 14.9, 14.12 |
| Poda, explosión combinatoria | Complejidad O(n), backtracking | 14.12 |
| Optimización, descenso del gradiente | NumPy, redes neuronales | 7, 14.7 |
| Sensores y datos | ETL, Pandas, matrices de imagen | 7, 9 |
| Tipos de aprendizaje, entrenamiento | scikit-learn, `train_test_split`, normalización (E27) | 10, 12, 14.4 |
| Ciclo percepción → procesamiento → actuación | Bucles, funciones, entrada y salida | 0.3, 3, 4 |
| Agente inteligente | Clases y objetos, apps con eventos | 13, 0.9 |
| Sesgos y privacidad | `groupby` para detectar desequilibrios en los datos | 0.10, 7 |
| IA en el mundo real, ética | Streamlit y Gradio para compartir modelos de forma responsable | 13, 14.8 |

**Preguntas de autoevaluación** (aula virtual):
1. ¿Cuál es la diferencia fundamental entre ML y DL?
2. ¿Por qué el Deep Learning necesita más datos que el ML tradicional?
3. ¿Qué es un LLM y por qué funciona tan bien?
4. ¿Cuáles fueron los 3 hitos más importantes de la historia de la IA y por qué?
5. ¿Cuándo usarías IA clásica, ML o DL para un problema concreto?
6. ¿Qué diferencia hay entre sensorizar y percibir?
7. ¿Cómo se origina un sesgo algorítmico y cómo se evita?

**Recursos del aula virtual**:
- [Crash Course AI, episodios 1 y 2](https://www.youtube.com/watch?v=a0_lo_GDcFw): qué es la IA y su historia.
- [3Blue1Brown, *Neural Networks*](https://www.youtube.com/watch?v=aircAruvnKk): cómo funciona una red neuronal por dentro.
- [TensorFlow Playground](https://playground.tensorflow.org/): una red neuronal que aprende en el navegador.

**Glosario mínimo**: dato · información · conocimiento · algoritmo · grafo · estado · transición · poda · heurística · función objetivo · gradiente · mínimo local · agente · sensor · actuador · modelo · entrenamiento · época · etiqueta.

---

## 1️⃣ FUNDAMENTOS DE PROGRAMACIÓN

### 1.1 ¿Qué es un Programa?
Un programa es una **secuencia de instrucciones** que la computadora ejecuta en orden para realizar una tarea.

```python
# Instrucción 1: Pedir nombre
nombre = input("¿Cuál es tu nombre? ")

# Instrucción 2: Procesar
mensaje = f"Hola, {nombre}"

# Instrucción 3: Mostrar resultado
print(mensaje)
```

### 1.2 Variables y Asignación
Una **variable** es un contenedor que almacena un valor.

```python
edad = 25           # Variable con valor entero
nombre = "Ana"      # Variable con texto
promedio = 8.5      # Variable con decimal
```

**Reglas de nombres**:
- Deben empezar con letra o guión bajo
- Solo letras, números y guiones bajos
- Mayúsculas/minúsculas importan: `edad` ≠ `Edad`

### 1.3 Tipos de Datos Básicos

| Tipo | Ejemplo | Función | Referencias |
|------|---------|---------|-------------|
| **int** | 25 | Números enteros | [docs.python.org/int](https://docs.python.org/3/library/functions.html#int) |
| **float** | 8.5 | Números decimales | [docs.python.org/float](https://docs.python.org/3/library/functions.html#float) |
| **str** | "texto" | Cadenas de texto | [docs.python.org/str](https://docs.python.org/3/library/stdtypes.html#string-methods) |
| **bool** | True/False | Verdadero/Falso | [docs.python.org/bool](https://docs.python.org/3/library/functions.html#bool) |
| **list** | [1,2,3] | Colecciones ordenadas | [docs.python.org/list](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) |
| **dict** | {a:1} | Pares clave-valor | [docs.python.org/dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) |

**Conversión entre tipos**:
```python
int("25")           # Convierte string a entero: 25
float("8.5")        # Convierte string a decimal: 8.5
str(25)             # Convierte número a string: "25"
bool(1)             # Convierte a booleano: True
```

### 1.4 Operadores Aritméticos

| Operador | Nombre | Ejemplo | Resultado |
|----------|--------|---------|-----------|
| `+` | Suma | 5 + 3 | 8 |
| `-` | Resta | 5 - 3 | 2 |
| `*` | Multiplicación | 5 * 3 | 15 |
| `/` | División | 15 / 3 | 5.0 |
| `//` | División entera | 15 // 4 | 3 |
| `%` | Módulo (resto) | 15 % 4 | 3 |
| `**` | Potencia | 2 ** 3 | 8 |

**Importancia del módulo (%)**:
```python
# Determinar si número es par
numero = 10
if numero % 2 == 0:
    print("Es par")
else:
    print("Es impar")
```

[Referencia oficial: Operadores aritméticos](https://docs.python.org/3/reference/lexical_analysis.html#operators)

### 1.5 Nombres, constantes y más operadores

**Reglas para nombrar variables**: empiezan por letra o `_`; pueden llevar letras, dígitos y `_`; distinguen mayúsculas (`nota` y `Nota` son dos variables distintas) y no pueden ser palabras reservadas (`if`, `for`, `while`, `def`, `class`, `True`, `None`…). Por convenio se escriben en `minusculas_con_guiones_bajos` y con nombres que expliquen qué guardan: `temperatura_media` mejor que `t2`.

**Constantes**: Python no tiene un tipo «constante». Lo que hay es un **convenio**: si el nombre va en MAYÚSCULAS, nadie debería cambiarlo.

```python
IVA = 0.21                 # constante por convenio
NOTA_APROBADO = 5
precio = 40
print(precio * (1 + IVA))  # 48.4
```

**Operadores de asignación compuesta, pertenencia e identidad**:

```python
puntos = 10
puntos += 5        # puntos = puntos + 5  → 15
puntos //= 2       # división entera       → 7
puntos **= 2       # potencia              → 49

concellos = ["Marín", "Bueu", "Cangas"]
print("Bueu" in concellos)        # True  (pertenencia)
print("Vigo" not in concellos)    # True

a = [1, 2]
b = [1, 2]
print(a == b)      # True:  mismo contenido
print(a is b)      # False: son dos objetos distintos en memoria
```

| Operador | Pregunta que responde | Ejemplo |
|----------|-----------------------|---------|
| `==` | ¿Tienen el mismo **valor**? | `[1, 2] == [1, 2]` → `True` |
| `is` | ¿Son el **mismo objeto**? | Se usa casi solo con `None`: `if x is None:` |
| `in` | ¿Está **dentro**? | `"a" in "casa"` → `True` |
| `//`, `%` | Cociente entero y resto | `17 // 5` → `3`, `17 % 5` → `2` |

**Precedencia**: primero `**`, después `*  /  //  %`, después `+  -`, después las comparaciones y al final `not`, `and`, `or`. Ante la duda, paréntesis: `(a + b) * 2`.

---

## 2️⃣ TIPOS DE DATOS EN PYTHON

### 2.1 Strings (Cadenas de Texto)

**Creación**:
```python
# Comillas simples
texto1 = 'Hola'

# Comillas dobles
texto2 = "Mundo"

# Triple comilla (múltiples líneas)
texto3 = """
Línea 1
Línea 2
"""
```

**Métodos importantes**:
```python
texto = "Hola Mundo"

# Conversión
texto.lower()           # "hola mundo"
texto.upper()           # "HOLA MUNDO"
texto.capitalize()      # "Hola mundo"
texto.title()          # "Hola Mundo"

# Búsqueda
texto.find("Mundo")    # 5 (posición)
"Mundo" in texto       # True

# Separación
texto.split()          # ["Hola", "Mundo"]
texto.split(" ")       # ["Hola", "Mundo"]

# Limpieza
"  texto  ".strip()    # "texto"

# Reemplazo
texto.replace("Mundo", "Python")  # "Hola Python"

# Conteo
texto.count("o")       # 2
```

**F-strings (formato moderno)**:
```python
nombre = "Ana"
edad = 25
mensaje = f"Me llamo {nombre} y tengo {edad} años"
# Resultado: "Me llamo Ana y tengo 25 años"
```

[Referencia: Métodos de strings](https://docs.python.org/3/library/stdtypes.html#string-methods)

### 2.2 Números (int y float)

**Diferencias**:
```python
# int: Números exactos, sin decimales
edad = 25

# float: Números con decimales (aproximados)
promedio = 8.5
```

**Cuidado con float**:
```python
# Problema de precisión
0.1 + 0.2 == 0.3  # False! (es 0.30000000000000004)

# Solución
round(0.1 + 0.2, 1) == 0.3  # True
```

[Referencia: Aritmética de punto flotante](https://docs.python.org/3/tutorial/floatingpoint.html)

### 2.3 Booleanos (True/False)

Usados en condicionales:
```python
es_adulto = True
es_alumno = False

# Valores que se consideran False:
False, 0, 0.0, "", [], {}, None

# Todos los demás son True
1, -1, "texto", [1], {"a": 1}
```

### 2.4 Conversión de tipos (*casting*)

`input()` **siempre devuelve un texto**. Para operar con números hay que convertirlo:

```python
edad_txt = "16"
print(edad_txt + "1")          # "161": junta textos
print(int(edad_txt) + 1)       # 17:   suma números

int("42")        # 42
float("3.5")     # 3.5
str(2026)        # "2026"
int(7.9)         # 7  (trunca, no redondea)
round(7.9)       # 8
bool("")         # False (texto vacío)
bool("0")        # True  (¡es un texto con un carácter!)
list("IA")       # ['I', 'A']
```

| Conversión | Funciona | Falla con `ValueError` |
|------------|----------|------------------------|
| `int()` | `int("12")`, `int(" 12 ")`, `int(3.9)` | `int("3.9")`, `int("doce")`, `int("")` |
| `float()` | `float("3.9")`, `float("1e3")` | `float("3,9")` (coma decimal española) |

**Conversión implícita**: al mezclar `int` y `float`, Python pasa a `float` sin avisar (`3 + 0.5` → `3.5`). Entre texto y número **no** convierte: `"3" + 2` da `TypeError`. Para leer números que escribe una persona, se combinan `strip()`, `replace(",", ".")` y `try/except` (14.14).

### 2.5 Entrada, salida y formato

```python
nombre = input("¿Cómo te llamas? ")          # lo que escribe el usuario (texto)
nota = float(input("Nota del examen: "))     # convertido a número

print("Ola", nombre)                         # varios valores: separa con espacio
print("2026", "11", "08", sep="-")           # 2026-11-08
print("Cargando", end="... ")                # no salta de línea
print("listo")                               # Cargando... listo
```

**F-strings con formato**: después de `:` se indica cómo mostrar el valor.

```python
media = 7.4567
alumnado = 1234567
print(f"Media: {media:.2f}")         # Media: 7.46    (2 decimales)
print(f"Aprobados: {0.8125:.1%}")    # Aprobados: 81.2%
print(f"Población: {alumnado:,}")    # Población: 1,234,567
print(f"|{'Marín':<10}|")            # |Marín     |   (alinear a la izquierda)
print(f"|{'Marín':>10}|")            # |     Marín|   (a la derecha)
print(f"|{7:03d}|")                  # |007|          (relleno con ceros)
print(f"{media=}")                   # media=7.4567   (útil para depurar)
```

Con estas marcas se hacen tablas alineadas en la consola, como las de los informes de E15.

### 2.6 Cadenas a fondo: índices, *slicing* e inmutabilidad

Una cadena es una **secuencia de caracteres**: cada uno tiene una posición que empieza en 0, y las posiciones negativas cuentan desde el final.

```python
palabra = "Pontevedra"
#          0123456789
palabra[0]       # 'P'
palabra[-1]      # 'a'
palabra[0:5]     # 'Ponte'   (del 0 al 4: el final no se incluye)
palabra[5:]      # 'vedra'
palabra[::2]     # 'Pneer'   (de dos en dos)
palabra[::-1]    # 'ardevetnoP' (al revés)
len(palabra)     # 10
```

Las cadenas son **inmutables**: `palabra[0] = "p"` da `TypeError`. Los métodos **no cambian** la cadena, **devuelven una nueva** que hay que guardar: `palabra = palabra.lower()`.

**Métodos para comprobar y unir**:

```python
"2026".isdigit()          # True  (solo dígitos)
"Antía".isalpha()         # True  (solo letras, también con tilde)
"ola mundo".isalpha()     # False (el espacio no es letra)
"IES".isupper()           # True
"informe.csv".endswith(".csv")       # True
"https://x.gal".startswith("https")  # True
"-".join(["2026", "11", "08"])       # '2026-11-08'  (lo contrario de split)
"Hola mundo".index("mundo")          # 5  (como find, pero da error si no está)
"Hola mundo".find("Vigo")            # -1
```

**Recorrer una cadena**: `for letra in palabra:` da cada carácter; `for i, letra in enumerate(palabra):` da también la posición. Con `ord("A")` (65) y `chr(65)` ("A") se pasa de carácter a número Unicode y al revés (UD4, sección de texto como números).

---

## 3️⃣ ESTRUCTURAS DE CONTROL

### 3.1 Condicionales (if/elif/else)

**Estructura básica**:
```python
edad = 18

if edad < 13:
    print("Eres niño")
elif edad < 18:
    print("Eres adolescente")
else:
    print("Eres adulto")
```

**Operadores de comparación**:
```python
5 == 5      # Igual: True
5 != 3      # Distinto: True
5 > 3       # Mayor: True
5 >= 5      # Mayor o igual: True
5 < 10      # Menor: True
5 <= 5      # Menor o igual: True
```

**Operadores lógicos**:
```python
edad = 25
tiene_licencia = True

# AND (ambas deben ser True)
if edad >= 18 and tiene_licencia:
    print("Puede conducir")

# OR (al menos una True)
if edad < 13 or edad > 65:
    print("Descuento especial")

# NOT (invierte)
if not tiene_licencia:
    print("Necesita licencia")
```

[Referencia: Control de flujo](https://docs.python.org/3/tutorial/controlflow.html)

### 3.2 Bucles (for y while)

**Bucle for** (número definido de iteraciones):
```python
# Iterar sobre rango
for i in range(1, 5):  # 1, 2, 3, 4
    print(i)

# Iterar sobre lista
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)

# Con índice
for i, fruta in enumerate(frutas):
    print(f"{i}: {fruta}")
```

**Bucle while** (mientras condición sea verdadera):
```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1  # Incrementar: contador = contador + 1
```

**Control de bucles**:
```python
# break: Salir del bucle
for i in range(10):
    if i == 5:
        break  # Sale cuando i es 5

# continue: Saltar a siguiente iteración
for i in range(5):
    if i == 2:
        continue  # Salta i=2
    print(i)  # Imprime 0, 1, 3, 4
```

[Referencia: Bucles](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)

### 3.3 Bucles anidados y programas de patrones

Un bucle dentro de otro: **el exterior recorre las filas y el interior, lo que va en cada fila**. Por cada vuelta del exterior, el interior se ejecuta entero.

```python
# Tabla de multiplicar del 1 al 3
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i*j:3}", end="")
    print()          # salto de línea al acabar cada fila
#   1  2  3
#   2  4  6
#   3  6  9
```

Los **patrones** de asteriscos o números son el ejercicio clásico para entrenar esta idea. El truco es escribir una tabla: fila `i` → cuántos espacios y cuántos símbolos.

```python
n = 4
# Triángulo:  fila i → i asteriscos
for i in range(1, n + 1):
    print("*" * i)

# Pirámide:   fila i → (n - i) espacios y (2i - 1) asteriscos
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# Números:    fila i → 1 2 … i
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Letras:     fila i → la letra i-ésima repetida (chr(65) es 'A')
for i in range(1, n + 1):
    print(chr(64 + i) * i)
```

Salida de la pirámide con `n = 4`:

```text
   *
  ***
 *****
*******
```

En Python, `"*" * i` repite un texto, así que muchos patrones salen con un solo bucle. Los apuntes en inglés de los que parte esta sección usan siempre dos bucles con `print(..., end="")`: los dos caminos son correctos, y conviene saber hacerlo de las dos formas porque en otros lenguajes no existe la multiplicación de textos.

**Coste**: dos bucles anidados de `n` vueltas hacen `n × n` operaciones. Con 1 000 filas ya es un millón. Es la misma razón por la que comparar cada imagen con todas las demás (UD3) o cada palabra con todas (UD4) se vuelve lento muy rápido.

### 3.4 Problemas numéricos clásicos

Casi todos se resuelven con dos herramientas: `n % 10` (la última cifra) y `n // 10` (quitar la última cifra).

```python
def suma_cifras(n):
    n = abs(n)                 # así también funciona con negativos
    total = 0
    while n > 0:
        total += n % 10        # última cifra
        n //= 10               # quitarla
    return total

def invertir(n):
    resultado = 0
    while n > 0:
        resultado = resultado * 10 + n % 10
        n //= 10
    return resultado

def es_capicua(n):             # «palíndromo numérico»
    return n == invertir(n)

def es_armstrong(n):           # suma de cada cifra elevada al número de cifras
    k = len(str(n))
    return n == sum(int(c) ** k for c in str(n))

def es_primo(n):
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5) + 1):   # basta llegar a la raíz cuadrada
        if n % d == 0:
            return False
    return True

print(suma_cifras(2026), invertir(2026), es_capicua(1221))   # 10 6202 True
print([n for n in range(100, 1000) if es_armstrong(n)])      # [153, 370, 371, 407]
print([n for n in range(30) if es_primo(n)])                 # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

| Problema | Idea clave | Cuidado con |
|----------|-----------|-------------|
| Par o impar | `n % 2 == 0` | Nada: funciona también con negativos |
| Primo | Probar divisores hasta √n | 0 y 1 **no** son primos |
| Factorial | Acumular un producto empezando en 1 | `0! = 1` |
| Fibonacci | `a, b = b, a + b` | Empieza en 0, 1 |
| Suma de cifras / invertir | `% 10` y `// 10` | Con negativos, `while n > 0` no entra: usar `abs()` |
| Capicúa | Comparar con el número invertido | `invertir(120)` da `21`: los ceros finales se pierden |
| Año bisiesto | Divisible entre 4 y no entre 100, **o** entre 400 | 1900 no fue bisiesto; 2000 sí |

**`for … else`**: el bloque `else` de un bucle se ejecuta **solo si el bucle no terminó con `break`**. Es otra forma de escribir el test de primo:

```python
n = 91
for d in range(2, n):
    if n % d == 0:
        print(n, "no es primo:", d, "×", n // d)
        break
else:
    print(n, "es primo")
# 91 no es primo: 7 × 13
```

Los apuntes de origen prueban divisores **hasta `n`**: funciona, pero con un número de 12 cifras haría un billón de pruebas en vez de un millón. Pensar cuánto trabajo hace un algoritmo es la idea central de la algoritmia (14.12).

---

## 4️⃣ FUNCIONES

Una función es un **bloque de código reutilizable**.

### 4.1 Definición básica

```python
def saludar():
    print("¡Hola!")

saludar()  # Ejecutar función
```

### 4.2 Funciones con parámetros

```python
def saludar(nombre):
    print(f"¡Hola, {nombre}!")

saludar("Ana")  # Imprime: ¡Hola, Ana!
```

### 4.3 Funciones con return

```python
def suma(a, b):
    resultado = a + b
    return resultado

total = suma(5, 3)
print(total)  # 8
```

### 4.4 Parámetros por defecto

```python
def saludar(nombre, idioma="español"):
    if idioma == "español":
        return f"¡Hola, {nombre}!"
    elif idioma == "inglés":
        return f"Hello, {nombre}!"

saludar("Ana")              # Usa defecto: "¡Hola, Ana!"
saludar("Ana", "inglés")    # "Hello, Ana!"
```

### 4.5 Docstrings

```python
def es_par(numero):
    """
    Determina si un número es par.
    
    Args:
        numero (int): Número a verificar
    
    Returns:
        bool: True si es par, False si es impar
    """
    return numero % 2 == 0

help(es_par)  # Muestra el docstring
```

[Referencia: Funciones](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

### 4.6 Argumentos y valores de retorno

```python
def ficha(nombre, curso="1º BAC", *, centro="IES Chan do Monte"):
    return f"{nombre} · {curso} · {centro}"

ficha("Uxía")                          # posicional + valores por defecto
ficha("Brais", "2º BAC")               # dos posicionales
ficha(curso="2º BAC", nombre="Antía")  # nombrados: el orden da igual
ficha("Xoán", centro="IES de Vigo")    # tras el * solo se admite nombrado
```

**Devolver varios valores**: en realidad se devuelve una **tupla**, que se desempaqueta en varias variables.

```python
def min_max(notas):
    return min(notas), max(notas)

baja, alta = min_max([6.5, 9, 4.25, 7])
print(baja, alta)                      # 4.25 9
```

Una función **sin `return`** devuelve `None`. Error típico: `lista = lista.sort()` deja `lista` en `None`, porque `sort()` ordena en el sitio y no devuelve nada (5.4).

### 4.7 Funciones lambda

Una **lambda** es una función **anónima de una sola expresión**. Devuelve el resultado sin escribir `return`.

```python
doble = lambda x: x * 2          # equivale a: def doble(x): return x * 2
print(doble(21))                 # 42
```

Donde de verdad se usa es **como argumento de otra función**, sobre todo para decir **por qué ordenar**:

```python
alumnado = [("Uxía", 8.5), ("Brais", 6.0), ("Antía", 9.25)]
print(sorted(alumnado, key=lambda a: a[1], reverse=True))
# [('Antía', 9.25), ('Uxía', 8.5), ('Brais', 6.0)]

palabras = ["ría", "Ourense", "mar", "Lugo"]
print(sorted(palabras, key=len))             # ['ría', 'mar', 'Lugo', 'Ourense']
print(max(palabras, key=str.lower))          # 'ría'
```

Si una lambda se guarda en una variable para usarla varias veces (como `doble` arriba), la guía de estilo PEP 8 recomienda **escribir un `def`**: tiene nombre en los mensajes de error y admite docstring. Los apuntes de origen usan `square = lambda x: x * x` como ejemplo básico; sirve para entender la sintaxis, pero no es buena práctica.

### 4.8 `map`, `filter` y `reduce`

Tres herramientas de **programación funcional**: transformar, seleccionar y combinar.

```python
from functools import reduce

temperaturas_c = [12, 18, 25, 31]
print(list(map(lambda c: c * 9 / 5 + 32, temperaturas_c)))   # [53.6, 64.4, 77.0, 87.8]
print(list(filter(lambda c: c >= 20, temperaturas_c)))       # [25, 31]
print(reduce(lambda a, b: a * b, [1, 2, 3, 4]))              # 24

# map con dos listas: empareja elemento a elemento
print(list(map(lambda a, b: a + b, [1, 2, 3], [10, 20, 30])))   # [11, 22, 33]
```

| Herramienta | Qué hace | Equivalente con comprensión (5.6) |
|-------------|----------|-----------------------------------|
| `map(f, datos)` | Aplica `f` a cada elemento | `[f(x) for x in datos]` |
| `filter(f, datos)` | Se queda con los que cumplen `f` | `[x for x in datos if f(x)]` |
| `reduce(f, datos)` | Combina todo en un valor | Muchas veces hay una función hecha: `sum`, `max`, `math.prod` |

Dos detalles: `map` y `filter` devuelven un **iterador** (por eso `list(...)`), que **se gasta** al recorrerlo una vez; y `reduce` vive en `functools`, no es una función integrada. En Python moderno las comprensiones suelen ser más legibles, pero `map` aparece mucho en Pandas (`df["col"].map(...)`) y la idea de «aplicar una función a cada dato» es la misma que en las capas de una red neuronal.

### 4.9 Recursión

Una función **recursiva** se llama a sí misma con un problema **más pequeño**. Necesita dos partes: un **caso base** que para y un **caso recursivo** que se acerca al caso base.

```python
def factorial(n):
    if n == 0:                 # caso base
        return 1
    return n * factorial(n - 1)   # caso recursivo

def cuenta_atras(n):
    if n == 0:
        print("¡Despegue!")
        return
    print(n)
    cuenta_atras(n - 1)

print(factorial(5))            # 120   (5 · 4 · 3 · 2 · 1)
```

Cada llamada queda «apilada» en memoria esperando el resultado de la siguiente. Sin caso base, la pila se llena: Python corta a unas 1 000 llamadas con `RecursionError`. Fibonacci recursivo es elegante pero **lentísimo** (`fib(35)` repite millones de cálculos); la solución con memoria, `@lru_cache`, está en 14.12, igual que las Torres de Hanói.

| Recursión | Iteración (bucles) |
|-----------|--------------------|
| Código corto cuando el problema es recursivo (árboles, carpetas, búsqueda en grafos de 0.7) | Más rápida y con menos memoria |
| Riesgo de `RecursionError` | Riesgo de bucle infinito si no cambia la condición |

### 4.10 Ámbito de las variables (regla LEGB)

El **ámbito** es la zona del programa donde se puede usar un nombre. Python busca cada nombre en este orden y se queda con el primero que encuentra:

| Letra | Ámbito | Dónde |
|-------|--------|-------|
| **L** | Local | Dentro de la función que se ejecuta |
| **E** | *Enclosing* (envolvente) | En la función que contiene a la actual |
| **G** | Global | Fuera de todas las funciones, en el archivo |
| **B** | *Built-in* | Nombres de Python: `print`, `len`, `sum`… |

```python
mensaje = "global"

def exterior():
    mensaje = "envolvente"
    def interior():
        print(mensaje)         # no hay local → usa el envolvente
    interior()

exterior()                     # envolvente
print(mensaje)                 # global: la función no la cambió

contador = 0
def sumar_visita():
    global contador            # sin esta línea: UnboundLocalError
    contador += 1

sumar_visita(); sumar_visita()
print(contador)                # 2
```

`nonlocal` hace lo mismo que `global` pero con la variable de la función envolvente. **Consejo**: casi siempre es mejor **pasar datos como parámetros y devolverlos con `return`** que modificar globales; el código se entiende y se prueba mejor (14.14). Otro error de ámbito muy común: llamar `sum = 0` o `list = [...]` a una variable **tapa** la función integrada, y después `sum(notas)` falla.

---

## 5️⃣ ESTRUCTURAS DE DATOS COMPLEJAS

### 5.1 Listas

**Creación**:
```python
numeros = [1, 2, 3, 4, 5]
mixto = [1, "texto", 3.14, True]
vacía = []
```

**Acceso**:
```python
numeros = [10, 20, 30, 40, 50]

numeros[0]      # Primer elemento: 10
numeros[-1]     # Último elemento: 50
numeros[1:3]    # Slice (elementos 1 a 2): [20, 30]
numeros[:2]     # Primeros 2: [10, 20]
numeros[2:]     # Desde elemento 2: [30, 40, 50]
```

**Métodos**:
```python
numeros = [1, 2, 3]

numeros.append(4)           # Añade al final: [1,2,3,4]
numeros.insert(1, 1.5)      # Inserta en posición: [1,1.5,2,3,4]
numeros.remove(2)           # Quita elemento: [1,1.5,3,4]
numeros.pop()               # Quita último y devuelve
numeros.index(3)            # Posición de 3: 2
numeros.sort()              # Ordena la lista
numeros.reverse()           # Invierte la lista
len(numeros)                # Largo: cantidad de elementos
```

**Comprensión de listas**:
```python
# Forma tradicional
pares = []
for i in range(10):
    if i % 2 == 0:
        pares.append(i)

# Forma moderna (comprensión)
pares = [i for i in range(10) if i % 2 == 0]
# Resultado: [0, 2, 4, 6, 8]
```

[Referencia: Listas](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

### 5.2 Diccionarios

**Creación**:
```python
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Madrid"
}
```

**Acceso**:
```python
persona["nombre"]           # "Ana"
persona.get("nombre")       # "Ana" (más seguro)
persona.get("teléfono")     # None (no error)
```

**Métodos**:
```python
diccionario = {"a": 1, "b": 2}

diccionario["c"] = 3        # Añadir clave-valor
diccionario.keys()          # Todas las claves
diccionario.values()        # Todos los valores
diccionario.items()         # Pares (clave, valor)
diccionario.update({"d": 4})  # Mezclar dicts
```

**Iteración**:
```python
persona = {"nombre": "Ana", "edad": 25}

# Iterar sobre claves
for clave in persona:
    print(clave)

# Iterar sobre pares
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
```

[Referencia: Diccionarios](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

### 5.3 Tuplas

Listas **inmutables** (no se pueden cambiar):
```python
coordenadas = (10, 20)
coordenadas[0]          # 10
coordenadas[0] = 15     # ERROR! No se puede

# Útil para retornar múltiples valores
def obtener_coordenadas():
    return (10, 20)

x, y = obtener_coordenadas()
```

### 5.4 Listas a fondo: más métodos, copias y alias

```python
notas = [7, 4.5, 9, 6]
notas.extend([8, 5])         # añade varios: [7, 4.5, 9, 6, 8, 5]
notas.count(9)               # cuántas veces aparece: 1
ordenada = sorted(notas)     # devuelve una lista NUEVA ordenada
notas.sort(reverse=True)     # ordena la MISMA lista (no devuelve nada)
ultima = notas.pop()         # quita y devuelve la última: 4.5
del notas[0]                 # borra por posición
notas.clear()                # vacía la lista
```

| `append(x)` | `extend(lista)` | `insert(i, x)` |
|-------------|-----------------|----------------|
| Añade **un** elemento al final (si es una lista, entra como sublista) | Añade **cada** elemento | Añade en la posición `i` |

**Alias frente a copia**: `b = a` **no copia** la lista, le pone otro nombre. Lo que cambie por un lado se ve por el otro.

```python
a = [1, 2, 3]
b = a            # alias: el mismo objeto
c = a.copy()     # copia (también a[:] o list(a))
a.append(4)
print(b)         # [1, 2, 3, 4]
print(c)         # [1, 2, 3]
```

Con listas de listas, `copy()` solo copia el primer nivel; para copiarlo todo, `copy.deepcopy()`. El mismo problema aparece en Pandas: `df2 = df` es un alias y `df2 = df.copy()` una copia.

### 5.5 Conjuntos (`set`)

Un **conjunto** guarda elementos **sin repetir y sin orden**. No tiene posiciones (`s[0]` da error).

```python
visitas = ["Vigo", "Marín", "Vigo", "Lugo", "Marín"]
unicas = set(visitas)              # {'Vigo', 'Marín', 'Lugo'} (en cualquier orden)
print(len(unicas))                 # 3 ciudades distintas
vacio = set()                      # ¡{} crea un diccionario vacío, no un conjunto!

unicas.add("Ourense")
unicas.discard("Cádiz")            # no da error si no está (remove sí lo daría)

ingles = {"Uxía", "Brais", "Antía"}
frances = {"Brais", "Xoán"}
print(ingles | frances)            # unión: los 4
print(ingles & frances)            # intersección: {'Brais'}
print(ingles - frances)            # diferencia: {'Uxía', 'Antía'}
print(ingles ^ frances)            # diferencia simétrica: en uno solo
```

Usos en IA y datos: **quitar duplicados**, saber el **vocabulario** de un texto (`set(texto.split())`, UD4), comparar etiquetas de dos clasificadores y comprobar pertenencia muy rápido (`"Vigo" in unicas` no recorre nada: usa *hashing*, 14.9). Para quitar duplicados **conservando el orden**: `list(dict.fromkeys(visitas))`.

| | Lista | Tupla | Conjunto | Diccionario |
|-|-------|-------|----------|-------------|
| Sintaxis | `[1, 2]` | `(1, 2)` | `{1, 2}` | `{"a": 1}` |
| Orden y posición | Sí | Sí | No | Por clave (mantiene orden de inserción) |
| Repetidos | Sí | Sí | No | Claves no |
| Se puede modificar | Sí | No | Sí | Sí |
| Típico para | Secuencias de datos | Registros fijos, coordenadas | Únicos, pertenencia | Buscar por nombre |

### 5.6 Comprensiones de listas, diccionarios y conjuntos

Una **comprensión** construye una colección en una línea: `[expresión for elemento in datos if condición]`.

```python
notas = {"Uxía": 8.5, "Brais": 4.0, "Antía": 9.25, "Xoán": 4.75}

cuadrados = [x ** 2 for x in range(1, 6)]                    # [1, 4, 9, 16, 25]
aprobados = [n for n, x in notas.items() if x >= 5]          # ['Uxía', 'Antía']
calificacion = ["apto" if x >= 5 else "no apto" for x in notas.values()]
# ['apto', 'no apto', 'apto', 'no apto']

redondeadas = {n: round(x) for n, x in notas.items()}        # diccionario
# {'Uxía': 8, 'Brais': 4, 'Antía': 9, 'Xoán': 5}
largos = {len(n) for n in notas}                             # conjunto: {4, 5}

tabla = [[i * j for j in range(1, 4)] for i in range(1, 4)]  # anidada
# [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

Fíjate en las dos posiciones del `if`: **al final filtra** (deja menos elementos); **delante del `for`, con `else`, transforma** (deja todos, con un valor u otro). `round(8.5)` da 8 y `round(4.75)` da 5: Python redondea los empates al **par** más cercano (*redondeo del banquero*), algo que sorprende cuando se pasan notas.

Si la comprensión no cabe en una línea o tiene varios `if`, es mejor un bucle normal: la legibilidad manda (14.14).

### 5.7 Funciones integradas y módulos útiles

**Integradas** (no hay que importar nada):

```python
datos = [7, 3, 9, 3]
len(datos), sum(datos), min(datos), max(datos)    # (4, 22, 3, 9)
sorted(datos), list(reversed(datos))              # ([3, 3, 7, 9], [3, 9, 3, 7])
abs(-4), round(3.14159, 2), pow(2, 10)            # (4, 3.14, 1024)
type(3.5), isinstance(3.5, float)                 # (<class 'float'>, True)
list(range(0, 10, 3))                             # [0, 3, 6, 9]
list(zip(["a", "b"], [1, 2]))                     # [('a', 1), ('b', 2)]
any(x > 8 for x in datos), all(x > 0 for x in datos)   # (True, True)
```

`help(función)` y `dir(objeto)` explican qué hace algo y qué métodos tiene, sin salir del cuaderno.

**Módulos de la biblioteca estándar**: vienen con Python, pero hay que importarlos.

```python
import math, random, statistics
from collections import Counter
from datetime import date

math.sqrt(16), math.pi, math.ceil(4.1), math.floor(4.9)   # (4.0, 3.14159..., 5, 4)
random.seed(1)                       # misma «suerte» siempre: resultados reproducibles
random.randint(1, 6)                 # un dado
random.choice(["piedra", "papel", "tijera"])
statistics.mean([7, 3, 9, 3]), statistics.median([7, 3, 9, 3])   # (5.5, 5.0)
Counter("abracadabra").most_common(2)                    # [('a', 5), ('b', 2)]
(date(2027, 6, 23) - date(2026, 11, 8)).days             # días que faltan para San Xoán
```

| Forma | Ejemplo | Cuándo |
|-------|---------|--------|
| `import math` | `math.sqrt(2)` | Lo normal: se ve de dónde viene cada función |
| `from math import sqrt` | `sqrt(2)` | Una o dos funciones que se usan mucho |
| `import numpy as np` | `np.array(...)` | Alias que usa todo el mundo: `np`, `pd`, `plt` |
| `from math import *` | — | **Evitar**: no se sabe qué nombres entran y pueden tapar otros |

Un **módulo** es un archivo `.py`; un **paquete** es una carpeta de módulos; una **librería** como NumPy o Pandas (sección 7) es un paquete que se instala con `pip` (en Colab ya vienen casi todas). `random.seed()` es la misma idea que `random_state=42` en scikit-learn (UD5): fijar la semilla para que otra persona obtenga los mismos resultados.

### 5.8 Chuleta de repaso de Python básico

| Tema | Lo esencial | Error típico |
|------|-------------|--------------|
| Tipos | `int`, `float`, `str`, `bool`, `None` | `input()` devuelve texto: convertir con `int()` / `float()` |
| Cadenas | Índices desde 0, `[inicio:fin:paso]`, inmutables | Olvidar guardar el resultado: `s.upper()` sola no cambia `s` |
| Condicionales | `if` / `elif` / `else`, `and`, `or`, `not` | `=` (asignar) en lugar de `==` (comparar) |
| Bucles | `for x in datos`, `range(ini, fin, paso)`, `while`, `break`, `continue` | `range(1, 10)` no incluye el 10 |
| Listas | `append`, `extend`, `sort`, `sorted`, *slicing* | `b = a` no copia; `lista = lista.sort()` da `None` |
| Tuplas | Inmutables; `(5,)` con una sola coma | `(5)` es un número, no una tupla |
| Conjuntos | Únicos, sin orden, `| & - ^` | `{}` es un diccionario vacío |
| Diccionarios | `d[clave]`, `d.get(clave, defecto)`, `.items()` | `d[clave]` con clave inexistente da `KeyError` |
| Funciones | `def`, parámetros, `return`, valores por defecto | Sin `return` devuelve `None` |
| Lambda y funcional | `sorted(datos, key=lambda x: ...)`, `map`, `filter` | `map` es un iterador: se gasta tras recorrerlo |
| Ámbito | Regla LEGB, `global`, `nonlocal` | Llamar `sum` o `list` a una variable |
| Recursión | Caso base + caso recursivo | Olvidar el caso base → `RecursionError` |
| Módulos | `import`, `from … import`, alias | `from x import *` |

Para practicar todo esto hay un bloque de ejercicios (E28–E37) en la página de [ejercicios](ejercicios.html#bloque-f--más-práctica-de-python-básico-e28e37).

---

## 6️⃣ CONCEPTOS ESTADÍSTICOS BÁSICOS

### 6.1 Media (Promedio)
```
Media = (suma de todos los valores) / (cantidad de valores)

Datos: [10, 20, 30]
Media = (10 + 20 + 30) / 3 = 60 / 3 = 20
```

**En Python**:
```python
datos = [10, 20, 30]
media = sum(datos) / len(datos)  # 20
```

### 6.2 Mediana (Valor Central)
```
Pasos:
1. Ordenar datos
2. Si cantidad es impar: elemento del medio
3. Si cantidad es par: promedio de dos elementos centrales

Datos: [10, 20, 30] → Mediana = 20
Datos: [10, 20, 30, 40] → Mediana = (20+30)/2 = 25
```

### 6.3 Moda (Valor Más Frecuente)
```
Moda = elemento que aparece más veces

Datos: [1, 1, 1, 2, 3, 3, 4]
Moda = 1 (aparece 3 veces)
```

**En Python**:
```python
from collections import Counter

datos = [1, 1, 1, 2, 3, 3]
frecuencias = Counter(datos)
moda = frecuencias.most_common(1)[0][0]  # 1
```

### 6.4 Desviación Estándar
Mide **cuánto varían** los datos respecto a la media.

```
σ = √(promedio de (cada valor - media)²)

Datos con poca variación: σ pequeña
Datos con mucha variación: σ grande
```

[Referencia: Estadística](https://es.wikipedia.org/wiki/Estad%C3%ADstica_descriptiva)

---

## 7️⃣ LIBRERÍAS CIENTÍFICAS

### 7.1 NumPy (Computación Numérica)

**¿Por qué NumPy?**
```
Lista Python:  0.5 segundos (lento, intérprete)
NumPy array:   0.0005 segundos (rápido, C compilado)
Aceleración:   1000x
```

**Instalación**:
```bash
pip install numpy
```

**Crear arrays**:
```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
arr2d = np.array([[1, 2], [3, 4]])
zeros = np.zeros(5)              # [0, 0, 0, 0, 0]
ones = np.ones(3)                # [1, 1, 1]
rango = np.arange(0, 10, 2)     # [0, 2, 4, 6, 8]
```

**Operaciones vectorizadas** (sin bucles):
```python
arr = np.array([1, 2, 3, 4])

arr * 2              # [2, 4, 6, 8]
arr ** 2             # [1, 4, 9, 16]
np.sqrt(arr)         # [1, 1.41, 1.73, 2]

# Funciones de reducción
np.mean(arr)         # 2.5
np.sum(arr)          # 10
np.max(arr)          # 4
np.min(arr)          # 1
np.std(arr)          # Desviación estándar
```

**Matrices**:
```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

np.dot(A, B)         # Multiplicación matricial
A.T                  # Transposición
```

[Referencia: NumPy documentation](https://numpy.org/doc/stable/)

### 7.2 Pandas (Manipulación de Datos)

**¿Por qué Pandas?**
```
10 líneas de código Python
1 línea de código Pandas
→ Más legible, más rápido, menos errores
```

**Instalación**:
```bash
pip install pandas
```

**Crear DataFrame**:
```python
import pandas as pd

# Desde diccionario
df = pd.DataFrame({
    "nombre": ["Ana", "Bruno", "Carlos"],
    "edad": [25, 30, 28],
    "ciudad": ["Madrid", "Barcelona", "Valencia"]
})

# Desde CSV
df = pd.read_csv("datos.csv")

# Desde JSON
df = pd.read_json("datos.json")
```

**Exploración**:
```python
df.shape                # (3, 3) - filas, columnas
df.dtypes              # Ver tipos de columnas
df.info()              # Información completa
df.describe()          # Estadísticas
```

**Selección de datos**:
```python
df['nombre']                    # Una columna
df[['nombre', 'edad']]         # Varias columnas
df.loc[0]                       # Primera fila
df[df['edad'] > 25]            # Filtrado
```

**Operaciones**:
```python
df['edad'].mean()              # Media
df['edad'].sum()               # Suma
df.sort_values('edad')         # Ordenar
df.groupby('ciudad')['edad'].mean()  # Agrupar
```

**Limpieza**:
```python
df.isnull().sum()              # Contar NaN
df = df.dropna()               # Eliminar NaN
df = df.drop_duplicates()      # Eliminar duplicados
df['edad'] = df['edad'].astype(int)  # Cambiar tipo
```

[Referencia: Pandas documentation](https://pandas.pydata.org/docs/)

---

## 8️⃣ VISUALIZACIÓN CON MATPLOTLIB

**Instalación**:
```bash
pip install matplotlib
```

**Gráfico básico**:
```python
import matplotlib.pyplot as plt

meses = ["Enero", "Febrero", "Marzo"]
ventas = [1000, 1500, 1200]

# Gráfico de línea
plt.plot(meses, ventas, marker='o')
plt.title("Ventas por mes")
plt.xlabel("Mes")
plt.ylabel("Ventas ($)")
plt.show()

# Gráfico de barras
plt.bar(meses, ventas)
plt.title("Ventas por mes")
plt.show()
```

**Personalizaciones**:
```python
plt.figure(figsize=(10, 6))    # Tamaño
plt.plot(meses, ventas, 
         color='blue',          # Color
         marker='o',            # Punto
         linewidth=2,           # Grosor
         label='Ventas')       # Leyenda
plt.legend()                     # Mostrar leyenda
plt.grid(True)                   # Cuadrícula
plt.savefig('grafico.png')      # Guardar
```

[Referencia: Matplotlib documentation](https://matplotlib.org/stable/contents.html)

---

## 9️⃣ CONCEPTOS ETL Y ANÁLISIS DE DATOS

### 9.1 ETL (Extract - Transform - Load)

**EXTRACT** (Extraer):
- Leer datos de CSV, JSON, APIs, bases de datos
```python
df = pd.read_csv("datos.csv")
```

**TRANSFORM** (Transformar):
- Limpiar, validar, enriquecer, normalizar
```python
# Limpiar
df = df.dropna()

# Validar
df = df[df['edad'] > 0]

# Enriquecer
df['año_nacimiento'] = 2024 - df['edad']

# Normalizar
from sklearn.preprocessing import StandardScaler
df[['edad', 'salario']] = StandardScaler().fit_transform(df[['edad', 'salario']])
```

**LOAD** (Cargar):
- Guardar en formato final
```python
df.to_csv("datos_procesados.csv", index=False)
df.to_json("datos.json")
```

### 9.2 EDA (Exploratory Data Analysis)

Pasos:
1. **Cargar datos**: `pd.read_csv()`
2. **Información**: `df.shape`, `df.dtypes`, `df.info()`
3. **Estadísticas**: `df.describe()`
4. **Faltantes**: `df.isnull().sum()`
5. **Distribuciones**: `df.hist()`, `df.boxplot()`
6. **Correlaciones**: `df.corr()`
7. **Visualizar**: `plt.plot()`, `df.plot()`

### 9.3 Normalización y Escalado

**¿Por qué escalar?**
```
Edad: 0-100
Salario: 0-1000000

Sin escalar: Salario domina totalmente
Con escalar: Ambos contribuyen equitativamente
```

**StandardScaler** (media=0, desv.std=1):
```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
datos_escalados = scaler.fit_transform(datos)
```

**MinMaxScaler** (rango 0-1):
```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
datos_escalados = scaler.fit_transform(datos)
```

---

## 🔟 INTRODUCCIÓN A MACHINE LEARNING

### 10.1 ¿Qué es Machine Learning?

**Machine Learning** es la capacidad de las máquinas de **aprender de los datos sin ser programadas explícitamente**.

**Tres tipos principales**:

1. **Aprendizaje Supervisado** (Datos etiquetados)
   - Tenemos ejemplos CON respuestas correctas
   - La máquina aprende a predecir
   - Ejemplos: clasificación, regresión
   - **En UD5**: Regresión lineal, clasificación con scikit-learn

2. **Aprendizaje No Supervisado** (Datos SIN etiquetas)
   - Encontrar patrones sin respuestas conocidas
   - Ejemplos: clustering, reducción dimensional
   - **En UD4 y UD5**: Análisis de imágenes, agrupación de datos

3. **Refuerzo** (Aprender por interacción)
   - La máquina aprende por prueba-error
   - Recibe recompensas/castigos
   - Ejemplos: juegos, robots

### 10.2 Datos → Aprendizaje → Predicción

```
Fase 1: DATOS (UD2 - Aquí estamos)
  ├─ Recopilar
  ├─ Limpiar (ETL)
  ├─ Explorar (EDA)
  └─ Preparar (Normalización)

Fase 2: APRENDIZAJE (UD5 - Siguiente unidad)
  ├─ Dividir: Entrenamiento / Prueba
  ├─ Entrenar: Modelo aprende patrones
  ├─ Evaluar: ¿Qué tan bien predice?
  └─ Optimizar: Ajustar parámetros

Fase 3: PREDICCIÓN (UD5)
  └─ Usar modelo para datos nuevos
```

### 10.3 Ejemplo Básico: Predicción de Precios

```python
# DATOS (UD2)
import pandas as pd
df = pd.read_csv("casas.csv")  # tamaño, precio, localización...
df_limpio = df.dropna()
df_normalizado = (df - df.mean()) / df.std()

# APRENDIZAJE (UD5)
from sklearn.linear_model import LinearRegression
X = df_normalizado[['tamaño', 'habitaciones']]  # características
y = df_normalizado['precio']  # objetivo

modelo = LinearRegression()
modelo.fit(X, y)  # El modelo APRENDE

# PREDICCIÓN (UD5)
nueva_casa = [[100, 3]]  # tamaño=100, habitaciones=3
precio_predicho = modelo.predict(nueva_casa)
print(f"Precio estimado: ${precio_predicho[0]}")
```

### 10.4 Conceptos Clave para UD5

**Antes de UD5, debes dominar en UD2**:
- ✅ NumPy: operaciones matriciales, álgebra lineal
- ✅ Pandas: preparación de datos, filtrado
- ✅ Estadística: media, desviación estándar, correlación
- ✅ Normalización: escalar datos al rango 0-1 o media=0
- ✅ Conceptos EDA: explorar distribuciones, outliers

**En UD5 aprenderás**:
- 🔄 Train/Test Split: dividir datos
- 🎯 Algoritmos supervisados: regresión, clasificación
- 📊 Métricas: accuracy, precision, recall, RMSE
- 🧠 Redes Neuronales: si tiempo lo permite
- 🔗 Pipelines completos: datos → predicciones

[Referencia: scikit-learn tutorial](https://scikit-learn.org/stable/getting_started.html)

### 10.5 Conexión UD2 → UD5

```
UD2 EJERCICIOS                UD5 APLICACIÓN
E1-E12: Fundamentos     →     Sintaxis necesaria
E13-E17: Datos complejos →    Preparación ETL
E18-E19: NumPy          →     Operaciones matriciales
E20-E22: Pandas         →     DataFrames en ML
E23-E24: Matplotlib     →     Visualizar modelos
E25-E27: ETL+EDA        →     Pipeline completo
                        ↓
                  UD5: ML Avanzado
                  - Regresión lineal
                  - Clasificación
                  - Validación cruzada
                  - Ajuste de hiperparámetros
```

---

## 1️⃣1️⃣ INTRODUCCIÓN A BIG DATA

### 11.1 ¿Qué es Big Data?

**Big Data** se refiere a conjuntos de datos **tan grandes o complejos** que herramientas convencionales no pueden procesarlos eficientemente.

**Las "5 V" del Big Data**:
1. **Volumen**: Gigabytes, Terabytes, Petabytes (millones de filas)
2. **Velocidad**: Datos en tiempo real, streaming
3. **Variedad**: Datos de múltiples fuentes y formatos
4. **Veracidad**: Calidad y exactitud de datos
5. **Valor**: Extraer insight significativo

### 11.2 Herramientas y Tecnologías

| Herramienta | Uso | Conexión con Curso |
|-------------|-----|-------------------|
| **Hadoop** | Procesamiento distribuido | UD2: Procesamiento en paralelo |
| **Spark** | Procesamiento rápido | UD2: NumPy y Pandas a escala |
| **SQL/Bases de datos** | Consultas grandes | UD2: ETL y consultas |
| **NoSQL** | Datos no estructurados | UD2: Archivos JSON, flexibilidad |
| **Apache Kafka** | Streaming de datos | UD2: Datos en tiempo real |

### 11.3 Big Data y Python

**Herramientas Python para Big Data**:

```python
# PySpark: Pandas pero para millones de filas
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ejemplo").getOrCreate()
df_grande = spark.read.csv("datos_masivos.csv", header=True)
df_grande.filter(df_grande.edad > 25).show()

# Dask: Pandas paralelo en múltiples núcleos
import dask.dataframe as dd

df = dd.read_csv("datos_*.csv")
resultado = df.groupby('ciudad')['salario'].mean().compute()
```

### 11.4 Flujo de Trabajo con Big Data

```
1. CAPTURA (Fuentes diversas)
   ├─ APIs en tiempo real
   ├─ IoT sensores
   ├─ Redes sociales
   └─ Bases de datos empresariales

2. ALMACENAMIENTO (UD2 conexión)
   ├─ Data Lakes (almacén centralizado)
   ├─ Data Warehouses (datos procesados)
   └─ Cloud Storage (AWS S3, Google Cloud)

3. PROCESAMIENTO (UD2: Donde estamos)
   ├─ ETL (Extracción, transformación, carga)
   ├─ Limpieza y validación
   └─ Análisis exploratorio

4. ANÁLISIS (UD2 + UD5)
   ├─ Estadísticas descriptivas
   ├─ Machine Learning
   └─ Deep Learning con imágenes (UD4)

5. VISUALIZACIÓN (UD2: Matplotlib)
   ├─ Dashboards
   ├─ Gráficos interactivos
   └─ Reportes automatizados
```

### 11.5 Big Data en Contexto del Curso

**UD2 (Aquí)**:
- Aprende principios de procesamiento de datos
- NumPy, Pandas, Matplotlib: base para herramientas Big Data
- ETL: el proceso fundamental en Big Data
- EDA: exploración es crítica con datos masivos

**UD3 (Lenguaje Natural)**:
- NLP con Big Data: procesar millones de textos
- Análisis de sentimientos a escala
- Tokenización, vectorización (análogo a normalización UD2)

**UD4 (Visión Artificial)**:
- Imágenes = datos estructurados enormes
- Procesamiento en paralelo (similar a Big Data)
- CNNs: redes neuronales para volúmenes masivos

**UD5 (Machine Learning)**:
- ML requiere Big Data para modelos precisos
- Validación cruzada con 100K+ muestras
- Escalabilidad: de 1,000 a 1,000,000 filas

### 11.6 Ejercicios UD2 como Preparación

```
Habilidades UD2 → Aplicables a Big Data

E25: ETL básico              → Pipelines empresariales
E26: EDA básico              → Exploración de petabytes
E27: Normalización           → Preprocesamiento distribuido
E23-E24: Visualización       → Dashboards interactivos
E18-E19: NumPy vectorizado   → Spark RDDs, Dask particiones
E20-E22: Pandas agrupación   → Distributed groupby
```

**Próximos pasos después de UD2**:
- 📊 UD3: Aplicar ETL a millones de textos (NLP)
- 🖼️ UD4: Procesar datasets de imágenes masivos
- 🧠 UD5: Entrenar modelos ML con Big Data
- ☁️ Futuro: Cloud (AWS, Google Cloud, Azure)

[Referencia: Apache Spark documentation](https://spark.apache.org/docs/latest/)
[Referencia: Dask documentation](https://dask.org/)

---

## 1️⃣2️⃣ ECOSISTEMA DE LIBRERÍAS: PYTORCH, SCIKIT-LEARN Y SEABORN

### 12.1 Mapa general: cada librería tiene su función

Antes de comparar librerías conviene saber **qué problema resuelve cada una**. No todas compiten entre sí: muchas se usan juntas en el mismo proyecto.

| Librería | Función principal | Pregunta que responde | Unidad |
|----------|-------------------|------------------------|--------|
| **NumPy** | Cálculo numérico con arrays | ¿Cómo opero con muchos números a la vez? | UD2 |
| **Pandas** | Tablas de datos (DataFrames) | ¿Cómo cargo, limpio y organizo los datos? | UD2 |
| **Matplotlib** | Gráficos básicos y personalizables | ¿Cómo dibujo mis datos? | UD2 |
| **Seaborn** | Gráficos estadísticos rápidos y vistosos | ¿Qué patrones esconden mis datos? | UD2 |
| **scikit-learn** | Machine Learning clásico | ¿Cómo entreno un modelo que prediga? | UD2 (intro) → UD3, UD5 |
| **PyTorch** | Deep Learning (redes neuronales) | ¿Cómo entreno una red neuronal profunda? | UD2 (conocer) → UD4, UD5 |
| **TensorFlow/Keras** | Deep Learning (alternativa a PyTorch) | La misma que PyTorch | UD4, UD5 |

**El flujo típico de un proyecto de IA**:

```
 DATOS            EXPLORAR           MODELO CLÁSICO       MODELO PROFUNDO
 NumPy  ─────►   Matplotlib  ─────►  scikit-learn  ─────►  PyTorch / Keras
 Pandas          Seaborn             (tablas, pocos       (imágenes, texto,
                                      datos)               audio, muchos datos)
```

---

### 12.2 ¿Dónde encaja PyTorch?

**¿Qué es PyTorch?**
- Librería de **Deep Learning** (aprendizaje profundo) creada por Meta AI, hoy gestionada por la PyTorch Foundation
- Permite construir y entrenar **redes neuronales**
- Muy usada en investigación y en modelos actuales (muchos modelos de lenguaje y de visión están hechos con PyTorch)
- Su objeto básico es el **tensor**: un array como los de NumPy, pero que puede calcularse en la GPU y "recuerda" las operaciones para poder aprender (cálculo automático de gradientes)

**Relación con lo que ya sabes**:

```python
import numpy as np
import torch

# NumPy (UD2)
a = np.array([1.0, 2.0, 3.0])
print(a * 2)              # [2. 4. 6.]

# PyTorch: casi idéntico
t = torch.tensor([1.0, 2.0, 3.0])
print(t * 2)              # tensor([2., 4., 6.])

# Se puede pasar de uno a otro
t2 = torch.from_numpy(a)
a2 = t.numpy()
```

**Por eso NumPy es la base**: quien domina los arrays de NumPy (E18-E19) entiende los tensores de PyTorch casi sin esfuerzo.

**Ubicación en el curso**:

| Unidad | Qué se hace con PyTorch | Nivel |
|--------|--------------------------|-------|
| **UD2** (sesiones de librerías, laboratorio de introducción a ML) | Conocer qué es, para qué sirve y ver un ejemplo con tensores. El currículo LOMLOE cita PyTorch entre las librerías de UD2 (criterio CA1.2: *coñecer as bibliotecas polas súas funcionalidades*) | Conocer |
| **UD4 Visión Artificial** (sesiones 10-15: CNN y Transfer Learning) | Alternativa a TensorFlow/Keras para entrenar redes convolucionales. `torchvision` ofrece datasets (MNIST, CIFAR-10) y modelos preentrenados (ResNet, MobileNet) | Aplicar |
| **UD5 Machine Learning** (bloque de redes neuronales) | Construir una red neuronal sencilla y compararla con los modelos de scikit-learn | Aplicar |
| **UD3 Lenguaje Natural** | Solo como referencia: los modelos de lenguaje modernos (Hugging Face Transformers) funcionan sobre PyTorch | Conocer |

**Ejemplo mínimo de red neuronal (para UD5)**:

```python
import torch
import torch.nn as nn

# Red con 4 entradas (medidas de una flor), 16 neuronas ocultas y 3 salidas (especies)
modelo = nn.Sequential(
    nn.Linear(4, 16),
    nn.ReLU(),
    nn.Linear(16, 3)
)

funcion_error = nn.CrossEntropyLoss()
optimizador = torch.optim.Adam(modelo.parameters(), lr=0.01)

# Bucle de entrenamiento (X_train: tensor float, y_train: tensor de enteros)
for epoca in range(100):
    prediccion = modelo(X_train)              # 1. Predecir
    error = funcion_error(prediccion, y_train) # 2. Medir el error
    optimizador.zero_grad()
    error.backward()                           # 3. Calcular cómo corregir
    optimizador.step()                         # 4. Ajustar los pesos
```

Fíjate en que el bucle de entrenamiento es un **bucle `for` normal** (E6): los fundamentos de UD2 siguen siendo la base.

**PyTorch frente a TensorFlow/Keras**:

| Aspecto | PyTorch | TensorFlow/Keras |
|---------|---------|-------------------|
| Estilo | Python "puro", se ve cada paso del entrenamiento | Más automático (`model.fit()`), parecido a scikit-learn |
| Curva de aprendizaje | Algo más exigente al principio | Más sencilla para empezar |
| Uso actual | Dominante en investigación y modelos recientes | Muy extendido en industria y en material educativo |
| En este curso | Alternativa / ampliación en UD4-UD5 | Herramienta principal prevista en UD4 |

**Recomendación didáctica**: en Bachillerato basta con usar **una** de las dos en profundidad. Keras es más fácil para el primer contacto con CNN (UD4). PyTorch es una buena ampliación para el alumnado más avanzado, o si se quieren usar modelos de Hugging Face.

**Instalación**:
```bash
# Versión solo CPU (suficiente para el aula)
pip install torch torchvision
# Instrucciones según sistema: https://pytorch.org/get-started/locally/
```

⚠️ PyTorch ocupa bastante (cientos de MB). En el aula suele ser más práctico usar **Google Colab**, que ya lo trae instalado.

[Referencia: Tutoriales oficiales de PyTorch](https://pytorch.org/tutorials/)
[Referencia: Learn the Basics (PyTorch)](https://pytorch.org/tutorials/beginner/basics/intro.html)

---

### 12.3 scikit-learn frente a Seaborn

**Idea clave**: **no son alternativas**. Hacen cosas distintas y se usan **juntas**:

- **Seaborn** sirve para **VER** los datos (visualización estadística)
- **scikit-learn** sirve para **APRENDER** de los datos (modelos de Machine Learning)

Una comparación más justa sería *Seaborn frente a Matplotlib* (las dos dibujan) o *scikit-learn frente a PyTorch* (las dos entrenan modelos). Las dos comparaciones aparecen más abajo.

#### Comparación directa

| Aspecto | Seaborn | scikit-learn |
|---------|---------|--------------|
| **Para qué sirve** | Visualizar datos y relaciones estadísticas | Entrenar, evaluar y usar modelos de ML |
| **Qué produce** | Gráficos (imágenes) | Modelos, predicciones y métricas |
| **Fase del proyecto** | Exploración (EDA) y presentación de resultados | Preparación, modelado y evaluación |
| **Se apoya en** | Matplotlib + Pandas | NumPy (+ SciPy) |
| **Entrada típica** | Un DataFrame de Pandas | Arrays o DataFrames (X = características, y = objetivo) |
| **Funciones típicas** | `histplot`, `boxplot`, `scatterplot`, `pairplot`, `heatmap` | `train_test_split`, `fit`, `predict`, `StandardScaler`, `accuracy_score` |
| **Ejercicios UD2** | E23, E24, E26 (gráficos y EDA) | E27 (normalización) y laboratorio de introducción a ML |
| **Unidades posteriores** | Todas (para mostrar resultados) | UD3 (clasificar textos), UD5 (núcleo de la unidad) |
| **Dificultad** | Baja: una línea = un gráfico | Media: hay que entender entrenamiento y prueba |

#### Cómo trabajan juntas: ejemplo completo con Iris

```python
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# --- DATOS (Pandas) ---
iris = load_iris(as_frame=True)
df = iris.frame
df["especie"] = df["target"].map(dict(enumerate(iris.target_names)))

# --- 1. EXPLORAR CON SEABORN ---
sns.pairplot(df.drop(columns="target"), hue="especie")   # relaciones entre medidas
plt.show()

sns.heatmap(df.drop(columns=["target", "especie"]).corr(),
            annot=True, cmap="coolwarm")                  # correlaciones
plt.show()

# --- 2. MODELAR CON SCIKIT-LEARN ---
X = df[iris.feature_names]
y = df["target"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

escalador = StandardScaler()                  # igual que en E27
X_train = escalador.fit_transform(X_train)
X_test = escalador.transform(X_test)

modelo = KNeighborsClassifier(n_neighbors=5)
modelo.fit(X_train, y_train)                  # aprender
pred = modelo.predict(X_test)                 # predecir
print(f"Exactitud: {accuracy_score(y_test, pred):.0%}")

# --- 3. MOSTRAR RESULTADOS CON SEABORN ---
sns.heatmap(confusion_matrix(y_test, pred), annot=True,
            xticklabels=iris.target_names, yticklabels=iris.target_names)
plt.xlabel("Predicción")
plt.ylabel("Real")
plt.show()
```

**Lectura del ejemplo**: Seaborn aparece **antes** del modelo (para entender los datos) y **después** (para enseñar los resultados). scikit-learn está **en medio** (para aprender).

#### Seaborn frente a Matplotlib

| Aspecto | Matplotlib | Seaborn |
|---------|-----------|---------|
| Nivel | Bajo nivel: control total | Alto nivel: construido sobre Matplotlib |
| Código | Más líneas por gráfico | Una línea para gráficos estadísticos |
| Estética por defecto | Sencilla | Más cuidada |
| Trabaja con DataFrames | Sí, pero hay que indicar columnas a mano | Directamente (`data=df, x=..., y=..., hue=...`) |
| Gráficos estadísticos (boxplot por grupos, pairplot, mapas de calor) | Laboriosos | Inmediatos |

```python
# Matplotlib: histograma de pétalos por especie (varias líneas)
for especie in df["especie"].unique():
    plt.hist(df[df["especie"] == especie]["petal length (cm)"],
             alpha=0.5, label=especie)
plt.legend()
plt.show()

# Seaborn: lo mismo en una línea
sns.histplot(data=df, x="petal length (cm)", hue="especie")
plt.show()
```

**Conclusión**: se aprende primero Matplotlib (E23) para entender cómo se construye un gráfico, y después Seaborn para ganar rapidez en el análisis exploratorio (E26).

#### scikit-learn frente a PyTorch

| Aspecto | scikit-learn | PyTorch |
|---------|-------------|---------|
| Tipo de modelos | ML clásico: regresión, árboles, KNN, SVM, clustering | Redes neuronales profundas |
| Datos ideales | Tablas (CSV), de cientos a cientos de miles de filas | Imágenes, texto, audio; grandes volúmenes |
| Facilidad | Muy alta: `fit()` y `predict()` | Media-alta: hay que escribir el bucle de entrenamiento |
| Necesita GPU | No | Recomendable para modelos grandes |
| En el curso | UD3 (clasificar textos con TF-IDF), UD5 (núcleo) | UD4 (CNN, opcional frente a Keras), UD5 (redes neuronales) |

**Regla práctica para el alumnado**: si los datos caben en una tabla, **empieza siempre por scikit-learn**. Pasa a PyTorch o Keras solo cuando trabajes con imágenes, texto o audio, o cuando un modelo clásico no sea suficiente.

**Instalación**:
```bash
pip install seaborn scikit-learn
```

[Referencia: Seaborn tutorial](https://seaborn.pydata.org/tutorial.html)
[Referencia: scikit-learn: Getting Started](https://scikit-learn.org/stable/getting_started.html)
[Referencia: scikit-learn: elegir el estimador adecuado](https://scikit-learn.org/stable/machine_learning_map.html)

---

## 1️⃣3️⃣ CREAR APLICACIONES: ESCRITORIO Y WEB

### 13.1 ¿Por qué crear aplicaciones?

Un análisis o un modelo de IA que solo funciona en un notebook lo puede usar **quien lo programó**. Una aplicación permite que **cualquier persona** lo use: escribe un dato, pulsa un botón y obtiene la respuesta.

```
 SCRIPT / NOTEBOOK              APLICACIÓN
 Solo el programador    ───►    Cualquier usuario
 Se ejecuta el código           Se pulsan botones, se rellenan campos
 Resultado en consola           Resultado en ventana o página web
```

**Dos grandes familias**:

| Tipo | Dónde se ejecuta | Ejemplo cotidiano | Librerías Python |
|------|------------------|-------------------|------------------|
| **App de escritorio** | En el ordenador, en su propia ventana | Calculadora, bloc de notas | tkinter, CustomTkinter, PySide6/PyQt6, Kivy, Flet |
| **App web** | En el navegador (servidor + página) | Formularios online, paneles de datos | Streamlit, Gradio, Flask, Django, FastAPI, Dash |

### 13.2 Concepto clave: programación orientada a eventos

Hasta ahora los programas se ejecutaban **de arriba abajo** y terminaban. Una aplicación gráfica funciona distinto: **espera** a que el usuario haga algo (un clic, una tecla) y entonces **reacciona** ejecutando una función.

```
 Programa clásico (E1-E27)        Aplicación con interfaz
 ─────────────────────────        ───────────────────────
 instrucción 1                    crear ventana y botones
 instrucción 2                    ┌─► esperar evento ◄──┐
 instrucción 3                    │   ¿clic en botón?   │
 fin                              │   → ejecutar función ┘
                                  └── (bucle hasta cerrar)
```

Por eso las **funciones** (sección 4, E9) son imprescindibles: cada botón tiene asociada una función que se ejecuta al pulsarlo.

---

### 13.3 Aplicaciones de escritorio

#### tkinter (incluida en Python)

**¿Qué es?** La librería gráfica **estándar** de Python. Viene instalada con Python en Windows y macOS (en algunas distribuciones Linux hay que instalar el paquete `python3-tk`).

**Ventajas**: sin instalación extra, sencilla, mucha documentación, ideal para aprender eventos.
**Desventajas**: aspecto algo anticuado; no sirve para la web.

**Elementos básicos (widgets)**:

| Widget | Para qué sirve | Equivalente en un formulario |
|--------|----------------|------------------------------|
| `Tk()` | Ventana principal | La hoja |
| `Label` | Mostrar texto | Una etiqueta |
| `Entry` | Escribir una línea de texto | Una casilla |
| `Button` | Ejecutar una función al pulsar | Botón "Enviar" |
| `Text` | Texto de varias líneas | Cuadro de comentarios |
| `Listbox` / `ttk.Combobox` | Elegir de una lista | Desplegable |
| `messagebox` | Ventanas de aviso | Mensaje emergente |

**Ejemplo: calculadora de nota media (conecta con E11)**:

```python
import tkinter as tk
from tkinter import messagebox

def calcular_media():
    texto = entrada.get()                       # 1. Leer lo escrito
    try:
        notas = [float(n) for n in texto.split(",")]   # 2. Convertir (E10, E14)
    except ValueError:
        messagebox.showerror("Error", "Escribe números separados por comas")
        return
    media = sum(notas) / len(notas)             # 3. Calcular (E11)
    resultado.config(text=f"Media: {media:.2f}")  # 4. Mostrar

ventana = tk.Tk()
ventana.title("Calculadora de medias")

tk.Label(ventana, text="Notas (separadas por comas):").pack(padx=10, pady=5)
entrada = tk.Entry(ventana, width=30)
entrada.pack(padx=10)
tk.Button(ventana, text="Calcular", command=calcular_media).pack(pady=5)
resultado = tk.Label(ventana, text="Media: -")
resultado.pack(pady=5)

ventana.mainloop()                              # Bucle de eventos
```

Fíjate: `command=calcular_media` va **sin paréntesis**. Se le pasa la función para que tkinter la ejecute cuando se pulse el botón.

**Gráficos de Matplotlib dentro de tkinter**: con `FigureCanvasTkAgg` (de `matplotlib.backends.backend_tkagg`) se puede incrustar un gráfico en la ventana, lo que une E23 con una app de escritorio.

**Convertir la app en un ejecutable (.exe)**:
```bash
pip install pyinstaller
pyinstaller --onefile --windowed mi_app.py   # Genera dist/mi_app.exe
```

[Referencia: tkinter (documentación oficial)](https://docs.python.org/3/library/tkinter.html)
[Referencia: TkDocs tutorial](https://tkdocs.com/tutorial/)

#### Otras librerías de escritorio

| Librería | Qué aporta | Nivel | Cuándo usarla |
|----------|-----------|-------|---------------|
| **CustomTkinter** | tkinter con aspecto moderno (modo oscuro, botones redondeados). Se programa casi igual | Fácil | Cuando el alumnado ya domina tkinter y quiere una app más vistosa |
| **PySide6 / PyQt6** | Basadas en Qt, el estándar profesional. Diseñador visual (Qt Designer). PySide6 es la versión oficial de Qt, con licencia LGPL; PyQt6 usa GPL o licencia comercial | Media-alta | Aplicaciones complejas y de aspecto profesional |
| **Kivy** | Interfaces táctiles; funciona también en Android e iOS | Media | Apps para móvil o pantallas táctiles |
| **Flet** | Interfaces modernas basadas en Flutter; el mismo código funciona como app de escritorio, web o móvil | Fácil-media | Una sola app para varias plataformas |

---

### 13.4 Aplicaciones web

**Cómo funciona una app web**:

```
  NAVEGADOR (cliente)                    SERVIDOR (Python)
  ┌─────────────────┐   petición        ┌─────────────────────┐
  │ Página: botones,│ ───────────────►  │ Recibe los datos    │
  │ formularios     │                   │ Ejecuta Python      │
  │                 │ ◄───────────────  │ (Pandas, modelo ML) │
  └─────────────────┘   respuesta       └─────────────────────┘
```

Hay dos tipos de librerías: las que **generan la página automáticamente** desde Python (Streamlit, Gradio, Dash) y los **frameworks web** clásicos, donde se programa también el HTML (Flask, Django, FastAPI).

#### Streamlit: paneles de datos en pocas líneas

**¿Qué es?** Convierte un script de Python en una página web interactiva. No hace falta saber HTML. Es la opción más directa para **presentar un análisis de datos**.

```python
# archivo: app_titanic.py   →   ejecutar con: streamlit run app_titanic.py
import streamlit as st
import pandas as pd

st.title("Supervivencia en el Titanic")

archivo = st.file_uploader("Sube titanic.csv", type="csv")
if archivo is not None:
    df = pd.read_csv(archivo)
    clase = st.selectbox("Clase del pasajero", sorted(df["Pclass"].unique()))
    filtrado = df[df["Pclass"] == clase]                 # Filtrado (E20)
    st.metric("Tasa de supervivencia", f"{filtrado['Survived'].mean():.0%}")
    st.bar_chart(filtrado.groupby("Sex")["Survived"].mean())   # GroupBy (E22)
    st.dataframe(filtrado.head(20))
```

**Publicar gratis**: Streamlit Community Cloud, conectado a un repositorio de GitHub.

[Referencia: Streamlit docs](https://docs.streamlit.io/)

#### Gradio: demos de modelos de IA

**¿Qué es?** Crea una interfaz web para **probar un modelo de IA**: se definen las entradas, la función y las salidas. Muy usada en Hugging Face Spaces para compartir modelos.

```python
import gradio as gr

def analizar(texto):
    positivas = ["bien", "genial", "feliz", "bueno"]
    negativas = ["mal", "triste", "horrible", "malo"]
    palabras = texto.lower().split()
    puntos = sum(p in positivas for p in palabras) - sum(p in negativas for p in palabras)
    if puntos > 0:
        return "Positivo 😊"
    if puntos < 0:
        return "Negativo 😞"
    return "Neutro 😐"

demo = gr.Interface(fn=analizar, inputs="text", outputs="text",
                    title="Analizador de sentimientos")
demo.launch()        # Abre la app en el navegador
```

Este ejemplo usa una regla sencilla. En UD3 la función `analizar` se sustituye por un modelo entrenado, y en UD4 la entrada pasa a ser una imagen (`inputs="image"`).

[Referencia: Gradio docs](https://www.gradio.app/docs)

#### Frameworks web clásicos

| Librería | Qué es | Nivel | Uso en el curso |
|----------|--------|-------|-----------------|
| **Flask** | Microframework: rutas + plantillas HTML. Se entiende cómo funciona la web por dentro | Media | Ampliación: web propia que usa un modelo |
| **Django** | Framework completo: usuarios, base de datos, panel de administración | Alta | Fuera del alcance del curso; útil como referencia profesional |
| **FastAPI** | Para crear **APIs** (servicios que devuelven datos en JSON) muy rápidas | Media | Ampliación UD5: servir un modelo como API |
| **Dash** (Plotly) | Paneles de datos interactivos con gráficos Plotly | Media | Alternativa a Streamlit con más control |

**Ejemplo mínimo con Flask**:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "<h1>Hola desde Flask</h1>"

@app.route("/cuadrado/<int:n>")
def cuadrado(n):
    return f"El cuadrado de {n} es {n ** 2}"

if __name__ == "__main__":
    app.run(debug=True)      # Abrir http://127.0.0.1:5000/cuadrado/7
```

[Referencia: Flask docs](https://flask.palletsprojects.com/)
[Referencia: FastAPI docs](https://fastapi.tiangolo.com/)

---

### 13.5 Comparación y elección

| Necesito... | Librería recomendada | Por qué |
|-------------|----------------------|---------|
| Primera app con ventanas, sin instalar nada | **tkinter** | Viene con Python |
| Una app de escritorio con aspecto moderno | **CustomTkinter** | Mismo código que tkinter, mejor aspecto |
| Una app profesional y compleja | **PySide6** | Estándar Qt |
| Una app para móvil | **Kivy** o **Flet** | Funcionan en Android/iOS |
| Presentar un análisis de datos en la web | **Streamlit** | Script → web en minutos |
| Que otros prueben mi modelo de IA | **Gradio** | Diseñado para demos de modelos |
| Entender cómo funciona una web | **Flask** | Mínimo y transparente |
| Ofrecer mi modelo como servicio | **FastAPI** | APIs rápidas y documentadas |

### 13.6 Dónde encajan en el curso

| Unidad / momento | Librería | Actividad propuesta |
|------------------|----------|---------------------|
| **UD2 · Bloque A** (funciones) | tkinter | Mini-apps: conversor de unidades, calculadora de medias (E3, E11 con ventana) |
| **UD2 · Laboratorio 1** (sesiones 47-52, sistema de gestión) | tkinter / CustomTkinter | Interfaz gráfica para el sistema de gestión: alta de registros, búsqueda, gráfico Matplotlib integrado |
| **UD2 · Capstone** (sesiones 65-70) | Streamlit | Presentar el análisis del dataset de Kaggle como panel web interactivo |
| **UD3 · Visión artificial** (proyecto final) | Gradio / Streamlit | Subir una foto y ver la clase que predice la CNN |
| **UD4 · Lenguaje natural** (proyecto: chatbot / sentimientos) | Gradio | Demo web del analizador de sentimientos o del chatbot |
| **UD5 · Machine Learning** | Streamlit / FastAPI | App que recibe datos (p. ej., características de una casa) y devuelve la predicción (ver 13.7) |
| **Ampliación** | Flask, PySide6, Kivy, Flet | Proyectos personales del alumnado avanzado |

**Instalación** (tkinter no necesita instalación):
```bash
pip install customtkinter streamlit gradio flask
```

### 13.7 Del notebook a la app: desplegar un modelo

Un modelo que solo existe dentro de un cuaderno no lo puede usar nadie más. **Desplegar** (*deploy*) es ponerlo en un sitio donde reciba datos nuevos y devuelva predicciones a personas o a otros programas.

> **Analogía:** entrenar es inventar una receta en la cocina de pruebas. Desplegar es abrir el restaurante: llegan clientes, la cocina repite la receta igual cada vez y alguien vigila que la comida siga saliendo bien.

**El ciclo de vida completo de un modelo** (enlaza con el ciclo de vida de los datos de la UD5, CA5.1):

```
 Recoger → Preparar → Entrenar → Evaluar → Guardar y versionar → Desplegar → Vigilar → Reentrenar
 (secc. 9)  (secc. 9)  (secc. 10, 14.4)      (este apartado)     (app/API)   (deriva)   (vuelta)
```

**Formas de desplegar**:

| Tipo | Cómo funciona | Ejemplo | Herramientas |
|------|---------------|---------|--------------|
| **App interactiva** | Una interfaz para que una persona pruebe el modelo | Demo para la clase | **Streamlit, Gradio** (sección 13.4) |
| **API en tiempo real** | Otro programa envía datos y recibe la predicción en milisegundos | Comprobar si un pago es fraude | FastAPI, Flask |
| **Por lotes** (*batch*) | Se predice para muchas filas a una hora fija | Puntuar cada noche a todos los clientes | Script programado (14.10) |
| **En el dispositivo** (*edge*) | El modelo va dentro del móvil o del robot | Filtros de la cámara | TFLite, ONNX |

#### Paso 1 · Guardar el modelo entrenado (serialización)

Entrenar puede tardar mucho; **guardar el modelo** permite entrenarlo una vez y usarlo muchas. Con scikit-learn se usa `joblib`, que viene con la librería.

```python
# entrenar.py: se ejecuta UNA vez; entrena y guarda el pipeline completo
import json, joblib, sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

X, y = load_iris(return_X_y=True, as_frame=True)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

modelo = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5))
modelo.fit(X_tr, y_tr)
precision = modelo.score(X_te, y_te)                 # 0.933

joblib.dump(modelo, "modelo_iris_v1.joblib")        # el modelo, con su escalado incluido
with open("modelo_iris_v1.json", "w") as f:          # metadatos: versión y calidad
    json.dump({"version": "1.0", "accuracy_test": round(precision, 3),
               "sklearn": sklearn.__version__, "columnas": list(X.columns),
               "clases": ["setosa", "versicolor", "virginica"]}, f, indent=2)
```

**Tres reglas para guardar modelos**:
1. **Guarda el pipeline completo** (escalado + modelo), no solo el modelo. Si no, tendrás que repetir a mano el preprocesamiento y te equivocarás.
2. **Apunta la versión de las librerías** (como en el `.json`). Un modelo guardado con una versión de scikit-learn puede fallar con otra.
3. **Nunca cargues un archivo `.joblib` o `.pkl` de una fuente desconocida**: al cargarlo se puede ejecutar código oculto. Trátalo como si fuera un programa.

#### Paso 2 · Cargar una vez y predecir

Error típico: cargar el modelo **dentro** de la función que predice, de modo que cada predicción lo vuelve a leer del disco. Se carga **una sola vez** al arrancar.

```python
# predecir.py
import json, joblib
import pandas as pd

MODELO = joblib.load("modelo_iris_v1.joblib")      # se carga UNA vez
META = json.load(open("modelo_iris_v1.json"))

def predecir(medidas: dict) -> dict:
    faltan = set(META["columnas"]) - set(medidas)
    if faltan:                                       # validar la entrada antes de predecir
        raise ValueError(f"Faltan columnas: {sorted(faltan)}")
    fila = pd.DataFrame([medidas])[META["columnas"]]
    probs = MODELO.predict_proba(fila)[0]
    i = probs.argmax()
    return {"especie": META["clases"][i], "confianza": round(float(probs[i]), 2),
            "version_modelo": META["version"]}

print(predecir({"sepal length (cm)": 5.1, "sepal width (cm)": 3.5,
                "petal length (cm)": 1.4, "petal width (cm)": 0.2}))
# {'especie': 'setosa', 'confianza': 1.0, 'version_modelo': '1.0'}
```

#### Paso 3 · Ponerle una cara: app con Streamlit

```python
# app.py  →  streamlit run app.py
import streamlit as st
from predecir import predecir, META

st.title("🌸 ¿Qué especie de iris es?")
st.caption(f"Modelo v{META['version']} · accuracy en test {META['accuracy_test']:.0%}")

medidas = {col: st.slider(col, 0.0, 8.0, 3.0, 0.1) for col in META["columnas"]}
if st.button("Predecir"):
    r = predecir(medidas)
    st.success(f"Especie: **{r['especie']}** (confianza {r['confianza']:.0%})")
```

Se puede publicar gratis en Streamlit Community Cloud conectándolo a un repositorio de GitHub. El archivo `requirements.txt` debe indicar las librerías y sus versiones (14.14).

#### Paso 4 (ampliación) · Una API para otros programas

Una **API** permite que una app móvil o una web pida predicciones enviando datos en **JSON** por HTTP. Con **FastAPI**:

```python
# api.py  →  uvicorn api:app --reload   ·   documentación automática en /docs
from fastapi import FastAPI, HTTPException
from predecir import predecir

app = FastAPI(title="API Iris")

@app.get("/health")                 # ¿está viva la API?
def health():
    return {"estado": "ok"}

@app.post("/predict")               # recibe las medidas en JSON y devuelve la especie
def predict(medidas: dict):
    try:
        return predecir(medidas)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))   # 422 = datos de entrada no válidos
```

| Concepto | Significado |
|----------|-------------|
| **Endpoint** | Una dirección de la API (`/predict`, `/health`) |
| **GET / POST** | Pedir información / enviar datos para que se procesen |
| **JSON** | Formato de texto para intercambiar datos (sección 2, 14.10) |
| **Código de estado** | 200 = bien · 404 = no existe · 422 = datos mal formados · 500 = error del servidor |

**Mejor con Pydantic.** FastAPI valida los datos de entrada con la librería **Pydantic** (ver [Análisis de datos 1.5](datos.html#15-validar-con-reglas-pydantic)). En lugar de recibir un `dict` cualquiera, se describe cómo deben ser las medidas y FastAPI rechaza solo, con un error 422 y un mensaje por campo, lo que no cumpla las reglas: un texto donde va un número, un valor negativo o una medida que falta. Además, la ficha aparece en la documentación automática de `/docs`.

```python
from pydantic import BaseModel, Field

class Medidas(BaseModel):          # alias: el nombre de la columna en el modelo entrenado
    sepalo_largo: float = Field(gt=0, lt=30, alias="sepal length (cm)")
    sepalo_ancho: float = Field(gt=0, lt=30, alias="sepal width (cm)")
    petalo_largo: float = Field(gt=0, lt=30, alias="petal length (cm)")
    petalo_ancho: float = Field(gt=0, lt=30, alias="petal width (cm)")

@app.post("/predict")
def predict(medidas: Medidas):     # FastAPI valida antes de entrar en la función
    return predecir(medidas.model_dump(by_alias=True))
```

Si llega `{"sepal length (cm)": "cinco", "petal length (cm)": -1}`, la API responde 422 con cuatro errores: «cinco» no es un número, la longitud del pétalo debe ser mayor que 0, y faltan las dos anchuras. La función `predecir` ya no tiene que comprobarlo.

#### Paso 5 · Comprobar que funciona: tests

```python
# test_predecir.py  →  pytest
import pytest
from predecir import predecir

FLOR = {"sepal length (cm)": 6.7, "sepal width (cm)": 3.0,
        "petal length (cm)": 5.2, "petal width (cm)": 2.3}

def test_devuelve_una_especie_valida():
    r = predecir(FLOR)
    assert r["especie"] in ["setosa", "versicolor", "virginica"]
    assert 0 <= r["confianza"] <= 1

def test_rechaza_entrada_incompleta():
    with pytest.raises(ValueError):
        predecir({"sepal length (cm)": 5.0})
```

#### Más allá del aula: qué hacen los profesionales

Estos conceptos no se programan en el curso, pero conviene conocerlos para entender cómo funcionan los servicios de IA reales:

| Concepto | Idea en una frase |
|----------|-------------------|
| **Docker** | Empaquetar la app con su Python y sus librerías en un «contenedor» que funciona igual en cualquier ordenador |
| **Nube** (Cloud Run, Azure, AWS) | Ejecutar ese contenedor en servidores que crecen según el número de usuarios |
| **CI/CD** (GitHub Actions) | Cada vez que se sube código, se ejecutan los tests y, si pasan, se publica automáticamente |
| **Monitorización y deriva** (*drift*) | Los datos del mundo cambian (nuevos clientes, nuevas costumbres) y el modelo empeora sin avisar: hay que vigilar sus predicciones y reentrenarlo |
| **Versionado** (MLflow, DVC) | Guardar qué datos, qué código y qué parámetros produjeron cada versión del modelo |
| **Seguridad** | Claves de acceso, límite de peticiones, no guardar contraseñas en el código y validar siempre la entrada |
| **MLOps** | Todo lo anterior junto: DevOps aplicado al aprendizaje automático |

> **Conexión con la ética** (UD1, UD5): un modelo desplegado toma decisiones sobre personas reales. La **deriva** puede volverlo injusto con el tiempo aunque al principio funcionase bien. Por eso se vigila y se documenta.

**Checklist antes de publicar un modelo del curso**:
- [ ] Se ha evaluado con datos que no vio al entrenar (y se indica la métrica en la app).
- [ ] Se ha guardado el pipeline completo y la versión de las librerías.
- [ ] La entrada se valida (faltan campos, valores imposibles).
- [ ] Hay al menos dos tests que pasan.
- [ ] `requirements.txt` con versiones; sin contraseñas ni datos personales en el repositorio.
- [ ] La app explica qué hace el modelo, su precisión y sus límites.

> Ejemplos de 13.7 comprobados (entrenar, guardar, cargar, predecir y los dos tests). Streamlit y FastAPI no se pudieron ejecutar en el entorno de prueba: ejecútalos en local o en Colab tras `pip install streamlit fastapi uvicorn`.

---

## 1️⃣4️⃣ AMPLIACIÓN: MATERIALES COMPLEMENTARIOS

Esta sección recoge y ordena el contenido de los materiales complementarios del curso: guías de Pandas, Seaborn, EDA, Machine Learning, redes neuronales, IA generativa, hashing, automatización, y colecciones de ejercicios y algoritmos. Las fuentes están al final, en el apartado 14.15. Cada bloque indica con qué ejercicio (E1–E27) o con qué unidad conecta.

---

### 14.1 IA, ML, Deep Learning e IA Generativa: no son lo mismo

Son cuatro términos **relacionados pero no intercambiables**. Cada uno está contenido en el anterior:

```
┌──────────────────────────────────────────────────────────┐
│ INTELIGENCIA ARTIFICIAL (IA): máquinas que hacen tareas  │
│ que requieren "inteligencia" (razonar, decidir, ver...)  │
│  ┌────────────────────────────────────────────────────┐  │
│  │ MACHINE LEARNING (ML): aprende patrones de los     │  │
│  │ DATOS en vez de programar cada regla               │  │
│  │  ┌──────────────────────────────────────────────┐  │  │
│  │  │ DEEP LEARNING (DL): ML con redes neuronales  │  │  │
│  │  │ de muchas capas                              │  │  │
│  │  │  ┌────────────────────────────────────────┐  │  │  │
│  │  │  │ IA GENERATIVA (GenAI): usa DL para     │  │  │  │
│  │  │  │ CREAR contenido nuevo (texto, imagen,  │  │  │  │
│  │  │  │ audio, vídeo, código)                  │  │  │  │
│  │  │  └────────────────────────────────────────┘  │  │  │
│  │  └──────────────────────────────────────────────┘  │  │
│  └────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────┘
```

**Fórmula fácil**: IA → *Inteligencia* · ML → *Aprendizaje* · DL → *Redes neuronales profundas* · GenAI → *Generación*

| Término | Idea clave | Ejemplos | Unidad del curso |
|---------|-----------|----------|------------------|
| **IA** | Campo amplio: máquinas con comportamiento inteligente | Sistemas expertos, ajedrez, recomendadores, coche autónomo | UD1 |
| **ML** | Aprende de datos para predecir o clasificar | Filtro de spam, precio de una casa, riesgo de crédito, abandono de clientes | UD5 (intro en sección 10) |
| **DL** | Redes neuronales de muchas capas; aprende patrones complejos | Reconocimiento facial, de voz, detección de objetos | UD4 y UD5 |
| **GenAI** | Genera contenido nuevo a partir de lo aprendido | Chatbots (ChatGPT, Claude), generadores de imágenes, asistentes de código | UD3 |

**Diferencia clave ML ↔ GenAI**: un modelo de ML clásico *clasifica o predice* ("¿este correo es spam?"). Un modelo generativo *crea* ("escribe un correo"). Una analogía de los materiales: el ML es "una persona con un cerebro muy potente para reconocer patrones"; la GenAI es "una persona creativa que, además, produce cosas nuevas".

---

### 14.2 Hoja de ruta: 10 cosas que aprender antes de empezar con IA

Resumen de la guía *AI Roadmap 2026*, que coincide casi paso a paso con el orden de la UD2:

| Paso | Qué aprender | En este documento | Ejercicios |
|------|-------------|-------------------|-----------|
| 1 | Python básico: variables, bucles, funciones, clases | Secciones 1–4 | E1–E12 |
| 2 | Estructuras de datos: list, dict, tuple, set | Sección 5 | E13–E17 |
| 3 | Resolver problemas: dividir en pasos y depurar | 14.12 (algoritmia) | Todos |
| 4 | NumPy | Sección 7 | E18–E19 |
| 5 | Pandas: cargar, limpiar, explorar | Secciones 7, 9; 14.3 | E20–E22, E25 |
| 6 | Matemáticas: álgebra lineal, probabilidad, estadística | Sección 6 | E15–E17 |
| 7 | Evaluar un modelo: train/test, accuracy, sobreajuste | Sección 10; 14.4 | E27 |
| 8 | Un proyecto real pequeño que entiendas bien | Capstone (sesiones 65–70) | — |
| 9 | Aprender construyendo, no esperar a "estar listo" | — | — |
| 10 | Recursos: tutorial oficial de Python, TheAlgorithms/Python | Sección 15 | — |

> **Mensaje para el alumnado**: no hace falta saberlo todo antes de empezar. Se entiende más construyendo un proyecto pequeño que esperando a sentirse preparado.

---

### 14.3 Referencia rápida de Pandas (las funciones que más se usan)

Selección de las guías *100 Pandas Functions* y *45 líneas de Pandas*, agrupada por la tarea que resuelve:

| Tarea | Funciones | Ejemplo |
|-------|-----------|---------|
| **Cargar / guardar** | `read_csv`, `read_excel`, `read_json`, `to_csv`, `to_excel` | `df = pd.read_csv("datos.csv")` |
| **Primer vistazo** | `head`, `tail`, `shape`, `info`, `describe`, `dtypes`, `columns`, `sample` | `df.info()` |
| **Valores únicos** | `unique`, `nunique`, `value_counts` | `df["Sex"].value_counts()` |
| **Seleccionar** | `df["col"]`, `df[["a","b"]]`, `loc` (por etiqueta), `iloc` (por posición) | `df.loc[df["Age"] > 30, "Name"]` |
| **Filtrar** | máscaras booleanas, `query`, `isin`, `between` | `df.query("Pclass == 1 and Age < 18")` |
| **Nulos** | `isnull().sum()`, `dropna`, `fillna`, `ffill`, `interpolate` | `df["Age"].fillna(df["Age"].median())` |
| **Duplicados** | `duplicated().sum()`, `drop_duplicates` | `df = df.drop_duplicates()` |
| **Tipos** | `astype`, `to_datetime`, `to_numeric`, `"category"` | `df["fecha"] = pd.to_datetime(df["fecha"])` |
| **Columnas** | `rename`, `drop`, `assign`, `insert` | `df.rename(columns={"Pclass": "clase"})` |
| **Transformar** | `apply`, `map`, `replace`, `where`, `clip`, `cut`, `qcut` | `df["grupo"] = pd.cut(df["Age"], [0, 18, 65, 100])` |
| **Texto** | `str.lower`, `str.strip`, `str.contains`, `str.split`, `str.replace` | `df["Name"].str.contains("Mrs")` |
| **Ordenar** | `sort_values`, `sort_index`, `nlargest`, `nsmallest`, `rank` | `df.nlargest(5, "Fare")` |
| **Agrupar** | `groupby` + `mean/sum/count/agg`, `pivot_table`, `crosstab` | `df.groupby("Pclass")["Survived"].mean()` |
| **Combinar** | `concat`, `merge`, `join` | `pd.merge(a, b, on="id", how="left")` |
| **Reorganizar** | `melt`, `pivot`, `stack`, `unstack`, `explode` | `df.melt(id_vars="pais")` |
| **Estadística** | `mean`, `median`, `mode`, `std`, `var`, `quantile`, `corr`, `cumsum` | `df["Fare"].quantile([.25, .75])` |
| **Series temporales** | `dt.year`, `dt.month`, `resample`, `rolling`, `shift`, `pct_change` | `ventas.resample("M").sum()` |
| **Índice** | `set_index`, `reset_index` | `df.reset_index(drop=True)` |

**Patrones de una línea muy útiles**:
```python
df.isnull().mean().sort_values(ascending=False)       # % de nulos por columna
df.select_dtypes(include="number").columns            # solo columnas numéricas
df["col"].value_counts(normalize=True)                # proporciones en vez de conteos
df.groupby("Pclass").agg(media=("Age", "mean"), n=("Age", "size"))   # agregación con nombre
df.loc[:, df.isnull().mean() < 0.5]                   # quitar columnas con >50 % de nulos
```

---

### 14.4 Pipeline completo de Machine Learning con scikit-learn

Las *200 órdenes de Machine Learning* se pueden ordenar como las **fases de un proyecto**. Este es el esqueleto que se ampliará en UD5:

```
1 Cargar → 2 Explorar → 3 Limpiar → 4 Codificar y escalar → 5 Dividir
   → 6 Entrenar → 7 Evaluar → 8 Ajustar → 9 Guardar
```

| Fase | Herramientas principales |
|------|--------------------------|
| **Limpiar** | `dropna`, `fillna` (media, mediana o moda), `SimpleImputer`, `KNNImputer`, eliminar outliers con IQR |
| **Codificar** (texto → números) | `pd.get_dummies`, `OneHotEncoder` (categorías sin orden), `OrdinalEncoder` / `LabelEncoder` (con orden o para la variable objetivo) |
| **Escalar** | `StandardScaler` (media 0, desviación 1), `MinMaxScaler` (de 0 a 1), `RobustScaler` (resistente a outliers) |
| **Seleccionar variables** | `SelectKBest`, `PolynomialFeatures`, matriz de correlación |
| **Dividir** | `train_test_split` (con `stratify=y` para mantener las proporciones de clases) |
| **Modelos de clasificación** | `LogisticRegression`, `KNeighborsClassifier`, `DecisionTreeClassifier`, `RandomForestClassifier`, `SVC`, `GaussianNB` |
| **Modelos de regresión** | `LinearRegression`, `Ridge`, `Lasso`, `RandomForestRegressor` |
| **No supervisado** | `KMeans`, `PCA` |
| **Evaluar (clasificación)** | `accuracy_score`, `precision_score`, `recall_score`, `f1_score`, `confusion_matrix`, `classification_report` |
| **Evaluar (regresión)** | `mean_absolute_error`, `mean_squared_error`, `r2_score` |
| **Validación** | `cross_val_score`, `KFold`, `StratifiedKFold` |
| **Ajuste de hiperparámetros** | `GridSearchCV`, `RandomizedSearchCV` |
| **Todo junto** | `Pipeline`, `ColumnTransformer` |
| **Guardar** | `joblib.dump` / `joblib.load` |

**Eliminar outliers con el rango intercuartílico (IQR)**: conecta con la sección 6.
```python
Q1, Q3 = df["Fare"].quantile([0.25, 0.75])
IQR = Q3 - Q1
df_sin_outliers = df[df["Fare"].between(Q1 - 1.5 * IQR, Q3 + 1.5 * IQR)]
```

**Ejemplo completo con `Pipeline`** (dataset Titanic de Seaborn; `load_dataset` lo descarga, así que necesita conexión a Internet):
```python
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

df = sns.load_dataset("titanic")
X = df[["pclass", "sex", "age", "fare", "embarked"]]
y = df["survived"]

numericas = ["pclass", "age", "fare"]
categoricas = ["sex", "embarked"]

preprocesado = ColumnTransformer([
    ("num", Pipeline([("imputar", SimpleImputer(strategy="median")),
                      ("escalar", StandardScaler())]), numericas),
    ("cat", Pipeline([("imputar", SimpleImputer(strategy="most_frequent")),
                      ("onehot", OneHotEncoder(handle_unknown="ignore"))]), categoricas),
])

modelo = Pipeline([("prep", preprocesado),
                   ("rf", RandomForestClassifier(n_estimators=200, max_depth=5, random_state=42))])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42)

modelo.fit(X_train, y_train)
print(classification_report(y_test, modelo.predict(X_test)))
print("Validación cruzada (5 particiones):", cross_val_score(modelo, X, y, cv=5).mean().round(3))
```

**¿Por qué un `Pipeline`?** Porque garantiza que la imputación y el escalado se **aprenden solo con los datos de entrenamiento**. Si se escala todo el dataset antes de dividirlo, el modelo "ve" información del test (*data leakage*) y la evaluación sale demasiado optimista.

**Métricas: cuál usar**

| Métrica | Pregunta que responde | Cuándo importa |
|---------|----------------------|----------------|
| **Accuracy** | ¿Qué % acierta en total? | Clases equilibradas |
| **Precision** | De los que predije positivos, ¿cuántos lo eran? | Cuando un falso positivo es caro (spam que borra un correo importante) |
| **Recall** | De los positivos reales, ¿cuántos encontré? | Cuando un falso negativo es caro (no detectar una enfermedad) |
| **F1** | Equilibrio entre precision y recall | Clases desequilibradas |
| **MAE / RMSE** | ¿Cuánto me equivoco de media? (en las unidades de la variable) | Regresión |
| **R²** | ¿Qué parte de la variación explica el modelo? (1 = perfecto) | Regresión |

---

### 14.5 Catálogo de gráficos de Seaborn para EDA

Resumen de *Complete Seaborn for Data Science* y *36 líneas de Matplotlib/Seaborn*. **Primero se elige la pregunta y después el gráfico**:

| Pregunta | Gráfico | Código Seaborn |
|----------|---------|----------------|
| ¿Cómo se distribuye una variable numérica? | Histograma + KDE | `sns.histplot(df, x="age", kde=True)` |
| ¿Qué categoría tiene un valor medio mayor? | Barras | `sns.barplot(df, x="class", y="fare")` |
| ¿Cuántos casos hay de cada categoría? | Conteo | `sns.countplot(df, x="class", hue="survived")` |
| ¿Hay valores atípicos? | Caja (boxplot) | `sns.boxplot(df, x="class", y="age")` |
| ¿Cómo se compara la forma de las distribuciones? | Violín | `sns.violinplot(df, x="sex", y="age", split=True, hue="survived")` |
| ¿Se relacionan dos variables numéricas? | Dispersión | `sns.scatterplot(df, x="age", y="fare", hue="sex")` |
| ¿Cómo evoluciona en el tiempo? | Línea | `sns.lineplot(df, x="year", y="passengers")` |
| ¿Qué variables están correlacionadas? | Mapa de calor | `sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")` |
| Visión general de todas las relaciones | Pairplot | `sns.pairplot(df, hue="species")` |
| ¿Hay tendencia lineal? | Regresión | `sns.regplot(df, x="total_bill", y="tip")` |
| Comparar por subgrupos en paneles | Facetas | `sns.catplot(df, x="class", y="survived", col="sex", kind="bar")` |

**Parámetros que se repiten en casi todos**: `hue` (color por categoría), `style` (forma del marcador), `size` (tamaño), `palette` (paleta de colores), `col`/`row` (paneles), `order` (orden de las categorías) y `ax` (dibujar en un eje concreto de Matplotlib).

**Errores frecuentes y buenas prácticas**:
- Un gráfico debe responder **una** pregunta: título, ejes con nombre y unidades.
- No uses tartas con muchas categorías; las barras se comparan mejor.
- En los gráficos de barras, empieza el eje Y en 0 para no exagerar diferencias.
- Usa paletas aptas para el daltonismo (`"colorblind"`) y no más de 6–8 colores.
- **Correlación no es causalidad**: que dos variables suban juntas no significa que una cause la otra.
- Con muchos puntos, reduce la opacidad (`alpha=0.3`) o usa `hexbin`/`kdeplot`.

---

### 14.6 Checklist de Análisis Exploratorio de Datos (EDA)

Síntesis de la guía *Exploratory Data Analysis* (con el dataset Titanic) y del flujo de trabajo Seaborn + Pandas. Amplía la sección 9:

| Paso | Qué hacer | Código típico |
|------|-----------|---------------|
| 1. **Entender** | ¿Qué es cada fila? ¿Y cada columna? ¿Cuál es la variable objetivo? | `df.shape`, `df.head()`, `df.info()` |
| 2. **Calidad** | Nulos, duplicados, tipos incorrectos | `df.isnull().sum()`, `df.duplicated().sum()`, `df.dtypes` |
| 3. **Limpiar nulos** | Eliminar columnas casi vacías; numéricas → mediana; categóricas → moda; series temporales → `ffill`/`interpolate` | `df["age"].fillna(df.groupby(["pclass","sex"])["age"].transform("median"))` |
| 4. **Arreglar texto y tipos** | Espacios, mayúsculas, fechas, categorías | `df["city"].str.strip().str.title()`, `astype("category")` |
| 5. **Outliers** | Detectar (boxplot, IQR) y decidir: eliminar, recortar (*winsorizar*) o transformar con log | `df["fare"].clip(upper=df["fare"].quantile(.99))`, `np.log1p(df["fare"])` |
| 6. **Univariante** | Distribución de cada variable | `histplot`, `countplot`, `describe()` |
| 7. **Bivariante** | Relación de cada variable con la objetivo | `groupby` + `mean`, `barplot`, `boxplot` |
| 8. **Multivariante** | Interacciones entre varias variables | `pivot_table` + `heatmap`, facetas, `pairplot` |
| 9. **Ingeniería de variables** | Crear variables útiles (tamaño de familia, título del nombre, grupo de edad) | `df["familia"] = df["sibsp"] + df["parch"] + 1` |
| 10. **Codificar y escalar** | Preparar para ML (14.4) | `get_dummies`, `StandardScaler` |
| 11. **Conclusiones** | Escribir 3–5 hallazgos en lenguaje claro | Celda Markdown en el notebook |

**Agrupación inteligente** (rellenar la edad según clase y sexo, en vez de con una sola mediana global):
```python
df["age"] = df["age"].fillna(df.groupby(["pclass", "sex"])["age"].transform("median"))
```

**EDA automático** (para ampliar, nunca para sustituir el análisis propio): `ydata-profiling`, `sweetviz`, `dtale`, `autoviz`.
```python
# pip install ydata-profiling
from ydata_profiling import ProfileReport
ProfileReport(df, title="Informe Titanic").to_file("informe.html")
```

---

### 14.7 Redes neuronales desde cero

Base de *Neural Networks Beginner Notes* y *Deep Learning*. Es la introducción a la parte de Deep Learning de **UD4 (Visión Artificial)** y **UD5 (Machine Learning)**.

#### La neurona artificial

Una neurona hace tres cosas: **multiplica** cada entrada por un peso, **suma** todo más un sesgo (*bias*) y **aplica** una función de activación.

```
 x1 ──(w1)──┐
 x2 ──(w2)──┼──► z = w1·x1 + w2·x2 + w3·x3 + b ──► f(z) ──► salida
 x3 ──(w3)──┘
```

```python
import numpy as np

x = np.array([1.0, 2.0, 3.0])        # entradas
w = np.array([0.2, 0.4, 0.2])        # pesos
b = 0.0                              # sesgo
z = np.dot(x, w) + b                 # suma ponderada → 1.6
salida = 1 / (1 + np.exp(-z))        # activación sigmoide → 0.832
print(round(z, 2), round(salida, 3))
```

#### Funciones de activación

| Función | Fórmula | Salida | Uso típico |
|---------|---------|--------|-----------|
| **Sigmoide** | 1 / (1 + e⁻ᶻ) | 0 a 1 | Última capa en clasificación binaria |
| **Tanh** | (eᶻ − e⁻ᶻ)/(eᶻ + e⁻ᶻ) | −1 a 1 | Capas ocultas (redes antiguas, RNN) |
| **ReLU** | max(0, z) | 0 a ∞ | **Capas ocultas** (la más usada: rápida y simple) |
| **Softmax** | eᶻⁱ / Σ eᶻʲ | Probabilidades que suman 1 | Última capa en clasificación multiclase |

```python
z = np.array([-2.0, 0.0, 2.0])
print("sigmoide:", np.round(1 / (1 + np.exp(-z)), 3))   # [0.119 0.5 0.881]
print("relu    :", np.maximum(0, z))                     # [0. 0. 2.]
s = np.exp([2.0, 1.0, 0.1]); print("softmax :", np.round(s / s.sum(), 3))  # [0.659 0.242 0.099]
```

#### Cómo aprende una red

```
1. FORWARD: los datos atraviesan la red y sale una predicción
2. PÉRDIDA (loss): se mide el error entre la predicción y el valor real
3. BACKWARD (backpropagation): con la regla de la cadena se calcula
   cuánto contribuyó cada peso al error (el gradiente)
4. ACTUALIZAR: cada peso se mueve un poco en sentido contrario al gradiente
   w_nuevo = w − tasa_aprendizaje × gradiente
5. Repetir muchas veces (épocas)
```

| Pérdida | Para qué | Fórmula |
|---------|----------|---------|
| **MSE** (error cuadrático medio) | Regresión | media de (real − predicho)² |
| **MAE** | Regresión, menos sensible a outliers | media de \|real − predicho\| |
| **Entropía cruzada binaria (BCE)** | Clasificación binaria | −media[y·log(p) + (1−y)·log(1−p)] |
| **Entropía cruzada categórica** | Clasificación multiclase | −Σ y·log(p) |

**Descenso de gradiente con un solo peso** (aprender que y = 2x):
```python
x, y_real = 1.0, 2.0
w, lr = 0.0, 0.2
for paso in range(1, 6):
    pred = w * x
    grad = 2 * (pred - y_real) * x          # derivada del error cuadrático
    w = w - lr * grad
    print(f"paso {paso}: w = {w:.3f}")      # 0.800, 1.280, 1.568, 1.741, 1.844 → se acerca a 2
```

**Contar parámetros**: una capa densa con `n_entrada` entradas y `n_salida` neuronas tiene `n_entrada × n_salida` pesos + `n_salida` sesgos. Una red 3 → 4 → 4 → 2 tiene (12+4) + (16+4) + (8+2) = **46 parámetros**.

#### Sobreajuste y cómo evitarlo

```
 Subajuste (underfitting)     Buen ajuste          Sobreajuste (overfitting)
 modelo demasiado simple      generaliza bien      memoriza el entrenamiento
 error alto en train y test   error bajo en ambos  error bajo en train, alto en test
```

Técnicas: **más datos**, **regularización** (L2), **dropout** (apagar neuronas al azar durante el entrenamiento), **early stopping** (parar cuando el error de validación deja de bajar) y **aumento de datos** (en imágenes: girar, recortar, voltear).

#### Una red con scikit-learn (sin necesidad de PyTorch)

```python
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
escalador = StandardScaler().fit(X_train)
red = MLPClassifier(hidden_layer_sizes=(16, 8), max_iter=1000, random_state=42)
red.fit(escalador.transform(X_train), y_train)
print("Accuracy test:", round(red.score(escalador.transform(X_test), y_test), 3))   # ≈ 0.965
print("Épocas de entrenamiento:", red.n_iter_)
```

> `MLPClassifier` también admite `early_stopping=True`, pero con datasets pequeños puede parar demasiado pronto: compruébalo siempre comparando la accuracy con y sin él.

#### Arquitecturas: cuál se usa para qué

| Arquitectura | Idea | Datos | Dónde se ve |
|--------------|------|-------|-------------|
| **Red densa (MLP)** | Todas las neuronas conectadas con la capa siguiente | Tablas | UD5 |
| **CNN** (convolucional) | Filtros (*kernels*) que recorren la imagen detectando bordes, texturas, formas; *pooling* para reducir tamaño | Imágenes | **UD4** (CIFAR-10, MNIST) |
| **RNN** (recurrente) | Tiene "memoria" (estado oculto) de lo anterior | Secuencias, texto, series temporales | UD3, UD5 |
| **LSTM / GRU** | RNN con "puertas" que deciden qué recordar y qué olvidar | Secuencias largas | UD3 |
| **Transformer** | Mecanismo de **atención**: cada palabra "mira" a todas las demás | Texto (LLM), también imágenes | **UD3** (14.8) |

---

### 14.8 IA Generativa y modelos de lenguaje (LLM)

Resumen de *GenAI: Zero to Hero*. Es la base conceptual de **UD3 (Lenguaje Natural)**.

#### Cómo "lee" un LLM: tokens y embeddings

```
"Me gusta Python"
     │  1. TOKENIZACIÓN: el texto se trocea en tokens (palabras o trozos)
     ▼
["Me", " gusta", " Py", "thon"]  →  [1234, 5678, 910, 1112]   (números)
     │  2. EMBEDDINGS: cada token se convierte en un vector de números
     ▼
[0.12, -0.80, 0.33, ...]   ← palabras de significado parecido tienen vectores cercanos
     │  3. TRANSFORMER: capas de atención relacionan cada token con el resto
     ▼
     4. PREDICCIÓN DEL SIGUIENTE TOKEN: probabilidades para cada posible token
        " es" 41 %   " mucho" 22 %   "." 9 % ...
     │  5. Se elige uno, se añade al texto y se repite
     ▼
"Me gusta Python porque es..."
```

**Idea clave**: un LLM no "busca" respuestas; **genera el texto token a token**, eligiendo cada vez un token probable según lo que ha aprendido de enormes cantidades de texto.

**Embeddings en Python** (similitud entre frases, la base de la búsqueda semántica):
```python
import numpy as np

def similitud_coseno(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

gato  = np.array([0.9, 0.8, 0.1])   # vectores de juguete
perro = np.array([0.8, 0.9, 0.2])
coche = np.array([0.1, 0.2, 0.9])
print(round(similitud_coseno(gato, perro), 2))   # 0.99 → significados parecidos
print(round(similitud_coseno(gato, coche), 2))   # 0.3 → significados distintos
```

#### Parámetros de generación

| Parámetro | Qué controla | Valor bajo | Valor alto |
|-----------|-------------|-----------|-----------|
| **Temperatura** | Aleatoriedad | Respuestas previsibles y precisas | Respuestas creativas y variadas |
| **Top-k** | Solo se elige entre los k tokens más probables | Más conservador | Más variedad |
| **Top-p** | Solo se eligen tokens hasta sumar una probabilidad p | Más conservador | Más variedad |
| **Ventana de contexto** | Cuántos tokens "recuerda" a la vez (pregunta + respuesta + historial) | Conversaciones cortas | Documentos largos |

#### Prompting: cómo pedir bien

| Prompt malo | Prompt bueno |
|-------------|-------------|
| "Háblame del clima" | "Explica el cambio climático a alumnado de 1º de Bachillerato en 5 puntos, con un ejemplo de Galicia en cada uno" |
| "Haz una función" | "Escribe una función de Python `media(notas)` que reciba una lista de floats, devuelva la media con 2 decimales y lance `ValueError` si la lista está vacía. Añade 3 ejemplos de uso" |

Buenas prácticas: dar **contexto** y **rol**, indicar el **formato** de salida, dar **ejemplos** y **iterar** refinando el prompt.

#### Conceptos que aparecerán en UD3

| Concepto | Qué es |
|----------|--------|
| **LLM** | *Large Language Model*: Transformer entrenado con muchísimo texto (GPT, Claude, Gemini, Llama, Mistral) |
| **Fine-tuning** | Reentrenar un modelo con datos propios para una tarea concreta |
| **RAG** | *Retrieval-Augmented Generation*: antes de responder, el sistema busca documentos relevantes (con embeddings) y se los da al modelo como contexto. Reduce las invenciones |
| **Alucinación** | El modelo genera algo falso con total seguridad. **Siempre hay que verificar** |
| **Multimodal** | Modelos que entienden y generan texto, imagen, audio... |
| **Agente** | LLM que, además de responder, usa herramientas (buscar, ejecutar código) para completar tareas |

**Usos reales**: chatbots y asistentes, resúmenes, traducción, generación de código, búsqueda semántica, recomendación, generación de imágenes y música.

> ⚠️ **Ética** (conecta con UD1): sesgos aprendidos de los datos, privacidad (no introducir datos personales), derechos de autor, desinformación y uso responsable en tareas académicas.

---

### 14.9 Hashing: por qué los diccionarios son tan rápidos

Basado en *DSA en Python, Fase 7: Hashing*. Explica qué hay **dentro** de `dict` y `set` (sección 5, E13–E14).

**Hashing** = convertir una clave (texto, número...) en un número de tamaño fijo (el **hash**) mediante una **función hash**. Ese número indica en qué posición de una tabla se guarda el dato.

```
 clave "manzana" ──► función hash ──► 3 ──► tabla[3] = ("manzana", 1.20)
 buscar "manzana" ─► función hash ──► 3 ──► se accede directamente: ¡sin recorrer la lista!
```

| Operación | Lista (`list`) | Diccionario / conjunto (hash) |
|-----------|---------------|-------------------------------|
| Buscar un elemento | O(n): recorre uno a uno | **O(1)** de media: acceso directo |
| Insertar | O(1) al final | O(1) de media |
| Borrar | O(n) | O(1) de media |

```python
print(hash("manzana") % 8)          # posición en una tabla de 8 huecos (varía entre ejecuciones)

# Tabla hash hecha a mano, con encadenamiento para las colisiones
class TablaHash:
    def __init__(self, tamaño=8):
        self.cubetas = [[] for _ in range(tamaño)]

    def _indice(self, clave):
        return hash(clave) % len(self.cubetas)

    def guardar(self, clave, valor):
        cubeta = self.cubetas[self._indice(clave)]
        for par in cubeta:
            if par[0] == clave:
                par[1] = valor
                return
        cubeta.append([clave, valor])

    def obtener(self, clave):
        for k, v in self.cubetas[self._indice(clave)]:
            if k == clave:
                return v
        raise KeyError(clave)

t = TablaHash()
t.guardar("manzana", 1.20); t.guardar("pera", 0.95)
print(t.obtener("pera"))            # 0.95
```

**Colisión**: dos claves distintas que dan la misma posición. Se resuelve con **encadenamiento** (cada hueco guarda una lista, como arriba) o con **direccionamiento abierto** (buscar el siguiente hueco libre).

**Por qué las claves de un `dict` deben ser inmutables**: si una clave cambiara, su hash cambiaría y no se volvería a encontrar. Por eso `str`, `int` y `tuple` pueden ser claves, pero `list` no.

**Problemas clásicos que se resuelven con hashing**:
```python
from collections import Counter

frase = "el perro y el gato y el pez"
print(Counter(frase.split()).most_common(2))     # frecuencias → [('el', 3), ('y', 2)]

def tiene_duplicados(lista):
    return len(lista) != len(set(lista))         # O(n) en vez de O(n²)

def dos_suman(numeros, objetivo):                # ¿qué dos números suman el objetivo?
    vistos = {}
    for i, n in enumerate(numeros):
        if objetivo - n in vistos:
            return vistos[objetivo - n], i
        vistos[n] = i

print(dos_suman([2, 7, 11, 15], 9))              # (0, 1)
```

**Hash criptográfico** (otra aplicación: contraseñas, integridad de archivos, blockchain):
```python
import hashlib
print(hashlib.sha256("mi_contraseña".encode()).hexdigest()[:16])   # siempre el mismo resultado
```

---

### 14.10 Automatización con Python

Resumen de *Python Automation Complete Notes*. Automatizar es escribir scripts que hacen tareas repetitivas con poca intervención humana: organizar archivos, descargar datos, actualizar hojas de cálculo, enviar correos o probar webs.

**Buenas prácticas antes de empezar**:
```bash
python -m venv .venv                  # entorno virtual por proyecto
source .venv/bin/activate             # macOS/Linux  (Windows: .venv\Scripts\activate)
pip install requests beautifulsoup4 pandas openpyxl python-dotenv schedule
```
Las claves secretas (API keys, contraseñas) van en un archivo `.env` leído con `python-dotenv`, **nunca dentro del código** ni subidas a GitHub.

| Tarea | Librería | Ejemplo |
|-------|----------|---------|
| Archivos y carpetas | `os`, `pathlib`, `shutil` | Ordenar descargas por extensión |
| Llamar a APIs web | `requests` | Descargar datos del tiempo en JSON |
| Extraer datos de webs (*scraping*) | `BeautifulSoup`, `Playwright` | Leer titulares de una página |
| Hojas de cálculo | `pandas`, `openpyxl` | Unir 12 Excel mensuales en uno |
| Correo | `smtplib`, `email.message` | Enviar un informe automático |
| Programar tareas | `schedule`, `time` | Ejecutar un script cada día a las 8:00 |
| Registro de lo que pasa | `logging` | Guardar errores en un archivo `.log` |
| Bases de datos | `sqlite3`, `SQLAlchemy` | Guardar resultados (14.11) |
| Varias tareas a la vez | `concurrent.futures` | Descargar 50 archivos en paralelo |
| Ratón y teclado | `pyautogui` | Automatizar una aplicación sin API |

**Ejemplo 1: ordenar una carpeta por tipo de archivo**
```python
from pathlib import Path
import shutil

carpeta = Path("Descargas")
tipos = {".pdf": "Documentos", ".jpg": "Imagenes", ".png": "Imagenes", ".csv": "Datos"}

for archivo in carpeta.iterdir():
    if archivo.is_file() and archivo.suffix.lower() in tipos:
        destino = carpeta / tipos[archivo.suffix.lower()]
        destino.mkdir(exist_ok=True)
        shutil.move(str(archivo), destino / archivo.name)
```

**Ejemplo 2: consultar una API con gestión de errores**
```python
import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {"latitude": 42.88, "longitude": -8.54, "current_weather": True}   # Santiago
try:
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()                       # lanza error si el código no es 200
    print(r.json()["current_weather"]["temperature"], "°C")
except requests.RequestException as e:
    print("No se pudo obtener el dato:", e)
```

**Ejemplo 3: tarea programada con registro**
```python
import logging, schedule, time

logging.basicConfig(filename="tareas.log", level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")

def copia_de_seguridad():
    logging.info("Copia de seguridad realizada")

schedule.every().day.at("08:00").do(copia_de_seguridad)
while True:
    schedule.run_pending()
    time.sleep(60)
```

> ⚠️ **Scraping responsable**: lee los términos de uso y el `robots.txt` de la web, no hagas peticiones masivas (añade pausas) y usa una API oficial si existe.

**Conexión con la IA**: la automatización es la fase de **Extracción** del ETL (sección 9) y permite alimentar los modelos con datos actualizados. Los LLM también pueden llamarse desde Python (`openai`, `anthropic`) para automatizar resúmenes o clasificaciones de textos (UD3).

---

### 14.11 Testing y bases de datos

Temas presentes en *1000 Python Examples* (Gábor Szabó) y en las notas de automatización.

#### Pruebas automáticas con `pytest`

Un **test** es un pequeño programa que comprueba que otro funciona. Si mañana cambias el código y rompes algo, los tests lo detectan.

```python
# archivo: notas.py
def media(notas):
    if not notas:
        raise ValueError("La lista está vacía")
    return round(sum(notas) / len(notas), 2)
```
```python
# archivo: test_notas.py      →  ejecutar con:  pytest
import pytest
from notas import media

def test_media_normal():
    assert media([5, 7, 9]) == 7

def test_media_decimales():
    assert media([5, 6]) == 5.5

def test_lista_vacia():
    with pytest.raises(ValueError):
        media([])
```

Para empezar sin instalar nada, `assert` dentro del propio script ya sirve: `assert media([4, 6]) == 5`.

#### Bases de datos con `sqlite3` (incluido en Python)

SQLite guarda una base de datos completa en **un solo archivo**. Es ideal para el Laboratorio 1 (sistema de gestión, sesiones 47–52).

```python
import sqlite3
import pandas as pd

con = sqlite3.connect("instituto.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS alumnos (id INTEGER PRIMARY KEY, nombre TEXT, nota REAL)")
cur.executemany("INSERT INTO alumnos (nombre, nota) VALUES (?, ?)",
                [("Ana", 8.5), ("Luis", 6.0), ("Sara", 9.2)])      # ? evita la inyección SQL
con.commit()

for fila in cur.execute("SELECT nombre, nota FROM alumnos WHERE nota >= ?", (7,)):
    print(fila)

df = pd.read_sql("SELECT * FROM alumnos", con)    # de SQL a Pandas en una línea
print(round(df["nota"].mean(), 2))
con.close()
```

| SQL | Equivalente en Pandas |
|-----|----------------------|
| `SELECT nombre FROM t` | `df["nombre"]` |
| `WHERE nota >= 7` | `df[df["nota"] >= 7]` |
| `GROUP BY curso` | `df.groupby("curso")` |
| `ORDER BY nota DESC` | `df.sort_values("nota", ascending=False)` |
| `JOIN` | `pd.merge` |

---

### 14.12 Algoritmia: pensar antes de programar

Síntesis de *Algoritmos resueltos con Python* (Condor y De la Cruz) y de *Ejercicios de programación con Python* (José A. Alonso).

#### Del problema al código

```
1. ANALIZAR      ¿Qué datos entran? ¿Qué debe salir? ¿Qué restricciones hay?
2. DISEÑAR       Pseudocódigo o diagrama de flujo
3. CODIFICAR     Traducir a Python
4. PROBAR        Casos normales, casos límite (lista vacía, 0, negativos)
5. MEJORAR       ¿Se puede hacer más claro o más rápido?
```

**Pseudocódigo → Python** (¿un año es bisiesto?):
```
INICIO                                  def es_bisiesto(año):
  LEER año                                  return (año % 4 == 0 and año % 100 != 0) \
  SI (año MOD 4 = 0 Y año MOD 100 ≠ 0)             or año % 400 == 0
     O año MOD 400 = 0 ENTONCES
       ESCRIBIR "Bisiesto"               print(es_bisiesto(2024))   # True
  SINO                                   print(es_bisiesto(1900))   # False
       ESCRIBIR "No bisiesto"
FIN
```

**Símbolos del diagrama de flujo**: óvalo = inicio/fin · paralelogramo = entrada/salida · rectángulo = proceso · rombo = decisión · flechas = orden de ejecución.

#### Estructuras y técnicas

| Técnica | Idea | Ejemplo en Python |
|---------|------|-------------------|
| **Secuencial** | Instrucciones una tras otra | Calcular el área de un triángulo |
| **Selectiva** | `if / elif / else`, `match` | Clasificar una nota |
| **Repetitiva** | `for`, `while` | Tabla de multiplicar |
| **Vectores y matrices** | Listas y listas de listas / NumPy | Traspuesta de una matriz |
| **Comprensión de listas** | Crear listas en una línea | `[x**2 for x in range(10) if x % 2 == 0]` |
| **Recursión** | Una función que se llama a sí misma con un problema más pequeño | Factorial, Fibonacci, Torres de Hanói |
| **Funciones de orden superior** | Funciones que reciben funciones | `map`, `filter`, `sorted(key=...)`, `lambda` |
| **Divide y vencerás** | Partir el problema en mitades | Búsqueda binaria, *quicksort*, *mergesort* |
| **Programación dinámica** | Guardar resultados ya calculados para no repetirlos | Fibonacci con memoria |
| **Búsqueda en espacios de estados** | Explorar posibilidades paso a paso | Laberintos, sudoku, 8 reinas (base de la IA clásica, UD1) |

```python
from functools import lru_cache

def factorial(n):                     # recursión: caso base + caso recursivo
    return 1 if n <= 1 else n * factorial(n - 1)

@lru_cache                            # programación dinámica: memoriza resultados
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)

def busqueda_binaria(lista, x):       # divide y vencerás: O(log n), lista ORDENADA
    izq, der = 0, len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == x:
            return medio
        if lista[medio] < x:
            izq = medio + 1
        else:
            der = medio - 1
    return -1

print(factorial(5), fib(50), busqueda_binaria([1, 3, 5, 7, 9, 11], 7))   # 120 12586269025 3
```

**Complejidad (notación O)**: cómo crece el tiempo cuando crecen los datos.

| Notación | Nombre | Ejemplo | 1 000 datos ≈ |
|----------|--------|---------|---------------|
| O(1) | Constante | Acceso a un `dict` | 1 paso |
| O(log n) | Logarítmica | Búsqueda binaria | 10 pasos |
| O(n) | Lineal | Recorrer una lista | 1 000 pasos |
| O(n log n) | Casi lineal | `sorted()` | 10 000 pasos |
| O(n²) | Cuadrática | Dos bucles anidados | 1 000 000 pasos |

**Representación de datos** (de *Más de 400 ejercicios de programación*): un ordenador lo guarda todo en bits. Con `n` bits se representan 2ⁿ valores (16 bits → 0 a 65 535). Python lo muestra con `bin(10)` → `'0b1010'`, `int("1010", 2)` → `10` y `hex(255)` → `'0xff'`.

---

### 14.13 Banco de ejercicios complementarios

Ejercicios inspirados en las colecciones adjuntas, ordenados según los ejercicios del curso. Sirven como refuerzo (🟢), práctica (🟡) o ampliación (🔴).

| Bloque | Ejercicios del curso | Ejercicios complementarios | Nivel |
|--------|----------------------|----------------------------|-------|
| Variables y E/S | E1–E12 | Convertir grados °C ↔ °F; calcular el área de figuras geométricas; devolver el cambio con el mínimo de monedas | 🟢 |
| Condicionales | E1–E12 | Máximo y mínimo de 3 números; par o impar; año bisiesto; validar una contraseña (longitud, mayúscula, número) | 🟢 |
| Bucles | E1–E12 | Sucesiones típicas (Fibonacci, primos, triangulares); dibujar triángulos y rombos con `*`; adivinar un número | 🟢🟡 |
| Funciones | E1–E12 | Números romanos ↔ decimales; MCD y MCM; ¿es palíndromo?; factorial recursivo | 🟡 |
| Listas | E1–E12 | Porciones (*slicing*); aplanar listas anidadas; eliminar duplicados sin perder el orden; *quicksort* | 🟡🔴 |
| Diccionarios / conjuntos | E13–E14 | Agenda de contactos; contar valores y palabras; "dos suman" con hashing (14.9) | 🟡 |
| Cadenas | E1–E14 | Suma de los números de una frase; cifrado César; contar vocales | 🟢🟡 |
| Matrices / NumPy | E18–E19 | Suma y producto de matrices; validar un sudoku; traspuesta sin NumPy | 🟡🔴 |
| Pandas | E20–E22 | Detectar transacciones inválidas en un CSV; ventas por mes y región; top 5 productos | 🟡 |
| Visualización | E23–E24, E26 | Los 10 gráficos de EDA (14.5) con el dataset `tips` o `penguins` de Seaborn | 🟡 |
| ETL / ML | E25–E27 | Pipeline completo de Titanic (14.4); comparar 3 modelos con validación cruzada | 🔴 |
| Automatización | Ampliación | Ordenar una carpeta; unir Excel; consultar una API del tiempo (14.10) | 🟡🔴 |

**Fuentes de ejercicios con solución** para el alumnado:
- *30 Ejercicios de Python* (Código Pitón): de "Nada de Hola Mundo" a "Detectando transacciones inválidas", con dificultad creciente.
- *Ejercicios de Python con soluciones*: 12 unidades ordenadas por tema.
- *Más de 400 ejercicios de programación* (Marzal y Gracia, UJI): representación de datos, expresiones, control de flujo, listas, funciones y ficheros.
- *Ejercicios de programación con Python* (José A. Alonso, Univ. de Sevilla): definiciones por comprensión, recursión, funciones de orden superior, tipos abstractos de datos, grafos y algoritmos avanzados. Nivel avanzado.
- *Algoritmos resueltos con Python* (Condor y De la Cruz): cada ejercicio con análisis, pseudocódigo, diagrama de flujo y código.
- *1000 Python Examples* (Gábor Szabó): ejemplos cortos de casi cualquier tema (Tk, Flask, SQLite, testing, NumPy, Pandas).
- *Program in Python* (Keshwam): introducción breve en inglés.

---

### 14.14 Buenas prácticas de Python y conceptos avanzados

Síntesis de *Python Complete Notes: Beginner to Advanced* (Achal Singh, TheAutomationEngineer). Las 18 fichas del material repasan lo que ya está en las secciones 1–5 (variables, operadores, condicionales, bucles, funciones, cadenas y colecciones) y añaden lo siguiente.

#### Estilo y organización de un proyecto

| Práctica | Cómo |
|----------|------|
| **PEP 8** (guía de estilo oficial) | 4 espacios de sangría, líneas de 79–99 caracteres, espacios alrededor de los operadores. Herramientas: `black`, `flake8`, `pylint` |
| **Nombres** | `variable_y_funcion` (snake_case) · `NombreDeClase` (PascalCase) · `CONSTANTE` (MAYÚSCULAS) · `modulo.py` |
| **Estructura** | `src/` para el código, `tests/` para las pruebas, `README.md`, `requirements.txt`, `.gitignore` |
| **Entorno virtual** | `python -m venv .venv`; no se sube a GitHub (va en `.gitignore`) |
| **Dependencias** | `pip freeze > requirements.txt` y `pip install -r requirements.txt` |
| **Módulos y paquetes** | Un archivo `.py` es un **módulo**; una carpeta de módulos es un **paquete** (con `__init__.py`). `import modulo` o `from modulo import funcion` |
| **Funciones pequeñas** | Una función hace una sola cosa, con un *docstring* (`"""…"""`) que explica qué hace. Principio **DRY**: no repetir código |

#### Errores frecuentes que conviene evitar

```python
# ❌ Argumento por defecto mutable: la lista se comparte entre llamadas
def añadir(x, lista=[]):
    lista.append(x)
    return lista
print(añadir(1), añadir(2))      # [1, 2] [1, 2]  ← ¡sorpresa!

# ✅ Correcto
def añadir(x, lista=None):
    lista = [] if lista is None else lista
    lista.append(x)
    return lista
print(añadir(1), añadir(2))      # [1] [2]
```

| Error | Por qué es malo | Alternativa |
|-------|-----------------|-------------|
| `except: pass` | Esconde los errores | Capturar la excepción concreta (`except ValueError:`) y avisar |
| `API_KEY = "12345"` en el código | Se publica al subirlo a GitHub | Variables de entorno o archivo `.env` (14.10) |
| `f = open(...)` sin cerrar | Se quedan archivos abiertos | `with open(...) as f:` |
| Variables globales | Código difícil de seguir | Pasar datos como parámetros y devolver resultados |
| Copiar y pegar código | Los errores se multiplican | Crear una función |
| `==` frente a `is` | `==` compara valores; `is` comprueba si son **el mismo objeto** | `a == b` para comparar; `x is None` para None |

> **Una corrección al material:** la ficha 2 afirma que Python no hace conversiones automáticas de tipo. Las hace en casos seguros: `3 + 2.5` da `5.5` (int → float) y `True + 1` da `2`. Lo que **no** hace es mezclar tipos incompatibles: `"3" + 2` da `TypeError`, y entonces hay que convertir a mano con `int("3")`.

#### Excepciones completas: `try / except / else / finally` y `raise`

```python
class EdadNoValida(Exception):              # excepción propia
    pass

def leer_edad(texto):
    try:
        edad = int(texto)                    # puede lanzar ValueError
    except ValueError:
        print("Escribe un número entero")
        return None
    else:                                    # solo si no hubo error
        if edad < 0:
            raise EdadNoValida("La edad no puede ser negativa")
        return edad
    finally:                                 # se ejecuta SIEMPRE
        print("Lectura terminada")

print(leer_edad("17"))                       # Lectura terminada · 17
print(leer_edad("hola"))                     # Escribe un número entero · Lectura terminada · None
```

**Leer un *traceback***: se lee **de abajo arriba**. La última línea dice el tipo de error (`ZeroDivisionError`) y la anterior, el archivo y la línea donde ocurrió.

#### Programación orientada a objetos: los cuatro pilares

| Pilar | Idea | Ejemplo |
|-------|------|---------|
| **Encapsulación** | Juntar datos y métodos y proteger el estado interno | `self.__saldo` solo se cambia con `ingresar()` |
| **Herencia** | Una clase hija reutiliza la de la madre | `class Perro(Animal)` |
| **Polimorfismo** | El mismo método hace cosas distintas según el objeto | `animal.hablar()` → «Guau» o «Miau» |
| **Abstracción** | Mostrar qué hace y esconder cómo | `from abc import ABC, abstractmethod` |

Las librerías de IA usan estos pilares constantemente. Todos los modelos de scikit-learn heredan de una clase base y comparten `fit()` y `predict()`: es **polimorfismo**. Por eso se puede cambiar un modelo por otro sin cambiar el resto del código (14.4). El agente aspirador de 0.9 es otro ejemplo de clase.

#### Conceptos avanzados

```python
# Generador: produce valores de uno en uno (no guarda toda la lista en memoria)
def pares(n):
    for i in range(0, n, 2):
        yield i
print(list(pares(10)))                       # [0, 2, 4, 6, 8]

# Decorador: añade comportamiento a una función sin modificarla
import time
def cronometrar(func):
    def envoltura(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        print(f"{func.__name__} tardó {time.perf_counter() - inicio:.4f} s")
        return resultado
    return envoltura

@cronometrar
def suma_cuadrados(n):
    return sum(i * i for i in range(n))      # generador dentro de sum()
suma_cuadrados(1_000_000)

# *args y **kwargs: número variable de argumentos
def resumen(*notas, **datos):
    return f"{datos.get('nombre', '?')}: media {sum(notas) / len(notas):.1f}"
print(resumen(7, 8, 9, nombre="Uxía"))       # Uxía: media 8.0

# Funciones integradas muy útiles
nombres, notas = ["Ana", "Brais"], [8.5, 6.0]
for i, (n, x) in enumerate(zip(nombres, notas), start=1):
    print(i, n, x)                           # 1 Ana 8.5 · 2 Brais 6.0
print(any(x < 5 for x in notas), all(x >= 5 for x in notas))   # False True
```

| Concepto | Para qué | Dónde aparece en IA |
|----------|----------|---------------------|
| **Iterador / generador** (`yield`) | Recorrer datos enormes sin cargarlos todos en memoria | Cargar imágenes por lotes para entrenar una red (`DataLoader`) |
| **Decorador** (`@`) | Añadir registro, tiempo, permisos… | `@app.post("/predict")` en FastAPI (13.7), `@st.cache_data` en Streamlit, `@lru_cache` (14.12) |
| **Gestor de contexto** (`with`) | Abrir y cerrar recursos de forma segura | Archivos, conexiones a bases de datos, `torch.no_grad()` |
| `*args`, `**kwargs` | Funciones flexibles | Pasar hiperparámetros a un modelo: `Modelo(**params)` |

**Rendimiento**: las comprensiones suelen ser más rápidas que los bucles con `append`. Se debe preferir las funciones integradas y usar `set` para comprobar si un elemento está en una colección (O(1), 14.9). Para medir tiempos, `timeit`.

### 14.15 Materiales complementarios utilizados

| Material | Tema | Secciones |
|----------|------|-----------|
| AI vs ML vs Deep Learning vs GenAI | Jerarquía de conceptos | 14.1 |
| AI Roadmap 2026 (@codedsoul_05) | Hoja de ruta de aprendizaje | 14.2 |
| 100 Pandas Functions · 45 líneas de Pandas | Referencia de Pandas | 14.3 |
| 200 Machine Learning Commands | Pipeline de ML | 14.4 |
| Complete Seaborn for Data Science · 36 líneas Matplotlib/Seaborn | Visualización | 14.5 |
| Exploratory Data Analysis (EDA) | Análisis exploratorio | 14.6 |
| Neural Networks Beginner Notes · Deep Learning | Redes neuronales | 14.7 |
| GenAI: Zero to Hero | IA generativa y LLM | 14.8 |
| DSA in Python – Phase 7: Hashing | Hashing | 14.9 |
| Python Automation Complete Notes | Automatización | 14.10 |
| 1000 Python Examples (G. Szabó) | Testing, SQLite, GUI, web | 14.11, 13 |
| Algoritmos resueltos con Python (Condor, De la Cruz) · Ejercicios de programación con Python (J. A. Alonso) | Algoritmia | 14.12 |
| 30 Ejercicios de Python · Ejercicios Python con soluciones · Más de 400 ejercicios (Marzal, Gracia) · Program in Python (Keshwam) | Ejercicios | 14.13 |
| Python Complete Notes: Beginner to Advanced (Achal Singh, TheAutomationEngineer) | Repaso de Python, buenas prácticas, POO, Python avanzado | 1–5, 14.14 |
| ML Model Deployment Handbook: From Notebook to Production | Guardar, servir, probar y desplegar modelos; MLOps | 13.7 |
| Python Part 1 y Part 2: Core Python (@codedsoul_05), apuntes manuscritos procesados con OCR | Conversión de tipos, formato, patrones, problemas numéricos, cadenas, conjuntos, comprensiones, `lambda`, `map`/`filter`/`reduce`, recursión, ámbito, módulos | 1.5, 2.4–2.6, 3.3–3.4, 4.6–4.10, 5.4–5.8 y ejercicios E28–E37 |

---

## 1️⃣5️⃣ REFERENCIAS EXTERNAS

### Documentación Oficial

| Tema | Referencia | URL |
|------|-----------|-----|
| **Python** | Documentación oficial | https://docs.python.org/3/ |
| **Strings** | String methods | https://docs.python.org/3/library/stdtypes.html#string-methods |
| **Listas** | List methods | https://docs.python.org/3/tutorial/datastructures.html |
| **Diccionarios** | Dict reference | https://docs.python.org/3/library/stdtypes.html#mapping-types-dict |
| **NumPy** | NumPy docs | https://numpy.org/doc/stable/ |
| **Pandas** | Pandas docs | https://pandas.pydata.org/docs/ |
| **Matplotlib** | Matplotlib gallery | https://matplotlib.org/stable/gallery/ |
| **scikit-learn** | sklearn docs | https://scikit-learn.org/stable/ |
| **Seaborn** | Seaborn docs | https://seaborn.pydata.org/ |
| **PyTorch** | PyTorch docs | https://pytorch.org/docs/stable/ |
| **tkinter** | tkinter docs | https://docs.python.org/3/library/tkinter.html |
| **Streamlit** | Streamlit docs | https://docs.streamlit.io/ |
| **Gradio** | Gradio docs | https://www.gradio.app/docs |
| **Flask** | Flask docs | https://flask.palletsprojects.com/ |

### Tutoriales Recomendados

**Principiantes**:
- [Python.org Tutorial](https://docs.python.org/3/tutorial/)
- [W3Schools Python](https://www.w3schools.com/python/)
- [Real Python](https://realpython.com/)

**Análisis de Datos**:
- [Kaggle Learn](https://www.kaggle.com/learn) - Cursos gratuitos
- [DataCamp](https://www.datacamp.com/) - Plataforma de aprendizaje
- [Coursera Python for Data Analysis](https://www.coursera.org/courses?query=python%20data%20analysis)

**Estadística**:
- [Khan Academy Statistics](https://www.khanacademy.org/math/statistics-probability)
- [StatQuest with Josh Starmer](https://www.youtube.com/c/joshstarmer) - YouTube

### Libros Recomendados

| Libro | Autor | Nivel | Tema |
|-------|-------|-------|------|
| Python Crash Course | Eric Matthes | Principiante | Python general |
| Fluent Python | Luciano Ramalho | Intermedio | Python avanzado |
| Python Data Science Handbook | Jake VanderPlas | Intermedio | NumPy, Pandas, Matplotlib |
| Introduction to Statistical Learning | James et al. | Avanzado | Estadística y ML |

[Fluent Python (PDF)](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/)

### Herramientas Online

| Herramienta | URL | Propósito |
|-------------|-----|----------|
| **Google Colab** | https://colab.research.google.com | Jupyter en la nube |
| **Replit** | https://replit.com | IDE online |
| **Kaggle** | https://kaggle.com | Datasets y competencias |
| **Stack Overflow** | https://stackoverflow.com | Respuestas a preguntas |
| **GitHub** | https://github.com | Código y ejemplos |

### Cheat Sheets (Hojas de Referencia)

- [Python Cheat Sheet](https://www.pythoncheatsheet.org/)
- [NumPy Cheat Sheet](https://numpy.org/doc/stable/user/basics.broadcasting.html)
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [Matplotlib Cheat Sheet](https://matplotlib.org/cheatsheets/)

---

## 📦 IDEs LOCALES Y DATASETS RECOMENDADOS

### IDEs Locales (Entornos de Desarrollo)

#### 1️⃣ VS Code (Visual Studio Code)

**¿Qué es?**
- Editor ligero y rápido (no es un IDE completo)
- Extensible: add-ons para Python, debugging, etc.
- Excelente para desarrollo profesional y enseñanza

**Ventajas**:
- ⚡ Muy rápido y ligero
- 🔧 Toneladas de extensiones
- 💻 Gratis y multiplataforma
- 📝 Perfecto para escribir código limpio

**Desventajas**:
- 📚 Menos funcionalidades "mágicas" que PyCharm
- ⚙️ Requiere más configuración manual

**Instalación**:
```bash
# 1. Descargar VS Code: https://code.visualstudio.com/
# 2. Instalar extensión Python (Microsoft)
# 3. Instalar extensión Pylance (ayudas de código)
```

**Cómo usarlo para UD2**:
```python
# Crear archivo: ejercicio1.py
print("Hola, Python")

# Para ejecutar:
# Opción 1: Click derecho → Run Python File
# Opción 2: Terminal → python ejercicio1.py
```

**Configuración recomendada**:
```json
// settings.json (Ctrl+Shift+P → "Preferences: Open User Settings (JSON)")
// Requiere instalar las extensiones "Black Formatter" y "Pylint" (Microsoft)
{
    "editor.formatOnSave": true,
    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter"
    }
}
```

---

#### 2️⃣ PyCharm Community Edition

**¿Qué es?**
- IDE **completo** especializado en Python
- Detección automática de errores
- Refactorización poderosa
- Integración Git perfecta

**Ventajas**:
- 🧠 Entiende tu código: autocompletado inteligente
- 🐛 Debugging visual excelente
- 🔄 Refactorización automática
- 📊 Análisis de código incorporado
- 💡 Sugerencias automáticas

**Desventajas**:
- 🐌 Más pesado que VS Code
- 💾 Consume más RAM (~2GB)
- ⏳ Tiempo de inicio más lento

**Instalación**:
```bash
# 1. Descargar Community Edition: https://www.jetbrains.com/pycharm/download/
# 2. Instalar (el Community es gratis permanentemente)
# 3. Crear nuevo proyecto
```

**Estructura de Proyecto PyCharm**:
```
mi_proyecto/
├── venv/              # Entorno virtual (automático)
├── ejercicios/
│   ├── ejercicio1.py
│   ├── ejercicio2.py
│   └── datos.csv
└── main.py
```

**Características útiles**:
```python
# Ctrl+Space: Autocompletado
# Ctrl+/: Comentar línea
# Shift+F6: Renombrar variable en todas partes
# Alt+Enter: "Bombilla" - sugerencias automáticas

# Ejemplo: PyCharm detecta:
lista = [1, 2, 3]
lista.appnd(4)  # ⚠️ Error: "appnd" debería ser "append"
```

**Debugging en PyCharm**:
```python
# Hacer click en la línea número para añadir breakpoint
# Luego: Shift+F9 para ejecutar en debug
# Paso a paso: F10 (siguiente línea), F11 (dentro función)

numero = 10
# >>> Breakpoint aquí
if numero % 2 == 0:
    print("Es par")
```

---

#### 3️⃣ Jupyter Notebook

**¿Qué es?**
- Análisis **interactivo** de datos en tu navegador
- Mezcla código, resultados y texto en celdas
- Ideal para exploración y aprendizaje

**Ventajas**:
- 📖 Excelente para aprender y explorar
- 📊 Visualizar resultados inmediatamente
- 📝 Documentación junto al código
- 🐍 Python en el navegador

**Desventajas**:
- 🔀 No es ideal para código de producción
- 💾 Requiere más recursos que edición básica
- 🐛 Debugging más complicado

**Instalación**:
```bash
pip install jupyter notebook
# Luego ejecutar:
jupyter notebook
# Se abre en: http://localhost:8888
```

**Estructura de Jupyter**:
```
Celda 1: [Código] - Importar librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Celda 2: [Código] - Cargar datos
df = pd.read_csv("datos.csv")
df.head()

Celda 3: [Texto Markdown]
# Análisis de datos
Este notebook explora la distribución de edades

Celda 4: [Código] - Visualizar
plt.hist(df['edad'])
plt.show()  # Resultado aparece abajo
```

**Atajos útiles**:
```
Shift+Enter: Ejecutar celda actual
Ctrl+Enter: Ejecutar sin pasar a siguiente
A: Insertar celda arriba
B: Insertar celda abajo
M: Convertir a Markdown
Y: Convertir a código
DD: Eliminar celda
```

**Ejemplo completo en Jupyter**:
```python
# Celda 1
import pandas as pd
import matplotlib.pyplot as plt

# Celda 2
datos = {
    'nombre': ['Ana', 'Bruno', 'Carlos'],
    'edad': [25, 30, 28],
    'ciudad': ['Madrid', 'Barcelona', 'Valencia']
}
df = pd.DataFrame(datos)
print(df)

# Celda 3
# Calculo de edad promedio
edad_promedio = df['edad'].mean()
print(f"Edad promedio: {edad_promedio:.1f}")

# Resultado aparece automáticamente:
# Edad promedio: 27.7
```

---

### Comparación: ¿Cuál usar?

| Tarea | VS Code | PyCharm | Jupyter |
|------|---------|---------|---------|
| Ejercicios básicos (E1-E12) | ✅ Ideal | ✅ Ideal | ⚠️ Overkill |
| Proyectos pequeños | ✅ Perfecto | ✅ Perfecto | ❌ No |
| Análisis de datos (E20-E27) | ✅ Bueno | ✅ Bueno | ✅✅ Ideal |
| Aprender/Explorar | ⚠️ Básico | ✅ Bueno | ✅✅ Excelente |
| Debugging | ⚠️ Básico | ✅✅ Excelente | ❌ Complicado |
| Velocidad (inicio) | ✅ Rápido | ❌ Lento | ✅ Rápido |
| Recursos (RAM) | ✅ Bajo | ❌ Alto | ⚠️ Medio |

**Recomendación para UD2**:
- **E1-E12**: VS Code o PyCharm
- **E13-E22**: PyCharm (debugging)
- **E23-E27**: Jupyter Notebook (análisis e iteración)

---

### Datasets Recomendados

> **Más allá de Kaggle.** Para buscar datos propios (portales gallegos, españoles e internacionales, UCI, Hugging Face, Our World in Data, NASA, OMS, Banco Mundial) y saber cómo elegirlos, mira la sección 1.6 de [Análisis de datos](datos.html#16-dónde-encontrar-datos-más-allá-de-kaggle).

#### 1️⃣ Iris Dataset (Flores)

**Descripción**:
- Dataset **clásico** para machine learning
- 150 muestras de 3 especies de flores iris
- 4 características: largo sépalo, ancho sépalo, largo pétalo, ancho pétalo

**Tamaño**: Muy pequeño (~5 KB)

**Características**:
- Limpio (sin datos faltantes)
- Bien balanceado
- Perfecto para **principiantes**

**Cómo usarlo en UD2**:
```python
from sklearn.datasets import load_iris
import pandas as pd

# Cargar
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target_names[iris.target]

# Explorar
print(df.head())
print(df.describe())
print(df['species'].value_counts())

# Gráficos
import matplotlib.pyplot as plt
df.plot(subplots=True, figsize=(12, 8))
plt.show()
```

**Usar en ejercicio**:
- E15: Calcular estadísticas de cada especie
- E20: Crear DataFrame y filtrar
- E23: Visualizar distribuciones
- E26: EDA completo

**Descarga**:
```bash
# Ya está incluido en sklearn, o:
# https://archive.ics.uci.edu/ml/datasets/iris
```

---

#### 2️⃣ Titanic Dataset (Kaggle)

**Descripción**:
- 891 pasajeros del Titanic
- **Objetivo**: Predecir quién sobrevivió
- Características: edad, género, clase, tarifa, puerto

**Tamaño**: Pequeño (~60 KB)

**Características**:
- **Datos reales** con imperfecciones
- Contiene **valores faltantes**
- Ideal para aprender limpieza de datos

**Cómo usarlo en UD2**:
```python
import pandas as pd

# Descargar de Kaggle o local
df = pd.read_csv('titanic.csv')

print(df.shape)           # (891, 12)
print(df.info())          # Ver tipos y NaN
print(df.isnull().sum())  # Contar faltantes

# Limpieza
df_clean = df.dropna(subset=['Age', 'Embarked']).copy()
df_clean['Age'] = df_clean['Age'].astype(int)

# Análisis
supervivencia = df_clean['Survived'].mean()
print(f"Tasa supervivencia: {supervivencia:.1%}")

# Por género
print(df_clean.groupby('Sex')['Survived'].mean())
```

**Usar en ejercicio**:
- E14: Validación de datos
- E25: ETL completo (limpiar, transformar, guardar)
- E26: EDA (distribuciones, correlaciones)
- E27: Normalización para ML

**Descarga**:
```bash
# Kaggle: https://www.kaggle.com/c/titanic
# O directo: https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv
```

---

#### 3️⃣ World Happiness Report

**Descripción**:
- Encuesta anual de felicidad en 160+ países
- Características: PIB, esperanza de vida, libertad, confianza
- **Objetivo**: Explorar qué hace feliz un país

**Tamaño**: Pequeño (~50 KB por año)

**Características**:
- Datos **socioeconómicos** reales
- Múltiples años (2015-2023)
- Ideal para análisis temporal

**Cómo usarlo en UD2**:
```python
import pandas as pd

df = pd.read_csv('world-happiness-report.csv')
# ⚠️ Los nombres de columnas cambian según el año/versión del fichero
# (p. ej. 'Life Ladder' o 'Ladder score'; 'Country' o 'Country name').
# Compruébalos siempre con df.columns y adapta el código.

# Explorar
print(df.columns)
print(df.head(10))

# Estadísticas
print(df['Life Ladder'].describe())  # Score felicidad

# Comparar países
top5 = df.nlargest(5, 'Life Ladder')[['Country name', 'Life Ladder']]
print(top5)

# Análisis por región
if 'Region' in df.columns:
    print(df.groupby('Region')['Life Ladder'].mean())

# Visualizar
import matplotlib.pyplot as plt
df.sort_values('Life Ladder', ascending=False).head(10).plot(
    x='Country name', y='Life Ladder', kind='barh'
)
plt.show()
```

**Usar en ejercicio**:
- E16: Agrupar por región/año
- E22: GroupBy y agregación
- E23: Gráficos comparativos
- E26: Correlación entre variables

**Descarga**:
```bash
# Kaggle: https://www.kaggle.com/datasets/ajaypalsinghlo/world-happiness-report-2023
# O: https://worldhappiness.report/
```

---

#### 4️⃣ House Prices Dataset (Kaggle)

**Descripción**:
- 1,460 casas en Ames, Iowa
- **Objetivo**: Predecir precio de venta
- 79 características: tamaño, habitaciones, año, condición

**Tamaño**: Mediano (~500 KB)

**Características**:
- Datos **reales complejos**
- Contiene muchas variables
- Perfecto para aprender **feature engineering**

**Cómo usarlo en UD2**:
```python
import pandas as pd
import numpy as np

df = pd.read_csv('house-prices-advanced-regression-techniques/train.csv')

print(df.shape)           # (1460, 81)
print(df.info())          # Ver tipos

# Explorar precio
print(df['SalePrice'].describe())

# Encontrar correlación con precio
correlaciones = df.corr(numeric_only=True)['SalePrice'].sort_values(ascending=False)
print(correlaciones.head(10))

# Gráfico: Tamaño vs Precio
import matplotlib.pyplot as plt
plt.scatter(df['GrLivArea'], df['SalePrice'])
plt.xlabel('Área')
plt.ylabel('Precio')
plt.show()

# Ejercicio: Normalizar características
from sklearn.preprocessing import StandardScaler
caracteristicas_numericas = df.select_dtypes(include=[np.number]).columns
df_normalizado = df.copy()
df_normalizado[caracteristicas_numericas] = StandardScaler().fit_transform(
    df[caracteristicas_numericas]
)
```

**Usar en ejercicio**:
- E22: Análisis y agregación
- E25: ETL real (muchas transformaciones)
- E26: EDA en profundidad
- E27: Normalización necesaria para ML

**Descarga**:
```bash
# Kaggle: https://www.kaggle.com/c/house-prices-advanced-regression-techniques
# Descargar: train.csv
```

---

### Matriz de Datasets por Ejercicio

| Dataset | E15 | E17 | E20-E22 | E25 | E26 | E27 |
|---------|-----|-----|---------|-----|-----|-----|
| **Iris** | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| **Titanic** | ✅ | ✅✅ | ✅✅ | ✅✅ | ✅✅ | ✅✅ |
| **Happiness** | ✅ | ✅ | ✅✅ | ✅ | ✅✅ | ⚠️ |
| **House Prices** | ⚠️ | ✅✅ | ✅✅ | ✅✅ | ✅✅ | ✅✅ |

**Recomendación por progreso**:
1. **Empezar**: Iris (simple, limpio)
2. **Intermedio**: Titanic (datos reales, imperfecciones)
3. **Avanzado**: House Prices (complejidad real)
4. **Exploración**: World Happiness (diferentes enfoques)

---

### Cómo Descargar y Usar Datasets

**Opción 1: Desde Kaggle (Recomendado)**
```bash
# Instalar kaggle CLI
pip install kaggle

# Configurar: https://www.kaggle.com/settings/account
# Descargar: cp kaggle.json ~/.kaggle/

# Descargar dataset
kaggle datasets download -d ajaypalsinghlo/world-happiness-report-2023

# Extraer
unzip world-happiness-report-2023.zip
```

**Opción 2: Descarga manual**
```bash
# Ir a Kaggle, buscar dataset
# Hacer click en "Download"
# Guardar en carpeta del proyecto
```

**Opción 3: Desde sklearn (solo Iris)**
```python
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris(as_frame=True)
df = iris.frame          # DataFrame listo con columna 'target'
print(df.head())
```

---

## 📝 GUÍA PRÁCTICA: CÓMO USAR ESTOS CONCEPTOS

### Para resolver E1-E3 (I/O básico)
**Conceptos necesarios**: Secciones 1, 2.1, 3.1
**Tiempo**: 1 hora
**Verificación**: Tu código ejecuta sin errores y produce salida

### Para resolver E4-E6 (Control de flujo)
**Conceptos necesarios**: Secciones 3.1, 3.2
**Tiempo**: 2 horas
**Verificación**: Las condiciones actúan correctamente, los bucles no son infinitos

### Para resolver E7-E9 (Estructuras y funciones)
**Conceptos necesarios**: Secciones 4, 5.1, 5.2
**Tiempo**: 3 horas
**Verificación**: Las funciones devuelven valores correctos

### Para resolver E13-E17 (Datos complejos)
**Conceptos necesarios**: Secciones 5.2, 5.3, 6
**Tiempo**: 4 horas
**Verificación**: Puedes leer CSV y calcular estadísticas

### Para resolver E18-E19 (NumPy)
**Conceptos necesarios**: Secciones 7.1 + referencias NumPy
**Tiempo**: 3 horas
**Verificación**: Arrays funcionan sin bucles, operaciones son rápidas

### Para resolver E20-E22 (Pandas)
**Conceptos necesarios**: Secciones 7.2 + referencias Pandas
**Tiempo**: 4 horas
**Verificación**: DataFrames se cargan, filtran y agrupan correctamente

### Para resolver E23-E27 (Análisis completo)
**Conceptos necesarios**: Secciones 7-9 + referencias sklearn
**Tiempo**: 6 horas
**Verificación**: Gráficos muestran datos significativamente, pipeline ETL funciona

---

## 🎓 PASOS PARA APRENDER EFECTIVAMENTE

1. **Lee la teoría** de la sección correspondiente
2. **Prueba los ejemplos** en tu intérprete Python
3. **Modifica los ejemplos** (cambia valores, crea variaciones)
4. **Lee el enunciado** del ejercicio
5. **Diseña el algoritmo** (pseudocódigo, diagrama flujo)
6. **Implementa el código** paso a paso
7. **Prueba con distintos valores** (casos normales, extremos, errores)
8. **Consulta referencias** cuando no entiendas
9. **Compara con la solución** proporcionada
10. **Reflexiona** sobre lo que aprendiste

---

## 🔗 CONCEPTOS QUE SE CONECTAN

```
Ejercicio 1-3 (print, input)
    ↓
Ejercicio 4-6 (if, for)
    ↓
Ejercicio 7-9 (listas, funciones)
    ↓
Ejercicio 13-17 (dicts, CSV, estadísticas)
    ↓
Ejercicio 18-19 (NumPy: rápido)
    ↓
Ejercicio 20-22 (Pandas: automático)
    ↓
Ejercicio 23-24 (Matplotlib: visualización)
    ↓
Ejercicio 25-27 (ETL, EDA: completo)
    ↓
  ╔════════════════════════════════════╗
  ║  UD2 ← PUENTE → SIGUIENTE CURSO    ║
  ╠════════════════════════════════════╣
  ║ UD3: NLP (lenguaje natural)        ║
  ║ - Aplicar ETL a textos masivos     ║
  ║ - Análisis de sentimientos         ║
  ║ - Big Data: millones de palabras   ║
  ║                                    ║
  ║ UD4: Visión Artificial             ║
  ║ - Imágenes como datos numéricos    ║
  ║ - Redes convolucionales            ║
  ║ - Big Data: datasets de imágenes   ║
  ║                                    ║
  ║ UD5: Machine Learning              ║
  ║ - NumPy para álgebra lineal        ║
  ║ - Pandas para preparación          ║
  ║ - scikit-learn para algoritmos     ║
  ║ - Big Data: escalar modelos        ║
  ╚════════════════════════════════════╝
```

---

## ✅ CHECKLIST: ¿Domino estos conceptos?

**Conceptos de IA (UD1)**:
- ☐ Distingo dato, información y conocimiento
- ☐ Sé decidir si un sistema es IA (¿aprende?, ¿se adapta?, ¿decide según el contexto?)
- ☐ Represento un problema como espacio de estados y lo resuelvo con búsqueda y poda
- ☐ Explico qué es una función objetivo y el descenso del gradiente
- ☐ Describo un agente con sus cinco componentes, sensores y actuadores
- ☐ Distingo IA clásica, ML y DL, y sensorizar de percibir
- ☐ Explico qué es un sesgo algorítmico y cómo detectarlo en los datos

**Básico**:
- ☐ Variables y tipos de datos
- ☐ Operadores aritméticos
- ☐ Strings y métodos
- ☐ Condicionales if/else
- ☐ Bucles for/while

**Intermedio**:
- ☐ Listas y acceso
- ☐ Diccionarios
- ☐ Funciones con return
- ☐ Slicing (listas[1:3])
- ☐ Comprensión de listas

**Avanzado**:
- ☐ NumPy arrays y operaciones
- ☐ Pandas DataFrames
- ☐ Filtrado y groupby
- ☐ Conceptos estadísticos
- ☐ Matplotlib básico

**Machine Learning (Introducción)**:
- ☐ Diferencia entre supervisado/no supervisado
- ☐ Concepto de entrenamiento y predicción
- ☐ Normalización para ML
- ☐ Relación entre UD2 y UD5

**Librerías del ecosistema IA**:
- ☐ Sé qué hace cada librería (NumPy, Pandas, Matplotlib, Seaborn, scikit-learn, PyTorch)
- ☐ Entiendo que Seaborn sirve para ver los datos y scikit-learn para aprender de ellos
- ☐ Sé en qué unidades se usa PyTorch (UD4, UD5) y por qué NumPy es su base
- ☐ Sé elegir entre scikit-learn (datos en tabla) y PyTorch/Keras (imágenes, texto, audio)

**Aplicaciones de escritorio y web**:
- ☐ Sé guardar un modelo con joblib y cargarlo una sola vez para predecir
- ☐ Sé qué es una API, un endpoint y para qué sirve /predict
- ☐ Entiendo la programación orientada a eventos (botón → función)
- ☐ Sé crear una ventana con tkinter (Label, Entry, Button)
- ☐ Distingo app de escritorio y app web
- ☐ Sé cuándo usar Streamlit (datos) y cuándo Gradio (demos de modelos)

**Redes neuronales e IA generativa**:
- ☐ Distingo IA, ML, Deep Learning e IA generativa
- ☐ Sé qué hace una neurona (pesos, sesgo, activación)
- ☐ Entiendo el ciclo forward → pérdida → backpropagation → actualizar
- ☐ Sé qué son tokens, embeddings y la predicción del siguiente token
- ☐ Sé escribir un buen prompt y sé que hay que verificar las respuestas

**Herramientas complementarias**:
- ☐ Sé por qué un diccionario busca en O(1) (hashing)
- ☐ Sé crear un pipeline de scikit-learn sin fuga de datos
- ☐ Sé automatizar una tarea sencilla (archivos, API)
- ☐ Sé escribir un test con assert o pytest y guardar datos en SQLite

**Big Data (Introducción)**:
- ☐ Las 5 V del Big Data
- ☐ Concepto de ETL a escala empresarial
- ☐ Herramientas: Spark, Hadoop
- ☐ Conexión entre UD2 y UD3/UD4/UD5

---

## 🎯 PRÓXIMOS PASOS

**Después de UD2, estás preparado para**:
1. **UD5: Machine Learning** - Usar Pandas + NumPy para entrenar modelos
2. **UD4: Visión Artificial** - Procesar imágenes como matrices NumPy
3. **UD3: Lenguaje Natural** - Aplicar ETL a textos, análisis de sentimientos
4. **Cloud Computing** - Escalar a Spark, PySpark, Databricks
5. **Análisis de Datos Profesional** - Crear pipelines ETL empresariales

---

**Documento de teoría fundamental y conexión con unidades siguientes**

*Última actualización: Noviembre 2026*
*Sección 0: conceptos fundamentales de IA de la UD1 · Secciones 10-14: Puentes hacia UD3, UD4, UD5, ecosistema de librerías, creación de aplicaciones y ampliación con materiales complementarios*
*Para cuestiones específicas, consulta las referencias externas proporcionadas*
