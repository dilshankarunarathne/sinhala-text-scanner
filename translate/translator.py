from googletrans import Translator

translator = Translator()


def translate_text(si_text: str) -> str:
    text = translator.translate(si_text, dest='English')
    return text.text
