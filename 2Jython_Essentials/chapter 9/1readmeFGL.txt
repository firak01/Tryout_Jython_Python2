20261124
html_soure_viewer enthält alle benötigten Dateien in einer .py Datei.
	Das Beispiel ist besonders interessant, weil:

Es beginnt mit 
dem HtmlTreeViewer
		Dieser erstellt ein Swing-Layout
		List den Inhalt der übergebenen URL mit einer Python Klasse aus.
		
		Nutzt dann den eigenen entwicklten Python HtmlTreeParser um das Model 
		für den Swing Viewer bereitzustellen.
		

HtmlTreeParser erbt von htmllib.HTMLParser (also einer Python-Klasse)
        Er nutzt wiederum eine Klasse
        	HtmlTagTreeModel(swing.tree.TreeModel), die also Java Swing erbt !!!!!!
        	
        	Dies wird gefüttert mit der selbst erstellten Tag Klasse. 
        	Dies ist eine selbst erstellte Python/Java Datenstruktur.
        	
	
 