set terminal pdfcairo size 10in,7.5in font "Arial,12"
set output 'euler_vs_adams_plot.pdf'

set title "Comparacion Metedo Euler vs Adams"
set xlabel "Tiempo (t)"
set ylabel "Valor"
set grid
set xrange [0:100]
set xtics 2
set ytics 1

set style line 1 lc rgb "blue"       pt 7 ps 0.1
set style line 2 lc rgb "orange"     pt 7 ps 0.1

plot \
    "height_euler_results.txt" using 1:2 with points ls 1 title "Height Euler", \
    "height_adams_results.txt" using 1:2 with points ls 2 title "Height Adams"