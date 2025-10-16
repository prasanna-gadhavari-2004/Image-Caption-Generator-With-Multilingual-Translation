def translate_caption(caption, target_language="hi"):
    from googletrans import Translator
    try:
        translator = Translator()
        translated = translator.translate(caption, dest=target_language)
        return translated.text
    except Exception as e:
        print("Translation failed:", e)
        return f"[Translation failed] {caption}"
