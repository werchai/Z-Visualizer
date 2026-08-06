import numpy as np


def spectrum_levels(samples: np.ndarray, sample_rate: int, bands: int = 32) -> np.ndarray:
    """Convert a mono audio buffer into normalized spectrum bar levels."""
    if bands <= 0:
        raise ValueError("bands must be greater than zero")

    if samples.size == 0:
        return np.zeros(bands, dtype=float)

    window = np.hanning(samples.size)
    fft = np.fft.rfft(samples * window)
    magnitudes = np.abs(fft)

    if magnitudes.size <= 1:
        return np.zeros(bands, dtype=float)

    freqs = np.fft.rfftfreq(samples.size, d=1.0 / sample_rate)
    freqs = np.maximum(freqs, 1.0)

    # Emphasize human-audible changes and avoid low-frequency dominance.
    weighted = np.log1p(magnitudes) * np.sqrt(freqs)

    split = np.geomspace(1, weighted.size, num=bands + 1, dtype=int)
    split = np.clip(split, 1, weighted.size)

    levels = np.zeros(bands, dtype=float)
    for i in range(bands):
        start = split[i] - 1
        end = max(start + 1, split[i + 1])
        levels[i] = float(np.mean(weighted[start:end]))

    peak = float(np.max(levels))
    if peak > 0:
        levels /= peak

    return np.clip(levels, 0.0, 1.0)
