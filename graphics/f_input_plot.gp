set terminal pdfcairo size 10in,7.5in font "Arial,12"
set output 'f_input_plot.pdf'

set title "Funcion de Entrada"
set xlabel "Tiempo (t)"
set ylabel "Valor de Entrada"
set grid
set xrange [0:100]
set xtics 2
set ytics 1

plot "f_input.txt" using 1:2 with points pt 7 ps 0.1 title "Input"