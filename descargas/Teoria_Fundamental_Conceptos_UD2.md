# Teoría Fundamental y Referencias Externas
## Teoría del curso: de la UD1 a la UD5

Esta teoría es común a **todo el curso**. Empezó como el apoyo de la UD2 (Python para IA) y ha crecido con la UD1 y con la base de la UD3, la UD4 y la UD5. Cada sección lleva una etiqueta con su unidad, en el índice y junto al título: al pulsarla se abre la página de esa unidad. La UD2 no tiene página propia: su desarrollo es esta teoría y los [ejercicios](ejercicios.html).

---

## 📚 Tabla de Contenidos

| Sección | Unidad |
|---------|--------|
| 0. Punto de partida: conceptos fundamentales de IA | [UD1](ud1.html) |
| 1. Fundamentos de programación (nombres, constantes, operadores) | UD2 |
| 2. Tipos de datos en Python (conversión, entrada/salida y formato, cadenas a fondo) | UD2 |
| 3. Estructuras de control (bucles anidados, patrones, problemas numéricos) | UD2 |
| 4. Funciones (argumentos, lambda, map/filter/reduce, recursión, ámbito) | UD2 |
| 5. Estructuras de datos complejas (listas, tuplas, conjuntos, comprensiones, módulos, tablas y CSV sin Pandas) | UD2 |
| 6. Conceptos estadísticos (descriptiva, cuartiles, puntuación z, correlación, contraste de hipótesis) | UD2 |
| 7. Librerías científicas (NumPy: crear, unir, dividir y guardar arrays; Pandas) | UD2 |
| 8. Visualización (Matplotlib) | UD2 |
| 9. ETL y análisis de datos | UD2 |
| 10. Introducción a Machine Learning | [UD5](ud5-ml.html) |
| 11. Introducción a Big Data | UD2 · [UD5](ud5-ml.html) |
| 12. Ecosistema de librerías: PyTorch, scikit-learn y Seaborn | UD2 · [UD3](ud3-vision.html) · [UD5](ud5-ml.html) |
| 13. Crear aplicaciones: escritorio y web, desplegar un modelo e infraestructura como código (Terraform) | UD2 · [UD5](ud5-ml.html) |
| 14. Ampliación: IA, ML, DL y GenAI, pipeline de ML, EDA, redes neuronales, IA generativa, hashing, automatización, testing, algoritmia, buenas prácticas, recursos, redes y grafos, preguntas de repaso tipo entrevista | [UD1](ud1.html) a [UD5](ud5-ml.html), según el apartado |
| 15. Referencias externas, IDEs, datasets y guía práctica | General |

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

**Conexión con UD2**: casi todo lo que programamos en E1–E99 es **programación determinista** (no IA). Es la base imprescindible: los modelos de IA (sección 10, UD5) se construyen encima de ella.

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

**Otras dos formas de formatear** que aparecen en código antiguo y en muchos apuntes. Las tres dan el mismo resultado:

```python
nombre, nota = "Iria", 7
print(f"{nombre}: {nota:.2f}")                 # f-string (Python 3.6+): la recomendada
print("{}: {:.2f}".format(nombre, nota))       # str.format()
print("%s: %.2f" % (nombre, nota))             # operador %: el más antiguo (%s texto, %d entero, %f decimal)
print(f"|{nombre:^10}|", f"|{nombre:*^10}|")   # |   Iria   | |***Iria***|  (centrar y rellenar)
```

Con `%` y varios valores, los paréntesis son obligatorios: `"%s: %.2f" % nombre, nota` da `TypeError` (ejercicio E61).

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

**Más métodos útiles**:

```python
s = "  o can de Marín  "
s.strip(), s.lstrip(), s.rstrip()   # quitar espacios: por los dos lados, la izquierda, la derecha
"o can de marín".capitalize()       # 'O can de marín'   (solo la primera letra)
"o can de marín".title()            # 'O Can De Marín'   (cada palabra)
"banana".count("a")                 # 3
"I love Python".find("Python")      # 7
" ".join("Python é xenial".split()) # normalizar espacios: 'Python é xenial'
```

**Cuidado con las tildes.** Muchos programas de ejemplo cuentan vocales con `ch in "aeiou"`: en gallego o castellano se dejan fuera «á», «é», «ó»… Antes de comparar letras, conviene quitar las tildes con `unicodedata` (E32, E59).

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

> **Ojo:** el valor por defecto se crea **una sola vez**, al definir la función. Si es una lista o un diccionario (`def engadir(nota, lista=[])`), todas las llamadas comparten el mismo objeto y se va llenando. Se usa `None` y se crea dentro: `if lista is None: lista = []` (ver [14.18](#1418-preguntas-de-repaso-de-python-tipo-entrevista)).

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

### 5.3 Tuplas a fondo: registros que no cambian

Una **tupla** es una secuencia **ordenada** e **inmutable**: como una lista, pero una vez creada no se puede cambiar. Admite repetidos y datos de tipos distintos. Se usa para datos que van juntos y no deben modificarse: unas coordenadas, una fecha, una fila de una tabla o los valores que devuelve una función.

**Crear una tupla.** Lo que crea la tupla es la **coma**, no los paréntesis:

```python
coordenadas = (42.39, -8.70)      # latitud y longitud de Marín
t = 10, 20, 30                    # también es una tupla (sin paréntesis)
vacia = ()
una = (5,)                        # una sola: hace falta la coma
no_es = (5)                       # ¡es el número 5!
print(type(una), type(no_es))     # <class 'tuple'> <class 'int'>
print(tuple("IA"), tuple([1, 2])) # ('I', 'A') (1, 2): convertir desde otra secuencia
```

**Leer y recorrer.** Igual que en las listas: índices desde 0, índices negativos y *slicing* (que devuelve otra tupla).

```python
t = (10, 20, 30, 40, 50)
print(t[0], t[-1])        # 10 50
print(t[1:4], t[::-1])    # (20, 30, 40) (50, 40, 30, 20, 10)
for x in t:
    print(x)
```

**Solo dos métodos**, porque no se puede añadir ni quitar nada:

```python
t = (1, 2, 2, 3, 2, 4)
print(t.count(2))         # 3: cuántas veces aparece
print(t.index(2))         # 1: posición de la primera aparición
print(t.index(2, 3))      # 4: la primera a partir de la posición 3
t.index(9)                # ValueError: tuple.index(x): x not in tuple
```

**Operaciones** (todas crean una tupla nueva o devuelven un valor):

| Operación | Ejemplo | Resultado |
|-----------|---------|-----------|
| Longitud | `len((1, 2, 2))` | `3` |
| Unir | `(1, 2) + (3,)` | `(1, 2, 3)` |
| Repetir | `("A",) * 3` | `('A', 'A', 'A')` |
| Pertenencia | `3 in (1, 2, 3)` | `True` |
| Mínimo, máximo, suma | `min(t)`, `max(t)`, `sum(t)` | como en las listas |
| Ordenar | `sorted((3, 1, 2))` | `[1, 2, 3]` (¡una **lista**!) |

**Inmutable, pero con matices.**

```python
t = (1, 2)
t[0] = 9                  # TypeError: 'tuple' object does not support item assignment

a = (1, 2)
b = a
a += (3,)                 # no cambia la tupla: crea otra nueva y la asigna a «a»
print(a, b)               # (1, 2, 3) (1, 2)   b sigue igual (con listas cambiarían las dos, 5.4)

ficha = ("Uxía", [7, 8])  # la tupla guarda una referencia a la lista...
ficha[1].append(9)        # ...y la lista sí se puede cambiar
print(ficha)              # ('Uxía', [7, 8, 9])
```

La tupla no deja cambiar **qué objetos** guarda, pero si uno de ellos es mutable (una lista), su **contenido** sí puede cambiar. Por eso una tupla que contiene listas no es del todo «segura» ni sirve como clave de diccionario.

> **Trampa curiosa:** `ficha[1] += [10]` da `TypeError`... y aun así la lista **sí** cambia. `+=` primero amplía la lista (que se deja) y después intenta volver a guardarla en la tupla (que no se deja). Moraleja: no metas listas dentro de tuplas si quieres datos fijos.

**Desempaquetar** es repartir los elementos en variables. Es lo más útil de las tuplas:

```python
nome, idade = ("Brais", 16)

a, b = 5, 10
a, b = b, a                       # intercambiar sin variable auxiliar: (b, a) se crea antes de asignar

primeiro, *resto = [7, 5, 9, 6]   # 7 y [5, 9, 6]: el * recoge «lo que sobre» en una lista
*_, ultimo = [7, 5, 9, 6]         # 6   (_ indica «no me interesa»)

x, y = (1, 2, 3)                  # ValueError: too many values to unpack (expected 2)
```

Muchas funciones de Python devuelven tuplas para desempaquetarlas: `divmod(135, 60)` da `(2, 15)` (2 h 15 min), `enumerate` da parejas `(posición, elemento)`, `zip` junta elementos de varias secuencias, y `dict.items()` da parejas `(clave, valor)`:

```python
for i, (nome, nota) in enumerate([("Iria", 7), ("Noa", 9)], start=1):
    print(i, nome, nota)          # 1 Iria 7 / 2 Noa 9
```

Una función que «devuelve varios valores» devuelve en realidad **una tupla** (4.6):

```python
def resumen(notas):
    return min(notas), max(notas), sum(notas) / len(notas)

minima, maxima, media = resumen([6, 9, 7.5])
print(minima, maxima, media)      # 6 9 7.5
```

**Comparar y ordenar.** Las tuplas se comparan **elemento a elemento**, como las palabras en un diccionario: si el primero empata, decide el segundo. Por eso una tupla sirve de clave para ordenar por varios criterios:

```python
print((8, "Xoán") < (8, "Zaira"))   # True: empatan en 8 y decide el nombre
notas = [("Noa", 8), ("Iria", 6.5), ("Xoán", 8)]
print(sorted(notas, key=lambda p: (-p[1], p[0])))   # nota de mayor a menor y, si empatan, por nombre
# [('Noa', 8), ('Xoán', 8), ('Iria', 6.5)]
```

**Tuplas como claves de diccionario y en conjuntos.** Una tupla de valores inmutables se puede usar como clave (es *hashable*, 14.9); una lista no:

```python
distancias = {("Vigo", "Pontevedra"): 27, ("Pontevedra", "Santiago"): 61}
print(distancias[("Vigo", "Pontevedra")])   # 27

tablero = {(0, 0): "X", (1, 1): "O"}        # casillas de un tres en raya por (fila, columna)
{("Uxía", [7, 8]): 1}                       # TypeError: unhashable type: 'list'
```

**Tuplas con nombre** (`namedtuple`): una tupla cuyos campos tienen nombre. Se lee mejor que `alumno[2]` y sigue siendo inmutable y ligera; es un paso intermedio antes de las clases (14.14):

```python
from collections import namedtuple

Alumno = namedtuple("Alumno", ["nome", "idade", "curso"])
a = Alumno("Antía", 16, "1BAC")
print(a.nome, a[1])               # Antía 16
print(a._replace(curso="2BAC"))   # Alumno(nome='Antía', idade=16, curso='2BAC'): crea otra
```

**¿Tupla o lista?**

| | Tupla | Lista |
|-|-------|-------|
| Sintaxis | `(1, 2, 3)` | `[1, 2, 3]` |
| Se puede cambiar | No | Sí |
| Métodos | `count`, `index` | muchos: `append`, `remove`, `sort`... |
| Clave de diccionario o elemento de conjunto | Sí, si todo lo que contiene es inmutable | No |
| Memoria | algo menos (80 bytes frente a 104 con 5 números, `sys.getsizeof`) | algo más, para poder crecer |
| Uso típico | registro fijo: coordenadas, fechas, filas, varios valores devueltos | colección que cambia: añadir, quitar, ordenar |

> **Ojo con «las tuplas son mucho más rápidas»**: crear una tupla de constantes sí es más rápido, pero recorrer o sumar una tupla o una lista tarda prácticamente lo mismo (compruébalo con `timeit`). La razón para elegir tupla es **la intención**: el dato no debe cambiar, y Python te avisará si alguien lo intenta.

**En IA y datos:** la forma de un array de NumPy o de un DataFrame es una tupla (`df.shape` → `(filas, columnas)`, sección 7); `df.itertuples()` recorre las filas como tuplas con nombre; un píxel RGB es una tupla `(r, g, b)` (UD3), y los bigramas de un texto se cuentan como tuplas de palabras: `zip(palabras, palabras[1:])` (UD4).

Para practicar: [Bloque P · Tuplas](ejercicios.html#bloque-p--tuplas-e83e86).

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

**Quitar elementos: cuatro formas.**

| Forma | Qué quita | Si no existe |
|-------|-----------|--------------|
| `lista.remove(x)` | La **primera** aparición del **valor** `x` | `ValueError: list.remove(x): x not in list` |
| `lista.pop(i)` | El elemento de la **posición** `i` (sin `i`, el último) y lo **devuelve** | `IndexError` (también con la lista vacía) |
| `del lista[i]` o `del lista[i:j]` | Una posición o un trozo | `IndexError` |
| `lista.clear()` | Todo; la variable sigue existiendo, vacía | — |

```python
frutas = ["mazá", "pera", "uva", "pera"]
frutas.remove("pera")              # ['mazá', 'uva', 'pera']: solo la primera
if "kiwi" in frutas:               # comprobar antes evita el ValueError
    frutas.remove("kiwi")
```

Lo mismo pasa con `index(x)`: si `x` no está, da `ValueError`. Se comprueba antes con `x in lista`.

**Cambiar un trozo con *slicing*.** Asignar a un trozo puede cambiar el tamaño de la lista:

```python
n = [1, 2, 3, 4, 5]
n[1:4] = [10, 20]     # 3 elementos por 2:   [1, 10, 20, 5]
n[1:1] = [7, 8]       # trozo vacío = insertar: [1, 7, 8, 10, 20, 5]
n[3:5] = []           # lista vacía = borrar:  [1, 7, 8, 5]
```

**`+` y `*` con listas.** `a + b` une dos listas en una **nueva** y `a * 3` repite la lista tres veces. `lista + 10` da `TypeError`: solo se pueden sumar listas con listas (`lista + [10]`).

**Cinco trampas habituales con listas**

```python
# 1. sort() ordena la lista y devuelve None
a = [3, 1, 2]
a = a.sort()               # a vale None: la lista se ha perdido
a = sorted([3, 1, 2])      # bien: sorted devuelve una lista nueva

# 2. += modifica la lista; + crea otra (importa si hay un alias)
x = [1, 2]; y = x
x = x + [3]                # x: [1, 2, 3]   y: [1, 2]
x = [1, 2]; y = x
x += [3]                   # x: [1, 2, 3]   y: [1, 2, 3]  (la misma lista)

# 3. Repetir una lista de listas repite la MISMA fila
mal = [[0] * 3] * 3
mal[0][0] = 9              # [[9, 0, 0], [9, 0, 0], [9, 0, 0]]
bien = [[0] * 3 for _ in range(3)]
bien[0][0] = 9             # [[9, 0, 0], [0, 0, 0], [0, 0, 0]]

# 4. Borrar mientras se recorre la lista se salta elementos
nums = [1, 2, 2, 3, 2, 4]
for v in nums:
    if v == 2:
        nums.remove(v)
print(nums)                # [1, 3, 2, 4]: ¡queda un 2!
nums = [v for v in nums if v != 2]     # bien: crear una lista nueva

# 5. copy() no copia las sublistas
import copy
orig = [[1, 2], [3, 4]]
sup, prof = orig.copy(), copy.deepcopy(orig)
orig[0].append(99)
print(sup, prof)           # [[1, 2, 99], [3, 4]] [[1, 2], [3, 4]]
```

**Listas de listas (matrices).** Una tabla se guarda como una lista de filas y se accede con dos índices: `m[fila][columna]`.

```python
m = [[1, 2, 3],
     [4, 5, 6]]
m[1][2]                                   # 6: fila 1, columna 2
for fila in m:                            # recorrer fila a fila
    print(*fila)                          # 1 2 3 / 4 5 6
traspuesta = [list(c) for c in zip(*m)]   # [[1, 4], [2, 5], [3, 6]]
suma_filas = [sum(f) for f in m]          # [6, 15]
suma_columnas = [sum(c) for c in zip(*m)] # [5, 7, 9]
```

`zip(*m)` reparte las filas como argumentos de `zip`, que las recorre a la vez y devuelve las columnas. Para matrices grandes o cálculo numérico se usa NumPy ([7.1](#71-numpy-computación-numérica)).

**Recetas útiles**

```python
list(dict.fromkeys([3, 1, 3, 2, 1]))      # [3, 1, 2]: sin repetidos y manteniendo el orden
alumnado = [{"nome": "Brais", "nota": 7.5}, {"nome": "Uxía", "nota": 9},
            {"nome": "Antía", "nota": 7.5}]
sorted(alumnado, key=lambda a: (-a["nota"], a["nome"]))
# Uxía 9, Antía 7.5, Brais 7.5: nota de mayor a menor y, si empatan, por nombre
```

`set(lista)` también quita repetidos, pero **pierde el orden**.

**Errores típicos con listas**

| Error | Ejemplo | Causa | Solución |
|-------|---------|-------|----------|
| `IndexError: list index out of range` | `[10, 20, 30][5]` | Posición que no existe | Comprobar con `len()`; recordar que el último es `len(lista) − 1` |
| `TypeError: 'int' object is not iterable` | `for x in 10:` | Recorrer algo que no es una secuencia | `for x in range(10)` o una lista |
| `AttributeError: 'list' object has no attribute 'add'` | `nums.add(4)` | Método que no existe (`add` es de los conjuntos) | `nums.append(4)` |
| `ValueError: ... x not in list` | `nums.remove(5)` | El valor no está | Comprobar antes con `in` |
| `TypeError: can only concatenate list (not "int") to list` | `nums + 10` | Sumar una lista y un número | `nums + [10]` o `nums.append(10)` |

Los ejercicios [E70–E74](ejercicios.html#bloque-m--listas-a-fondo-e70e74) practican todo esto.

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
| Datos y decimales | Lista de diccionarios = tabla; `csv.DictReader`; `Decimal` para dinero | Sumar textos de un CSV; `0.1 + 0.2 == 0.3` da `False` |

Para practicar todo esto hay un bloque de ejercicios (E28–E37) en la página de [ejercicios](ejercicios.html#bloque-f--más-práctica-de-python-básico-e28e37).

### 5.9 De Python puro a una tabla de datos

Antes de usar Pandas (sección 7) conviene saber trabajar con datos tabulares **solo con Python**. Así es como llegan muchos datos de una API o de un JSON, y así se entiende qué hace `pd.DataFrame` por dentro.

**Una lista de diccionarios es una tabla**: la lista son las filas y cada diccionario, una fila con `columna → valor`.

```python
socios = [
    {"nombre": "Uxía",  "grupo": "A", "cuota": 30},
    {"nombre": "Brais", "grupo": "B", "cuota": 20},
    {"nombre": "Antía", "grupo": "A", "cuota": 30},
    {"nombre": "Xoán",  "grupo": "B", "cuota": 0},
]
pendientes = [s["nombre"] for s in socios if s["cuota"] == 0]
print(pendientes)                                   # ['Xoán']
print(sum(s["cuota"] for s in socios))              # 80

from collections import Counter
print(Counter(s["grupo"] for s in socios))          # Counter({'A': 2, 'B': 2})
print(max(socios, key=lambda s: s["cuota"])["nombre"])   # Uxía (el primero de los empatados)
```

Lo mismo con Pandas sería `pd.DataFrame(socios)`: si entiendes la versión con bucles, Pandas deja de ser magia.

**Leer y escribir CSV con el módulo `csv`**: `DictReader` devuelve cada fila como un diccionario con los nombres de la cabecera.

```python
import csv

with open("socios.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.DictWriter(f, fieldnames=["nombre", "grupo", "cuota"])
    escritor.writeheader()
    escritor.writerows(socios)

with open("socios.csv", encoding="utf-8") as f:     # with cierra el archivo solo
    filas = list(csv.DictReader(f))

print(filas[0])                     # {'nombre': 'Uxía', 'grupo': 'A', 'cuota': '30'}
print(filas[0]["cuota"] + filas[1]["cuota"])         # 3020  ← ¡se juntan dos textos!
print(sum(int(f["cuota"]) for f in filas))           # 80
```

**Todo lo que sale de un CSV es texto**: `'30' + '20'` da `'3020'`. Hay que convertir con `int()` o `float()` antes de operar. Con tildes, indica siempre `encoding="utf-8"`.

**Limpiar valores sucios fila a fila.** Los datos reales llegan con errores. En lugar de que el programa se pare en la primera fila mala, se captura **el error concreto** y se marca el valor como desconocido (`None`), para revisarlo después:

```python
crudos = ["4500", "3.000", "", "dous mil", "1250,5"]

def a_numero(texto):
    try:
        return float(texto.replace(".", "").replace(",", "."))   # formato español
    except ValueError:
        return None

limpios = [a_numero(v) for v in crudos]
print(limpios)        # [4500.0, 3000.0, None, None, 1250.5]
print(f"{limpios.count(None)} valores para revisar")   # 2 valores para revisar
```

Un `except:` **sin indicar el error** también atraparía fallos de programación (un nombre mal escrito, por ejemplo) y los escondería. Se captura solo lo que se espera, aquí `ValueError`.

**Decimales y dinero.** Los `float` se guardan en binario y muchos decimales no son exactos:

```python
print(0.1 + 0.2)                  # 0.30000000000000004
print(round(2.675, 2))            # 2.67 (no 2.68: 2.675 se guarda como 2.67499999…)

from decimal import Decimal, ROUND_HALF_UP
print(Decimal("2.675").quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))   # 2.68
```

Para comparar decimales se usa `math.isclose(a, b)` en lugar de `==`; para dinero, `Decimal` creado **a partir de texto** (`Decimal(2.675)` arrastraría el error del float) o trabajar en céntimos con enteros. Y se redondea **al final**, no en cada paso.

| Trampa | Qué pasa | Cómo evitarla |
|--------|----------|---------------|
| Sumar columnas de un CSV | Se juntan textos: `'30' + '20'` = `'3020'` | `int()` / `float()` al leer |
| `except:` sin tipo | Esconde errores de programación | `except ValueError:` |
| `0.1 + 0.2 == 0.3` | `False` | `math.isclose()` |
| `round()` con dinero | 2.675 → 2.67 | `Decimal("2.675")` o céntimos |
| `print` en lugar de `return` | La función devuelve `None` | Devolver el resultado; imprimir fuera |

Los ejercicios E38–E41 de la página de [ejercicios](ejercicios.html#bloque-g--tablas-csv-y-datos-sucios-sin-pandas-e38e41) practican todo esto con un CSV de una biblioteca escolar.

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

### 6.5 Varianza y desviación: población o muestra

La **varianza** es la media de los cuadrados de las distancias a la media; la **desviación típica** es su raíz cuadrada, y se mide en las mismas unidades que los datos. Hay dos versiones, y cada librería usa una por defecto:

| | Divide entre | NumPy | Pandas | `statistics` |
|---|---|---|---|---|
| **De la población** (todos los datos que existen) | n | `np.std(x)` (por defecto) | `s.std(ddof=0)` | `pstdev(x)` |
| **De una muestra** (una parte, para estimar la de todos) | n − 1 | `np.std(x, ddof=1)` | `s.std()` (por defecto) | `stdev(x)` |

```python
import numpy as np, pandas as pd
A = [10, 2, 3, 4, 5, 6, 7, 8, 9, 10]
np.std(A)              # 2.728  (población)
pd.Series(A).std()     # 2.875  (muestra)
```

Los dos resultados son correctos; solo responden a preguntas distintas. Si el mismo cálculo da cifras diferentes en NumPy y en Pandas, casi siempre es por esto. Con muchos datos, la diferencia es despreciable.

Para la **moda**, `statistics.multimode([1, 1, 2, 2, 3])` devuelve todas las modas (`[1, 2]`); `Counter` o `scipy.stats.mode` dan solo una.

### 6.6 Cuartiles, percentiles y valores atípicos

Los **cuartiles** parten los datos ordenados en cuatro partes iguales: Q1 (25 %), la mediana (50 %) y Q3 (75 %). Un **percentil** es lo mismo con cualquier porcentaje: estar en el percentil 90 significa superar al 90 % de los datos. No hace falta ordenar antes: las funciones lo hacen solas.

```python
tiempos = [12, 14, 13, 15, 14, 16, 13, 41, 15, 14]    # minutos para llegar al instituto
q1, q3 = np.quantile(tiempos, [0.25, 0.75])           # 13.25 y 15.0
iqr = q3 - q1                                         # rango intercuartílico: 1.75
atipicos = [t for t in tiempos if t < q1 - 1.5 * iqr or t > q3 + 1.5 * iqr]   # [41]
np.mean(tiempos), np.median(tiempos)                  # 16.7 y 14.0
```

El **rango intercuartílico** (IQR = Q3 − Q1) mide la dispersión del 50 % central, y la regla de 1,5·IQR es la que dibuja los puntos sueltos de un diagrama de caja. Un solo día de 41 minutos sube la media a 16,7 pero apenas mueve la mediana (14): con valores atípicos, la mediana describe mejor el caso típico. Qué hacer con un atípico (¿error o dato real?) se decide en el [EDA](#146-checklist-de-análisis-exploratorio-de-datos-eda).

### 6.7 Estandarizar: la puntuación z

Para comparar datos en escalas distintas se **estandariza**: `z = (x − media) / desviación`. La z dice a cuántas desviaciones típicas está un valor de la media.

```python
mates = np.array([4, 6, 7, 8, 5])
fisica = np.array([3, 4, 5, 9, 4])
z = lambda x: (x - x.mean()) / x.std()
z(mates)     # [-1.41  0.    0.71  1.41 -0.71]
z(fisica)    # [-0.95 -0.48  0.    1.91 -0.48]
```

El cuarto alumno tiene un 8 en Mates y un 9 en Física, pero el 9 es más destacado (z = 1,91 frente a 1,41) porque en Física el grupo sacó notas más bajas. Un valor con |z| > 3 suele considerarse atípico.

`StandardScaler` de scikit-learn hace exactamente esto con cada columna ([UD5](ud5-ml.html)). Ojo con una idea muy repetida: estandarizar **no convierte los datos en una distribución normal**. Solo los desplaza y cambia de escala; si la distribución era asimétrica (como los ingresos), sigue igual de asimétrica, con media 0 y desviación 1.

### 6.8 Correlación y recta de regresión

La **correlación de Pearson** (`r`) mide si dos variables numéricas suben o bajan juntas **en línea recta**: va de −1 a 1; cerca de 0 significa que no hay relación lineal (puede haber otra).

```python
from scipy import stats
horas = [1, 2, 2, 3, 4, 5, 6, 7]                     # horas de estudio
nota = [3.5, 4.0, 5.5, 5.0, 6.5, 7.0, 8.5, 8.0]
r = np.corrcoef(horas, nota)[0, 1]                   # 0.947
recta = stats.linregress(horas, nota)
recta.slope, recta.intercept                         # 0.81 y 2.964
recta.slope * 4.5 + recta.intercept                  # 6.61: predicción para 4,5 h
```

La **pendiente** (0,81) es lo que sube la nota por cada hora más; la **ordenada en el origen** (2,964), la nota estimada con 0 horas. Para predecir se usan las dos: algunos apuntes escriben la ordenada a mano o la olvidan, y la recta queda desplazada. Y siempre: **correlación no es causalidad**, y la recta solo vale dentro del rango de los datos (con 20 horas predeciría un 19,2).

### 6.9 ¿Diferencia real o casualidad? Contraste de hipótesis

Un grupo que repasó con cuestionarios sacó de media 7,08 y otro sin cuestionarios, 5,92. ¿Funcionan los cuestionarios o es casualidad? Un **contraste de hipótesis** responde a esta pregunta: si en realidad no hubiera ninguna diferencia (**hipótesis nula**), ¿sería raro ver una diferencia tan grande como esta solo por azar?

La forma más intuitiva de responder es **simularlo**: mezclar las notas de los dos grupos, repartirlas al azar muchas veces y contar cuántas veces sale una diferencia igual o mayor.

```python
a = np.array([6.5, 7.0, 5.5, 8.0, 7.5, 6.0, 7.0, 8.5, 6.5, 7.5, 9.0, 6.0])   # con cuestionarios
b = np.array([5.5, 6.0, 7.0, 5.0, 6.5, 6.0, 4.5, 7.5, 5.5, 6.5, 6.0, 5.0])   # sin cuestionarios
dif_real = a.mean() - b.mean()                       # 1.17

rng = np.random.default_rng(42)
todas, extremas = np.concatenate([a, b]), 0
for _ in range(10_000):
    rng.shuffle(todas)                               # repartir al azar entre los dos grupos
    if abs(todas[:12].mean() - todas[12:].mean()) >= abs(dif_real):
        extremas += 1
print(extremas / 10_000)                             # 0.0108: el p-valor
```

Solo en un 1 % de los repartos al azar sale una diferencia tan grande. Ese porcentaje es el **p-valor**. Por convenio, si es menor que 0,05 se dice que la diferencia es **estadísticamente significativa**: es poco probable que se deba solo al azar.

La **prueba t** llega a casi lo mismo con una fórmula, suponiendo que los datos son aproximadamente normales:

```python
t, p = stats.ttest_ind(a, b, equal_var=False)        # t = 2.94, p = 0.0078
```

`equal_var=False` es la **prueba de Welch**, que no supone que los dos grupos tengan la misma dispersión; es la opción recomendable por defecto. Basta con mirar el p-valor: no hace falta buscar valores críticos en tablas.

**Cómo no interpretarlo:**

- Con **pocos datos**, casi nada sale significativo: con solo los 4 primeros alumnos de cada grupo, p = 0,24. «No significativo» no significa «no hay diferencia», sino «no hay pruebas suficientes».
- Con **muchos datos**, cualquier diferencia minúscula sale significativa: con 20 000 alumnos por grupo, una diferencia de 0,04 puntos da p = 0,004. Significativo no es lo mismo que **importante**: hay que mirar también el tamaño de la diferencia.
- El p-valor **no** es la probabilidad de que la hipótesis nula sea cierta.
- Este estudio no demuestra que los cuestionarios causen la mejora: si los grupos no se formaron al azar, puede haber otras diferencias entre ellos.

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

**Más formas de crear arrays**:
```python
np.linspace(0, 1, 5)          # [0.   0.25 0.5  0.75 1.  ]: 5 valores igual de separados, ¡incluye el final!
np.full((2, 3), 7)            # matriz 2×3 llena de sietes
np.eye(3)                     # matriz identidad 3×3 (unos en la diagonal); np.identity(3) es lo mismo

rng = np.random.default_rng(42)          # generador con semilla: siempre los mismos números
rng.random((2, 3))                       # decimales entre 0 y 1 (sin llegar a 1)
rng.integers(1, 11, size=(2, 3))         # enteros del 1 al 10: ¡el final no se incluye!
```

`arange(0, 10, 2)` excluye el final, como `range`; `linspace(0, 1, 5)` lo incluye. Las funciones antiguas `np.random.rand` y `np.random.randint` siguen funcionando, pero hoy se recomienda el generador `default_rng`, que hace los resultados repetibles y no depende de un estado global.

**Forma de un array: `shape`, `ndim`, `dtype` y `reshape`**:
```python
a = np.arange(6).reshape(2, 3)    # [[0 1 2]
                                  #  [3 4 5]]
a.shape, a.ndim, a.dtype, a.size  # (2, 3) 2 int64 6: forma (una tupla, 5.3), dimensiones, tipo y n.º de elementos
a.reshape(3, -1)                  # 3 filas y «las columnas que hagan falta»: (3, 2)
a.flatten()                       # [0 1 2 3 4 5]: aplanar a una dimensión
```

`reshape` solo funciona si el número de elementos encaja: 6 elementos pueden ser 2×3 o 3×2, pero no 4×2 (`ValueError`). Es lo que se hace con las imágenes antes de una red densa (UD3): una imagen de 28×28 se convierte en un vector de 784.

**Máscaras: filtrar sin bucles**:
```python
notas = np.array([4.5, 7, 9.5, 3, 6])
notas > 5                             # [False  True  True False  True]
notas[notas > 5]                      # [7.  9.5 6. ]
np.where(notas >= 5, "AP", "SS")      # ['SS' 'AP' 'AP' 'SS' 'AP']
(notas >= 5).sum(), (notas >= 5).mean()   # 3 aprobados, 0.6 = 60 %
```

Para combinar condiciones se usan `&` (y), `|` (o) y `~` (no), **con paréntesis**: `notas[(notas >= 5) & (notas < 7)]`. Con `and` y `or` da error, igual que en Pandas.

**Unir y dividir arrays**:
```python
a = np.arange(6).reshape(2, 3)        # [[0 1 2] [3 4 5]]
b = np.array([[10, 20, 30]])

np.vstack((a, b))                     # una fila más debajo: 3×3 (= np.concatenate((a, b)))
np.hstack((a, a))                     # columnas al lado: 2×6 (= np.concatenate((a, a), axis=1))

x = np.arange(10)
np.split(x, 2)                        # dos trozos de 5
np.split(x, 3)                        # ValueError: array split does not result in an equal division
np.array_split(x, 3)                  # trozos de 4, 3 y 3: no exige partes iguales
np.split(x, [3, 7])                   # cortar por las posiciones 3 y 7: [0 1 2] [3 4 5 6] [7 8 9]
```

`vstack` necesita el mismo número de **columnas**, y `hstack`, el mismo número de **filas**. `np.split(x, 3)` solo funciona si el tamaño es divisible entre 3; para repartir datos en lotes casi iguales se usa `array_split`.

**Matrices**:
```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

A @ B                # producto de matrices (forma recomendada; np.dot(A, B) es lo mismo)
A * B                # ¡elemento a elemento! No es el producto de matrices
A.T                  # transpuesta
A @ np.eye(2)        # la identidad no cambia la matriz: [[1. 2.] [3. 4.]]
```

**Guardar y cargar arrays**:
```python
np.save("notas.npy", notas)                       # un array, formato binario de NumPy
np.load("notas.npy")                              # [4.5 7.  9.5 3.  6. ]
np.savez("datos.npz", notas=notas, matriz=A)      # varios arrays con nombre en un archivo
d = np.load("datos.npz"); d["matriz"]             # se recuperan por su nombre: d.files → ['notas', 'matriz']
np.savetxt("notas.csv", notas.reshape(1, -1), delimiter=",", fmt="%.1f")   # texto: 4.5,7.0,9.5,3.0,6.0
np.loadtxt("notas.csv", delimiter=",")
```

`.npy` y `.npz` guardan exactamente la forma y el tipo, y se leen muy rápido, pero solo los entiende NumPy. Para compartir datos con otras personas o con una hoja de cálculo es mejor un CSV, y para tablas con columnas de distinto tipo, Pandas (7.2). Se practica en el [ejercicio E88](ejercicios.html#bloque-q--de-las-chuletas-al-código-e87e90).

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

### 7.3 Pandas a fondo

La sección 7.2 da lo mínimo. Esta recorre las operaciones que se usan en casi cualquier análisis, con un mismo ejemplo: las notas (inventadas) de un grupo de 1º BAC.

```python
import pandas as pd
import numpy as np

notas = pd.DataFrame({
    "alumno":  ["Uxía", "Brais", "Antía", "Xoán", "Iria", "Martín"],
    "grupo":   ["A", "B", "A", "B", "A", "B"],
    "mates":   [8.5, 4.0, 9.25, np.nan, 6.5, 5.75],
    "fisica":  [7.0, 5.5, 8.0, 4.5, np.nan, 6.0],
    "faltas":  [2, 11, 0, 7, 3, 5],
})
```

**Series e índice.** Cada columna es una **Series**: una lista de valores con un **índice** (las etiquetas de las filas). Por defecto el índice es 0, 1, 2…, pero puede ser cualquier cosa:

```python
s = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
s["b"]            # 20   por etiqueta
s.iloc[-1]        # 40   por posición (también negativa)
s["a":"c"]        # a, b, c: con etiquetas el final SÍ se incluye
s.iloc[0:2]       # a, b:    con posiciones, el final NO se incluye (como en Python)
```

**`loc` frente a `iloc`.** Es la fuente de errores más común:

| | `df.loc[filas, columnas]` | `df.iloc[filas, columnas]` |
|-|---------------------------|----------------------------|
| Usa | **Etiquetas** (nombres del índice y de columnas) y condiciones | **Posiciones** (0, 1, 2…) |
| Rango `a:b` | Incluye el final | No incluye el final |
| Ejemplo | `notas.loc[notas["grupo"] == "A", ["alumno", "mates"]]` | `notas.iloc[:3, 0:3]` |

En Pandas actual, `s[-1]` con el índice por defecto **da error** (`KeyError`: busca la etiqueta −1, que no existe). Para posiciones, siempre `iloc`. Muchos apuntes antiguos usan `s[-1]` y en su versión funcionaba.

**Filtrar.** Las condiciones se combinan con `&` (y), `|` (o) y `~` (no), **cada una entre paréntesis**:

```python
notas[(notas["grupo"] == "A") & (notas["mates"] >= 7)]          # Uxía y Antía
notas[notas["alumno"].isin(["Brais", "Xoán"])]
notas[notas["faltas"].between(3, 7)]                            # incluye 3 y 7
notas.query("faltas > 5 and grupo == 'B'")                      # lo mismo, escrito como texto
```

Con `and` / `or` de Python da error (`ValueError: The truth value of a Series is ambiguous`): una columna tiene muchos valores, no uno.

**Crear, cambiar y borrar columnas.**

```python
notas["media"] = notas[["mates", "fisica"]].mean(axis=1)        # media de cada fila (ignora NaN)
notas["estado"] = np.where(notas["media"] >= 5, "apto", "no apto")
notas["nivel"] = pd.cut(notas["media"], bins=[0, 5, 7, 9, 10],
                        labels=["IN", "SU/BI", "NT", "SB"], right=False)
notas.loc[notas["faltas"] > 10, "aviso"] = "absentismo"         # cambiar solo algunas filas
notas = notas.rename(columns={"fisica": "física"})
notas = notas.drop(columns=["aviso"])
```

`np.where` es un `if` para columnas enteras y `pd.cut` reparte números en tramos. Ojo con `mean(axis=1)`: ignora los huecos, así que a Xoán, sin nota de mates, le calcula la media solo con física (4,5). Para cambiar **algunas filas** de una columna, siempre `df.loc[condición, "columna"] = valor`, en un solo paso. La forma encadenada `df[condición]["columna"] = valor` **no cambia nada** en Pandas 3 (y en Pandas 2 daba un aviso): modifica una copia temporal.

**Valores que faltan.** `NaN` significa «no hay dato».

```python
notas.isna().sum()                                  # cuántos faltan por columna
notas["mates"].fillna(notas["mates"].median())      # rellenar con la mediana
notas.dropna(subset=["física"])                     # quitar filas sin nota de física
notas.dropna(subset=["mates", "física"])            # quitar a quien le falte alguna de las dos
```

Antes de rellenar, conviene preguntarse **por qué falta**: si Xoán no tiene nota de mates porque no se presentó, rellenar con la mediana le inventa una nota de 6,5. A veces es mejor dejarlo como `NaN` o crear una columna «no presentado».

**Ordenar y quedarse con los primeros.**

```python
notas.sort_values(["grupo", "media"], ascending=[True, False])   # por grupo y, dentro, de mayor a menor
notas.nlargest(3, "media")                                       # los tres mejores
```

**Agrupar con varias funciones a la vez** (agregación con nombre):

```python
resumen = notas.groupby("grupo").agg(
    alumnos=("alumno", "count"),
    media_mates=("mates", "mean"),
    max_faltas=("faltas", "max"),
)
print(resumen.round(2))
#        alumnos  media_mates  max_faltas
# grupo
# A            3         8.08           3
# B            3         4.88          11
```

`count` cuenta los valores **no vacíos**: si se usara con `mates`, el grupo B daría 2, porque a Xoán le falta la nota. Para una tabla de doble entrada: `pd.pivot_table(notas, index="grupo", columns="estado", values="alumno", aggfunc="count")`.

**Unir tablas: `merge` y `concat`.**

```python
optativas = pd.DataFrame({"alumno": ["Uxía", "Brais", "Antía", "Lucía"],
                          "optativa": ["TIC", "Francés", "TIC", "Música"]})

pd.merge(notas, optativas, on="alumno")                  # inner: solo los que están en las dos (3)
pd.merge(notas, optativas, on="alumno", how="left")      # todas las notas; NaN si no hay optativa (6)
pd.merge(notas, optativas, on="alumno", how="outer", indicator=True)   # todos, y de dónde viene cada fila (7)

grupo_c = pd.DataFrame({"alumno": ["Noa"], "grupo": ["C"], "mates": [7.0]})
pd.concat([notas, grupo_c], ignore_index=True)           # apilar filas (columnas que faltan → NaN)
```

| Operación | Une por | Como en SQL |
|-----------|---------|-------------|
| `merge(..., how="inner")` | Una columna común; solo coincidencias | `INNER JOIN` |
| `merge(..., how="left")` | Todas las filas de la izquierda | `LEFT JOIN` |
| `merge(..., how="outer")` | Todas las filas de las dos | `FULL OUTER JOIN` |
| `concat([a, b])` | Pone una tabla **debajo** de otra (o al lado, con `axis=1`) | `UNION` |

`indicator=True` añade la columna `_merge` (`both`, `left_only`, `right_only`) y es la forma más rápida de ver qué no ha casado: aquí, Lucía tiene optativa pero no notas. Si la columna de unión tiene repetidos por error, `merge` **multiplica filas**; `validate="one_to_one"` lo detecta.

**Aplicar funciones.**

| Método | Se aplica a | Ejemplo |
|--------|-------------|---------|
| `Series.map(f o dict)` | Cada valor de una columna | `notas["grupo"].map({"A": "mañana", "B": "tarde"})` |
| `Series.apply(f)` | Cada valor de una columna | `notas["alumno"].apply(len)` |
| `DataFrame.apply(f, axis=1)` | Cada **fila** | `notas.apply(lambda f: f["mates"] - f["física"], axis=1)` |
| `DataFrame.map(f)` | Cada celda de la tabla | `notas[["mates", "física"]].map(round, na_action="ignore")` |
| `.str.…` | Textos de una columna | `notas["alumno"].str.upper()`, `.str.contains("ia")` |

`na_action="ignore"` salta los huecos: sin él, `round(NaN)` daría error. `applymap`, que aparece en muchos apuntes, se llama `DataFrame.map` desde Pandas 2.1 y **ya no existe** en Pandas 3. Y antes de usar `apply`, busca la versión **vectorizada**: `notas["mates"] - notas["física"]` hace lo mismo que el `apply` de la tabla y es decenas de veces más rápido con tablas grandes.

**Fechas.**

```python
entregas = pd.DataFrame({"fecha": ["10/01/2026", "12/01/2026", "15/01/2026", "02/02/2026"],
                         "tarea": ["T1", "T2", "T3", "T4"]})
entregas["fecha"] = pd.to_datetime(entregas["fecha"], dayfirst=True)    # día/mes/año español
entregas["dia_semana"] = entregas["fecha"].dt.day_name()
entregas["dias_desde_anterior"] = entregas["fecha"].diff().dt.days
print(entregas.set_index("fecha").resample("MS")["tarea"].count())      # entregas por mes
```

Sin `dayfirst=True`, «02/02/2026» no da problemas, pero «10/01/2026» podría leerse como 1 de octubre. Con `.dt` se sacan el año, el mes, el día o el nombre del día, y `resample` agrupa por periodos de tiempo (días, semanas `"W"`, meses `"MS"`).

**Leer y escribir archivos.**

| Formato | Leer | Escribir | Detalles |
|---------|------|----------|----------|
| CSV | `pd.read_csv("f.csv", sep=";", decimal=",", encoding="utf-8")` | `df.to_csv("f.csv", index=False)` | Los CSV españoles suelen usar `;` y coma decimal |
| Excel | `pd.read_excel("f.xlsx", sheet_name="Hoja1")` | `df.to_excel("f.xlsx", index=False)` | Necesita `openpyxl` (en Colab ya está) |
| JSON | `pd.read_json("f.json")` | `df.to_json("f.json", orient="records")` | Habitual en APIs |

`index=False` evita guardar el índice como una columna sin nombre que aparece al volver a leer el archivo.

**Gráficos directos.** Todo DataFrame tiene `.plot()` (usa Matplotlib por debajo, sección 8): `resumen["media_mates"].plot(kind="bar")`, `notas.plot(kind="scatter", x="faltas", y="media")`, `notas["media"].plot(kind="hist", bins=5)`.

**Pandas 2 y Pandas 3.** Colab y los ordenadores del aula pueden tener versiones distintas (`pd.__version__`). Lo que más cambia al pasar a Pandas 3: la asignación encadenada deja de funcionar, `applymap` desaparece y las columnas de texto tienen un tipo propio (`str` en lugar de `object`). El código de esta sección funciona en las dos.

| Error típico | Qué pasa | Forma correcta |
|--------------|----------|----------------|
| `s[-1]` con el índice por defecto | `KeyError` | `s.iloc[-1]` |
| `df[cond]["col"] = valor` | No cambia el original | `df.loc[cond, "col"] = valor` |
| `cond1 and cond2` | `ValueError` | `(cond1) & (cond2)` |
| `df.dropna()` sin guardar | El original sigue igual | `df = df.dropna()` |
| `inplace=True` | Funciona, pero se desaconseja y no ahorra memoria | Asignar el resultado: `df = df.rename(...)` |
| `merge` con claves repetidas | Filas multiplicadas sin aviso | `validate="one_to_one"` |
| Guardar sin `index=False` | Aparece una columna «Unnamed: 0» al volver a leer | `to_csv(..., index=False)` |

Los ejercicios E53–E58 de la página de [ejercicios](ejercicios.html#bloque-j--pandas-a-fondo-e53e58) practican todo esto.

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
   - **En UD3 y UD5**: Análisis de imágenes, agrupación de datos

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
   └─ Deep Learning con imágenes (UD3)

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

**UD3 (Visión Artificial)**:
- Imágenes = datos estructurados enormes
- Procesamiento en paralelo (similar a Big Data)
- CNNs: redes neuronales para volúmenes masivos

**UD4 (Lenguaje Natural)**:
- NLP con Big Data: procesar millones de textos
- Análisis de sentimientos a escala
- Tokenización, vectorización (análogo a normalización UD2)

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
- 🖼️ UD3: Procesar datasets de imágenes masivos
- 📊 UD4: Aplicar ETL a millones de textos (NLP)
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
| **scikit-learn** | Machine Learning clásico | ¿Cómo entreno un modelo que prediga? | UD2 (intro) → UD4, UD5 |
| **PyTorch** | Deep Learning (redes neuronales) | ¿Cómo entreno una red neuronal profunda? | UD2 (conocer) → UD3, UD5 |
| **TensorFlow/Keras** | Deep Learning (alternativa a PyTorch) | La misma que PyTorch | UD3, UD5 |

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
| **UD3 Visión Artificial** (sesiones 10-15: CNN y Transfer Learning) | Alternativa a TensorFlow/Keras para entrenar redes convolucionales. `torchvision` ofrece datasets (MNIST, CIFAR-10) y modelos preentrenados (ResNet, MobileNet) | Aplicar |
| **UD5 Machine Learning** (bloque de redes neuronales) | Construir una red neuronal sencilla y compararla con los modelos de scikit-learn | Aplicar |
| **UD4 Lenguaje Natural** | Solo como referencia: los modelos de lenguaje modernos (Hugging Face Transformers) funcionan sobre PyTorch | Conocer |

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
| En este curso | Alternativa / ampliación en UD3-UD5 | Herramienta principal prevista en UD3 |

**Recomendación didáctica**: en Bachillerato basta con usar **una** de las dos en profundidad. Keras es más fácil para el primer contacto con CNN (UD3). PyTorch es una buena ampliación para el alumnado más avanzado, o si se quieren usar modelos de Hugging Face.

#### PyTorch paso a paso: de los tensores a guardar el modelo

El ejemplo mínimo de arriba entrena con todos los datos de golpe. Un proyecto real añade cinco piezas: el **dispositivo** (CPU o GPU), los **gradientes automáticos**, la carga de datos **por lotes**, la **evaluación** y **guardar** el modelo. Este es el recorrido completo, en el orden en que se usa.

**1. Tensores: atributos y tipos.**
```python
x = torch.tensor([[1, 2, 3], [4, 5, 6]])
x.shape, x.dtype, x.device       # torch.Size([2, 3]) torch.int64 cpu
x.float()                        # a decimales (float32): lo que esperan las capas de la red
x.long()                         # a enteros largos (int64): lo que espera CrossEntropyLoss en las etiquetas
x.view(3, 2), x.reshape(3, 2)    # cambiar la forma (view solo si el tensor está seguido en memoria; reshape siempre)
x[0], x[:, 1], x[0:1]            # indexar como en NumPy (7.1)
```

**2. CPU o GPU, sin que falle en ningún ordenador.**
```python
dispositivo = "cuda" if torch.cuda.is_available() else "cpu"
modelo = modelo.to(dispositivo)            # el modelo...
X, y = X.to(dispositivo), y.to(dispositivo)  # ...y los datos tienen que estar en el MISMO sitio
```
Si se escribe directamente `torch.device("cuda")`, el `.to(dispositivo)` da error en un ordenador sin tarjeta gráfica de NVIDIA, que es lo normal en el aula (en un Mac con chip Apple se usa `"mps"`). Si el modelo está en la GPU y los datos en la CPU, PyTorch da el error *Expected all tensors to be on the same device*.

**3. Gradientes automáticos (*autograd*).** Es la retropropagación de [14.7](#147-redes-neuronales-desde-cero), pero hecha por PyTorch:
```python
x = torch.tensor(3.0, requires_grad=True)   # «vigila» las operaciones con x
y = x ** 2
y.backward()                                # calcula dy/dx
print(x.grad)                               # tensor(6.): la derivada de x² es 2x, y 2·3 = 6
```

**4. Datos por lotes con `Dataset` y `DataLoader`.** Igual que un generador (14.14), entrega los datos de 32 en 32 y los baraja en cada época:
```python
from torch.utils.data import TensorDataset, DataLoader

datos_train = TensorDataset(X_train, y_train)          # junta entradas y etiquetas
cargador = DataLoader(datos_train, batch_size=32, shuffle=True)
for xb, yb in cargador:                                 # cada vuelta, un lote
    ...
```
Para imágenes, `torchvision` trae datasets (MNIST, CIFAR-10) y **transformaciones** que se aplican a cada imagen al cargarla: `T.Compose([T.Resize((224, 224)), T.ToTensor()])`. Ojo: `T.Resize(224)` con un solo número no deja la imagen en 224×224, sino que pone el **lado menor** a 224 y mantiene la proporción.

**5. El bucle de entrenamiento completo, con evaluación.**
```python
funcion_error = nn.CrossEntropyLoss()
optimizador = torch.optim.Adam(modelo.parameters(), lr=1e-3)

for epoca in range(20):
    modelo.train()                               # modo entrenamiento: dropout y BatchNorm activos
    for xb, yb in cargador:
        xb, yb = xb.to(dispositivo), yb.to(dispositivo)
        pred = modelo(xb)                        # 1. predecir
        error = funcion_error(pred, yb)          # 2. medir el error
        optimizador.zero_grad()                  # 3. borrar los gradientes del lote anterior
        error.backward()                         # 4. calcular los gradientes
        optimizador.step()                       # 5. ajustar los pesos

    modelo.eval()                                # modo evaluación: dropout apagado
    with torch.no_grad():                        # sin guardar gradientes: más rápido y menos memoria
        pred_val = modelo(X_val.to(dispositivo)).argmax(dim=1)
        acierto = (pred_val == y_val.to(dispositivo)).float().mean().item()
    print(f"Época {epoca + 1}: error {error.item():.3f}, acierto en validación {acierto:.1%}")
```
- Si falta `zero_grad()`, los gradientes de cada lote **se suman** a los anteriores y el entrenamiento se descontrola.
- Si después de `eval()` se olvida volver a `train()`, el *dropout* deja de actuar en las épocas siguientes. Por eso `modelo.train()` va al principio de cada época.
- `CrossEntropyLoss` recibe las **puntuaciones** de la última capa (sin `softmax`: ya lo aplica ella) y las etiquetas como números de clase en `long`.
- No conviene llamar igual a la función de error y al valor del error: si se escribe `loss = nn.CrossEntropyLoss()` y luego `loss = loss(pred, y)` dentro del bucle, en el segundo lote `loss` ya no es una función y da error.

**6. Guardar y cargar.** Se guardan los **pesos** (`state_dict`), no el objeto entero:
```python
torch.save(modelo.state_dict(), "modelo.pth")

modelo2 = nn.Sequential(nn.Linear(4, 16), nn.ReLU(), nn.Linear(16, 3))   # la misma arquitectura
modelo2.load_state_dict(torch.load("modelo.pth"))
modelo2.eval()                                   # antes de predecir
```
Desde PyTorch 2.6, `torch.load` carga por defecto solo pesos (`weights_only=True`), porque cargar un objeto cualquiera de un archivo puede ejecutar código malicioso. Es la misma precaución que con `pickle` y `joblib` (13.7): no abrir modelos de origen desconocido.

| Paso | Keras | PyTorch |
|------|-------|---------|
| Definir la red | `keras.Sequential([...])` | `nn.Sequential(...)` |
| Error y optimizador | `model.compile(loss=..., optimizer=...)` | `nn.CrossEntropyLoss()`, `torch.optim.Adam(...)` |
| Entrenar | `model.fit(X, y, epochs=20)` | bucle `for` escrito a mano (paso 5) |
| Evaluar | `model.evaluate(X_test, y_test)` | `model.eval()` + `torch.no_grad()` |
| Guardar | `model.save("modelo.keras")` | `torch.save(model.state_dict(), "modelo.pth")` |

El [ejercicio E89](ejercicios.html#bloque-q--de-las-chuletas-al-código-e87e90) pide encontrar los fallos de los bucles de entrenamiento de las chuletas.

> Código de PyTorch y TensorFlow revisado con la documentación oficial, pero no ejecutado en el entorno de prueba (las librerías no estaban instaladas): pruébalo en Google Colab, que ya las trae.

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
| **Unidades posteriores** | Todas (para mostrar resultados) | UD4 (clasificar textos), UD5 (núcleo de la unidad) |
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
| En el curso | UD4 (clasificar textos con TF-IDF), UD5 (núcleo) | UD3 (CNN, opcional frente a Keras), UD5 (redes neuronales) |

**Regla práctica para el alumnado**: si los datos caben en una tabla, **empieza siempre por scikit-learn**. Pasa a PyTorch o Keras solo cuando trabajes con imágenes, texto o audio, o cuando un modelo clásico no sea suficiente.

**Instalación**:
```bash
pip install seaborn scikit-learn
```

[Referencia: Seaborn tutorial](https://seaborn.pydata.org/tutorial.html)
[Referencia: scikit-learn: Getting Started](https://scikit-learn.org/stable/getting_started.html)
[Referencia: scikit-learn: elegir el estimador adecuado](https://scikit-learn.org/stable/machine_learning_map.html)

### 12.4 Librerías «poco conocidas»: cuáles merecen la pena

En redes circulan listas de librerías «que nadie conoce» y que lo hacen todo con una línea. Algunas son muy útiles; otras ahorran trabajo a costa de **esconder justo lo que hay que aprender**, o llevan años sin actualizarse. Revisión de diez muy compartidas (estado a noviembre de 2026):

| Librería | Qué hace | Veredicto para el curso |
|----------|----------|-------------------------|
| **cleanlab** | Detecta **etiquetas probablemente erróneas** y datos raros a partir de las probabilidades de un modelo (*confident learning*) | ✅ **Útil** en la UD5 y en Análisis de datos: muchos conjuntos reales tienen etiquetas mal puestas. No es magia: señala candidatos que una persona debe revisar |
| **drawdata** | Dibujar con el ratón puntos de dos clases dentro de Jupyter y obtener un DataFrame | ✅ **Muy didáctica**: dibujar datos «difíciles» y ver cómo responden k-NN, un árbol o k-medias (UD5) |
| **black** | Formatea el código automáticamente con un estilo fijo | ✅ **Recomendable**. Hoy también se usa `ruff format`, compatible y mucho más rápido. Enlaza con el estilo de 14.14 |
| **PivotTableJS** (`pivottablejs`) | Tabla dinámica interactiva, arrastrando columnas, en Jupyter | 🟡 Bien para **explorar**, pero no deja código: para el informe, `pd.pivot_table` (7.3) |
| **LazyPredict** | Entrena unos 40 modelos de scikit-learn con su configuración por defecto y los ordena por resultado | 🟡 Solo como **vistazo inicial**. Usa una única división entrenamiento/prueba y no ajusta hiperparámetros; elegir el «ganador» por esa tabla es ajustar con la prueba (fuga de datos, UD5 sección 6). Mantenimiento irregular |
| **PyCaret** | *AutoML* de «poco código»: preparación, comparación, ajuste y despliegue con pocas funciones | 🟡 Interesante para ver un flujo completo, **después** de haberlo hecho a mano. La versión estable no siempre admite la última versión de Python: comprobar antes de instalar |
| **PyTorch Lightning** | Organiza el bucle de entrenamiento de PyTorch (GPU, registros, puntos de control) | 🟡 Ampliación: solo tiene sentido si ya se usa PyTorch (12.2). En el curso basta con Keras |
| **Reflex** | Aplicaciones web completas (interfaz y servidor) escritas solo en Python | 🟡 Alternativa a Streamlit (sección 13) para aplicaciones más grandes; más compleja de aprender |
| **Lux** | Propone gráficos automáticamente al mostrar un DataFrame | ❌ **Abandonada**: la última versión (0.5.1) es de febrero de 2022 y puede no funcionar con Pandas actual. Para un EDA automático, mejor `ydata-profiling` o hacer los gráficos (sección 8) |
| **pyforest** | Importa «por arte de magia» `pd`, `np`, `plt`… cuando se usan, sin escribir los `import` | ❌ **Evitar**: esconde de dónde sale cada nombre, el cuaderno deja de funcionar en otro ordenador sin pyforest y va contra «explícito mejor que implícito» (14.14) |

**Criterios para decidir si usar una librería nueva** (sirven para cualquier lista de este tipo):

1. ¿Cuándo fue la **última versión** (en PyPI) y hay actividad en su repositorio?
2. ¿Funciona con **mi** versión de Python y de Pandas? (`pip install` en un entorno de prueba antes de usarla en clase).
3. ¿Me ahorra trabajo **repetitivo** o me ahorra **entender** algo? Lo primero, bien; lo segundo, solo cuando ya se sabe hacer a mano.
4. ¿Qué pasa con mis datos? Algunas herramientas «gratuitas» suben los datos a un servidor.
5. ¿La recomienda la documentación oficial o solo una publicación con un enlace acortado?

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

Este ejemplo usa una regla sencilla. En UD4 la función `analizar` se sustituye por un modelo entrenado, y en UD3 la entrada pasa a ser una imagen (`inputs="image"`).

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
| **Infraestructura como código** (Terraform, OpenTofu) | Describir en archivos los servidores y servicios de la nube para crearlos, cambiarlos y borrarlos de forma repetible ([13.8](#138-infraestructura-como-código-terraform)) |
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

### 13.8 Infraestructura como código: Terraform

Para que una app con un modelo (13.7) llegue a otras personas hace falta **infraestructura**: un servidor, una base de datos, un almacén de archivos, una red. Se puede crear a mano, haciendo clic en la web de un proveedor de nube, pero así nadie recuerda qué se configuró, es fácil equivocarse y no se puede repetir igual. La **infraestructura como código** (*Infrastructure as Code*, IaC) consiste en **describirla en archivos de texto**, guardarlos en Git como cualquier programa y dejar que una herramienta la cree, la cambie o la borre.

**Terraform** (de HashiCorp, hoy parte de IBM) es la herramienta de IaC más extendida. Funciona con cientos de proveedores: nubes (AWS, Azure, Google Cloud), Docker, GitHub, e incluso archivos del propio ordenador.

**La idea clave: es declarativo.** No se escriben los pasos («crea un servidor, después ábrele el puerto 80...»), sino **el estado final** que se quiere («quiero un servidor con el puerto 80 abierto»). Terraform compara ese estado deseado con el que existe y calcula él solo qué tiene que crear, cambiar o borrar. Por eso aplicar dos veces el mismo archivo no crea dos servidores: la segunda vez responde *No changes* (es **idempotente**).

| Concepto | Qué es | Ejemplo |
|----------|--------|---------|
| **Provider** | El «traductor» para un servicio concreto | `aws`, `azurerm`, `google`, `docker`, `local` |
| **Resource** | Algo que Terraform crea y gestiona | un servidor, un *bucket*, un archivo |
| **Data source** | Algo que ya existe y solo se **lee** | la última imagen de Ubuntu disponible |
| **Variable** | Un valor que se puede cambiar sin tocar el código | la región, el entorno (`dev` o `prod`) |
| **Output** | Un valor que se muestra al terminar | la dirección IP del servidor creado |
| **State** (`terraform.tfstate`) | El archivo donde Terraform apunta lo que ha creado | es su «memoria»: sin él no sabe qué es suyo |
| **Module** | Un grupo de recursos reutilizable, como una función | una red completa que se usa en varios proyectos |

**Un primer ejemplo sin nube y gratis.** El proveedor `local` crea archivos en el propio ordenador. No necesita cuenta, no cuesta dinero y permite ver el ciclo completo en el aula:

```hcl
# main.tf
terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.5"
    }
  }
}

variable "curso" {
  type    = string
  default = "1BAC"
}

resource "local_file" "benvida" {
  filename = "${path.module}/saida/benvida.txt"
  content  = "Benvida ao curso ${var.curso} de Tecnoloxías Intelixentes\n"
}

output "ficheiro" {
  value = local_file.benvida.filename
}
```

El lenguaje se llama **HCL**: bloques con llaves, `nombre = valor` y referencias como `var.curso` o `local_file.benvida.filename`. El ciclo de trabajo es siempre el mismo:

```bash
terraform init        # descarga el proveedor (crea la carpeta .terraform y .terraform.lock.hcl)
terraform fmt         # ordena el formato del código
terraform validate    # comprueba que la sintaxis es correcta
terraform plan        # muestra qué va a hacer, sin hacerlo: "Plan: 1 to add, 0 to change, 0 to destroy."
terraform apply       # lo hace (pide escribir "yes"); crea saida/benvida.txt y el terraform.tfstate
terraform apply -var="curso=2BAC"   # cambia el contenido: el plan avisa de que va a reemplazar el archivo
terraform destroy     # borra todo lo que creó
```

**`plan` antes de `apply`, siempre.** En la nube, un `apply` sin revisar puede borrar una base de datos o crear máquinas que se cobran por horas. `plan` es el momento de leer con calma qué se va a crear (`+`), cambiar (`~`) o destruir (`-`).

**El mismo esquema en la nube.** Así sería un servidor en AWS (el ejemplo que traen muchas chuletas):

```hcl
provider "aws" {
  region = "eu-west-3"                     # París; la región decide dónde están los datos (RGPD)
}

data "aws_ami" "ubuntu" {                  # leer: la imagen de Ubuntu más reciente de Canonical
  most_recent = true
  owners      = ["099720109477"]           # el identificador de Canonical en AWS
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd*/ubuntu-*-24.04-amd64-server-*"]
  }
}

resource "aws_instance" "web" {            # crear: un servidor pequeño
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"
}

output "ip_publica" {
  value = aws_instance.web.public_ip
}
```

Sin el `filter`, `most_recent = true` devolvería la última imagen cualquiera publicada por Canonical, que puede no ser un Ubuntu de servidor. Es un detalle que las chuletas suelen omitir.

**Buenas prácticas y errores típicos:**

- **El archivo de estado es delicado.** `terraform.tfstate` puede guardar contraseñas y claves **en texto claro**. Nunca se sube a Git: en `.gitignore` van `.terraform/`, `*.tfstate` y `*.tfstate.backup`. Lo que sí se sube es `.terraform.lock.hcl`, que fija las versiones de los proveedores.
- **En equipo, estado remoto.** Si dos personas tienen cada una su `tfstate`, Terraform cree cosas distintas en cada ordenador. Se guarda en un **backend remoto** (un *bucket* de S3, Google Cloud Storage o Azure), declarado **dentro** del bloque `terraform { backend "s3" { ... } }`, con bloqueo para que no lo cambien dos personas a la vez.
- **Las claves de acceso nunca en los `.tf`.** Se pasan por variables de entorno o con la herramienta del proveedor (`aws configure`, `az login`, `gcloud auth`). Es la misma regla que en 13.7: sin contraseñas en el repositorio.
- **Variables** para lo que cambia entre entornos, **módulos** para no copiar y pegar, **etiquetas** (*tags*) en los recursos para saber de quién es cada uno y cuánto cuesta, y `output` para lo que otros necesiten saber.
- **Entornos separados** (`dev`, `staging`, `prod`): con `terraform workspace new staging` o, mejor en proyectos grandes, con carpetas distintas.
- **`terraform destroy` al terminar una práctica en la nube**: un servidor olvidado sigue facturando.

**Instalación.** En Windows, descargando el ejecutable de developer.hashicorp.com o con `choco install terraform`; en macOS, `brew tap hashicorp/tap` y `brew install hashicorp/tap/terraform` (el `brew install terraform` de muchas chuletas ya no funciona, porque Homebrew dejó de aceptar versiones nuevas tras el cambio de licencia); en Ubuntu, desde el repositorio `apt` de HashiCorp. Para el aula, el proveedor `local` o el de Docker evitan crear cuentas de nube.

**Licencia y alternativas.** Desde agosto de 2023 (a partir de la versión 1.6), Terraform no es software libre: usa la licencia BSL, que permite usarlo gratis pero no ofrecerlo como servicio que compita con HashiCorp. En respuesta nació **OpenTofu**, una copia libre gestionada por la Linux Foundation que acepta casi los mismos archivos (con la orden `tofu` en lugar de `terraform`). Otras herramientas: **Pulumi** (la infraestructura se escribe en Python u otros lenguajes), **Ansible** (más orientada a configurar servidores que ya existen) y las propias de cada nube (CloudFormation en AWS, Bicep en Azure).

| | Python (todo el curso) | Terraform |
|-|------------------------|-----------|
| Estilo | Imperativo: los pasos, en orden | Declarativo: el resultado final |
| Ejecutar dos veces | Lo repite todo | Si nada ha cambiado, no hace nada |
| Qué produce | Resultados, archivos, modelos | Servidores, redes, permisos... en la nube |
| Dónde encaja | Entrenar y servir el modelo (13.7) | Crear el sitio donde vive ese modelo |

El [ejercicio E90](ejercicios.html#bloque-q--de-las-chuletas-al-código-e87e90) propone leer un plan de Terraform y encontrar los fallos de seguridad de una configuración.

> Los archivos de Terraform de esta sección no se han ejecutado en el entorno de prueba (la herramienta no estaba disponible). Se han revisado con la documentación oficial; pruébalos con Terraform u OpenTofu instalados.

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
| **DL** | Redes neuronales de muchas capas; aprende patrones complejos | Reconocimiento facial, de voz, detección de objetos | UD3 y UD5 |
| **GenAI** | Genera contenido nuevo a partir de lo aprendido | Chatbots (ChatGPT, Claude), generadores de imágenes, asistentes de código | UD4 |

**Machine learning clásico frente a deep learning:**

| Aspecto | ML clásico (árboles, regresión, SVM...) | Deep learning (redes profundas) |
|---------|------------------------------------------|---------------------------------|
| Características | Las elige y prepara una persona (ingeniería de características) | La red las aprende de los datos en bruto (píxeles, palabras); sigue haciendo falta limpiar y preparar los datos |
| Datos | Funciona con cientos o miles de filas | Suele necesitar muchos más, salvo que se parta de un modelo preentrenado (*transfer learning*, UD3) |
| Cálculo | Un portátil basta | A menudo GPU o TPU |
| Interpretación | Más fácil (coeficientes, importancia de variables) | Más difícil: hacen falta técnicas de explicabilidad (UD5, sección 10) |
| Dónde gana | **Tablas** (notas, ventas, sensores): el *gradient boosting* suele igualar o superar a una red | Imágenes, texto, audio, vídeo |
| Ejemplos | Random forest, XGBoost, k vecinos | CNN, RNN y LSTM, Transformers |

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

Base de *Neural Networks Beginner Notes* y *Deep Learning*. Es la introducción a la parte de Deep Learning de **UD3 (Visión Artificial)** y **UD5 (Machine Learning)**.

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

**Retropropagación a mano: una neurona completa.** Con un solo peso, la derivada es inmediata. Con varios, la **regla de la cadena** reparte la culpa del error entre todos ellos: se calcula de atrás hacia delante, de la pérdida a la salida, de la salida a la suma y de la suma a cada peso. Es lo mismo que hacen PyTorch o Keras, solo que ellos lo automatizan para millones de pesos (la idea se inspira en *micrograd*, de A. Karpathy; el código es propio).

```python
import math

x1, x2 = 2.0, -1.0          # entradas
w1, w2, b = 0.5, 1.0, 0.0   # pesos y sesgo iniciales
y_real = 1.0                # respuesta correcta

def sigmoide(z):
    return 1 / (1 + math.exp(-z))

def perdida(w1, w2, b):
    p = sigmoide(w1 * x1 + w2 * x2 + b)
    return (p - y_real) ** 2

# Hacia delante (forward)
z = w1 * x1 + w2 * x2 + b    # 0.0
p = sigmoide(z)              # 0.5
L = (p - y_real) ** 2        # 0.25

# Hacia atrás (backward): cada paso multiplica por la derivada local
dL_dp = 2 * (p - y_real)     # -1.0
dp_dz = p * (1 - p)          # 0.25   derivada de la sigmoide
dL_dz = dL_dp * dp_dz        # -0.25
dL_dw1 = dL_dz * x1          # -0.5
dL_dw2 = dL_dz * x2          #  0.25
dL_db  = dL_dz * 1           # -0.25

# Comprobación numérica: mover un poco el peso y medir cuánto cambia la pérdida
h = 1e-6
print(round((perdida(w1 + h, w2, b) - perdida(w1 - h, w2, b)) / (2 * h), 4))   # -0.5
print(round((perdida(w1, w2 + h, b) - perdida(w1, w2 - h, b)) / (2 * h), 4))   #  0.25

# Entrenar: repetir forward, backward y actualizar
lr = 1.0
for paso in range(1, 31):
    p = sigmoide(w1 * x1 + w2 * x2 + b)
    dL_dz = 2 * (p - y_real) * p * (1 - p)
    w1 -= lr * dL_dz * x1
    w2 -= lr * dL_dz * x2
    b  -= lr * dL_dz
    if paso in (1, 10, 30):
        print(f"paso {paso:2}: predicción {p:.3f}, pérdida {(p - y_real) ** 2:.4f}")
# paso  1: predicción 0.500, pérdida 0.2500
# paso 10: predicción 0.930, pérdida 0.0049
# paso 30: predicción 0.961, pérdida 0.0015
```

Tres cosas que se ven en este ejemplo:

- **El signo dice hacia dónde mover.** `dL_dw1` es negativo: subir `w1` baja el error, así que la actualización `w1 -= lr * dL_dw1` lo sube. `dL_dw2` es positivo porque `x2` es negativo: ese peso tiene que bajar.
- **La comprobación numérica** es la forma de saber si una derivada calculada a mano está bien. Si los dos números no coinciden, hay un error en el *backward*.
- **El aprendizaje se frena.** De 0,93 a 0,96 cuesta 20 pasos, porque cuando la sigmoide se acerca a 1 su derivada `p·(1−p)` se hace muy pequeña. Ese mismo efecto, repetido capa tras capa, es el **desvanecimiento del gradiente** que dificulta entrenar redes profundas con sigmoides, y una de las razones por las que hoy se usa ReLU en las capas ocultas.

> **Prueba tú:** cambia `y_real` a `0.0` y predice antes de ejecutar el signo de cada derivada. Después añade una tercera entrada `x3` con su peso `w3`: ¿qué línea nueva hace falta en el *backward*?

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

#### Por qué hace falta la función de activación

Sin activación, cada capa calcula `W·x + b`, que es una operación **lineal**. Y dos operaciones lineales seguidas equivalen a una sola: `W₂(W₁x + b₁) + b₂ = (W₂W₁)x + (W₂b₁ + b₂)`. Por muchas capas que se apilen, la red no podría aprender nada que no aprenda una regresión lineal.

```python
import numpy as np
np.set_printoptions(precision=3)      # mostrar 3 decimales
rng = np.random.default_rng(0)
W1, b1 = rng.normal(size=(3, 2)), rng.normal(size=3)
W2, b2 = rng.normal(size=(1, 3)), rng.normal(size=1)
x = np.array([0.5, 1.2])

dos_capas = W2 @ (W1 @ x + b1) + b2
una_capa = (W2 @ W1) @ x + (W2 @ b1 + b2)
print(dos_capas, una_capa)            # [-4.745] [-4.745]: dan lo mismo
```

Además de las de la tabla anterior hay otras dos que conviene conocer:

| Función | Fórmula | Cuándo |
|---------|---------|--------|
| **Escalón** | 1 si z ≥ 0; 0 si no | El perceptrón original (1958). No se usa en redes profundas: su derivada es 0 en todas partes y el descenso de gradiente no puede aprender |
| **Leaky ReLU** | z si z > 0; 0,01·z si no | Como ReLU, pero con una pequeña pendiente en los negativos. Evita las «neuronas muertas»: una neurona ReLU que siempre recibe valores negativos da 0, su gradiente es 0 y deja de aprender |

Con `z = [−2, −0,5, 0, 0,5, 2]`: sigmoide → `[0,119 0,378 0,5 0,622 0,881]`, tanh → `[−0,964 −0,462 0 0,462 0,964]`, ReLU → `[0 0 0 0,5 2]` y Leaky ReLU → `[−0,02 −0,005 0 0,5 2]`.

**Softmax en la práctica.** Con números grandes, `np.exp(1000)` desborda y la división da `nan`. Las librerías restan antes el máximo, que no cambia el resultado:

```python
def softmax(v):
    e = np.exp(v - np.max(v))       # estable: el exponente mayor pasa a ser 0
    return e / e.sum()

print(softmax(np.array([2.0, 1.0, 0.1])))      # [0.659 0.242 0.099]
print(softmax(np.array([1000.0, 999.0])))      # [0.731 0.269]  (sin restar: [nan nan])
```

#### Propagación hacia delante con matrices

Con varias neuronas, las sumas ponderadas de una capa entera se hacen de una vez con un **producto de matrices**. Para cada capa:

```
Z = W · A_anterior + b        A = f(Z)
```

`W` tiene una fila por neurona de la capa y una columna por entrada. Ejemplo con 2 entradas, 2 neuronas ocultas con ReLU y 1 salida con sigmoide:

```python
X  = np.array([0.5, 1.2])
W1 = np.array([[0.4, -0.3],
               [0.8,  0.1]]);   b1 = np.array([0.1, -0.2])
W2 = np.array([0.7, -1.2]);     b2 = 0.3

Z1 = W1 @ X + b1                # [0.4·0.5 − 0.3·1.2 + 0.1, 0.8·0.5 + 0.1·1.2 − 0.2] = [-0.06, 0.32]
A1 = np.maximum(0, Z1)          # ReLU: [0, 0.32]
Z2 = W2 @ A1 + b2               # 0.7·0 − 1.2·0.32 + 0.3 = -0.084
y_hat = 1 / (1 + np.exp(-Z2))   # 0.479
```

La red da una probabilidad de 0,479. La primera neurona oculta ha quedado «apagada» (ReLU de un negativo): para este ejemplo no aporta nada. Hacer una vez este cálculo a mano es la mejor forma de entender qué hace `model.predict`.

#### Las funciones de pérdida, con números

```python
y_real = np.array([3.0, 5.0, 4.0, 6.0])
y_pred = np.array([2.5, 5.5, 4.0, 7.0])
mse = np.mean((y_real - y_pred) ** 2)    # 0.375
mae = np.mean(np.abs(y_real - y_pred))   # 0.5
```

Si la última predicción fuera 16 en vez de 7 (un error grande), el MSE salta a **25,1** y el MAE solo a **2,75**: al elevar al cuadrado, el MSE castiga mucho los errores grandes. Por eso el MAE es más robusto cuando hay valores atípicos.

La **entropía cruzada** castiga sobre todo equivocarse **con seguridad**. Si la respuesta correcta es 1 y la red dice:

| Probabilidad para la clase correcta | 0,9 | 0,6 | 0,1 | 0,01 |
|---|---|---|---|---|
| Pérdida −log(p) | 0,105 | 0,511 | 2,303 | 4,605 |

En multiclase solo cuenta la probabilidad de la clase correcta: con etiqueta `[0, 1, 0]` y predicción `[0,2, 0,7, 0,1]`, la pérdida es −log(0,7) = 0,357.

#### Descenso de gradiente: lotes y tasa de aprendizaje

Cada paso mueve los pesos en contra del gradiente: `w ← w − η · ∂L/∂w`, donde **η** es la **tasa de aprendizaje** (*learning rate*). Según cuántos ejemplos se usan para calcular el gradiente:

| Variante | Ejemplos por paso | Comportamiento |
|----------|-------------------|----------------|
| **Por lotes** (*batch*) | Todos | Estable, pero lento y necesita mucha memoria |
| **Estocástico** (SGD) | 1 | Rápido y ruidoso: los pasos zigzaguean |
| **Minilotes** (*mini-batch*) | 32, 64, 128… | El equilibrio habitual; es lo que hace Keras con `batch_size` |

Una **época** es una pasada completa por todos los datos de entrenamiento. Con 10 000 ejemplos y lotes de 32 hay ⌈10 000 / 32⌉ = **313 pasos por época** (el último lote tiene solo 16 ejemplos).

La tasa de aprendizaje decide si se llega al mínimo. Minimizando `L(w) = (w − 3)²` desde `w = 0`, 10 pasos:

```python
def descenso(eta, pasos=10, w=0.0):
    for _ in range(pasos):
        w = w - eta * 2 * (w - 3)      # la derivada de (w − 3)² es 2(w − 3)
    return w

for eta in (0.01, 0.1, 0.5, 0.9, 1.1):
    print(eta, round(descenso(eta), 2))
# 0.01 → 0.55   demasiado pequeña: avanza muy despacio
# 0.1  → 2.68   bien: se acerca a 3
# 0.5  → 3.0    en este caso concreto, llega en un paso
# 0.9  → 2.68   se pasa de largo y oscila: 5.4, 1.08, 4.54, 1.77…
# 1.1  → -15.58 diverge: cada paso empeora
```

El valor «bueno» depende del problema: 0,001 es el punto de partida habitual con Adam, pero no una ley.

#### Optimizadores: momento y Adam

El descenso de gradiente básico (SGD) tiene dos problemas: avanza despacio por zonas casi planas y un mismo `η` puede ser pequeño para unos pesos y enorme para otros. Los optimizadores modernos lo corrigen:

- **Momento** (*momentum*): acumula una «velocidad» con la media de los gradientes anteriores (`v ← β·v + g; w ← w − η·v`). Como una bola que rueda, atraviesa las zonas planas y amortigua los zigzags, aunque puede pasarse del mínimo.
- **RMSprop y Adagrad**: adaptan el tamaño del paso de **cada peso** según lo grandes que hayan sido sus gradientes.
- **Adam** combina las dos ideas: media de los gradientes (`m`) y media de sus cuadrados (`v`), con una corrección para los primeros pasos. El paso es `η · m̂ / (√v̂ + ε)`.

La ventaja práctica de Adam se ve multiplicando la función por 100 (`L = 100·(w − 3)²`), como si los datos vinieran en otra escala:

```python
def adam(escala, eta=0.3, pasos=200, b1=0.9, b2=0.999, eps=1e-8):
    w = m = v = 0.0
    for t in range(1, pasos + 1):
        g = escala * 2 * (w - 3)
        m = b1 * m + (1 - b1) * g
        v = b2 * v + (1 - b2) * g * g
        m_hat, v_hat = m / (1 - b1 ** t), v / (1 - b2 ** t)
        w -= eta * m_hat / (np.sqrt(v_hat) + eps)
    return w

print(round(adam(1), 3), round(adam(100), 3))      # 3.0 3.0
```

Adam llega a 3 en los dos casos, porque divide el gradiente por su propio tamaño. SGD con `η = 0,01` funciona con la escala 1, pero con la escala 100 oscila para siempre entre 0 y 6. Adam es la opción por defecto razonable, no «la mejor siempre»: en algunos problemas (sobre todo de imágenes) SGD con momento generaliza mejor.

#### Inicialización de los pesos

Los pesos no pueden empezar todos en 0: todas las neuronas de una capa calcularían lo mismo, recibirían el mismo gradiente y seguirían siendo iguales (problema de **simetría**). Se empiezan con números aleatorios pequeños, pero **cuánto** de pequeños importa. Pasando datos aleatorios por 20 capas ReLU de 256 neuronas, la desviación típica de la salida es:

| Pesos iniciales | Desviación de la salida tras 20 capas |
|-----------------|---------------------------------------|
| Desviación 0,01 (demasiado pequeños) | ≈ 10⁻¹⁹: la señal se apaga |
| **He**: varianza 2 / n_entradas | ≈ 0,84: la señal se mantiene |
| Desviación 0,2 (demasiado grandes) | ≈ 10⁷: la señal explota |

- **He** (varianza 2 / n_entradas) es la adecuada con ReLU.
- **Glorot o Xavier** (varianza 2 / (n_entradas + n_salidas)) es la adecuada con sigmoide o tanh, y la que usa Keras por defecto en las capas `Dense`.

#### Entrenar en Keras: épocas, validación, *dropout* y *early stopping*

```python
from tensorflow import keras

modelo = keras.Sequential([
    keras.Input(shape=(20,)),
    keras.layers.Dense(64, activation="relu"),
    keras.layers.Dropout(0.3),                     # apaga el 30 % de las neuronas en cada paso
    keras.layers.Dense(32, activation="relu"),
    keras.layers.Dense(1, activation="sigmoid"),
])
modelo.compile(optimizer=keras.optimizers.Adam(learning_rate=0.001),
               loss="binary_crossentropy", metrics=["accuracy"])

parar = keras.callbacks.EarlyStopping(monitor="val_loss", patience=5, restore_best_weights=True)
historia = modelo.fit(X_train, y_train, epochs=100, batch_size=32,
                      validation_split=0.2, callbacks=[parar])
modelo.evaluate(X_test, y_test)                    # el conjunto de prueba, solo al final
```

- `validation_split=0.2` aparta el 20 % del entrenamiento para vigilar el sobreajuste. El conjunto de **prueba** no se usa para decidir nada durante el entrenamiento: si se usa como validación (por ejemplo con `validation_data=(X_test, y_test)` y *early stopping*), su resultado deja de ser una estimación honesta (fuga de datos, [UD5 sección 6](ud5-ml.html)).
- **Dropout** solo actúa al entrenar. Keras multiplica las neuronas que quedan por 1/(1 − p) durante el entrenamiento, así que al predecir están todas activas y no hay que reescalar nada.
- **EarlyStopping** para cuando `val_loss` lleva `patience` épocas sin mejorar y, con `restore_best_weights=True`, se queda con los pesos de la mejor época.

Cómo leer las curvas de `historia.history`:

| Entrenamiento | Validación | Diagnóstico | Qué probar |
|---------------|------------|-------------|------------|
| Error alto | Error alto | **Subajuste**: el modelo es demasiado simple o ha entrenado poco | Más capas o neuronas, más épocas, mejores variables |
| Error bajo | Error bajo y parecido | **Buen ajuste** | Nada |
| Error bajo y bajando | Baja y luego **sube** | **Sobreajuste**: memoriza | Dropout, regularización L2, más datos, aumento de datos, *early stopping* |

Los ejercicios [E62–E69](ejercicios.html#bloque-l--deep-learning-con-números-e62e69) practican todo esto con números. Las redes convolucionales, con el cálculo de tamaños y parámetros, están en la [UD3](ud3-vision.html#5-clasificar-imágenes), y las recurrentes y los Transformers, en la [UD4](ud4-lenguaje.html#108-redes-para-secuencias-rnn-lstm-gru-y-atención).

#### Datos por lotes con `tf.data`, TensorBoard y exportar el modelo

Con pocos datos basta con pasar arrays de NumPy a `fit`, como arriba. Con muchas imágenes o textos que no caben en memoria se usa `tf.data`, que lee, baraja y agrupa los datos por lotes mientras la red entrena:

```python
import tensorflow as tf

train = (tf.data.Dataset.from_tensor_slices((X_train, y_train))
         .shuffle(1000)                  # 1.º barajar ejemplos (con un búfer de 1000)
         .batch(32)                      # 2.º agrupar en lotes de 32
         .prefetch(tf.data.AUTOTUNE))    # preparar el siguiente lote mientras se entrena el actual
val = tf.data.Dataset.from_tensor_slices((X_val, y_val)).batch(32)

registro = keras.callbacks.TensorBoard(log_dir="logs/")
modelo.fit(train, validation_data=val, epochs=20, callbacks=[parar, registro])
```

- **El orden importa**: `.shuffle(1000).batch(32)` baraja los ejemplos y después forma lotes. Al revés, `.batch(32).shuffle(1000)`, solo baraja el **orden de los lotes**: cada lote tiene siempre los mismos 32 ejemplos.
- Con un `Dataset`, `validation_split` **no funciona** (solo admite arrays de NumPy o tensores): la validación se prepara aparte y se pasa con `validation_data`. Tampoco se indica `batch_size` en `fit`, porque los lotes ya vienen hechos.
- **TensorBoard** guarda las curvas de error y acierto de cada época; se ven con `tensorboard --logdir logs/` en el navegador o, en Colab, con `%load_ext tensorboard` y `%tensorboard --logdir logs/`.
- **GPU**: `tf.config.list_physical_devices("GPU")` dice si hay alguna. TensorFlow la usa sola si la encuentra; `with tf.device("/GPU:0"):` solo hace falta para elegir una concreta.

**Guardar o exportar** no es lo mismo:

| Para qué | Cómo (Keras 3, TensorFlow 2.16 o posterior) | Notas |
|----------|----------------------------------------------|-------|
| Seguir entrenando o usarlo en Python | `modelo.save("modelo.keras")` y `keras.models.load_model("modelo.keras")` | `.h5` es el formato antiguo |
| Servirlo en producción (TF Serving, en la nube) | `modelo.export("export/")` | Crea un *SavedModel*; antes se hacía con `tf.saved_model.save` |
| Móvil o dispositivos pequeños | `modelo.export("modelo.tflite", format="litert")` | TensorFlow Lite se llama ahora LiteRT |
| Otros entornos | `modelo.export("modelo.onnx", format="onnx")` | ONNX lo leen muchos lenguajes y programas |

Es el mismo camino que [13.7](#137-del-notebook-a-la-app-desplegar-un-modelo) con scikit-learn: entrenar una vez, guardar, y cargar el modelo ya entrenado en la aplicación.

> Código de PyTorch y TensorFlow revisado con la documentación oficial, pero no ejecutado en el entorno de prueba (las librerías no estaban instaladas): pruébalo en Google Colab, que ya las trae.

#### La XOR: por qué hacen falta capas ocultas

Un perceptrón (una sola neurona con función escalón) aprende las puertas AND y OR, pero nunca la **XOR** (verdadero si las dos entradas son distintas): los casos (0,1) y (1,0) quedan en una diagonal y los casos (0,0) y (1,1) en la otra, y ninguna línea recta los separa ([UD5, ejercicio 9.1](ud5-ml.html)). Con una capa oculta sí se puede, porque XOR(a, b) = AND(OR(a, b), NAND(a, b)). Se puede construir a mano, sin entrenar:

```python
import numpy as np
paso = lambda z: (z >= 0).astype(int)                # neurona escalón
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
h_or   = paso(X @ np.array([1, 1]) - 0.5)            # [0 1 1 1]
h_nand = paso(X @ np.array([-1, -1]) + 1.5)          # [1 1 1 0]
xor    = paso(h_or + h_nand - 1.5)                   # AND de las dos: [0 1 1 0]
```

La capa oculta **transforma** las entradas en dos nuevas características (OR y NAND) con las que el problema sí se separa con una recta. Esa es la idea central del aprendizaje profundo: cada capa aprende una representación más útil que la anterior.

**La misma red, aprendiendo sola.** Con la retropropagación en forma de matrices (un lote de ejemplos a la vez), una red 2-4-1 con tanh y sigmoide aprende la XOR en unas líneas de NumPy:

```python
rng = np.random.default_rng(1)
X = X.astype(float)
y = np.array([[0], [1], [1], [0]], float)
W1, b1 = rng.normal(0, 1, (2, 4)), np.zeros((1, 4))
W2, b2 = rng.normal(0, 1, (4, 1)), np.zeros((1, 1))
sigmoide = lambda z: 1 / (1 + np.exp(-z))

for epoca in range(5001):
    h = np.tanh(X @ W1 + b1)                         # hacia delante
    p = sigmoide(h @ W2 + b2)
    dz2 = (p - y) / len(X)                           # hacia atrás (sigmoide + entropía cruzada)
    dW2, db2 = h.T @ dz2, dz2.sum(0, keepdims=True)
    dz1 = (dz2 @ W2.T) * (1 - h ** 2)                # regla de la cadena; tanh' = 1 − tanh²
    dW1, db1 = X.T @ dz1, dz1.sum(0, keepdims=True)
    W1 -= 0.5 * dW1; b1 -= 0.5 * db1; W2 -= 0.5 * dW2; b2 -= 0.5 * db2
print(p.round(3).ravel())                            # [0.    0.999 0.999 0.002]
```

La pérdida baja de 0,67 a 0,0009. Dos detalles que simplifican el cálculo: con sigmoide en la salida y entropía cruzada, el gradiente de la salida es simplemente `p − y`; y cada `dW` es la entrada de la capa (traspuesta) por el error de la capa. Es lo mismo que la neurona de antes, repetido capa a capa.

#### Normalización por lotes y por capa

Si las entradas de una capa cambian mucho de escala durante el entrenamiento, aprender es más lento e inestable. Las capas de **normalización** lo corrigen: restan la media y dividen entre la desviación, y después dejan que la red reescale con dos parámetros aprendidos (γ y β).

```python
lote = np.array([[1., 2.], [3., 4.], [5., 6.]])     # 3 ejemplos, 2 características
media, var = lote.mean(0), lote.var(0)              # [3. 4.] y [2.667 2.667]
normalizado = (lote - media) / np.sqrt(var + 1e-5)  # [[-1.225 -1.225] [0. 0.] [1.225 1.225]]
```

| Tipo | Normaliza usando | Dónde se usa |
|------|------------------|--------------|
| **Por lotes** (*BatchNorm*) | La media y la varianza de cada característica **en el lote** | CNN |
| **Por capa** (*LayerNorm*) | Todas las características de **un solo ejemplo** | Transformers y RNN ([UD4](ud4-lenguaje.html)) |

La normalización por lotes depende de los demás ejemplos del lote, así que al **predecir** no puede usarlos: con un lote de un solo ejemplo, todo daría 0. Por eso guarda durante el entrenamiento una media y una varianza acumuladas y usa esas al predecir. Si en PyTorch se olvida `model.eval()`, la red sigue en modo entrenamiento y las predicciones cambian según el lote: un error muy típico.

#### Calendarios de la tasa de aprendizaje

Al principio interesa avanzar rápido y al final, afinar. Por eso se suele **cambiar η durante el entrenamiento**:

| Calendario | Qué hace |
|------------|----------|
| Por escalones | Multiplica η por 0,1 cada cierto número de épocas |
| Coseno | Baja η suavemente hasta casi 0, con forma de coseno |
| Calentamiento (*warm-up*) | Empieza con η muy pequeña y la sube en los primeros pasos; habitual en Transformers |
| Al estancarse | Reduce η cuando la pérdida de validación deja de mejorar: `keras.callbacks.ReduceLROnPlateau(factor=0.5, patience=3)` |

#### Cuando la red no aprende: lista de comprobación

1. **Mira la pérdida antes de entrenar.** Con C clases equilibradas, softmax y entropía cruzada, una red sin entrenar debe dar unos **ln C** (con 10 clases, ln 10 ≈ 2,30): es lo que sale si reparte la probabilidad por igual. Si sale 15 o 23, algo está mal (pesos iniciales enormes, pérdida equivocada, etiquetas mal codificadas).
2. **Sobreajusta un lote diminuto.** Con 10 o 20 ejemplos, la red tiene que llegar a pérdida casi 0. Si no lo consigue, hay un error en el código (modelo, pérdida, etiquetas u optimizador), no falta de datos.
3. **Mira los datos y las etiquetas**: que cada imagen tenga su etiqueta, que se mezclen en cada época y que se normalicen igual en entrenamiento y en prueba.
4. **Prueba varias tasas de aprendizaje** en escala logarítmica (10⁻⁴, 10⁻³, 10⁻²): demasiado alta da `nan` u oscilaciones; demasiado baja, una curva plana.
5. **Compara con algo trivial**: predecir siempre la clase mayoritaria o la media. Si la red no lo supera, no está aprendiendo nada.

| Error típico | Síntoma |
|--------------|---------|
| Aplicar softmax antes de `CrossEntropyLoss` en PyTorch (ya la incluye) o usar `from_logits=True` en Keras con una salida softmax | Aprende mal o muy despacio |
| Olvidar `optimizer.zero_grad()` en PyTorch | Los gradientes se acumulan entre pasos; entrenamiento errático |
| Olvidar `model.eval()` al validar | *Dropout* y BatchNorm siguen activos: validación ruidosa |
| No mezclar los datos (ordenados por clase) | Cada lote tiene una sola clase; la pérdida sube y baja |
| Fuga de datos entre entrenamiento y prueba | Resultados demasiado buenos que desaparecen con datos nuevos |

#### Otras arquitecturas

| Arquitectura | Idea | Para qué |
|--------------|------|----------|
| **Autoencoder** | Comprime la entrada en pocos números (código latente) y la reconstruye | Reducir dimensiones, quitar ruido, detectar anomalías (lo que reconstruye mal es «raro») |
| **GAN** | Un generador crea falsificaciones y un discriminador intenta descubrirlas; mejoran compitiendo | Generar imágenes realistas, *deepfakes* ([UD3](ud3-vision.html)) |
| **Difusión** | Aprende a quitar ruido paso a paso; para generar, parte de ruido puro | Generadores de imágenes a partir de texto; más estables que las GAN, pero más lentos |
| **Redes de grafos (GNN)** | Cada nodo actualiza su información con la de sus vecinos ([14.17](#1417-redes-y-grafos-con-networkx)) | Moléculas, redes sociales, recomendaciones, tráfico |

Los ejercicios [E80–E82](ejercicios.html#bloque-o--redes-neuronales-desde-cero-e80e82) practican la XOR, la normalización y la depuración.

#### Capa de salida y función de pérdida según el problema

La última capa y la pérdida no se eligen por gusto: dependen de **qué** hay que predecir.

| Problema | Ejemplo | Última capa | Pérdida (Keras) |
|----------|---------|-------------|-----------------|
| **Regresión** | Precio de un piso, nota final | 1 neurona, **sin activación** (lineal) | `"mse"` o `"mae"` (con atípicos) |
| **Binaria** | ¿Spam o no? | 1 neurona con **sigmoide** | `"binary_crossentropy"` |
| **Multiclase** (una sola clase correcta) | Dígito del 0 al 9 | *n* neuronas con **softmax** | `"categorical_crossentropy"` con etiquetas *one-hot*; `"sparse_categorical_crossentropy"` con números de clase |
| **Multietiqueta** (varias a la vez) | Etiquetas de una foto: playa, personas, perro | *n* neuronas con **sigmoide** (una por etiqueta) | `"binary_crossentropy"` |

El último caso no suele aparecer en los apuntes resumidos y es un error frecuente: con softmax, las probabilidades **suman 1** y compiten entre sí; con una sigmoide por etiqueta, cada una es independiente.

```python
import numpy as np
logits = np.array([2.0, 0.5, -1.0])                        # playa, personas, perro
print((1 / (1 + np.exp(-logits))).round(3))                # sigmoide: [0.881 0.622 0.269] → playa y personas
print((np.exp(logits) / np.exp(logits).sum()).round(3))    # softmax:  [0.786 0.175 0.039] → «solo» playa
```

Una curiosidad que ayuda a entenderlo: una sigmoide con una neurona es **lo mismo** que una softmax con dos neuronas cuando la primera vale 0. Con z = 1,5, sigmoide(1,5) = 0,8176, y la softmax de [0; 1,5] da 0,8176 para la segunda clase. Por eso en binaria basta con una neurona.

#### Arquitecturas: cuál se usa para qué

| Arquitectura | Idea | Datos | Dónde se ve |
|--------------|------|-------|-------------|
| **Red densa (MLP)** | Todas las neuronas conectadas con la capa siguiente | Tablas | UD5 |
| **CNN** (convolucional) | Filtros (*kernels*) que recorren la imagen detectando bordes, texturas, formas; *pooling* para reducir tamaño | Imágenes | **UD3** (CIFAR-10, MNIST) |
| **RNN** (recurrente) | Tiene "memoria" (estado oculto) de lo anterior | Secuencias, texto, series temporales | UD4, UD5 |
| **LSTM / GRU** | RNN con "puertas" que deciden qué recordar y qué olvidar | Secuencias largas | UD4 |
| **Transformer** | Mecanismo de **atención**: cada palabra "mira" a todas las demás | Texto (LLM), también imágenes | **UD4** (14.8) |

---

### 14.8 IA Generativa y modelos de lenguaje (LLM)

Resumen de *GenAI: Zero to Hero*, ampliado con los apuntes visuales *15 Gen AI Concepts* (@darpan.decoded). Es la base conceptual de la **UD4 (Lenguaje)**.

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

#### Conceptos que aparecerán en la UD4

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

#### La ventana de contexto es un presupuesto

La **ventana de contexto** es la cantidad máxima de tokens que el modelo puede tener en cuenta a la vez. En ella tienen que caber **todas** estas piezas:

| Pieza | Ejemplo | Quién la pone |
|-------|---------|---------------|
| Instrucciones del sistema | «Eres un asistente del instituto, responde en gallego» | La aplicación (oculta) |
| Historial | Los mensajes anteriores de la conversación | Se reenvía entero en cada turno |
| Documentos añadidos | Un PDF, los fragmentos recuperados por RAG | La persona o la aplicación |
| Pregunta actual | «¿Cuándo es o exame de Física?» | La persona |
| Respuesta | Lo que el modelo va a escribir | El modelo (¡también ocupa sitio!) |

Cuando no cabe todo, la aplicación **recorta**: suele descartar los mensajes más antiguos, que el modelo «olvida». Por eso un chat muy largo pierde detalles del principio, y por eso un libro entero no se puede pegar en un modelo con una ventana pequeña: hay que trocearlo (*chunking*) y enviar solo los trozos útiles, que es lo que hace RAG. Los tamaños cambian muy rápido (de unos pocos miles de tokens en 2022 a cientos de miles o millones en 2025), así que conviene consultar la documentación del modelo que se use. Más tokens también significa **más coste y más tiempo** de respuesta.

```python
def recortar_historial(mensajes, max_tokens, tokens_de=lambda m: len(m.split())):
    """Se queda con los mensajes más recientes que caben en el presupuesto."""
    elegidos, usados = [], 0
    for m in reversed(mensajes):                 # del más nuevo al más viejo
        t = tokens_de(m)
        if usados + t > max_tokens:
            break
        elegidos.append(m)
        usados += t
    return list(reversed(elegidos)), usados

chat = ["Ola, son Uxía e estudo 1º BAC",
        "Gústame a física e o baloncesto",
        "Que libros me recomendas para o verán?",
        "E algún sobre intelixencia artificial?"]
print(recortar_historial(chat, 12))
# (['Que libros me recomendas para o verán?', 'E algún sobre intelixencia artificial?'], 12)
```

Aquí se cuentan **palabras** como aproximación; los modelos reales cuentan tokens con su propio *tokenizador*, y en gallego o castellano salen más tokens por palabra que en inglés. Fíjate en el efecto: el modelo ya no sabe que habla con Uxía ni qué le gusta. Algunas aplicaciones, en lugar de borrar, **resumen** lo antiguo o guardan datos en una «memoria» aparte.

#### Temperatura, top-k y top-p en Python

El modelo no da una palabra: da una **puntuación** (*logit*) para cada token posible. La función **softmax** las convierte en probabilidades, y la **temperatura** divide las puntuaciones antes: con temperatura baja la distribución se vuelve muy picuda (casi siempre gana el favorito); con temperatura alta se aplana (los tokens raros tienen más opciones).

```python
import numpy as np

tokens = ["azul", "nubrado", "gris", "escuro", "verde"]
logits = np.array([3.0, 2.0, 1.5, 0.5, -1.0])        # «O ceo está…»

def softmax(x, temperatura=1.0):
    z = x / temperatura
    e = np.exp(z - z.max())                           # restar el máximo evita desbordes
    return e / e.sum()

for t in (0.2, 1.0, 2.0):
    p = softmax(logits, t)
    print(t, " ".join(f"{tok}:{v:.2f}" for tok, v in zip(tokens, p)))
# 0.2 azul:0.99 nubrado:0.01 gris:0.00 escuro:0.00 verde:0.00
# 1.0 azul:0.59 nubrado:0.22 gris:0.13 escuro:0.05 verde:0.01
# 2.0 azul:0.40 nubrado:0.24 gris:0.19 escuro:0.11 verde:0.05

def top_k(p, k):
    q = np.zeros_like(p)
    mejores = np.argsort(p)[::-1][:k]                 # índices de los k más probables
    q[mejores] = p[mejores]
    return q / q.sum()                                # volver a repartir hasta sumar 1

def top_p(p, umbral):
    orden = np.argsort(p)[::-1]
    acumulada = np.cumsum(p[orden])
    n = np.searchsorted(acumulada, umbral) + 1        # cuántos hacen falta para llegar a p
    q = np.zeros_like(p)
    q[orden[:n]] = p[orden[:n]]
    return q / q.sum()

p = softmax(logits)
print(np.round(top_k(p, 2), 2))        # [0.73 0.27 0.   0.   0.  ]
print(np.round(top_p(p, 0.9), 2))      # [0.63 0.23 0.14 0.   0.  ]

rng = np.random.default_rng(0)
print([tokens[rng.choice(5, p=softmax(logits, 1.0))] for _ in range(8)])
# ['nubrado', 'azul', 'azul', 'azul', 'gris', 'gris', 'nubrado', 'nubrado']: muestrear da variedad
```

| Ajuste | Qué hace | Cuándo |
|--------|----------|--------|
| *Greedy* (temperatura 0) | Siempre el más probable | Extraer datos, clasificar, respuestas que se puedan repetir |
| Temperatura baja (≈ 0,2) | Casi siempre el favorito | Resúmenes, preguntas con respuesta concreta |
| Temperatura media o alta (≈ 0,7–1) | Más variedad | Lluvia de ideas, textos creativos |
| Top-k | Solo entre los k mejores | Evitar tokens absurdos de la cola |
| Top-p (núcleo) | Solo los mejores hasta sumar p | Igual, pero adaptándose: si el modelo duda, deja más opciones |

Los rangos exactos dependen de cada servicio; lo importante es la idea. Una temperatura baja **no** hace que el modelo diga la verdad: solo hace que repita su respuesta más probable, que puede estar mal.

#### RAG paso a paso

**RAG** (*Retrieval-Augmented Generation*) da al modelo los documentos correctos **antes** de que responda. Tiene dos fases:

| Fase | Cuándo | Pasos |
|------|--------|-------|
| **Preparar** (una vez) | Al cargar los documentos | Trocear en fragmentos → calcular el *embedding* de cada uno → guardarlos en una **base de datos vectorial** |
| **Responder** (cada pregunta) | Cada vez que alguien pregunta | *Embedding* de la pregunta → buscar los k fragmentos más parecidos (**recuperar**) → pegarlos en el prompt (**aumentar**) → el LLM responde con ellos (**generar**) |

Una versión mínima que funciona sin internet, usando TF-IDF (UD4) en lugar de un modelo de *embeddings*:

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documentos = [
    "A biblioteca abre de luns a venres de 9:00 a 14:30 e os martes pola tarde.",
    "Os préstamos de libros duran 15 días e pódense renovar unha vez.",
    "O comedor escolar funciona de 14:30 a 15:30.",
    "Para usar os portátiles hai que reservar na conserxería cun día de antelación.",
]
vectorizador = TfidfVectorizer()
matriz = vectorizador.fit_transform(documentos)       # «base de datos vectorial» de juguete

def recuperar(pregunta, k=2):
    sim = cosine_similarity(vectorizador.transform([pregunta]), matriz)[0]
    mejores = sim.argsort()[::-1][:k]
    return [(documentos[i], round(float(sim[i]), 2)) for i in mejores]

pregunta = "Canto tempo duran os préstamos?"
contexto = recuperar(pregunta)
print(contexto[0])
# ('Os préstamos de libros duran 15 días e pódense renovar unha vez.', 0.51)

prompt = ("Responde SÓ coa información do contexto. Se non está, di «non o sei».\n"
          "Contexto:\n" + "\n".join(f"- {d}" for d, _ in contexto) +
          f"\nPregunta: {pregunta}")
print(prompt)       # esto es lo que recibiría el LLM
```

TF-IDF solo encuentra **palabras iguales** («préstamos» con «préstamos»); un modelo de *embeddings* encuentra también **significados parecidos** («cuánto puedo tener un libro» con «préstamos de 15 días»). Las bases de datos vectoriales (FAISS, Chroma, Qdrant, Milvus, Weaviate, pgvector…) hacen esta búsqueda rápida con millones de fragmentos y guardan **metadatos** (fuente, fecha) para filtrar y citar.

**Lo que RAG no arregla:** si la recuperación trae el fragmento equivocado, el modelo responderá con seguridad a partir de él; y el modelo puede ignorar el contexto. Por eso se evalúa por separado **si recupera bien** y **si responde bien**, y se pide que cite el fragmento usado.

#### ¿Prompt, RAG o ajuste fino?

| Necesidad | Mejor opción | Por qué |
|-----------|--------------|---------|
| Cambiar el formato, el tono o dar ejemplos | **Prompt** (instrucciones y *few-shot*) | Gratis e inmediato |
| Responder con datos propios o actuales (normas del centro, apuntes, catálogo) | **RAG** | Los datos se actualizan sin reentrenar y se pueden citar |
| Un estilo o una tarea muy concreta que el prompt no consigue, con cientos o miles de ejemplos | **Ajuste fino** (*fine-tuning*), a menudo con **LoRA** | Cambia los pesos del modelo; caro y con riesgo de sobreajuste |
| Actuar: buscar en internet, calcular, consultar una base de datos | **Herramientas** (llamada a funciones) | El modelo no sabe hacerlo solo ni tiene datos en tiempo real |

Se suele empezar por el prompt, añadir RAG si faltan datos y dejar el ajuste fino para el final. Se pueden combinar.

#### Llamada a funciones, herramientas y agentes

Un LLM solo produce texto. Para **hacer** cosas, la aplicación le describe unas **herramientas** (nombre, para qué sirven, qué parámetros piden) y el modelo responde con un JSON que dice **qué herramienta usar y con qué datos**. Es el programa, no el modelo, quien la ejecuta y le devuelve el resultado.

```python
import json

def tiempo(concello):                                 # herramienta 1 (datos inventados)
    return {"Marín": "chuvia, 14 °C", "Lugo": "néboa, 9 °C"}.get(concello, "sen datos")

def calcular(expresion):                              # herramienta 2: solo + - * / y números, sin potencias
    if not set(expresion) <= set("0123456789+-*/. ()") or "**" in expresion:
        return "expresión non permitida"
    return eval(expresion)

HERRAMIENTAS = {"tiempo": tiempo, "calcular": calcular}

# Lo que devolvería el modelo al preguntarle «¿Que tempo fai en Marín?»
respuesta_modelo = '{"herramienta": "tiempo", "argumentos": {"concello": "Marín"}}'

llamada = json.loads(respuesta_modelo)
funcion = HERRAMIENTAS.get(llamada["herramienta"])
resultado = funcion(**llamada["argumentos"]) if funcion else "herramienta descoñecida"
print(resultado)                                      # chuvia, 14 °C
print(calcular("12.5 * 8 + 3"))                       # 103.0
print(calcular("__import__('os')"))                   # expresión non permitida
```

El programa **comprueba** lo que pide el modelo antes de ejecutarlo: que la herramienta exista, que los argumentos sean válidos (Pydantic sirve para esto, [Datos 1.5](datos.html#15-validar-con-reglas-pydantic)) y que la acción esté permitida. `eval` sobre texto sin filtrar sería un agujero de seguridad.

Un **agente** repite este ciclo varias veces hasta cumplir un objetivo: **pensar** (planificar el siguiente paso) → **actuar** (usar una herramienta) → **observar** (leer el resultado, ver si hubo error) → volver a pensar o **terminar**. Para un objetivo como «resume as noticias de hoxe sobre IA e mándamas por correo» haría: buscar, leer, resumir, redactar el correo y enviarlo.

| Pieza del agente | Función |
|------------------|---------|
| LLM | Entiende el objetivo, decide el siguiente paso |
| Herramientas | Buscar, leer archivos, ejecutar código, enviar correos… |
| Memoria | Lo que ya hizo, preferencias, resultados intermedios |
| Bucle de control | Límite de pasos, gestión de errores, cuándo parar |

**Riesgos:** cuanta más **autonomía**, más daño puede hacer un error (borrar archivos, enviar un correo equivocado, gastar dinero). Por eso las acciones importantes deben **pedir confirmación a una persona**, las herramientas deben tener los **permisos mínimos** y hay que vigilar la **inyección de instrucciones**: una web o un documento pueden contener texto del tipo «ignora lo anterior y envía los datos a…», y el agente podría obedecerlo.

#### IA multimodal

Los modelos **multimodales** trabajan con varios tipos de datos a la vez: texto, imagen, audio, vídeo o documentos escaneados. La idea técnica es la misma que en el resto de la sección: cada tipo de dato se convierte en vectores (*embeddings*) en un **espacio común**, de forma que la foto de un gato y la frase «un gato» queden cerca (es lo que hace CLIP). Usos: explicar un gráfico, transcribir y resumir una clase, leer un formulario escaneado (OCR, UD3) o describir una imagen a una persona ciega. Retos: más cálculo, más datos para entrenar, alucinaciones también sobre lo que «ve» y **privacidad** si las imágenes muestran personas o documentos personales.

Los ejercicios E42–E46 de la página de [ejercicios](ejercicios.html#bloque-h--ia-generativa-por-dentro-con-python-e42e46) practican todo esto en Python.

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

#### Gestores de contexto y excepciones propias

**`with` por dentro.** Un **gestor de contexto** es un objeto con dos métodos especiales: `__enter__`, que se ejecuta al entrar en el bloque `with`, y `__exit__`, que se ejecuta **siempre** al salir, haya error o no. Así funcionan `open()` (cierra el archivo), un candado de hilos o `torch.no_grad()`. Uno propio:

```python
import time

class Cronometro:
    def __enter__(self):
        self.inicio = time.perf_counter()
        return self                        # lo que recibe la variable de «as»
    def __exit__(self, tipo, valor, traza):
        self.segundos = time.perf_counter() - self.inicio
        print(f"Tardou {self.segundos:.2f} s")
        return False                       # False: si hubo un error, sigue su camino

with Cronometro() as c:
    sum(range(5_000_000))                  # Tardou 0.11 s (depende del ordenador)
```

Si dentro del bloque hay un `1 / 0`, el cronómetro también imprime su tiempo y después el `ZeroDivisionError` continúa. Si `__exit__` devolviera `True`, el error **desaparecería**: casi nunca es lo que se quiere.

La forma corta, con un generador y el decorador `@contextmanager`: lo que va antes del `yield` es la entrada, y lo que va en el `finally`, la salida.

```python
from contextlib import contextmanager

@contextmanager
def cronometro(nome):
    inicio = time.perf_counter()
    try:
        yield
    finally:
        print(f"{nome}: {time.perf_counter() - inicio:.2f} s")

with cronometro("suma"):
    sum(range(5_000_000))                  # suma: 0.11 s
```

**Una familia de excepciones propias.** Si un programa tiene varios errores relacionados, conviene una excepción **base** de la que hereden las demás. Así se pueden capturar todas juntas o cada una por separado:

```python
class ErroNota(Exception):
    """Error base de las notas."""

class NotaForaDeRango(ErroNota):
    def __init__(self, nota):
        super().__init__(f"A nota {nota} non está entre 0 e 10")
        self.nota = nota                   # el dato queda guardado para quien lo capture

class NotaNonNumerica(ErroNota):
    pass

def ler_nota(texto):
    try:
        nota = float(texto.replace(",", "."))
    except ValueError:
        raise NotaNonNumerica(f"«{texto}» non é un número") from None   # from None: oculta el error original
    if not 0 <= nota <= 10:
        raise NotaForaDeRango(nota)
    return nota

for t in ["7,5", "11", "sete"]:
    try:
        print(ler_nota(t))
    except ErroNota as e:                  # captura las dos
        print(type(e).__name__, "→", e)
# 7.5 · NotaForaDeRango → A nota 11.0 non está entre 0 e 10 · NotaNonNumerica → «sete» non é un número
```

**`assert` no sirve para validar datos.** `assert condición, "mensaje"` lanza `AssertionError` si la condición es falsa, y es útil para comprobar **suposiciones del propio programador** y en los tests (`pytest`, 14.11). Pero si Python se ejecuta con la opción `-O` (optimizar), los `assert` **se eliminan**: `assert 1 == 2` deja pasar el programa sin decir nada. Para comprobar lo que escribe el usuario o lo que llega de un archivo, `if` y `raise ValueError(...)`.

#### Programación orientada a objetos: los cuatro pilares

| Pilar | Idea | Ejemplo |
|-------|------|---------|
| **Encapsulación** | Juntar datos y métodos y proteger el estado interno | `self.__saldo` solo se cambia con `ingresar()` |
| **Herencia** | Una clase hija reutiliza la de la madre | `class Perro(Animal)` |
| **Polimorfismo** | El mismo método hace cosas distintas según el objeto | `animal.hablar()` → «Guau» o «Miau» |
| **Abstracción** | Mostrar qué hace y esconder cómo | `from abc import ABC, abstractmethod` |

Las librerías de IA usan estos pilares constantemente. Todos los modelos de scikit-learn heredan de una clase base y comparten `fit()` y `predict()`: es **polimorfismo**. Por eso se puede cambiar un modelo por otro sin cambiar el resto del código (14.4). El agente aspirador de 0.9 es otro ejemplo de clase.

#### POO con código: de una clase a un mini scikit-learn

Una **clase** es un molde; un **objeto** (o instancia) es una pieza hecha con ese molde. Este ejemplo recorre todo lo esencial con una ficha de alumnado:

```python
class Alumno:
    centro = "IES Chan do Monte"             # variable de CLASE: compartida por todos

    def __init__(self, nombre, nota):         # constructor: se ejecuta al crear el objeto
        self.nombre = nombre                  # variables de INSTANCIA: propias de cada objeto
        self.nota = nota                      # pasa por el setter de abajo (validación)

    @property
    def nota(self):                           # se lee como un atributo: a.nota
        return self._nota

    @nota.setter
    def nota(self, valor):                    # se ejecuta al hacer a.nota = ...
        if not 0 <= valor <= 10:
            raise ValueError(f"Nota fuera de rango: {valor}")
        self._nota = valor

    def aprobado(self):                       # método de instancia: usa self
        return self.nota >= 5

    @classmethod
    def desde_texto(cls, linea):              # método de clase: otra forma de construir
        nombre, nota = linea.split(";")
        return cls(nombre, float(nota))

    @staticmethod
    def redondear(nota):                      # método estático: utilidad, no usa self ni cls
        return round(nota * 2) / 2

    def __str__(self):                        # lo que muestra print()
        return f"{self.nombre} ({self.nota})"

    def __repr__(self):                       # lo que se ve en la consola o dentro de listas
        return f"Alumno({self.nombre!r}, {self.nota})"

    def __lt__(self, otro):                   # «menor que»: permite sorted()
        return self.nota < otro.nota

uxia = Alumno("Uxía", 8.5)
brais = Alumno.desde_texto("Brais;6.25")
print(uxia, uxia.aprobado(), Alumno.centro)    # Uxía (8.5) True IES Chan do Monte
print(sorted([uxia, brais]))                    # [Alumno('Brais', 6.25), Alumno('Uxía', 8.5)]
print(Alumno.redondear(6.3))                    # 6.5
try:
    brais.nota = 12
except ValueError as e:
    print(e)                                    # Nota fuera de rango: 12
```

| Tipo de método | Primer parámetro | Para qué | Se llama con |
|----------------|------------------|----------|--------------|
| De instancia | `self` (el objeto) | Trabajar con los datos de **ese** objeto | `uxia.aprobado()` |
| De clase (`@classmethod`) | `cls` (la clase) | Constructores alternativos, datos comunes | `Alumno.desde_texto(...)` |
| Estático (`@staticmethod`) | Ninguno | Utilidades relacionadas con la clase | `Alumno.redondear(6.3)` |

**Encapsulación en Python: convenios, no candados.** Python no tiene `private` como Java. Hay dos convenios:

| Nombre | Significado | ¿Se puede acceder desde fuera? |
|--------|-------------|-------------------------------|
| `nota` | Público | Sí |
| `_nota` | «Interno: no lo toques» (convenio entre programadores) | Sí, Python no lo impide |
| `__nota` | Python le cambia el nombre (*name mangling*) a `_Alumno__nota` para evitar choques con clases hijas | Sí, como `obj._Alumno__nota`; solo es más incómodo |

Por eso, en Python la forma idiomática de **proteger** un dato no es esconderlo, sino **validarlo** con `@property`, como la nota de arriba. Muchos apuntes dicen que `_x` «solo es accesible desde la clase y sus hijas» y `__x` «solo desde la clase»: eso es así en Java o C++, pero en Python son convenios.

**Métodos especiales (*dunder*)**: los que empiezan y acaban por doble guion bajo hacen que tus objetos funcionen con la sintaxis de Python: `__len__` con `len()`, `__eq__` con `==`, `__add__` con `+`, `__getitem__` con `obj[i]`, `__iter__` con `for`. Por eso un `DataFrame` responde a `len(df)` y `df["col"]`.

**Herencia, polimorfismo y abstracción**: así están hechos los modelos de scikit-learn. Una clase base abstracta obliga a que todos los modelos tengan `fit` y `predict`, y el código que los usa no necesita saber cuál es:

```python
from abc import ABC, abstractmethod

class Modelo(ABC):                                  # clase abstracta: no se puede instanciar
    @abstractmethod
    def fit(self, X, y): ...
    @abstractmethod
    def predict(self, X): ...

    def score(self, X, y):                          # método común: lo heredan todas
        aciertos = sum(p == r for p, r in zip(self.predict(X), y))
        return aciertos / len(y)

class Mayoria(Modelo):                              # predice siempre la clase más frecuente
    def fit(self, X, y):
        self.clase_ = max(set(y), key=y.count)
        return self
    def predict(self, X):
        return [self.clase_ for _ in X]

class Umbral(Modelo):                               # aprueba si las horas de estudio superan un umbral
    def __init__(self, umbral=4):
        self.umbral = umbral
    def fit(self, X, y):
        return self                                 # no aprende nada: regla fija
    def predict(self, X):
        return ["apto" if horas >= self.umbral else "no apto" for horas in X]

class UmbralAprendido(Umbral):                      # herencia: reutiliza predict de Umbral
    def fit(self, X, y):                            # sobrescribe fit (overriding)
        mejores = max(sorted(set(X)), key=lambda u: Umbral(u).score(X, y))
        self.umbral = mejores
        return super().fit(X, y)                    # llama al método de la clase madre

horas = [1, 2, 3, 4, 5, 6, 7, 8]
notas = ["no apto", "no apto", "no apto", "apto", "no apto", "apto", "apto", "apto"]
for m in [Mayoria(), Umbral(5), UmbralAprendido()]:              # polimorfismo
    m.fit(horas, notas)
    print(f"{type(m).__name__:<16} {m.score(horas, notas):.2f}")
# Mayoria          0.50
# Umbral           0.75
# UmbralAprendido  0.88
try:
    Modelo()
except TypeError as e:
    print("No se puede crear un Modelo abstracto")
```

| Concepto | En el ejemplo |
|----------|---------------|
| **Herencia** | `UmbralAprendido(Umbral)` reutiliza `predict` y `__init__` |
| **Sobrescritura** (*overriding*) | `UmbralAprendido.fit` sustituye al `fit` de `Umbral`; `super()` llama al original |
| **Polimorfismo** | El mismo bucle llama a `fit` y `score` sin saber qué modelo es |
| **Abstracción** | `Modelo(ABC)` define el contrato; no se puede instanciar |
| **Sobrecarga** (*overloading*) | Python **no** tiene varias funciones con el mismo nombre y distintos parámetros; se simula con valores por defecto (`umbral=4`) o `*args` |

En Python, una **interfaz** es una clase abstracta en la que todos los métodos son abstractos. A diferencia de Java, un método abstracto **puede** tener código, que las hijas aprovechan con `super()`. Para clases que solo guardan datos, `@dataclass` (módulo `dataclasses`) escribe solo `__init__`, `__repr__` y `__eq__`.

#### Herencia múltiple y orden de búsqueda (MRO)

Una clase puede heredar de varias. Cuando se llama a un método, Python lo busca en un orden fijo, el **MRO** (*Method Resolution Order*), que se calcula con un algoritmo llamado **linealización C3**: primero la propia clase, después sus padres de izquierda a derecha, sin repetir ninguna y sin que un padre aparezca antes que sus hijas.

```python
class A:
    def ola(self): return "A"
class B(A):
    def ola(self): return "B→" + super().ola()
class C(A):
    def ola(self): return "C→" + super().ola()
class D(B, C):
    def ola(self): return "D→" + super().ola()

print(D().ola())                              # D→B→C→A
print([k.__name__ for k in D.__mro__])        # ['D', 'B', 'C', 'A', 'object']
```

Fíjate: el `super()` de **B** llama a **C**, no a A. `super()` no significa «mi padre», sino «la siguiente clase del MRO del objeto». Por eso A solo se ejecuta una vez aunque D la herede por dos caminos (el problema del «diamante»). `D.mro()` devuelve lo mismo en forma de lista.

**Sobrecarga de métodos.** Python no permite dos métodos con el mismo nombre y distintos parámetros (como Java): el segundo sustituye al primero. Se consigue lo mismo con valores por defecto (`def suma(self, a, b=0, c=0)`) o con `*args`. Para elegir el código según el **tipo** del argumento existe `functools.singledispatch`.

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

#### Decoradores paso a paso

Un **decorador** es una función que recibe una función y devuelve otra que la «envuelve»: hace algo antes, la llama y hace algo después. Así se añade un comportamiento (registrar, medir tiempos, reintentar, comprobar permisos) **sin tocar** el código de la función original. Se entiende en cuatro pasos.

**1. Una función es un objeto más**: se puede guardar en una variable, pasar como argumento y devolver.

```python
def saludar(nome):
    return f"Ola, {nome}"

f = saludar           # sin paréntesis: la función, no su resultado
print(f("Iria"))      # Ola, Iria
```

**2. Un decorador escrito a mano.** La función interna (`envoltura`) recuerda `func` aunque `log` ya haya terminado: es un **cierre** (*closure*).

```python
def log(func):
    def envoltura(*args, **kwargs):
        print(f"→ {func.__name__}{args}")
        resultado = func(*args, **kwargs)
        print(f"← {resultado}")
        return resultado
    return envoltura

def media(a, b):
    return (a + b) / 2

media = log(media)    # «decorar» a mano
media(6, 9)           # → media(6, 9)
                      # ← 7.5
```

**3. La `@` es solo una abreviatura** de la línea `media = log(media)`:

```python
@log
def media(a, b):
    return (a + b) / 2
```

Este `@log` es el de las chuletas de Python, que lo usan sin definirlo: `log` no viene con Python, hay que escribirlo antes (o importarlo).

**4. `functools.wraps` conserva el nombre y la documentación.** Sin él, `media.__name__` vale `"envoltura"`, y los mensajes de error, la ayuda y algunas herramientas se confunden. Por eso todos los decoradores serios lo usan:

```python
import functools

def log(func):
    @functools.wraps(func)            # copia __name__, __doc__... de func a envoltura
    def envoltura(*args, **kwargs):
        print(f"→ {func.__name__}{args}")
        return func(*args, **kwargs)
    return envoltura
```

**Decoradores con parámetros.** `@reintentar(veces=3)` primero **llama** a `reintentar(3)`, que devuelve el decorador de verdad. Por eso hay tres funciones, una dentro de otra:

```python
def reintentar(veces):
    def decorador(func):
        @functools.wraps(func)
        def envoltura(*args, **kwargs):
            for intento in range(1, veces + 1):
                try:
                    return func(*args, **kwargs)
                except ConnectionError as e:          # solo el error que tiene sentido repetir
                    print(f"Intento {intento} fallido: {e}")
            raise ConnectionError(f"{func.__name__}: {veces} intentos sin éxito")
        return envoltura
    return decorador

@reintentar(veces=3)
def descargar():
    ...                                               # p. ej., pedir un CSV a una web (14.10)
```

**Varios decoradores a la vez** se aplican de abajo arriba (el más cercano a `def` envuelve primero):

```python
@dobre                # dobre(mais_un(tres)): (3 + 1) * 2 = 8
@mais_un
def tres():
    return 3
```

Con el orden cambiado, `(3 * 2) + 1 = 7`: el orden importa.

**Decoradores que ya usas sin saberlo:**

| Decorador | Qué hace | Dónde |
|-----------|----------|-------|
| `@property` | Un método que se usa como un atributo y permite validar | POO, más arriba |
| `@staticmethod`, `@classmethod` | Métodos que no necesitan el objeto | POO, más arriba |
| `@dataclass` | Escribe `__init__`, `__repr__` y `__eq__` por ti | POO, más arriba |
| `@functools.lru_cache` | Guarda resultados ya calculados (memoización): `fib(80)` sale al instante | [14.12](#1412-algoritmia-pensar-antes-de-programar) |
| `@app.route`, `@app.post` | Asocian una dirección web a una función | Flask y FastAPI (13.4, 13.7) |
| `@st.cache_data` | Streamlit no repite una carga lenta de datos | 13.7 |
| `@pytest.fixture` | Prepara datos para los tests | 14.11 |
| `@torch.no_grad()` | Desactiva el cálculo de gradientes en una función de predicción | 12.2 |

> **Ojo:** un decorador cambia lo que hace la función cada vez que se llama, así que conviene que sea sencillo y que no se trague los errores (`except Exception: pass` dentro de un decorador esconde todos los fallos del programa). Se practica en el [ejercicio E87](ejercicios.html#bloque-q--de-las-chuletas-al-código-e87e90).

#### Iteradores y generadores por dentro

Un **iterable** es algo que se puede recorrer (lista, texto, archivo); un **iterador** es el objeto que lleva la cuenta de por dónde va. `for` hace esto por debajo:

```python
it = iter(["Vigo", "Lugo"])     # pide un iterador al iterable
print(next(it))                  # Vigo
print(next(it))                  # Lugo
# next(it) otra vez → StopIteration: el for la captura y termina
```

Un **generador** es la forma fácil de crear un iterador: una función con `yield`, que **se pausa** en cada valor y continúa donde lo dejó. No guarda todo en memoria, por eso es la forma de recorrer datos enormes. El caso típico en IA es repartir los datos en **lotes** (*batches*) para entrenar:

```python
import sys

def lotes(datos, tamaño):
    for i in range(0, len(datos), tamaño):
        yield datos[i:i + tamaño]

for lote in lotes(list(range(10)), 4):
    print(lote)                  # [0, 1, 2, 3] · [4, 5, 6, 7] · [8, 9]

lista = [x * x for x in range(1_000_000)]
gen = (x * x for x in range(1_000_000))       # expresión generadora: paréntesis
print(sys.getsizeof(lista) > 8_000_000, sys.getsizeof(gen) < 500)   # True True
print(sum(gen) == sum(lista))                  # True, pero gen ya se ha gastado
```

La lista ocupa unos 8 MB; el generador, unos 200 bytes, porque calcula cada valor cuando se le pide. A cambio, **solo se puede recorrer una vez**.

#### Concurrencia: hilos, procesos y `asyncio`

Un programa normal hace las cosas **de una en una**. Hay tres formas de hacer varias a la vez, y elegir bien depende de **qué hace esperar** al programa:

| Tipo de tarea | Qué la frena | Ejemplo | Herramienta |
|---------------|--------------|---------|-------------|
| **De entrada/salida** (*I/O-bound*) | Esperar: red, disco, una API | Descargar 50 imágenes, llamar a una API de un LLM | Hilos (`threading`) o `asyncio` |
| **De cálculo** (*CPU-bound*) | El procesador | Procesar miles de imágenes, buscar primos | Procesos (`multiprocessing`) |

**El GIL.** En la versión habitual de Python, un candado interno (*Global Interpreter Lock*) deja que **solo un hilo ejecute código Python a la vez**. Mientras un hilo espera la red, otro avanza, así que los hilos aceleran las esperas, **pero no los cálculos**. Los procesos tienen cada uno su intérprete y su memoria, así que sí usan varios núcleos de verdad, a cambio de tardar más en arrancar y de no compartir variables. Desde Python 3.13 existe una versión opcional sin GIL, pero no es todavía la que se instala por defecto.

```python
import time, asyncio
from concurrent.futures import ThreadPoolExecutor

def descargar(n):                     # simula esperar a la red medio segundo
    time.sleep(0.5)
    return f"imagen_{n}.jpg"

t = time.perf_counter()
seguidas = [descargar(n) for n in range(8)]
print(f"De una en una: {time.perf_counter() - t:.1f} s")      # De una en una: 4.0 s

t = time.perf_counter()
with ThreadPoolExecutor(max_workers=8) as ex:                 # 8 hilos
    con_hilos = list(ex.map(descargar, range(8)))
print(f"Con hilos:     {time.perf_counter() - t:.1f} s")      # Con hilos:     0.5 s

async def descargar_async(n):         # corrutina: se puede pausar mientras espera
    await asyncio.sleep(0.5)
    return f"imagen_{n}.jpg"

async def principal():
    return await asyncio.gather(*(descargar_async(n) for n in range(8)))

t = time.perf_counter()
con_async = asyncio.run(principal())  # en Jupyter/Colab: await principal()
print(f"Con asyncio:   {time.perf_counter() - t:.1f} s")      # Con asyncio:   0.5 s
```

Para el cálculo, procesos. En un archivo `.py` (en Jupyter y Colab `multiprocessing` da problemas con funciones definidas en el cuaderno):

```python
from multiprocessing import Pool

def es_primo(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))

if __name__ == "__main__":            # obligatorio: evita que cada proceso vuelva a lanzar procesos
    numeros = range(5_000_000, 5_200_000)
    with Pool() as pool:              # tantos procesos como núcleos
        print(sum(pool.map(es_primo, numeros, chunksize=10_000)))   # 12894 primos
```

En un ordenador de dos núcleos, este cálculo pasa de 1,5 s (un solo proceso) a 0,8 s: casi la mitad, nunca menos, porque el reparto también cuesta. Con cuatro hilos no mejora: en la misma prueba tardó **más** (3,2 s), por el GIL y el coste de cambiar de un hilo a otro.

**Condiciones de carrera.** Si varios hilos modifican la misma variable, pueden pisarse: los dos leen 10, los dos suman 1 y los dos guardan 11. Se evita con un candado (`threading.Lock`) que deja pasar a un hilo cada vez:

```python
import threading
saldo, candado = 0, threading.Lock()

def ingresar(n):
    global saldo
    for _ in range(n):
        with candado:                 # sin estas dos líneas, el resultado sale mucho menor
            actual = saldo
            time.sleep(0)             # cede el turno: hace visible el problema
            saldo = actual + 1

hilos = [threading.Thread(target=ingresar, args=(1000,)) for _ in range(4)]
for h in hilos: h.start()
for h in hilos: h.join()             # esperar a que terminen
print(saldo)                          # 4000 (sin candado salía unos 1000)
```

| | Hilos | Procesos | `asyncio` |
|-|-------|----------|-----------|
| Memoria | Compartida (cuidado con las carreras) | Separada | Compartida, un solo hilo |
| Coste de arrancar | Bajo | Alto | Muy bajo |
| Bueno para | Esperas (red, disco) | Cálculo | Muchísimas esperas a la vez (servidores, APIs) |
| En IA | Descargar datos, llamar a varias APIs | Preprocesar imágenes en paralelo | Servir un modelo con FastAPI (13.7), pedir respuestas a un LLM en paralelo |

`asyncio` solo acelera lo que está escrito para ser asíncrono (`await` sobre algo que espera). Una función normal que bloquea, como `time.sleep` o leer un archivo con `open`, **bloquea todo** aunque esté dentro de `async def`. Las expresiones regulares (`re`) están en la UD4 (sección 10) y los archivos JSON y CSV, en 5.9 y 14.10.

#### Cómo ejecuta Python tu programa y cómo gestiona la memoria

**¿Interpretado o compilado?** Las dos cosas. Python (la versión habitual, CPython) primero **compila** todo el archivo a *bytecode*, unas instrucciones sencillas para su máquina virtual, y después las **interpreta**. Por eso un error de sintaxis al final del archivo impide ejecutar **cualquier** línea, aunque la primera sea correcta:

```python
print("Ola")
print("Adeus"          # SyntaxError: '(' was never closed... ¡y no se imprime «Ola»!
```

El *bytecode* de los módulos importados se guarda en la carpeta `__pycache__` (archivos `.pyc`) para no repetir la compilación. Se puede ver con el módulo `dis`:

```python
import dis
def media(a, b):
    return (a + b) / 2
dis.dis(media)          # LOAD_FAST_LOAD_FAST (a, b) · BINARY_OP (+) · LOAD_CONST 2 · BINARY_OP (/) · RETURN_VALUE
```

| | Compilado a código máquina (C, Go) | Python (CPython) |
|-|------------------------------------|------------------|
| Cuándo se traduce | Una vez, antes de ejecutar, a instrucciones del procesador | Cada vez que se ejecuta (o se reutiliza el `.pyc`), a *bytecode* |
| Errores de sintaxis | Al compilar | También antes de ejecutar nada |
| Errores de tipos (`"a" + 1`) | Normalmente al compilar | Solo cuando se ejecuta esa línea |
| Velocidad | Más rápido | Más lento; por eso NumPy y PyTorch hacen las cuentas en C (7.1) |

**Variables, objetos y `is`.** Una variable no es una caja: es una **etiqueta** pegada a un objeto. `==` pregunta si dos objetos **valen** lo mismo; `is`, si son **el mismo objeto**:

```python
l1, l2 = [1, 2], [1, 2]
print(l1 == l2, l1 is l2)            # True False: iguales, pero son dos listas
a, b = int("1000"), int("1000")
print(a == b, a is b)                # True False
x = None
print(x is None)                     # True: con None, True y False sí se usa «is»
```

Python reutiliza algunos objetos pequeños (los enteros de −5 a 256, algunas cadenas cortas), así que `256 is 256` puede dar `True` y `1000 is 1000`, `False`. Es un detalle interno que puede cambiar: para comparar valores, **siempre `==`**.

**Recuento de referencias y recolector de basura.** Cada objeto lleva la cuenta de cuántas etiquetas apuntan a él. Cuando llega a 0, se libera en ese momento. `del x` no borra el objeto: quita una etiqueta.

```python
import sys, gc
a = [1, 2, 3]
print(sys.getrefcount(a))     # 2 (a + la referencia temporal de la propia llamada)
b = a
print(sys.getrefcount(a))     # 3
del b
print(sys.getrefcount(a))     # 2   (los números exactos cambian entre versiones de Python)

class Nodo:
    def __init__(self):
        self.outro = None
x, y = Nodo(), Nodo()
x.outro, y.outro = y, x       # se apuntan entre sí: un ciclo
del x, y                      # nadie más los usa, pero cada uno sigue con 1 referencia
print(gc.collect())           # 2 (o más, si había otra basura pendiente): encuentra el ciclo y lo libera
```

El recuento no puede liberar los **ciclos**. Para eso está el **recolector de basura** (`gc`), que se ejecuta de vez en cuando y separa los objetos en tres **generaciones**: los nuevos se revisan a menudo y los que sobreviven, cada vez menos (casi todos los objetos mueren jóvenes). Para los objetos pequeños, Python usa además su propio reservador de memoria (*pymalloc*), que pide memoria al sistema en bloques grandes y la reparte, más rápido que pedirla objeto a objeto.

**Copias.** `b = a` no copia nada (otra etiqueta); `a.copy()` o `copy.copy(a)` copian solo el primer nivel (las listas de dentro se comparten), y `copy.deepcopy(a)` lo copia todo (ver 5.4).

**El GIL no protege tus datos.** Como se vio en *Concurrencia*, el GIL deja que solo un hilo ejecute *bytecode* a la vez, pero puede cambiar de hilo **entre dos instrucciones**. Una operación como «leer el contador y guardar el contador + 1» puede quedar partida:

```python
import threading, time
contador = 0
def sumar(n):
    global contador
    for _ in range(n):
        valor = contador        # leer
        time.sleep(0)           # cede el turno, como haría una operación real (leer un archivo, la red...)
        contador = valor + 1    # escribir
fios = [threading.Thread(target=sumar, args=(1000,)) for _ in range(4)]
for f in fios: f.start()
for f in fios: f.join()
print(contador)                 # ¡1000 o 1001 en lugar de 4000!
```

Con un candado (`candado = threading.Lock()` y `with candado:` alrededor de leer y escribir) sale siempre 4000. Desde Python 3.13 existe además una versión **sin GIL** (*free-threaded*), opcional y todavía minoritaria, donde los hilos sí trabajan a la vez en varios núcleos; con ella, los candados son todavía más necesarios.

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
| Python Notes: the 7-day plan (@thedataguy16), 14 páginas procesadas con OCR | Listas de diccionarios como tablas, CSV con `csv`, datos sucios con `try/except`, decimales y `Decimal`, trampas de copias y valores por defecto | 5.9 y ejercicios E38–E41 |
| 15 Gen AI Concepts, Part 1 (@darpan.decoded), apuntes visuales procesados con OCR | Ventana de contexto, temperatura y muestreo, RAG y bases vectoriales, ajuste fino, herramientas, agentes, multimodalidad | 14.8 y ejercicios E42–E46 |
| *Supervised Machine Learning – Complete Guide* (PDF, 27 págs.) | Preparación de datos con `ColumnTransformer`, regularización, umbral de decisión, desequilibrio, fuga de datos, ensembles, explicabilidad, plantilla de proyecto | [UD5](ud5-ml.html), secciones 2–7 y 10, ejercicios 3.2, 5.3 y 6.2 |
| *Transformer – Complete Handwritten Study Handbook* (@abhi_techhub), procesado con OCR | Codificación de posición, atención multicabeza, residual y normalización, máscara causal, atención cruzada, entrenamiento y coste | [UD4](ud4-lenguaje.html), sección 10.10 y ejercicios 10.8–10.9 |
| Python Part 3 (POO) y Part 4 (Python avanzado), Coded Soul (@codedsoul_05), procesados con OCR y MarkItDown | Clases, `@property`, métodos de clase y estáticos, métodos especiales, herencia, polimorfismo, clases abstractas; iteradores, generadores, hilos, procesos y `asyncio` | 14.14 y ejercicios E47–E52 |
| Python Part 1 y Part 2: Core Python (@codedsoul_05), apuntes manuscritos procesados con OCR | Conversión de tipos, formato, patrones, problemas numéricos, cadenas, conjuntos, comprensiones, `lambda`, `map`/`filter`/`reduce`, recursión, ámbito, módulos | 1.5, 2.4–2.6, 3.3–3.4, 4.6–4.10, 5.4–5.8 y ejercicios E28–E37 |
| *Pandas Library* (@Mastercode.sagar, 21 págs.), procesado con OCR y MarkItDown | Series, `loc`/`iloc`, filtros, valores que faltan, `merge`/`concat`, `groupby`, `apply`/`map`, fechas, Excel, gráficos | 7.3 y ejercicios E53–E58 |
| *Python Module 6: Strings* (@Mastercode.sagar, 11 págs.), procesado con OCR y MarkItDown | Formatos `%`, `format` y f-string, métodos de cadenas, programas típicos | 2.5, 2.6 y ejercicios E59–E61 |
| Listas de redes sociales: «10 great Python packages for Data Science» y «8 awesome GitHub repos» | Librerías y repositorios revisados uno a uno | 12.4 y repositorios de 14.15 |
| «The 25 Best Free Resources for Learning AI in 2026» (H. Sheikho, Substack, oct-2026) | Cursos, libros y vídeos gratuitos revisados uno a uno | 14.16; retropropagación a mano en 14.7 |
| Carrusel «Deep Learning Complete Notes» (@analyticswithsingh, 17 diapositivas, marcado como generado con IA) | Activaciones, propagación hacia delante, pérdidas, optimizadores, épocas y lotes, inicialización, dropout, CNN, RNN, Transformers; errores usados en E68 | 14.7, UD3 sección 5, ejercicios E62–E69 |
| *Python Module 7: Lists* (@Mastercode.sagar, 21 págs.) | Quitar elementos, *slicing* con asignación, `+` y `*`, trampas, listas de listas, recetas, errores típicos | 5.4 y ejercicios E70–E74 |
| *Python Module 8: Tuples* (@Mastercode.sagar, 15 págs.), procesado con OCR y MarkItDown | Crear tuplas, `count` e `index`, operaciones, tuplas anidadas, tupla frente a lista, desempaquetado, proyecto de registro | 5.3 y ejercicios E83–E86 |
| Seis chuletas dibujadas a mano (Python, NumPy, Pandas, PyTorch, TensorFlow y Terraform; sin autor indicado), publicadas tal cual en [Chuletas](chuletas.html) | Decoradores; `linspace`, `eye`, unir, dividir y guardar arrays; dispositivo, *autograd*, `DataLoader`, evaluación y `state_dict` en PyTorch; `tf.data`, TensorBoard y exportar en Keras; infraestructura como código | 7.1, 12.2, 13.8, 14.7, 14.14 y ejercicios E87–E90 |
| *200 Machine Learning Commands* (41 págs., sin autor indicado), procesado con MarkItDown | Línea base (`DummyClassifier`), exactitud equilibrada, MCC, curva precisión-exhaustividad, *log loss*, MAPE; curvas de validación y aprendizaje, `cross_validate`, estrategias de partición; silueta, DBSCAN, jerárquico, `GaussianMixture`, anomalías; `RobustScaler`, asimetría, `TargetEncoder`; variables de fecha, retrasos y medias móviles | [UD5](ud5-ml.html), secciones 2, 3, 5, 6, 7 y 8, y ejercicios E91–E94 |
| *Python Important Questions* (@abhi_techhub, 15 págs., sin capa de texto: Tesseract + MarkItDown) | Preguntas tipo entrevista: compilación a *bytecode*, memoria y recolector de basura, `is` frente a `==`, gestores de contexto, excepciones propias, MRO, trampas clásicas, programas típicos | 4.4, 14.14, 14.18 y ejercicios E95–E98 |
| Carrusel *Deep Learning Notes* (@ds_ai_ketan, 5 láminas generadas con IA) | ML frente a DL; capa de salida y pérdida según el problema; revisión crítica (multietiqueta, normalización por lotes, validación) | 14.1, 14.7 y ejercicio E99 |
| *Introduction to Data Science Using Python* (A. Agah, OER, licencia CC BY-NC 4.0) | Estadística descriptiva e inferencial, estandarizar, regresión, grafos y NetworkX; errores usados en E79 | 6.5–6.9, 14.17, ejercicios E75–E79 |
| *Neural Networks – Complete Study Guide* (codingwithmee_18, 49 págs.) | XOR con capa oculta, red desde cero en NumPy, normalización, calendarios de η, depuración, otras arquitecturas | 14.7 y ejercicios E80–E82 |

#### Repositorios para practicar con proyectos

Revisión de una lista muy compartida de «repos para aprender Python con proyectos» (estado a noviembre de 2026; las estrellas cambian cada día):

| Repositorio | Qué es en realidad | Para el curso |
|-------------|--------------------|---------------|
| [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) (≈ 290 000 ★) | Una **lista de enlaces** a tutoriales de proyectos, en muchos lenguajes; no contiene código propio | ✅ Buscar en la sección de Python ideas de proyecto final. Algunos enlaces llevan años sin revisarse |
| [realpython/materials](https://github.com/realpython/materials) | El código de los tutoriales de Real Python, carpeta por carpeta | ✅ Muy fiable; cada carpeta tiene un artículo que la explica (en inglés) |
| [markusschanta/awesome-jupyter](https://github.com/markusschanta/awesome-jupyter) | Lista de herramientas, extensiones y cuadernos de Jupyter | 🟡 Para el profesorado: buscar extensiones y cuadernos de ejemplo |
| [Python-World/python-mini-projects](https://github.com/Python-World/python-mini-projects) | Cientos de miniproyectos (juegos, utilidades) | 🟡 Ideas para practicar, pero el repositorio está **archivado desde 2022**: el código puede no funcionar con versiones actuales |
| [arpit-omprakash/100ProjectsOfCode](https://github.com/arpit-omprakash/100ProjectsOfCode) | Una **lista de 100 enunciados** de proyectos para cualquier lenguaje, sin soluciones | ✅ Buen banco de retos para quien termina antes; sin soluciones, obliga a pensar |
| [larymak/Python-project-Scripts](https://github.com/larymak/Python-project-Scripts) | Scripts de proyectos de todos los niveles, aportados por la comunidad | 🟡 Útil, pero la calidad varía mucho: revisar el código antes de usarlo |
| «Learn By Doing» y «Data Science Projects» | La lista no da el enlace y hay **varios repositorios** con esos nombres | ❌ No se puede recomendar sin saber cuál es: un nombre genérico sin enlace no es una fuente |

La lista no menciona ningún repositorio en castellano ni en gallego, y casi ninguno trata de **ciencia** con datos reales, aunque el título lo prometa. Para proyectos con datos de aquí, las fuentes de [Análisis de datos 1.6](datos.html#16-dónde-encontrar-datos-más-allá-de-kaggle) y los cuadernos del libro de la asignatura ([github.com/FranPuentes/iTI2025](https://github.com/FranPuentes/iTI2025)) encajan mejor. Los mismos criterios de 12.4 (actividad, versión, calidad, procedencia) sirven para elegir repositorios.

### 14.16 Recursos gratuitos para seguir aprendiendo IA

Revisión de la lista «The 25 Best Free Resources for Learning AI in 2026» (H. Sheikho, octubre de 2026). Todos son buenos, pero casi todos están pensados para la universidad o para profesionales. Aquí se ordenan según lo que sirve en 1º de Bachillerato (estado a noviembre de 2026).

**Para usar durante el curso.** Nivel adecuado, muy visuales y sin matemáticas universitarias. Están en inglés, pero los vídeos tienen subtítulos automáticos en castellano.

| Recurso | Qué es | Dónde encaja |
|---------|--------|--------------|
| [3Blue1Brown: *Neural Networks*](https://www.3blue1brown.com/topics/neural-networks) | Vídeos con animaciones: qué es una red, descenso de gradiente, retropropagación y, en los últimos capítulos, cómo funcionan los Transformers y la atención | 14.7, [UD4](ud4-lenguaje.html) 10.10 |
| [StatQuest (Josh Starmer)](https://www.youtube.com/@statquest) | Vídeos cortos que explican paso a paso un algoritmo o una idea de estadística | [UD5](ud5-ml.html): árboles, regresión logística, validación cruzada, *bias-variance* |
| [Google *Machine Learning Crash Course*](https://developers.google.com/machine-learning/crash-course) | Curso corto de Google con visualizaciones interactivas y ejercicios | UD5, para repasar vocabulario y métricas |
| [Kaggle Learn](https://www.kaggle.com/learn) | Microcursos en el navegador: Python, Pandas, *Intro to Machine Learning*, *Computer Vision*… | UD2, [UD3](ud3-vision.html), UD5 |
| [Jay Alammar: *The Illustrated Transformer*](https://jalammar.github.io/illustrated-transformer/) | Explicación del Transformer con dibujos, paso a paso | UD4 10.10, antes de leer cualquier artículo |
| [Hugging Face Learn](https://huggingface.co/learn) | Cursos prácticos de LLM, agentes, visión y difusión con las librerías de Hugging Face. El curso de LLM tiene [traducción parcial al castellano](https://huggingface.co/docs/course/es/chapter1/1) | Proyectos de UD3 y UD4 |

**Para quien quiera ir más lejos.** Alumnado muy motivado o profesorado. Requieren más tiempo, más inglés y, a veces, derivadas.

| Recurso | Qué es | Antes de empezar |
|---------|--------|------------------|
| [A. Karpathy: *Neural Networks: Zero to Hero*](https://karpathy.ai/zero-to-hero.html) | Construye desde cero una red, luego un modelo de lenguaje y un GPT pequeño, sin librerías que escondan nada | La retropropagación a mano de 14.7 es una versión mínima del primer vídeo |
| [fast.ai: *Practical Deep Learning for Coders*](https://course.fast.ai/) | Entrena modelos que funcionan desde la primera clase; la teoría llega después | Funciona en Colab |
| [MIT 6.S191: *Introduction to Deep Learning*](http://introtodeeplearning.com/) | Curso intensivo que se renueva cada año, con prácticas en Python | Buena panorámica de lo más reciente |
| [*Dive into Deep Learning*](https://d2l.ai/) | Libro interactivo con código ejecutable en cada capítulo | Necesita PyTorch |
| [mlcourse.ai](https://mlcourse.ai/) | Curso práctico con tareas y soluciones sobre datos reales | Alternativa al curso de Coursera |
| [M. Labonne: *LLM Course*](https://github.com/mlabonne/llm-course) | Hoja de ruta y cuadernos de Colab sobre ajuste fino, cuantización, RAG y despliegue | Profesorado: ideas para ampliar 14.8 |
| [Lil'Log (Lilian Weng)](https://lilianweng.github.io/) y [Hugging Face Papers](https://huggingface.co/papers) | Artículos de repaso muy documentados y selección diaria de artículos de investigación | Profesorado: estar al día |

**Para después del Bachillerato.** Son material universitario. Exigen álgebra lineal, cálculo de varias variables y probabilidad.

- *Mathematics for Machine Learning* ([mml-book.github.io](https://mml-book.github.io/)): las matemáticas que hay debajo de todo lo anterior.
- *Understanding Deep Learning* de S. Prince ([udlbook](https://udlbook.github.io/udlbook/)) y *Deep Learning* de Goodfellow, Bengio y Courville ([deeplearningbook.org](https://www.deeplearningbook.org/)). Este último es de 2016: sus capítulos de arquitecturas se han quedado antiguos y no trata los Transformers.
- Cursos de Stanford: [CS229](https://cs229.stanford.edu/) (ML), [CS231n](https://cs231n.stanford.edu/) (visión), [CS224n](https://web.stanford.edu/class/cs224n/) (lenguaje) y [CS336](https://stanford-cs336.github.io/) (entrenar un modelo de lenguaje desde cero, muy exigente).
- Aprendizaje por refuerzo: el libro de [Sutton y Barto](http://incompleteideas.net/book/the-book-2nd.html) y la guía [*Spinning Up*](https://spinningup.openai.com/) de OpenAI.

**Lo que no conviene recomendar.**

- *Machine Learning Handbook* de Yandex y *Deep Learning School* del MIPT: están **en ruso**.
- *Machine Learning Specialization* de Andrew Ng (Coursera): la lista dice que se puede seguir gratis como oyente, pero desde agosto de 2025 Coursera **retiró ese modo** en muchos cursos y en los de DeepLearning.AI solo deja ver gratis la primera semana. Antes de recomendarlo, comprueba cómo está el acceso.

**Lo que falta en la lista.** No incluye nada en castellano ni en gallego. Como primer curso de IA en castellano, sin programar, está [*Elements of AI*](https://www.elementsofai.com/) (Universidad de Helsinki; la versión en castellano, «Elementos de la IA», es de la UNED). Y para cualquier recurso sirven las mismas preguntas de 12.4: si está actualizado, qué nivel exige y quién lo publica.

### 14.17 Redes y grafos con NetworkX

Un **grafo** es un conjunto de **nodos** unidos por **aristas** (sección [0.7](#07-algoritmos-y-resolución-de-problemas-por-búsqueda)). Sirve para cualquier cosa hecha de conexiones: carreteras entre ciudades, amistades, seguidores en una red social, enlaces entre páginas web o rutas de autobús.

| Concepto | Qué es | Ejemplo |
|----------|--------|---------|
| **No dirigido** | La relación va en los dos sentidos | Amistad, carretera de doble sentido |
| **Dirigido** | Cada arista tiene sentido | Seguir a alguien en una red social |
| **Ponderado** | Cada arista tiene un valor | Kilómetros, minutos, número de mensajes |
| **Grado** | Número de aristas de un nodo (en dirigidos: de **entrada** y de **salida**) | Cuántos amigos tiene; cuántos seguidores |
| **Camino más corto** | El de menos aristas o, si hay pesos, el de menor suma | Ruta del GPS |
| **Componente conexa** | Grupo de nodos conectados entre sí, pero no con el resto | Dos grupos de amigos que no se conocen |

[NetworkX](https://networkx.org/) es la librería de Python para crear y analizar grafos. El grafo de carreteras de Galicia de la sección 0, con NetworkX:

```python
import networkx as nx

G = nx.Graph()
for ciudad, vecinas in galicia.items():          # el diccionario de la sección 0.7
    for vecina, km in vecinas.items():
        G.add_edge(ciudad, vecina, km=km)

G.number_of_nodes(), G.number_of_edges()         # 7 9
dict(G.degree())["Santiago"]                     # 4: la ciudad con más conexiones
nx.shortest_path(G, "Ferrol", "Ourense", weight="km")
# ['Ferrol', 'A Coruña', 'Santiago', 'Ourense']
nx.shortest_path_length(G, "Ferrol", "Ourense", weight="km")   # 238
```

Sin `weight="km"`, NetworkX busca el camino con **menos aristas**, y aquí hay dos empatados a tres tramos: por Santiago (238 km) y por Lugo (248 km). Con el peso, calcula el de **menos kilómetros** con el algoritmo de Dijkstra, el mismo que se programó a mano en la sección 0.

**¿Quién es importante en una red?** La **centralidad** lo mide, y hay varias formas de entender «importante». Con una red de amistades inventada de una clase:

```python
amistades = [("Uxía", "Brais"), ("Uxía", "Antía"), ("Brais", "Antía"), ("Antía", "Xoán"),
             ("Xoán", "Iria"), ("Iria", "Martín"), ("Martín", "Noa"), ("Iria", "Noa"),
             ("Xoán", "Noa"), ("Lucía", "Sabela"), ("Sabela", "Hugo")]
R = nx.Graph(amistades)
nx.degree_centrality(R)        # Antía, Xoán, Iria y Noa: 3 amistades cada una (0.333)
nx.betweenness_centrality(R)   # Xoán 0.25, Antía 0.22, el resto mucho menos
nx.closeness_centrality(R)     # Xoán 0.44, Antía 0.40
[sorted(c) for c in nx.connected_components(R)]
# [['Antía', 'Brais', 'Iria', 'Martín', 'Noa', 'Uxía', 'Xoán'], ['Hugo', 'Lucía', 'Sabela']]
```

| Centralidad | Pregunta que responde | En el ejemplo |
|-------------|-----------------------|---------------|
| **De grado** | ¿Quién tiene más conexiones directas? | Empate entre cuatro personas |
| **De intermediación** (*betweenness*) | ¿Por quién pasan más caminos más cortos entre otros? Son los **puentes** | Xoán y Antía unen los dos subgrupos de la clase |
| **De cercanía** (*closeness*) | ¿Quién está, de media, más cerca de todos? (inversa de la distancia media) | Xoán |

Que alguien tenga muchas conexiones no lo convierte en puente: Iria y Noa tienen tantas amistades como Xoán, pero si Xoán faltara, el grupo de Uxía y el de Martín quedarían menos conectados. Y Lucía, Sabela y Hugo forman una componente aparte: no hay ningún camino entre ellos y el resto.

Para dibujarlo: `nx.draw_networkx(R)` y `plt.show()`. En redes dirigidas se usa `nx.DiGraph()`, y `in_degree` / `out_degree` dan los seguidores y los seguidos.

**Sobre datos de personas reales:** analizar las relaciones de gente concreta (quién habla con quién, quién sigue a quién) es tratar datos personales. En clase se usan datos inventados o redes de ejemplo, como `nx.karate_club_graph()`.

Los ejercicios [E75–E79](ejercicios.html#bloque-n--estadística-y-redes-e75e79) practican la estadística de la sección 6 y estas redes.

### 14.18 Preguntas de repaso de Python (tipo entrevista)

Las mismas preguntas aparecen una y otra vez en exámenes, entrevistas de prácticas y listas de «preguntas importantes de Python». Esta tabla da la respuesta corta y el lugar de estos apuntes donde se explica con calma. Sirve para **repasar**: tapa la columna de la respuesta e intenta contestar.

| Pregunta | Respuesta corta | Dónde |
|----------|-----------------|-------|
| ¿Python es interpretado o compilado? | Las dos cosas: compila a *bytecode* y lo interpreta. Por eso un error de sintaxis impide ejecutar todo el archivo | [14.14, Cómo ejecuta Python...](#cómo-ejecuta-python-tu-programa-y-cómo-gestiona-la-memoria) |
| ¿Qué es el tipado dinámico? | El tipo va con el **valor**, no con la variable: `x = 5` y después `x = "cinco"` es válido. No significa «sin tipos»: `"5" + 5` da `TypeError` | [2](#2️⃣-tipos-de-datos-en-python), [2.4](#24-conversión-de-tipos-casting) |
| `type()` o `isinstance()` | `isinstance(x, int)` también acepta las clases hijas, y es lo que se usa para comprobar | [2.4](#24-conversión-de-tipos-casting) |
| Mutables e inmutables | Mutables: `list`, `dict`, `set`. Inmutables: `int`, `float`, `str`, `tuple`, `bool`. Un inmutable «cambia» creando otro objeto | [5.3](#53-tuplas-a-fondo-registros-que-no-cambian), [5.4](#54-listas-a-fondo-más-métodos-copias-y-alias) |
| ¿Por qué las cadenas son inmutables? | Para poder usarlas como claves de diccionario (su *hash* no puede cambiar), para compartirlas sin peligro entre variables y para que Python reutilice las repetidas | [2.6](#26-cadenas-a-fondo-índices-slicing-e-inmutabilidad), [14.9](#149-hashing-por-qué-los-diccionarios-son-tan-rápidos) |
| Lista, tupla, conjunto o diccionario | Lista: ordenada y cambiante. Tupla: registro fijo. Conjunto: sin repetidos, «¿está?» muy rápido. Diccionario: buscar por clave | [5](#5️⃣-estructuras-de-datos-complejas) |
| ¿Cuánto tarda buscar en un diccionario? | Un tiempo constante **de media**, O(1), gracias al *hash*; en una lista, O(n) | [14.9](#149-hashing-por-qué-los-diccionarios-son-tan-rápidos) |
| `/` frente a `//` | `7 / 2` = 3.5 siempre decimal; `7 // 2` = 3, división entera **hacia abajo** (`-7 // 2` = −4) | [1](#1️⃣-fundamentos-de-programación) |
| `is` frente a `==` | `==` compara valores; `is`, si es el mismo objeto. `is` solo para `None`, `True` y `False` | [14.14, Cómo ejecuta Python...](#cómo-ejecuta-python-tu-programa-y-cómo-gestiona-la-memoria) |
| `break`, `continue`, `pass` | Salir del bucle; saltar a la siguiente vuelta; no hacer nada (hueco que se rellenará) | [3.2](#32-bucles-for-y-while) |
| `*args` y `**kwargs` | Argumentos de más, en una tupla y en un diccionario | [4.6](#46-argumentos-y-valores-de-retorno) |
| Regla LEGB | Orden de búsqueda de un nombre: Local, Envolvente, Global, Integrado (*Built-in*) | [4.10](#410-ámbito-de-las-variables-regla-legb) |
| Cierre (*closure*) | Una función interna que recuerda variables de la función que la creó, aunque esa ya haya terminado | [Decoradores paso a paso](#decoradores-paso-a-paso) |
| Decorador | Función que envuelve a otra para añadirle algo sin cambiar su código | [Decoradores paso a paso](#decoradores-paso-a-paso) |
| Iterable, iterador y generador | Iterable: se puede recorrer (`iter()`). Iterador: da el siguiente con `next()` y se agota. Generador: un iterador escrito con `yield` | [Iteradores y generadores por dentro](#iteradores-y-generadores-por-dentro) |
| Gestor de contexto | Un objeto con `__enter__` y `__exit__` que se usa con `with` y garantiza la limpieza | [Gestores de contexto...](#gestores-de-contexto-y-excepciones-propias) |
| `else` y `finally` en un `try` | `else`: si **no** hubo error. `finally`: siempre, incluso tras un `return` | [Excepciones completas](#excepciones-completas-try--except--else--finally-y-raise) |
| Excepciones propias | Clases que heredan de `Exception`, mejor con una base común | [Gestores de contexto...](#gestores-de-contexto-y-excepciones-propias) |
| Los cuatro pilares de la POO | Encapsulación, herencia, polimorfismo y abstracción | [POO](#programación-orientada-a-objetos-los-cuatro-pilares) |
| `@classmethod` y `@staticmethod` | El primero recibe la clase (`cls`) y sirve para crear objetos de otras formas; el segundo no recibe nada: una utilidad dentro de la clase | [POO con código](#poo-con-código-de-una-clase-a-un-mini-scikit-learn) |
| ¿Hay sobrecarga de métodos? | No como en Java: valores por defecto o `*args` | [Herencia múltiple y MRO](#herencia-múltiple-y-orden-de-búsqueda-mro) |
| MRO y `super()` | Orden de búsqueda en herencia múltiple (C3); `super()` llama a la **siguiente** clase de ese orden | [Herencia múltiple y MRO](#herencia-múltiple-y-orden-de-búsqueda-mro) |
| Copia superficial y profunda | `copy()` comparte lo de dentro; `deepcopy()` lo duplica todo | [5.4](#54-listas-a-fondo-más-métodos-copias-y-alias) |
| ¿Cómo gestiona Python la memoria? | Recuento de referencias + recolector de basura para los ciclos | [Cómo ejecuta Python...](#cómo-ejecuta-python-tu-programa-y-cómo-gestiona-la-memoria) |
| GIL; hilos, procesos o `asyncio` | Un solo hilo ejecuta Python a la vez. Hilos o `asyncio` para esperar (red, archivos); procesos para calcular | [Concurrencia](#concurrencia-hilos-procesos-y-asyncio) |
| Módulo y paquete | Módulo: un archivo `.py`. Paquete: una carpeta de módulos (con `__init__.py`) | [5.7](#57-funciones-integradas-y-módulos-útiles) |
| Entorno virtual | Una carpeta con su propio Python y sus librerías para cada proyecto: `python -m venv venv` y activarlo | [Estilo y organización](#estilo-y-organización-de-un-proyecto) |
| Modos de `open()` | `"r"` leer, `"w"` escribir (¡borra lo que había!), `"a"` añadir al final, `"x"` crear (error si ya existe), `"b"` binario | [5.9](#59-de-python-puro-a-una-tabla-de-datos), [14.10](#1410-automatización-con-python) |

**Trampas clásicas («¿qué imprime?»).** Son las preguntas favoritas de los exámenes porque obligan a entender qué pasa por dentro:

```python
def engadir(nota, lista=[]):      # 1. el valor por defecto se crea UNA vez, al definir la función
    lista.append(nota)
    return lista
print(engadir(5), engadir(7))     # [5, 7] [5, 7]: ¡las dos llamadas comparten la misma lista!
# Solución: def engadir(nota, lista=None): if lista is None: lista = []

funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])       # 2. [2, 2, 2]: las lambdas leen «i» al llamarlas, cuando ya vale 2
funcs = [lambda i=i: i for i in range(3)]
print([f() for f in funcs])       #    [0, 1, 2]: el valor por defecto guarda el de cada vuelta

g = (x * x for x in range(3))
print(sum(g), sum(g))             # 3. 5 0: un generador se agota la primera vez

def f():
    try:
        return "try"
    finally:
        print("finally")          # 4. imprime «finally» y después «try»: finally va antes de salir
print(f())

print(1 < 2 < 3, (3 > 2) > 1)     # 5. True False: 1 < 2 < 3 es «1 < 2 and 2 < 3»; (3 > 2) es True, que vale 1
print(0.1 + 0.2 == 0.3)           # 6. False: los decimales no son exactos (2.2); usar math.isclose
print({True: "a", 1: "b", 1.0: "c"})   # 7. {True: 'c'}: True == 1 == 1.0 tienen el mismo hash: es la misma clave
```

Los ejercicios [E95–E98](ejercicios.html#bloque-s--python-a-fondo-preguntas-tipo-entrevista-e95e98) practican estas preguntas, los programas clásicos de las entrevistas (palíndromos, anagramas, primos...) y la revisión crítica de una hoja de «preguntas importantes de Python».

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
- [StatQuest with Josh Starmer](https://www.youtube.com/@statquest) - YouTube

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
  ║ UD3: Visión Artificial             ║
  ║ - Imágenes como datos numéricos    ║
  ║ - Redes convolucionales            ║
  ║ - Big Data: datasets de imágenes   ║
  ║                                    ║
  ║ UD4: NLP (lenguaje natural)        ║
  ║ - Aplicar ETL a textos masivos     ║
  ║ - Análisis de sentimientos         ║
  ║ - Big Data: millones de palabras   ║
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
- ☐ Sé en qué unidades se usa PyTorch (UD3, UD5) y por qué NumPy es su base
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
2. **UD3: Visión Artificial** - Procesar imágenes como matrices NumPy
3. **UD4: Lenguaje Natural** - Aplicar ETL a textos, análisis de sentimientos
4. **Cloud Computing** - Escalar a Spark, PySpark, Databricks
5. **Análisis de Datos Profesional** - Crear pipelines ETL empresariales

---

**Documento de teoría fundamental y conexión con unidades siguientes**

*Última actualización: Noviembre 2026*
*Sección 0: conceptos fundamentales de IA de la UD1 · Secciones 10-14: Puentes hacia UD3, UD4, UD5, ecosistema de librerías, creación de aplicaciones y ampliación con materiales complementarios*
*Para cuestiones específicas, consulta las referencias externas proporcionadas*
