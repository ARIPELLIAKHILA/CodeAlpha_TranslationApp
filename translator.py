import requests


def translate_text(text, source_language, target_language):
    try:
        if not text.strip():
            return ""

        if source_language == target_language:
            return text

        url = "https://api.mymemory.translated.net/get"

        params = {
            "q": text,
            "langpair": f"{source_language}|{target_language}"
        }

        response = requests.get(url, params=params, timeout=10)

        if response.status_code != 200:
            return f"Translation error: HTTP {response.status_code}"

        data = response.json()

        translated_text = data.get("responseData", {}).get("translatedText")

        if not translated_text:
            return "Translation error: No translation was returned."

        return translated_text

    except Exception as e:
        return f"Translation error: {e}"
