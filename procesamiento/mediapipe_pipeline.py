import cv2
import mediapipe as mp
from app import config
from utils.logger import log_info

# Inicialización de MediaPipe Face Detection (como ejemplo)
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

face_detection = mp_face_detection.FaceDetection(model_selection=config.MEDIA_PIPE_MODEL_SELECTION,
                                                 min_detection_confidence=config.MEDIA_PIPE_MIN_DETECTION_CONFIDENCE)

def procesar_frame_mediapipe(frame):
    """
    Procesa un frame (imagen) utilizando MediaPipe para detectar landmarks faciales.
    Retorna un diccionario con los resultados y/o los landmarks detectados.
    """
    # Convertir la imagen a RGB
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Procesar la imagen
    results = face_detection.process(image_rgb)
    
    # Si es necesario, dibujar detecciones en el frame (para debugging)
    if results.detections:
        for detection in results.detections:
            mp_drawing.draw_detection(frame, detection)
    
    # Retornar una estructura con los resultados
    return {"frame": frame, "detections": results.detections}
