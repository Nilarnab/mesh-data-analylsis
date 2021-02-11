def get_hash(n1, n2):
    return str(n1) + "_" + str(n2)


def rev(s):
    s = s.split("_")
    s = s[1] + "_" + s[0]
    return s


# reading the file


# reading points
points = []
file = open("./files/points.txt", "r")
for line in file:
    # print(x)
    line = line.split(" " * 14)
    points.append([float(line[1]), float(line[2]), float(line[3])])
    print(line)

edges = dict()
file = open("./files/triangles.txt", "r")
for line in file:
    # print(x)
    line = line.split(" ")

    new_line = []

    for l in line:
        if l != "":
            new_line.append(l)

    line = new_line

    print(line)

    p1 = int(line[1])
    p2 = int(line[2])
    p3 = int(line[3])

    l1 = get_hash(p1, p2)
    l2 = get_hash(p1, p3)
    l3 = get_hash(p2, p3)

    # print(l1, l2, l3)
    # print(rev(l1), rev(l2), rev(l3))

    if l1 in edges or rev(l1) in edges:
        # already counted
        if l1 in edges:
            edges[l1] += 1
        else:
            edges[rev(l1)] += 1
        pass
    else:
        edges[l1] = 1

    if l2 in edges or rev(l2) in edges:
        if l2 in edges:
            edges[l2] += 1
        else:
            edges[rev(l2)] += 1
        pass
    else:
        edges[l2] = 1

    if l3 in edges or rev(l3) in edges:
        if l3 in edges:
            edges[l3] += 1
        else:
            edges[rev(l3)] += 1
        pass
    else:
        edges[l3] = 1

for el in edges:
    print(el, ":", edges[el])

print("no of lines", len(edges))
edges = list(edges.keys())

while True:
    inp = input()
    if inp != 'exit':
        line = edges[int(inp) - 1]
        line = line.split("_")
        print("points", points[int(line[0]) - 1], points[int(line[1]) - 1])
    else:
        break
