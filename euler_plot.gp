set terminal pngcairo size 800,600 font "Arial,14"
set output 'euler_plot.png'

set title "Método de Euler - Simulación"
set xlabel "Tiempo (t)"
set ylabel "Valor de Euler"
set grid
set xrange [0:100]

plot "euler_results.txt" using 1:2 with lines title "Euler"