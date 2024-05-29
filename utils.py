def convert_kb(nkb: int) -> str:
    """Converts a number of kilobytes to the highest magnitude available (e.g. MB, GB)."""
    magnitudes = ["K", "M", "G", "T", "P", "E", "Z", "Y"]
    
    nb = float(nkb)

    mag = 0
    while nkb >= 1000 and mag < len(magnitudes) - 1:
        nkb /= 1000.0
        mag += 1
    
    return f"{nkb:.2f} {magnitudes[mag]}B"
