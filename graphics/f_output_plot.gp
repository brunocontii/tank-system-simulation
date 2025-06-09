set terminal pngcairo size 800,600 font "Arial,14"
set output 'f_output_plot.png'

set title "Funcion de Salida"
set xlabel "Tiempo (t)"
set ylabel "Valor de Salida"
set grid
set xrange [0:100]
set xtics 5

plot "f_output.txt" using 1:2 with dots title "Output"