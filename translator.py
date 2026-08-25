from translate import Translator


def translate_text(text, source_language, target_language):
    try:
        if source_language == target_language:
            return text

        translator = Translator(
            from_lang=source_language,
            to_lang=target_language
        )

        result = translator.translate(text)

        if not result:
            return "No translation was returned."

        return result

    except Exception as e:
        return f"Translation error: {e}"