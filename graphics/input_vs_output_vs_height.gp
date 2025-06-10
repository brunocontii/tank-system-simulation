# Configuracion general
set terminal pdfcairo size 10in,7.5in font "Arial,12"
set output 'input_vs_output_vs_height.pdf'

set title "Funciones de Entrada, Salida y Altura del tanque"
set xlabel "Tiempo (t)"
set ylabel "Valor"
set grid
set xrange [0:100]
set xtics 2
set ytics 1

# Opciones de estilo (colores, tipos de punto)
set style line 1 lc rgb "blue"    pt 7 ps 0.1
set style line 2 lc rgb "red"     pt 7 ps 0.1
set style line 3 lc rgb "green"   pt 7 ps 0.1

# Dibujo de funciones en un solo plot
plot \
    "f_input.txt"  using 1:2 with points ls 1 title "Input", \
    "f_output.txt" using 1:2 with points ls 2 title "Output", \
    "height_euler_results.txt" using 1:2 with points ls 3 title "Height Euler"
