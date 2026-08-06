import queue
import threading
import tkinter as tk
from tkinter import messagebox

import numpy as np
import soundcard as sc

from audio_processing import spectrum_levels


class SpectrumAnalyzerApp:
    def __init__(self, bands: int = 32, chunk_size: int = 2048):
        self.bands = bands
        self.chunk_size = chunk_size
        self.audio_queue: "queue.Queue[np.ndarray]" = queue.Queue(maxsize=3)
        self.stop_event = threading.Event()

        self.root = tk.Tk()
        self.root.title("Z-Visualizer")
        self.root.geometry("960x420")
        self.root.configure(bg="#101218")

        self.canvas = tk.Canvas(self.root, bg="#101218", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.root.bind("<Configure>", lambda _event: self.draw_bars(np.zeros(self.bands)))

        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def get_loopback_microphone(self):
        default_speaker = sc.default_speaker()
        if default_speaker is None:
            raise RuntimeError("No default speaker detected.")

        loopbacks = sc.all_microphones(include_loopback=True)
        for mic in loopbacks:
            if default_speaker.name in mic.name:
                return mic

        if loopbacks:
            return loopbacks[0]
        raise RuntimeError("No loopback-capable recording device found.")

    def capture_audio(self):
        try:
            mic = self.get_loopback_microphone()
            with mic.recorder(samplerate=48000, channels=2) as recorder:
                while not self.stop_event.is_set():
                    chunk = recorder.record(numframes=self.chunk_size)
                    mono = np.mean(chunk, axis=1)
                    levels = spectrum_levels(mono, sample_rate=48000, bands=self.bands)
                    if self.audio_queue.full():
                        try:
                            self.audio_queue.get_nowait()
                        except queue.Empty:
                            pass
                    self.audio_queue.put_nowait(levels)
        except Exception as exc:  # noqa: BLE001
            self.root.after(0, lambda: messagebox.showerror("Audio Error", str(exc)))
            self.root.after(0, self.close)

    def draw_bars(self, levels: np.ndarray):
        width = max(self.canvas.winfo_width(), 1)
        height = max(self.canvas.winfo_height(), 1)

        self.canvas.delete("bar")
        gap = 4
        bar_width = max((width - gap * (self.bands + 1)) / self.bands, 1)

        for i, value in enumerate(levels):
            left = gap + i * (bar_width + gap)
            right = left + bar_width
            bar_height = value * (height - 20)
            top = height - bar_height - 10
            self.canvas.create_rectangle(
                left,
                top,
                right,
                height - 10,
                fill="#39d353",
                outline="",
                tags="bar",
            )

    def update_ui(self):
        try:
            levels = self.audio_queue.get_nowait()
        except queue.Empty:
            levels = np.zeros(self.bands)

        self.draw_bars(levels)
        if not self.stop_event.is_set():
            self.root.after(16, self.update_ui)

    def run(self):
        worker = threading.Thread(target=self.capture_audio, daemon=True)
        worker.start()
        self.update_ui()
        self.root.mainloop()

    def close(self):
        self.stop_event.set()
        self.root.destroy()


if __name__ == "__main__":
    SpectrumAnalyzerApp().run()
