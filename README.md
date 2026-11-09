# Tryout_Jython
Java mit Python - Jython
Wichtig: Jython 2.7 funktioniert nur mit Python 2.<BR>
<BR>
Als Prototyp gibt es hier einen JavaClassPathLoaderZZZ,<BR>
der unter Eclipse die benötigten Java-Bibliotheken von im lokalen Repository liegenden Java-Projekte erfasst<BR>
und in den Python-Path lädt.<BR>
Gestartet wird das von JythonKernel.py<BR>
<BR>
Siehe dazu die letzten tryouts.


----------------------
u.a. Ergänzungen zu den Beispiele aus den Büchern
- "Definitive Guide To Jython" https://jython.readthedocs.io/en/latest/OpsExpressPF/ <BR>
<BR>
- "Jython Essentials"          https://www.oreilly.com/library/view/jython-essentials/9781449397364/ <BR>
                               Merke: Hier sind nur die Kapitel, die von Python ausgehend Java einbinden.<BR>
                               Kapitel 12 und 13 gehen von Java aus und binden Python ein. Sie sind im Projekt "Tryout_Jython_Java8" 
<br>
Bzw. sinnvoller Code / Tests in den Kapiteln<br>
oder umfangreichere Anpassungen, z.B. aufgrund der dann im Buch verwendeten neueren Syntax.
<BR>
<BR>




-----------------------

Merke:<br>
Unterhalb des Source Folders sind keine Packages angelegt sondern einfache Folder.<br>
Packages haben sehr strikte Namenskonventionen und es würde auch eine pyInit - Routine bereitgestellt(durch pyDev)<BR>

Auch bei einfachen Folder gibt es Probleme beim Umbenennen von Datein, wenn die Folder mit einer Zahl anfangen.
Darum beginnen sie mit c = chapter (Kapitel).