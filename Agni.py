import shapefile
aa = shapefile.Reader("E:/Agni/Agni.shp")
shapes = aa.shapes()
print len(shapes)