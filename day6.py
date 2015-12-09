

def coordinates(instruction_type, instruction):
    if instruction_type == 'off':
        (start_coordinate, end_coordinate) = \
            instruction.replace('turn off ', '').replace('\n', '').\
                split(' through ')
    elif instruction_type == 'on':
        (start_coordinate, end_coordinate) = \
            instruction.replace('turn on ', '').replace('\n', '').\
                split(' through ')
    else:
        (start_coordinate, end_coordinate) = \
            instruction.replace('toggle ', '').replace('\n', '').\
                split(' through ')
    return instruction_type, list(map(int, start_coordinate.split(','))), \
        list(map(int, end_coordinate.split(',')))

light_map = {}
brightness_map = {}

f = open('day6_light_instructions', 'r')
for line in f:
    if line.startswith('turn off'):
        (instruction_type, (start_x, start_y), (end_x, end_y) ) = \
            coordinates('off', line)
    elif line.startswith('turn on'):
        (instruction_type, (start_x, start_y), (end_x, end_y) ) = \
            coordinates('on', line)
    else:
        (instruction_type, (start_x, start_y), (end_x, end_y) ) = \
            coordinates('toggle', line)

    for x in range(start_x, (end_x+1)):
        for y in range(start_y, (end_y+1)):
            if instruction_type == 'off':
                light_map[(x, y)] = 'off'
                if (x, y) in brightness_map:
                    if brightness_map[(x, y)] > 0:
                        brightness_map[(x, y)] -= 1
                else:
                    brightness_map[(x, y)] = 0
            elif instruction_type == 'on':
                light_map[(x, y)] = 'on'
                if (x, y) in brightness_map:
                    brightness_map[(x, y)] += 1
                else:
                    brightness_map[(x, y)] = 1
            else:
                if (x, y) in light_map:
                    if light_map[(x, y)] == 'on':
                        light_map[(x, y)] = 'off'
                    else:
                        light_map[(x, y)] = 'on'
                else:
                    light_map[(x, y)] = 'on'
                if (x, y) in brightness_map:
                    brightness_map[(x, y)] += 2
                else:
                    brightness_map[(x, y)] = 2

light_count = 0
total_brightness = 0
for light in light_map:
    if light_map[light] == 'on':
        light_count += 1
    if brightness_map[light] >=0:
        total_brightness += brightness_map[light]

print('Lights that are on: ' + str(light_count))
print('Total brightnesss: ' + str(total_brightness))
