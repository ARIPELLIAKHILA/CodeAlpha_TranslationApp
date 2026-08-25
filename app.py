from flask import Flask, render_template, request
from translator import translate_text

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    translated_text = ""
    error = ""

    if request.method == "POST":
        text = request.form.get("text", "").strip()
        source_language = request.form.get("source_language", "en")
        target_language = request.form.get("target_language", "hi")

        if text:
            result = translate_text(
                text,
                source_language,
                target_language
            )

            if result.startswith("Translation error:"):
                error = result
            else:
                translated_text = result

    return render_template(
        "index.html",
        translated_text=translated_text,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)