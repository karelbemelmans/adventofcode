import re


def probe_hits(start, velocity, area):
    # print ("launch:", start, velocity, area)

    x, y = start
    vx, vy = velocity

    i = 0
    maxy = 0
    while i < 10000:
        i += 1

        # Position changes
        x += vx
        y += vy
        maxy = max(y, maxy)

        # Velocity changes
        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1

        vy -= 1

        if x in area['x'] and y in area['y']:
            # print ("   - HIT!")
            return True, maxy

        # If vx is 0 and we are not in the right area yet, we will never reach out point
        if vx == 0 and not x in area['x']:
            return False, 0

    return False, 0


def parse_input(input, p2=False):
    start = (0, 0)

    matches = re.match(r'^target area: x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)$', input)
    if matches:

        area = {}
        area['x'] = [x for x in range(int(matches.group(1)), int(matches.group(2)) + 1)]
        area['y'] = [y for y in range(int(matches.group(3)), int(matches.group(4)) + 1)]

        R = 200
        p1 = 0
        v = None
        hits = 0
        for i in range(-R, R):
            for j in range(-R, R):
                hit, maxy = probe_hits(start, (i, j), area)
                if hit:
                    hits += 1
                    if maxy > p1:
                        p1 = maxy
                        v = (i, j)

        if p2:
            return hits
        else:
            return (v, p1)


# Part 1
# assert parse_input('target area: x=20..30, y=-10..-5') == ((6, 9), 45)
# print("Part 1: ", parse_input('target area: x=102..157, y=-146..-90'))

# Part 2
# assert parse_input('target area: x=20..30, y=-10..-5', True) == 112
print("Part 2: ", parse_input('target area: x=102..157, y=-146..-90', True))



