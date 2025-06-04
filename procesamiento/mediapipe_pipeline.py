import cv2
import mediapipe as mp
from app import config
from utils.logger import log_info

# Inicialización de MediaPipe Face Mesh para obtener landmarks faciales
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=config.MEDIA_PIPE_MIN_DETECTION_CONFIDENCE,
    min_tracking_confidence=config.MEDIA_PIPE_MIN_TRACKING_CONFIDENCE)

def procesar_frame_mediapipe(frame):
    """
    Procesa un frame (imagen) utilizando MediaPipe para detectar landmarks faciales.
    Retorna un diccionario con el frame procesado y los landmarks detectados.
    """
    # Convertir la imagen a RGB
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Procesar la imagen para obtener landmarks faciales
    results = face_mesh.process(image_rgb)

    # Dibujar landmarks en el frame para depuración si se detectan
    if results.multi_face_landmarks:
        log_info(f"Se detectaron {len(results.multi_face_landmarks)} rostro(s)")
        for face_landmarks in results.multi_face_landmarks:
            mp_drawing.draw_landmarks(
                image=frame,
                landmark_list=face_landmarks,
                connections=mp_face_mesh.FACEMESH_TESSELATION,
                landmark_drawing_spec=None,
                connection_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1),
            )

    # Retornar una estructura con los resultados
    return {"frame": frame, "detections": results.multi_face_landmarks}
