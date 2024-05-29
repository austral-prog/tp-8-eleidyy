# Lista de Azara (tesoros y coordenadas)
azara_list = [
    ("Amethyst Octopus", "1F"),
    ("Angry Monkey Figurine", "5B"),
    ("Antique Glass Fishnet Float", "3D"),
    ("Brass Spyglass", "4B"),
    ("Carved Wooden Elephant", "8C"),
    ("Crystal Crab", "6A"),
    ("Glass Starfish", "6D"),
    ("Model Ship in Large Bottle", "8A"),
    ("Pirate Flag", "7F"),
    ("Robot Parrot", "1C"),
    ("Scrimshawed Whale Tooth", "2A"),
    ("Silver Seahorse", "4E"),
    ("Vintage Pirate Hat", "7E")
]

# Lista de Rui (nombres de ubicaciones, coordenadas y cuadrante)
rui_list = [
    ("Seaside Cottages", ("1", "C"), "Blue"),
    ("Aqua Lagoon (Island of Mystery)", ("1", "F"), "Yellow"),
    ("Deserted Docks", ("2", "A"), "Blue"),
    ("Spiky Rocks", ("3", "D"), "Yellow"),
    ("Abandoned Lighthouse", ("4", "B"), "Blue"),
    ("Hidden Spring (Island of Mystery)", ("4", "E"), "Yellow"),
    ("Stormy Breakwater", ("5", "B"), "Purple"),
    ("Old Schooner", ("6", "A"), "Purple"),
    ("Tangled Seaweed Patch", ("6", "D"), "Orange"),
    ("Quiet Inlet (Island of Mystery)", ("7", "E"), "Orange"),
    ("Windswept Hilltop (Island of Mystery)", ("7", "F"), "Orange"),
    ("Harbor Managers Office", ("8", "A"), "Purple"),
    ("Foggy Seacave", ("8", "C"), "Purple")
]

# 1.1. Extraer coordenadas
def get_coordinate(treasure_info):
    return treasure_info[1]

# 1.2. Formatear coordenadas
def convert_coordinate(coord):
    return (coord[0], coord[1])

# 1.3. Combinar registros
def create_record(treasure_info, location_info):
    treasure, azara_coord = treasure_info
    location_name, rui_coord, quadrant = location_info
    azara_coord_converted = convert_coordinate(azara_coord)
    
    if azara_coord_converted == rui_coord:
        return (treasure, azara_coord, location_name, rui_coord, quadrant)
    else:
        return "no coincide"

# Ejemplos de uso de las funciones
print(get_coordinate(('Scrimshawed Whale Tooth', '2A')))  # Debería imprimir: 2A
print(convert_coordinate("2A"))  # Debería imprimir: ('2', 'A')
print(create_record(('Brass Spyglass', '4B'), ('Abandoned Lighthouse', ('4', 'B'), 'Blue')))
# Debería imprimir: ('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue')
print(create_record(('Brass Spyglass', '4B'), ('Seaside Cottages', ('1', 'C'), 'Blue')))
# Debería imprimir: "no coincide"
