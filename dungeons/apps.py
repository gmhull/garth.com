from django.apps import AppConfig
import pathlib

class DungeonsConfig(AppConfig):
    name = 'dungeons'
    default = True


class FacialRecognitionModel(AppConfig):
    """App designed to look at user and assess whether they match a preset image."""

    name = 'facial_recognizer'
    MODEL_PATH = pathlib.Path("model")
    default = False
