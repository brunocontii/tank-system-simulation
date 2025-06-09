set terminal pngcairo size 800,600 font "Arial,14"
set output 'height_adams.png'

set title "Altura usando Método de Adams"
set xlabel "Tiempo (t)"
set ylabel "Valor de Adams"
set grid
set xrange [0:100]

plot "height_adams_results.txt" using 1:2 with lines title "Height for Adams"