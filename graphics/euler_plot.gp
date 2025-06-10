set terminal pdfcairo size 10in,7.5in font "Arial,12"
set output 'height_euler.pdf'

set title "Altura usando Método de Euler"
set xlabel "Tiempo (t)"
set ylabel "Valor de Euler"
set grid
set xrange [0:100]
set xtics 2
set ytics 1

plot "height_euler_results.txt" using 1:2 with points pt 7 ps 0.1 title "Height for Euler"