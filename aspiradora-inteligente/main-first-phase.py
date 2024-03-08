import sys
import time
import threading

from entities.Quadrant import Quadrant
from entities.VacummCleaner import VacummCleaner
from colorama import init, AnsiToWin32

init()
converter = AnsiToWin32(sys.stdout)


def clear_terminal():
    converter.write("\x1b[2J\x1b[H")


def user_thread():
    while True:
        key = input("")

        if key == "1":
            quadrant1.dirty()
            print("El cuadrante 1 ha sido ensuciado")
        elif key == "2":
            quadrant2.dirty()
            print("El cuadrante 2 ha sido ensuciado")
        elif key == "e":
            vacumm_cleaner.set_mode(0)
            print("La aspiradora ha sido configurada en modo estúpido")
        elif key == "i":
            vacumm_cleaner.set_mode(1)
            print("La aspiradora ha sido configurada en modo inteligente")
        else:
            print("opción inválida")


def vacumm_cleaner_thread():
    while True:
        vacumm_cleaner.clear()
        time.sleep(1)


if __name__ == "__main__":
    # Create Quadrants
    quadrant1 = Quadrant(None, None)
    quadrant2 = Quadrant(quadrant1, None)
    quadrant1.set_right_quadrant(quadrant2)

    # Create vacuum cleaner
    vacumm_cleaner = VacummCleaner(quadrant1)

    print("Insttucciones:")
    print("Inicialmente los dos cuadrantes están limpios")
    print("Para ensuciar el cuadrante 1, presione el número 1")
    print("Para ensuciar el cuadrante 2, presione el número 2\n")
    print("Inicialmente la aspiradora se encuentra en modo inteligente")
    print("Para cambiar la aspiradora a modo inteligente presione la tecla \"i\"")
    print("Para cambiar la aspiradora a modo estúpido presione la tecla\"e\"")
    print("Presione cualquier tecla para iniciar la simulación...")
    input()
    clear_terminal()

    thread_1 = threading.Thread(target=user_thread, name="Usuario")
    thread_2 = threading.Thread(target=vacumm_cleaner_thread, name="Aspiradora")

    thread_1.start()
    thread_2.start()
