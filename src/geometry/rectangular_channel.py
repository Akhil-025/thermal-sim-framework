def generate_rectangular_channel(length, width, height):
    hydraulic_diameter = 2 * width * height / (width + height)

    return {
        "type": "rectangular_channel",
        "length": length,
        "width": width,
        "height": height,
        "hydraulic_diameter": hydraulic_diameter
    }
