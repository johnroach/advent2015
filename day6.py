'''
--- Day 6: Probably a Fire Hazard ---

Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

For example:

turn on 0,0 through 999,999 would turn on (or leave on) every light.
toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
After following the instructions, how many lights are lit?

Your puzzle answer was 400410.

--- Part Two ---

You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of those lights by 1.

The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of those lights by 2.

What is the total brightness of all lights combined after following Santa's instructions?

For example:

turn on 0,0 through 0,0 would increase the total brightness by 1.
toggle 0,0 through 999,999 would increase the total brightness by 2000000.
Your puzzle answer was 15343601.
'''

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

def implement_instructions(x, y):
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

    [implement_instructions(x, y) for x in range(start_x, (end_x+1)) \
        for y in range(start_y, (end_y+1))]


light_count = 0
total_brightness = 0
for light in light_map:
    if light_map[light] == 'on':
        light_count += 1
    if brightness_map[light] >=0:
        total_brightness += brightness_map[light]

print('Lights that are on: ' + str(light_count))
print('Total brightnesss: ' + str(total_brightness))
