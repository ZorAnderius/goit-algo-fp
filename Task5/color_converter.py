def rgb_to_hex(hex_color: list) -> str:
    return "#{:02x}{:02x}{:02x}".format(hex_color[0], hex_color[1], hex_color[2])

def hex_to_rgb(hex_color: str) -> list:
    hex_color = hex_color.lstrip('#')
    hex_len = len(hex_color)
    rgb = [int(hex_color[i:i+hex_len//3], 16) for i in range(0, hex_len, hex_len//3)]

    return rgb