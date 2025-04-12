import cv2
import time
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Importar módulos del proyecto
from app import config
from captura.captura_video import iniciar_camaras
from captura.sincronizacion import sincronizar_frames
from procesamiento.mediapipe_pipeline import procesar_frame_mediapipe
from fusion.fusion_datos import fusionar_datos
from fusion.analisis import analizar_datos
from ui.visualizacion import mostrar_resultados
from utils.logger import log_info

def main():
    # Inicializar cámaras
    cam_frontal, cam_lateral = iniciar_camaras(config.CAMARA_FRONTAL, config.CAMARA_LATERAL)
    log_info("Cámaras inicializadas correctamente.")

    try:
        while True:
            # Captura de frames
            ret_frontal, frame_frontal = cam_frontal.read()
            ret_lateral, frame_lateral = cam_lateral.read()
            
            if not ret_frontal or not ret_lateral:
                log_info("Error al capturar frames, terminando el ciclo.")
                break
            
            # Sincronización de frames (agregamos un timestamp común)
            timestamp, frame_frontal_sync, frame_lateral_sync = sincronizar_frames(frame_frontal, frame_lateral)
            
            # Procesamiento con MediaPipe en cada frame
            resultado_frontal = procesar_frame_mediapipe(frame_frontal_sync)
            resultado_lateral = procesar_frame_mediapipe(frame_lateral_sync)
            
            # Fusionar los datos de ambas vistas (p.ej., reconstrucción 3D o fusión de landmarks)
            datos_fusionados = fusionar_datos(resultado_frontal, resultado_lateral, timestamp)
            
            # Análisis de la fusión para determinar dificultad de la vía aérea
            score, observaciones = analizar_datos(datos_fusionados)
            
            # Mostrar resultados y feedback en la UI
            mostrar_resultados(frame_frontal_sync, frame_lateral_sync, datos_fusionados, score, observaciones)
            
            # Condición de salida (tecla ESC)
            if cv2.waitKey(1) & 0xFF == 27:  # tecla ESC
                break

    finally:
        cam_frontal.release()
        cam_lateral.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
