from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from deep_translator import GoogleTranslator


class LanguageTranslatorGUI:
    def __init__(self):

        # Language display names mapped to translator codes
        self.languages = {
            "Afrikaans": "af",
            "Albanian": "sq",
            "Arabic": "ar",
            "Bulgarian": "bg",
            "Catalan": "ca",
            "Chinese (Simplified)": "zh-cn",
            "Croatian": "hr",
            "Czech": "cs",
            "Danish": "da",
            "Dutch": "nl",
            "English": "en",
            "Estonian": "et",
            "Finnish": "fi",
            "French": "fr",
            "German": "de",
            "Greek": "el",
            "Hindi": "hi",
            "Hungarian": "hu",
            "Indonesian": "id",
            "Italian": "it",
            "Japanese": "ja",
            "Korean": "ko",
            "Latvian": "lv",
            "Lithuanian": "lt",
            "Norwegian": "no",
            "Polish": "pl",
            "Portuguese": "pt",
            "Romanian": "ro",
            "Russian": "ru",
            "Slovak": "sk",
            "Slovenian": "sl",
            "Somali": "so",
            "Spanish": "es",
            "Swahili": "sw",
            "Swedish": "sv",
            "Tagalog": "tl",
            "Thai": "th",
            "Turkish": "tr",
            "Urdu": "ur",
            "Vietnamese": "vi",
            "Welsh": "cy",
            "Farsi (Persian)": "fa",
            "Dari": "fa",
            "Pashto": "ps"
        }

        # ---------- Main window ----------
        self.root = Tk()
        self.root.title("Language Translator")
        self.root.geometry("650x420")
        self.root.resizable(False, False)

        # ---------- Frames ----------
        top_frame = Frame(self.root)
        input_frame = Frame(self.root)
        output_frame = Frame(self.root)
        button_frame = Frame(self.root)

        # ---------- Language selection ----------
        Label(top_frame, text="From:").grid(row=0, column=0, padx=5, pady=5)
        self.from_lang = Combobox(
            top_frame,
            values=sorted(self.languages.keys()),
            state="readonly",
            width=22
        )
        self.from_lang.set("English")
        self.from_lang.grid(row=0, column=1, padx=5)

        Label(top_frame, text="To:").grid(row=0, column=2, padx=5)
        self.to_lang = Combobox(
            top_frame,
            values=sorted(self.languages.keys()),
            state="readonly",
            width=22
        )
        self.to_lang.set("Spanish")
        self.to_lang.grid(row=0, column=3, padx=5)

        # ---------- Input ----------
        Label(input_frame, text="Text to translate:").pack(anchor="w")
        self.input_text = Text(input_frame, height=5, width=75)
        self.input_text.pack()

        # ---------- Output ----------
        Label(output_frame, text="Translated text:").pack(anchor="w")
        self.output_text = Text(output_frame, height=5, width=75, state="disabled")
        self.output_text.pack()

        # ---------- Buttons ----------
        Button(button_frame, text="Translate", width=12, command=self.translate).pack(
            side="left", padx=5
        )
        Button(button_frame, text="Clear", width=12, command=self.clear).pack(
            side="left", padx=5
        )
        Button(button_frame, text="Quit", width=12, command=self.root.destroy).pack(
            side="left", padx=5
        )

        # ---------- Keyboard shortcuts ----------
        self.root.bind("<Return>", lambda e: self.translate())
        self.root.bind("<Escape>", lambda e: self.root.destroy())

        # ---------- Pack frames ----------
        top_frame.pack(pady=10)
        input_frame.pack(pady=5)
        output_frame.pack(pady=5)
        button_frame.pack(pady=10)

        self.root.mainloop()

    def translate(self):
        text = self.input_text.get("1.0", END).strip()
        if not text:
            messagebox.showwarning("Input Error", "Please enter text to translate.")
            return

        src_code = self.languages[self.from_lang.get()]
        tgt_code = self.languages[self.to_lang.get()]

        try:
            result = GoogleTranslator(
                source=src_code,
                target=tgt_code
            ).translate(text)

            self.output_text.config(state="normal")
            self.output_text.delete("1.0", END)
            self.output_text.insert(END, result)
            self.output_text.config(state="disabled")

        except Exception as e:
            messagebox.showerror("Translation Error", str(e))

    def clear(self):
        self.input_text.delete("1.0", END)
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", END)
        self.output_text.config(state="disabled")


if __name__ == "__main__":
    LanguageTranslatorGUI()

if __name__ == "__main__":
    LanguageTranslatorGUI()

