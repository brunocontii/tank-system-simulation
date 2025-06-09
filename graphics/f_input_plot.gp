set terminal pngcairo size 800,600 font "Arial,14"
set output 'f_input_plot.png'

set title "Funcion de Entrada"
set xlabel "Tiempo (t)"
set ylabel "Valor de Entrada"
set grid
set xrange [0:100]
set xtics 5

plot "f_input.txt" using 1:2 with dots title "Input"