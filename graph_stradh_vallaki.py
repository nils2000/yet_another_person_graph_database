import yapgd

yapgd.add_inhabitants("Vallaki",["Bluto Krogarow","Baron Vargas Vallakowitsch","Vater Lucian Petrowitsch",
"Yeska","Miliwoj","Willemina Rikalowa", "Udo Lukowitsch","Henrik van der Voort",
"Urwin Martikow","Danika Dorakowa", "Brom Urwinkow", "Bray Urwinkow","Szlodar Szlodarowitsch",
"Yevgeni Kruschkin","Nikolai Wachter","Karl Wachter","Fiona Wachter","Stella Wachter","Rictavio","Drusilla",
"Piccolo","Isek Strasni","Baronin Lydia Petrowa","Victor Vallakowitsch","Nikolaj Wachter","Ernst Larnak","Dhavit",
                                 "Magdalena",
"Amalthia","Haliq","Leo Dilisnya","Gunther Arasek","Yelena Arasek","Gadof Blinsky","Luwasch","Arrigal","Arabelle",
"Lars Kjurls"])
yapgd.add_multiple_edges_to("Werraben","races",["Urwin Martikow","Danika Dorakowa", "Brom Urwinkow", "Bray Urwinkow"])
yapgd.add_multiple("Vistani","groups","persons",["Luwasch","Arrigal","Arabelle","Alenka","Mirabel","Sorvia","Alexei",
                                                 "Madame Eva"])
yapgd.add_multiple("Dämmerungselfen","races","persons",["Patrina Velikowna","Kasimir Velikow","Savid"])
yapgd.add_item("Lars Kjurls","Miliz")
yapgd.add_item("Vater Lucian Petrowitsch","Lathander")
yapgd.add_items("Kirche St. Andral",["Vater Lucian Petrowitsch","Yeska","Miliwoj","Willemina Rikalowa"])
yapgd.add_item("Udo Lukowitsch","Schuhmacher")
yapgd.add_item("Henrik van der Voort","Sargmacher")
yapgd.add_item("Gasthaus Blauwasser","Gasthaus")
yapgd.add_items("Gasthaus Blauwasser",["Urwin Martikow","Danika Dorakowa", "Brom Urwinkow", "Bray Urwinkow",
                                       "Szlodar Szlodarowitsch", "Yevgeni Kruschkin","Nikolai Wachter","Karl Wachter",
                                       "Rictavio"])
yapgd.add_items("Wachterhaus",["Nikolai Wachter","Karl Wachter","Fiona Wachter","Stella Wachter","Ernst Larnak",
                               "Leo Dilisnya","Fürstin Lovina Wächter","Vasili van Holtz","Dhavit",
                                 "Magdalena","Amalthia","Haliq"])
yapgd.add_item("Drusilla","Pferd")
yapgd.add_item("Piccolo","Affe")
yapgd.add_items("Bürgermeister-Villa",["Baron Vargas Vallakowitsch","Isek Strasni","Victor Vallakowitsch",
                                       "Baronin Lydia Petrowa"])
yapgd.add_connection("Baronin Lydia Petrowa","Vater Lucian Petrowitsch",{"Rolle":"Schwester"})
yapgd.add_connection("Szoldar Grygorowitsch","Szlodar Szlodarowitsch",{"Rolle":"Vater"})
yapgd.add_item("Victor Vallakowitsch","Magier")
yapgd.add_item("Gadof Blinsky","Artificer")
yapgd.add_item("Fritz von Weerg","Artificer")