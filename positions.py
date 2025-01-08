import re
import csv

def parse_positions(file_path):
    positions = {}
    with open(file_path, 'r') as file:
        content = file.read()
        matches = re.finditer(r'(\d+)=\{\s*position=\{\s*([\d.]+)\s+([\d.]+)', content)
        for match in matches:
            node_id = int(match.group(1))
            x, y = float(match.group(2)), float(match.group(3))
            positions[node_id] = (x, y)
    return positions

def write_positions_to_csv(positions, output_file):
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        for node_id, (x, y) in positions.items():
            writer.writerow([node_id, x, y])

positions = parse_positions('positions.txt')
write_positions_to_csv(positions, 'positions.csv')