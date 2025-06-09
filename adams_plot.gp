set terminal pngcairo size 800,600 font "Arial,14"
set output 'adams_plot.png'

set title "Método de Adams - Simulación"
set xlabel "Tiempo (t)"
set ylabel "Valor de Adams"
set grid
set xrange [0:100]

plot "adams_results.txt" using 1:2 with lines title "Adams"