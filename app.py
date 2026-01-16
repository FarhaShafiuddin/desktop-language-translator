from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from deep_translator import GoogleTranslator


class LanguageTranslatorGUI:
    def __init__(self):

        # Language name → code mapping
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

    # Languages you explicitly had that are often missed
    "Farsi (Persian)": "fa",
    "Dari": "fa",
    "Pashto": "ps"
          
        }

        # Main window
        self.main_window = Tk()
        self.main_window.title("Language Translator")
        self.main_window.geometry("600x350")

        # Frames
        self.first_frame = Frame(self.main_window)
        self.second_frame = Frame(self.main_window)
        self.third_frame = Frame(self.main_window)
        self.fourth_frame = Frame(self.main_window)
        self.fifth_frame = Frame(self.main_window)

        # From language
        Label(self.first_frame, text="Translate from:").pack(side="left")
        self.from_lang = Combobox(
            self.first_frame,
            values=list(self.languages.keys()),
            state="readonly",
            width=20
        )
        self.from_lang.set("English")
        self.from_lang.pack(side="left", padx=5)

        # To language
        Label(self.second_frame, text="Translate to:").pack(side="left")
        self.to_lang = Combobox(
            self.second_frame,
            values=list(self.languages.keys()),
            state="readonly",
            width=20
        )
        self.to_lang.set("Spanish")
        self.to_lang.pack(side="left", padx=5)

        # Input text
        Label(self.third_frame, text="Text to translate:").pack(anchor="w")
        self.text_input = Text(self.third_frame, height=4, width=60)
        self.text_input.pack()

        # Output text
        Label(self.fourth_frame, text="Translated text:").pack(anchor="w")
        self.text_output = Text(self.fourth_frame, height=4, width=60, state="disabled")
        self.text_output.pack()

        # Buttons
        Button(self.fifth_frame, text="Translate", command=self.translate).pack(side="left", padx=5)
        Button(self.fifth_frame, text="Clear", command=self.clear).pack(side="left", padx=5)
        Button(self.fifth_frame, text="Quit", command=self.main_window.destroy).pack(side="left", padx=5)

        # Keyboard shortcuts
        self.main_window.bind("<Return>", lambda e: self.translate())
        self.main_window.bind("<Escape>", lambda e: self.main_window.destroy())

        # Pack frames
        for frame in (
            self.first_frame,
            self.second_frame,
            self.third_frame,
            self.fourth_frame,
            self.fifth_frame,
        ):
            frame.pack(pady=5)

        self.main_window.mainloop()

    def translate(self):
        text = self.text_input.get("1.0", END).strip()
        if not text:
            messagebox.showwarning("Input Error", "Please enter text to translate.")
            return

        src_code = self.languages[self.from_lang.get()]
        tgt_code = self.languages[self.to_lang.get()]

        try:
            translated = GoogleTranslator(
                source=src_code,
                target=tgt_code
            ).translate(text)

            self.text_output.config(state="normal")
            self.text_output.delete("1.0", END)
            self.text_output.insert(END, translated)
            self.text_output.config(state="disabled")

        except Exception as e:
            messagebox.showerror("Translation Error", str(e))

    def clear(self):
        self.text_input.delete("1.0", END)
        self.text_output.config(state="normal")
        self.text_output.delete("1.0", END)
        self.text_output.config(state="disabled")


if __name__ == "__main__":
    LanguageTranslatorGUI()

