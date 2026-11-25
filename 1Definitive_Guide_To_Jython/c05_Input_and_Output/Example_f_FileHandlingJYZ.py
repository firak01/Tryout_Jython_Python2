# -*- coding: utf-8 -*-

'''
Auszug aus dem Buch: "Definitive Guide to Jython"

Created on 02.11.2026

@author: Fritz Lindhauer


'''

# Write lines to file, flush, and close
my_file = open('mynewfile.txt','w')
my_file.write('This is the first line of text.\n')
my_file.write('This is the second line of text.\n')
my_file.write('This is the last line of text.\n')
my_file.flush()  # Unneccesary if closing the file but useful to clear buffer
my_file.close()

# Open file in read mode
my_file = open('mynewfile.txt','r')
a=my_file.read()
#ABER: IN MEINEM BEISPIEL IST DER GANZE DATEIINHALT IN DER 1. ZEILE
print "1. Zeile: '%s'" % a

# If we read again, we get a '' because cursor is at the end of text
#ABER: IN MEINEM BEISPIEL IST DANN DIE 2. ZEILE LEER
a=my_file.read()
print "2. Zeile: '%s'" % a


# Seek back to the beginning of file and perform read again
my_file.seek(0)
a=my_file.read()
print "wieder zurück zur 1. Zeile: '%s'" % a

###############################################################################
# Seek back to beginning of file and perform readline()
# Erst mit readline() kommt das Ergebnis korrekt Zeilenweise.
my_file.seek(0)
a=my_file.readline()
print "wieder zurück zur 1. Zeile: '%s'" % a

a=my_file.readline()
print "2. Zeile: '%s'" % a

a=my_file.readline()
print "3. Zeile: '%s'" % a

a=my_file.readline()
print "4. Zeile: '%s'" % a

# Use tell() to display current cursor position
ipos=my_file.tell()
print "file cursor position: '%s'" % ipos

my_file.seek(0)
ipos=my_file.tell()
print "wieder zurück zur: file cursor position: '%s'" % ipos

# Loop through lines of file
print "LOOP..."
for line in my_file:
     print "Zeile '%s'" % line