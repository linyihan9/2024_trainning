#  GeoJson  
##  GeoJson Type  
一共有七种，point multiPoint lineString multiLineString polygon multiPolygon geometryCollection  
###  Polygon  
无孔多边形
```
{ "type": "Polygon",
  "coordinates": [
    [
      [100.0, 0.0], [101.0, 0.0], [101.0, 1.0],
      [100.0, 1.0], [100.0, 0.0]
    ]
  ]
}
```  
含孔多边形  
```
{ "type": "Polygon",
  "coordinates": [
    [
      [100.0, 0.0], [101.0, 0.0], [101.0, 1.0],
      [100.0, 1.0], [100.0, 0.0]
    ],
    [
      [100.2, 0.2], [100.8, 0.2], [100.8, 0.8],
      [100.2, 0.8], [100.2, 0.2]
    ]
  ]
}
```
###  GeometryCollection  
```
{ "type": "GeometryCollection",
  "geometries": [
    { "type": "Point",
      "coordinates": [100.0, 0.0]
    },
    { "type": "LineString",
      "coordinates": [ [101.0, 0.0], [102.0, 1.0] ]
    }
  ]
}
```
