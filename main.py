from constants import SIM_TIME, STEP, H_0
from functions import euler, adams_bashforth_3, f_output, f_input, derivative
import os

output_dir = "graphics"
os.makedirs(output_dir, exist_ok=True)

steps = int(SIM_TIME / STEP) + 1
q = H_0

with open(os.path.join(output_dir, "height_euler_results.txt"), "w") as euler_file, \
     open(os.path.join(output_dir, "height_adams_results.txt"), "w") as adams_file, \
     open(os.path.join(output_dir, "f_output.txt"), "w") as f_output_file, \
     open(os.path.join(output_dir, "f_input.txt"), "w") as f_input_file:
    for i in range(steps):
        t = i * STEP
        euler_result = euler(t)
        adams_result = adams_bashforth_3(t)
        f_output_result = f_output(t, q)
        q += STEP * derivative(t, q) # calculando el proximo valor de q para el siguiente output
        f_input_result = f_input(t)
        euler_file.write(f"{t:.2f} {euler_result:.5f}\n")
        adams_file.write(f"{t:.2f} {adams_result:.5f}\n")
        f_output_file.write(f"{t:.2f} {f_output_result:.5f}\n")
        f_input_file.write(f"{t:.2f} {f_input_result:.5f}\n")
        # para ponerlo lindo en forma de tabla
        print(f"t={t:.2f} | Euler: {euler_result:.5f} | Adams-Bashforth 3: {adams_result:.5f} | F_output: {f_output_result:.5f} | F_input: {f_input_result:.5f}")

