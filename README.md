# Tank System Simulation

Se busca estudiar el comportamiento dinámico de un tanque cilíndrico de base horizontal, el cual recibe un flujo de entrada periódico y posee una válvula de salida cuyo caudal se ajusta automáticamente en función de la altura del líquido en el interior. El propósito es modelar matemáticamente la evolución de la altura dentro del tanque y, a partir de ello, analizar cómo actúa la válvula adicional cuando la altura supera un umbral crítico​.

## Prerrequisitos

* **Python**: Para ejecutar la simulación.
* **Gnuplot**: Para generar las gráficas.
* **Sistema operativo**: Linux. En caso de macOS o Windows buscar las herramientas adecuadas.

## Estructura de directorios

```
├── main.py                          # Archivo principal para ejecutar la simulación
├── functions.py                     # Archivo con las funciones de integracion (por ejemplo, Metodo Euler)
├── constants.py                     # Archivo con las contantes relacionadas al problema
└── graphics/                        # Carpeta con scripts y resultados de Gnuplot
    ├── *.txt                        # Archivos de salida de la simulación (por ejemplo, height_euler_results.txt)
    └── *.gp                         # Scripts Gnuplot para graficos
```

## Uso

1. **Ejecutar la simulación**

   En la raíz del proyecto, ejecutar:

   ```bash
   python main.py
   ```

   Esto generará varios archivos `.txt` con los datos simulados:

   * `height_euler_results.txt`
   * `height_adams_results.txt`
   * `f_input.txt`
   * `f_output.txt`

2. **Generar las gráficas**

   Acceder al directorio `graphics`:

   ```bash
   cd graphics
   ```

   Luego, ejecutar el script Gnuplot deseado. Por ejemplo, para crear la gráfica combinada de entrada, salida y altura:

   ```bash
   gnuplot input_vs_output_vs_height.gp
   ```

   Esto producirá el archivo `input_vs_output_vs_height.pdf`.

   Para generar otras gráficas, simplemente ejecutar el correspondiente `.gp`:

   ```bash
   gnuplot f_output_plot.gp
   gnuplot f_input_plot.gp
   gnuplot euler_vs_adams_plot.gp
   gnuplot euler_plot.gp
   gnuplot adams_plot.gp
   ```

3. **Visualizar las gráficas**

   Una vez generadas, puede abrir las gráficas con su visor de imágenes preferido. Por ejemplo, en macOS/Linux:

   ```bash
   open input_vs_output_vs_height.png
   ```
   O de manera manual.

## Notas

* Cada script Gnuplot (`.gp`) está preparado para leer automáticamente los archivos de datos generados por `main.py`.
* Algunas gráficas muestran una sola función (por ejemplo, solo el caudal de salida), mientras que otras son comparativas.
* Si desea agregar nuevas visualizaciones, basta con crear un nuevo archivo `.gp` en `graphics/` y seguir el mismo patrón.

