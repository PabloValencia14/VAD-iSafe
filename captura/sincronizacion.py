import time

def sincronizar_frames(frame_frontal, frame_lateral):
    """
    Asigna un timestamp común a ambos frames y retorna el timestamp y los frames sincronizados.
    En una implementación real, se podría usar una cola o sistema de buffers.
    """
    timestamp = time.time()
    # Aquí se podría incluir procesamiento adicional para sincronizar frames si hay desfase
    return timestamp, frame_frontal, frame_lateral
