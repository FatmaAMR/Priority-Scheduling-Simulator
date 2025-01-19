def get_blue_gradient(index, total_processes):
    blue_value = int(255 - (index * (255 // total_processes)))
    return f"#{blue_value:02x}{blue_value:02x}ff"
