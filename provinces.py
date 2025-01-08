import csv
from PIL import Image

def index_colors(path):
    provinces = []

    with open(path, mode='r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        for row in csv_reader:
            provinces.append(row)

    province_colors = []
    for province in provinces[1:]:
        province_color = (int(province[1]), int(province[2]), int(province[3]))
        province_colors.append(province_color)

    return province_colors

def map(file_path, color_list):
    adjacencies = [set() for _ in range(len(color_list))]

    with open('noland.txt', 'r') as file:
        water = [int(line.strip()) for line in file]

    with Image.open(file_path) as img:
        img = img.convert("RGB")
        width, height = img.size

        for y in range(1, height - 1):
            print(f"Processing pixels ({y}/2046)")
            for x in range(1, width - 1):

                pixel = img.getpixel((x, y))
                if color_list.index(pixel) in water:
                    continue

                neighbors = [
                    img.getpixel((x-1, y)),
                    img.getpixel((x+1, y)),
                    img.getpixel((x, y-1)),
                    img.getpixel((x, y+1))
                ]

                for neighbor in neighbors:
                    if neighbor != pixel:
                        neighbor = color_list.index(neighbor)
                        if neighbor in water:
                            continue
                        adjacencies[color_list.index(pixel)].add(neighbor)

    with open('adjacencies.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for adjacency in adjacencies:
            writer.writerow(adjacency)

    return adjacencies

def main():

    color_list = index_colors("definition.csv")
    map("provinces.bmp", color_list)

if __name__ == "__main__":
    main()