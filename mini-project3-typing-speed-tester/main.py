import random
import time
import tkinter as tk
from difflib import SequenceMatcher
from tkinter import ttk

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "A journey of a thousand miles begins with a single step.",
    "To be or not to be, that is the question.",
    "All that glitters is not gold.",
    "I think, therefore I am.",
    "The only way to do great work is to love what you do.",
    "Whether you think you can or you think you can't, you're right.",
    "If you want to live a happy life, tie it to a goal, not to people or things.",
]


def measure_accuracy(user_input: str, original_sentence: str) -> float:
    original = original_sentence.lower().split()
    typed = user_input.lower().split()

    matcher = SequenceMatcher(None, original, typed)
    correct = 0

    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            correct += (i2 - i1)

    accuracy = (correct / len(original)) * 100 if original else 0
    return round(accuracy, 2)


class TypingSpeedTester(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Typing Speed Tester")
        self.geometry("760x520")
        self.resizable(False, False)
        self.configure(bg="#f4f7fb")

        self.current_sentence = ""
        self.start_time = 0.0

        self.style = ttk.Style(self)
        self.style.theme_use("clam")
        self.style.configure("TLabel", background="#f4f7fb", font=("Segoe UI", 11))
        self.style.configure("Header.TLabel", font=("Segoe UI Semibold", 18, "bold"))
        self.style.configure("Section.TLabel", font=("Segoe UI Semibold", 14, "bold"), background="#ffffff")
        self.style.configure("TButton", font=("Segoe UI", 11), padding=10)
        self.style.configure("Result.TLabel", font=("Segoe UI", 12, "bold"))
        self.style.configure("Card.TFrame", background="#ffffff", relief="flat")
        self.style.configure("TLabelframe", background="#ffffff")
        self.style.configure("TLabelframe.Label", font=("Segoe UI Semibold", 14, "bold"), background="#ffffff")

        self.create_widgets()

    def create_widgets(self):
        header_frame = ttk.Frame(self, style="Card.TFrame", padding=(20, 18, 20, 12))
        header_frame.pack(fill="x", padx=20, pady=(20, 10))

        title_label = ttk.Label(header_frame, text="Typing Speed Tester", style="Header.TLabel")
        subtitle_label = ttk.Label(
            header_frame,
            text="Improve your typing performance with a responsive test interface.",
            wraplength=700,
        )
        title_label.pack(anchor="w")
        subtitle_label.pack(anchor="w", pady=(6, 0))

        sentence_frame = ttk.Frame(self, style="Card.TFrame", padding=20)
        sentence_frame.pack(fill="both", expand=True, padx=20, pady=10)

        sentence_title = ttk.Label(sentence_frame, text="Type this sentence:", font=("Segoe UI", 11, "bold"))
        sentence_title.pack(anchor="w")

        self.sentence_label = ttk.Label(
            sentence_frame,
            text="Click Start to load a sentence.",
            wraplength=700,
            font=("Segoe UI", 13),
            background="#ffffff",
        )
        self.sentence_label.pack(fill="x", pady=(8, 20))

        self.input_text = tk.Text(sentence_frame, wrap="word", height=7, font=("Segoe UI", 12), state="disabled", bd=2, relief="solid")
        self.input_text.pack(fill="both", expand=True)
        self.input_text.bind("<KeyPress>", self.on_keypress)

        controls_frame = ttk.Frame(self, style="Card.TFrame")
        controls_frame.pack(fill="x", padx=20, pady=(0, 10))

        self.start_button = ttk.Button(controls_frame, text="Start Test", command=self.start_test)
        self.start_button.pack(side="left", padx=(0, 10))

        self.submit_button = ttk.Button(controls_frame, text="Submit", command=self.submit_test, state="disabled")
        self.submit_button.pack(side="left", padx=(0, 10))

        self.reset_button = ttk.Button(controls_frame, text="Reset", command=self.reset_test, state="disabled")
        self.reset_button.pack(side="left")

        result_frame = ttk.Frame(self, style="Card.TFrame", padding=20)
        result_frame.pack(fill="x", padx=20, pady=(0, 20))

        result_card = ttk.Labelframe(result_frame, text="Test Results", padding=18)
        result_card.pack(fill="x", pady=(0, 0))

        self.status_label = ttk.Label(result_card, text="Waiting for results...", font=("Segoe UI", 11, "bold"), background="#eef3fb", foreground="#223a6c")
        self.time_label = ttk.Label(result_card, text="Time taken: Awaiting results", style="Result.TLabel")
        self.wpm_label = ttk.Label(result_card, text="Words per minute: Awaiting results", style="Result.TLabel")
        self.accuracy_label = ttk.Label(result_card, text="Accuracy: Awaiting results", style="Result.TLabel")
        self.performance_label = ttk.Label(result_card, text="Performance: N/A", font=("Segoe UI", 11), background="#eef3fb")
        self.summary_label = ttk.Label(result_card, text="Click Start then type the sentence to see your result here.", font=("Segoe UI", 10), background="#eef3fb", foreground="#444444", wraplength=700, justify="left")

        self.status_label.pack(anchor="w", pady=(0, 10), padx=10)
        self.time_label.pack(anchor="w", pady=(0, 6), padx=10)
        self.wpm_label.pack(anchor="w", pady=(0, 6), padx=10)
        self.accuracy_label.pack(anchor="w", pady=(0, 6), padx=10)
        self.performance_label.pack(anchor="w", pady=(0, 10), padx=10)
        self.summary_label.pack(anchor="w", pady=(0, 4), padx=10)

        footer_label = ttk.Label(
            self,
            text="Tip: Type the full sentence and press Submit when finished.",
            font=("Segoe UI", 9),
            foreground="#555555",
        )
        footer_label.pack(side="bottom", pady=(0, 12))

    def on_keypress(self, event):
        if self.start_time == 0.0:
            self.start_time = time.time()

    def start_test(self):
        self.current_sentence = random.choice(sentences)
        self.sentence_label.config(text=self.current_sentence)

        self.input_text.config(state="normal")
        self.input_text.delete("1.0", "end")
        self.input_text.focus_set()

        self.start_time = time.time()
        self.submit_button.config(state="normal")
        self.reset_button.config(state="normal")
        self.start_button.config(state="disabled")

        self.time_label.config(text="Time taken: —")
        self.wpm_label.config(text="Words per minute: —")
        self.accuracy_label.config(text="Accuracy: —")
        self.performance_label.config(text="Performance: N/A")
        self.status_label.config(text="Test in progress...")
        self.summary_label.config(text="Test started. Type the sentence and press Submit to see your score.")

    def submit_test(self):
        typed_text = self.input_text.get("1.0", "end").strip()
        if not typed_text:
            self.show_error("Please type the sentence before submitting.")
            return

        if self.start_time == 0.0:
            self.start_time = time.time()

        elapsed_time = time.time() - self.start_time
        elapsed_time = max(elapsed_time, 0.01)

        words_per_minute = len(typed_text.split()) / (elapsed_time / 60)
        accuracy = measure_accuracy(typed_text, self.current_sentence)

        self.time_label.config(text=f"Time taken: {elapsed_time:.2f} seconds")
        self.wpm_label.config(text=f"Words per minute: {words_per_minute:.2f}")
        self.accuracy_label.config(text=f"Accuracy: {accuracy:.2f}%")
        self.performance_label.config(text=self.get_performance_text(words_per_minute, accuracy))
        self.status_label.config(text="Results ready")
        self.summary_label.config(text=f"You typed {len(typed_text.split())} words. Accuracy and speed are shown above.")

        self.input_text.config(state="disabled")
        self.submit_button.config(state="disabled")
        self.start_button.config(state="normal")

    def reset_test(self):
        self.input_text.config(state="normal")
        self.input_text.delete("1.0", "end")
        self.input_text.config(state="disabled")
        self.sentence_label.config(text="Click Start to load a sentence.")
        self.start_time = 0.0
        self.current_sentence = ""
        self.start_button.config(state="normal")
        self.submit_button.config(state="disabled")
        self.reset_button.config(state="disabled")
        self.time_label.config(text="Time taken: —")
        self.wpm_label.config(text="Words per minute: —")
        self.accuracy_label.config(text="Accuracy: —")
        self.performance_label.config(text="Performance: N/A")
        self.status_label.config(text="Waiting for results...")

    def get_performance_text(self, wpm: float, accuracy: float) -> str:
        if accuracy >= 95:
            return "Performance: Excellent"
        if accuracy >= 85:
            return "Performance: Good"
        if accuracy >= 70:
            return "Performance: Fair"
        return "Performance: Needs improvement"

    def show_error(self, message: str) -> None:
        error_window = tk.Toplevel(self)
        error_window.title("Input needed")
        error_window.geometry("360x120")
        error_window.resizable(False, False)
        error_window.configure(bg="#f4f7fb")

        error_label = ttk.Label(error_window, text=message, wraplength=320, font=("Segoe UI", 10))
        error_label.pack(padx=20, pady=20)

        close_button = ttk.Button(error_window, text="OK", command=error_window.destroy)
        close_button.pack(pady=(0, 12))


if (__name__ == "__main__"):
    app = TypingSpeedTester()
    app.mainloop()
