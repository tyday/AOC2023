from helper import FileHelper



def get_map_value(data, i):
    if i in data:
        return data[i]
    else:
        return i

def get_data_values(i, j, data):
    new_data = data[i: j - 2]
    return_data = [a.strip() for a in new_data if a != '']
    return return_data


def get_map(maps):
    ret_map = {}
    for m in maps:
        vals = m.split()
        source = int(vals[1].strip())
        dest = int(vals[0].strip())
        count = int(vals[2].strip())
        for i in range(count):
            ret_map[source + i] = dest + i
    return ret_map




def parse_data(data):
    seeds = data[0].strip().split(":")[1].split()
    seeds = [int(a.strip()) for a in seeds]

    index_seed_to_soil = data.index("seed-to-soil map:") + 1
    index_soil_to_fertilizer = data.index("soil-to-fertilizer map:") + 1
    index_fertilize_to_water = data.index("fertilizer-to-water map:") + 1
    index_water_to_light = data.index("water-to-light map:") + 1
    index_light_to_temperature = data.index("light-to-temperature map:") + 1
    index_temperature_to_humidity = data.index("temperature-to-humidity map:") + 1
    index_humidity_to_location = data.index("humidity-to-location map:") + 1

    seed_to_soil = get_data_values(index_seed_to_soil, index_soil_to_fertilizer,data)
    soil_to_fertilizer = get_data_values(index_soil_to_fertilizer, index_fertilize_to_water, data)
    fertilize_to_water = get_data_values(index_fertilize_to_water, index_water_to_light, data)
    water_to_light = get_data_values(index_water_to_light, index_light_to_temperature,data)
    light_to_temperature = get_data_values(index_light_to_temperature, index_temperature_to_humidity, data)
    temperature_to_humidity = get_data_values(index_temperature_to_humidity, index_humidity_to_location, data)
    humidity_to_location = get_data_values(index_humidity_to_location, len(data) + 2, data)

    maps = {
        'seeds': seeds,
        'seed_to_soil' : get_map(seed_to_soil),
        'soil_to_fertilizer' : get_map(soil_to_fertilizer),
        'fertilize_to_water' : get_map(fertilize_to_water),
        'water_to_light' : get_map(water_to_light),
        'light_to_temperature' : get_map(light_to_temperature),
        'temperature_to_humidity' : get_map(temperature_to_humidity),
        'humidity_to_location' : get_map(humidity_to_location),
    }
    return maps


def get_end_locations(maps, seed):
    location = int(seed)
    location = get_map_value(maps['seed_to_soil'], location)
    location = get_map_value(maps['soil_to_fertilizer'], location)
    location = get_map_value(maps['fertilize_to_water'], location)
    location = get_map_value(maps['water_to_light'], location)
    location = get_map_value(maps['light_to_temperature'], location)
    location = get_map_value(maps['temperature_to_humidity'], location)
    location = get_map_value(maps['humidity_to_location'], location)
    return location

def part_one(data):
    maps = parse_data(data)
    seeds = maps['seeds']

    end_locations = []
    for seed in seeds:
        end_locations.append(get_end_locations(maps, seed))

    print("Part one: " + str(min(end_locations)))

if __name__ == '__main__':

    data = FileHelper.file_helper("data.txt")


    part_one(data)

