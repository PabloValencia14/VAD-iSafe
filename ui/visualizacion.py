import cv2
from app import config
from utils.logger import log_info

def mostrar_resultados(frame_frontal, frame_lateral, datos_fusionados, score, observaciones):
    """
    Función para visualizar los resultados:
      - Mostrar los frames de las cámaras.
      - Superponer información relevante (score, observaciones, landmarks, etc.).
    """
    # Copiar frames para no modificar el original (si se desea)
    frame_frontal_disp = frame_frontal.copy()
    frame_lateral_disp = frame_lateral.copy()
    
    # Superponer el score y observaciones en el frame frontal
    texto = f"Score: {score:.2f} - {observaciones}"
    cv2.putText(frame_frontal_disp, texto, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                0.8, (0, 255, 0), 2, cv2.LINE_AA)
    
    # Mostrar ventanas (puedes adaptar esta parte si trabajas con UI nativa)
    cv2.imshow(config.VENTANA_FRONTAL, frame_frontal_disp)
    cv2.imshow(config.VENTANA_LATERAL, frame_lateral_disp)
    
    log_info(f"Mostrando resultados - Score: {score:.2f}")
