from googletrans import Translator

translator = Translator()


def translate(si_text: str) -> str:
    return translator.translate(si_text, dest='English')
