import bpy
obdata = bpy.context.object.data


print("vertics")
for v in obdata.vertices:
    print(" ({}, {}, {}),".format(v.co.x, v.co.y, v.co.z))
    
print("edges")
for e in obdata.edges:
    print("({}, {}),".format(e.vertices[0], e.vertices[1]))
    
print("faces")
for f in obdata.polygons:
    for v in f.vertices:
        print("{}, ".format(v), end='')
    print()