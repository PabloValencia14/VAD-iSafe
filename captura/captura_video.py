import cv2
from utils.logger import log_info

def iniciar_camaras(indice_frontal: int, indice_lateral: int):
    """
    Inicializa y devuelve los objetos de captura de vídeo para la cámara frontal y lateral.
    """
    cam_frontal = cv2.VideoCapture(indice_frontal)
    cam_lateral = cv2.VideoCapture(indice_lateral)
    
    if not cam_frontal.isOpened():
        log_info("Error al abrir la cámara frontal.")
    if not cam_lateral.isOpened():
        log_info("Error al abrir la cámara lateral.")
    
    return cam_frontal, cam_lateral
