import psutil
import time
import os

def limpiar_pantalla():
    # Limpia la consola para que el texto no se acumule hacia abajo
    os.system('cls' if os.name == 'nt' else 'clear')

def generar_barra(porcentaje, longitud=20):
    # Crea una barra visual tipo [████░░░░░░]
    bloques_llenos = int(porcentaje / (100 / longitud))
    bloques_vacios = longitud - bloques_llenos
    return "█" * bloques_llenos + "░" * bloques_vacios

# Limpieza inicial
limpiar_pantalla()
print("📊 Iniciando Monitor de CPU (Presiona Ctrl+C para salir)...\n")

# Primera medición para calibrar psutil
psutil.cpu_percent(interval=None)

try:
    while True:
        # 1. Obtener métricas reales
        cpu_total = psutil.cpu_percent(interval=1)
        num_cores = psutil.cpu_count(logical=True)
        
        # 2. Generar la barra visual
        barra_visual = generar_barra(cpu_total)
        
        # 3. Limpiar y mostrar de forma atractiva
        limpiar_pantalla()
        print("=" * 50)
        print("💻 MONITOR DE RENDIMIENTO DEL SISTEMA")
        print("=" * 50)
        print(f" Núcleos Detectados : {num_cores} vCPUs")
        print(f" Uso Total de la CPU: [{barra_visual}] {cpu_total}%")
        print("=" * 50)
        print(" Actualizando cada 1 segundo...")
        
except KeyboardInterrupt:
    print("\n\n👋 Monitor detenido. ¡Hasta luego!")
