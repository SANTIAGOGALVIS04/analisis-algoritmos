## Tarea 1 — Algoritmos Greedy

Curso: Análisis de algoritmos
Institución: ITM
Periodo: 2026-2
Tema: Algoritmos greedy (voraces)
Lenguaje: Python 3

## 1. 860. Lemonade Change

Enunciado: 860. Lemonade Change — LeetCode

Código: lemonade-change/solution.py

Criterio greedy

Se recorren los pagos en el orden de llegada y se cuentan los billetes de $5 y $10 disponibles. Cuando un cliente paga con $10, se devuelve un billete de $5. Cuando paga con $20, se prioriza devolver un billete de $10 y uno de $5; si no es posible, se utilizan tres billetes de $5. Esta decisión conserva los billetes de $5 para los siguientes clientes. Si no se puede devolver el cambio exacto, se retorna False; si todos los clientes son atendidos, se retorna True.

Complejidad

Tiempo: O(n), porque se recorre el arreglo una sola vez.

Espacio auxiliar: O(1), porque se utilizan únicamente dos contadores.

Evidencia de aceptación



## 2. 455. Assign Cookies

Enunciado: 455. Assign Cookies — LeetCode

Código: assign-cookies/solution.py

Criterio greedy

Se ordenan los niños según su nivel de gula y las galletas según su tamaño, ambos de menor a mayor. Se intenta satisfacer primero al niño menos exigente con la galleta más pequeña disponible que cumpla su requisito. Si una galleta es demasiado pequeña, se descarta y se prueba la siguiente. De esta manera, se reservan las galletas grandes para los niños que las necesitan y se maximiza la cantidad de niños satisfechos.

Complejidad

Sean n la cantidad de niños y m la cantidad de galletas.

Tiempo: O(n log n + m log m), debido al ordenamiento de ambos arreglos. El recorrido posterior es O(n + m).

Espacio auxiliar: O(n + m) en el peor caso, considerando el espacio temporal que puede utilizar el ordenamiento de listas de Python. El recorrido utiliza O(1) variables adicionales.

Evidencia de aceptación



Estado de la entrega

Ambos problemas enviados y aceptados en LeetCode.

Capturas de aceptación incluidas en la carpeta evidencias.

Código fuente en Python 3.

Criterios greedy y análisis de complejidad documentados.

Nota: las evidencias deben corresponder a los envíos reales del estudiante en LeetCode.
