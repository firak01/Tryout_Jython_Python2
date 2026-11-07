from java.awt import Color
from java.lang import Comparable, System, ClassCastException
from java.util import Arrays


class ComparableColor(Color, Comparable):
    def __init__(self, color):
        Color.__init__(self, color.getRGB())

    def _RGBTuple(self):
        return (self.getRed(), self.getGreen(), self.getBlue())

    def compareTo(self, color1):
        rgb0 = self._RGBTuple()
        rgb1 = color1._RGBTuple()
        return cmp(rgb0,rgb1)

    def toString(self):
        return "#%02x%02x%02x" % self._RGBTuple()

    def __repr__(self):
        return "<co: %s>" % self.toString()

from jarray import array

colors = [Color.green, Color.magenta, Color.orange ,Color.red]

colorsArray = array(colors, Color)

try:
    Arrays.sort(colorsArray)
except ClassCastException:
    print "java.awt.Color does not implement Comparable" 

colorsArray = array(map(ComparableColor,colors), Color)

print
print "ComparableColor does:"
print "unsorted:",
for color in colorsArray:
    print color,
print

Arrays.sort(colorsArray)

System.out.print("sorted: ")
for color in colorsArray:
    System.out.print(color) # uses java.lang.Object.toString
    System.out.print(" ")
System.out.println()

