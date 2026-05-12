def normalize_plate(plate):
    return ''.join(filter(str.isalnum, plate)).upper().strip()