"""
AUTO-CLICKER POR IMAGEN (Windows)
----------------------------------
Este script busca en tu pantalla una imagen de referencia (una captura
del botón que querés que se clickee) y, apenas la encuentra, hace
click automáticamente ahí.

REQUISITOS (correr en una terminal, una sola vez):
    pip install pyautogui opencv-python pillow numpy

CÓMO PREPARAR LA IMAGEN DE REFERENCIA:
1. Sacá una captura de pantalla (Win + Shift + S) SOLO del botón,
   recortado bien ajustado (sin fondo de más).
2. Guardala como "boton.png" en la misma carpeta que este script.

CÓMO USAR:
1. Ajustá las variables de configuración más abajo si querés.
2. Ejecutá: python auto_clicker.py
3. Para detenerlo en cualquier momento: movés el mouse a la esquina
   superior izquierda de la pantalla (0,0) o presionás Ctrl+C en la
   terminal.

NOTA: pyautogui tiene un "modo de seguridad" (failsafe) activado por
defecto: si el mouse llega a la esquina (0,0) el script se corta solo.
Es intencional, para que siempre puedas frenarlo.
"""

import time
import sys
import pyautogui

# ---------------- CONFIGURACIÓN ----------------
IMAGEN_BOTON = "boton.png"   # nombre del archivo de imagen del botón
CONFIANZA = 0.85              # qué tan parecido debe ser el match (0 a 1)
INTERVALO_BUSQUEDA = 0.01       # segundos entre cada búsqueda en pantalla
COOLDOWN_DESPUES_DE_CLICK = 0.5  # segundos de espera después de clickear
                                # (para no clickear 10 veces seguidas)
# -------------------------------------------------

pyautogui.FAILSAFE = True  # mover el mouse a (0,0) detiene el script

def main():
    print("Auto-clicker iniciado. Buscando:", IMAGEN_BOTON)
    print("Para detener: mové el mouse a la esquina superior izquierda o Ctrl+C\n")

    while True:
        try:
            ubicacion = pyautogui.locateOnScreen(
                IMAGEN_BOTON, confidence=CONFIANZA
            )
            if ubicacion is not None:
                centro = pyautogui.center(ubicacion)
                pyautogui.click(centro)
                print(f"Click hecho en {centro}")
                time.sleep(COOLDOWN_DESPUES_DE_CLICK)
            else:
                time.sleep(INTERVALO_BUSQUEDA)

        except pyautogui.FailSafeException:
            print("\nDetenido por el usuario (failsafe).")
            sys.exit(0)
        except KeyboardInterrupt:
            print("\nDetenido por el usuario (Ctrl+C).")
            sys.exit(0)
        except Exception as e:
            # Si no encuentra la imagen a veces tira excepción según versión
            time.sleep(INTERVALO_BUSQUEDA)


if __name__ == "__main__":
    main()
