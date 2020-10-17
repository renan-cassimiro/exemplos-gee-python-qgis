from ee_plugin import Map

l8 = ee.ImageCollection("LANDSAT/LC08/C01/T1_TOA").filterDate('2014-03-30','2015-03-31');

imgMediana = l8.median(); 

ndvi = imgMediana.expression(
                        '(a-b)/(a+b)',
                        {
                          'a': imgMediana.select('B5'), 
                          'b': imgMediana.select('B4')
                        });

Map.addLayer(ndvi);