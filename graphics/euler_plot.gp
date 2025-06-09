set terminal pngcairo size 800,600 font "Arial,14"
set output 'height_euler.png'

set title "Altura usando Método de Euler"
set xlabel "Tiempo (t)"
set ylabel "Valor de Euler"
set grid
set xrange [0:100]

plot "height_euler_results.txt" using 1:2 with lines title "Height for Euler"