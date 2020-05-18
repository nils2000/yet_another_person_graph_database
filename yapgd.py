import networkx

G = networkx.MultiDiGraph()
indexes = dict()
edge_labels = dict()

def add_multiple_edges_to(center,center_quality,list_of_items,edgedesc=None):
    add_item(center,center_quality)
    for i in list_of_items:
        G.add_edge(i,center)
        if edgedesc:
            edge_labels[(item_1,item_2)] = edgedesc

def add_multiple(common_feature,comon_feature_quality,kind_of_items,list_of_items):
    for p in list_of_items:
        add_edge(p,kind_of_items,common_feature,comon_feature_quality)

def add_inhabitants(village,list_of_villagers):
    #add_item(village,"places")
    for p in list_of_villagers:
        add_edge(p,"persons",village,"places")

def add_items(item_quality:str,list_of_items:list):
    for i in list_of_items:
        add_item(i,item_quality)

def add_item(item:str,item_meaning:str):
    if item_meaning not in indexes.keys():
        G.add_node(item_meaning)
        add_index(item_meaning,indexes)
    if item not in G.nodes:
        add_node_and_register(item,item_meaning,G,indexes)
    else:
        if (item,item_meaning) not in G.edges:
            G.add_edge(item,item_meaning)

def add_connection(item_1,item_2,edgedesc=None):
    G.add_edge(item_1,item_2)
    if edgedesc: 
        edge_labels[(item_1,item_2)] = edgedesc

def add_edge(item_1,item_meaning_1,item_2,item_meaning_2,edgedesc=None):
    add_item(item_1,item_meaning_1)
    add_item(item_2,item_meaning_2)
    add_connection(item_1,item_2,edgedesc)

def add_index(index_name:str,index_register:dict):
    index_register[index_name] = set()

def add_node_and_register(node_name:str,index_name:str,graph:networkx.Graph,index_register:dict):
    graph.add_edge(node_name,index_name)
    index_register[index_name].add(node_name)

def in_neighbours(nodename:str):
    return [(x) for (x,y) in G.in_edges(nodename)]

def out_neighbours(nodename:str):
    return [(y) for (x,y) in G.out_edges(nodename)]

for i in ["groups","classes","persons","places","descriptions"]:
    add_index(i,indexes)

add_item("Vajra Safahr","persons")
add_item("Magier","classes")
G.add_edge("Vajra Safahr","Magier")
add_item("Xanathar-Gilde","groups")
add_item("Xanathar","persons")
G.add_edge("Xanathar","Xanathar-Gilde")
edge_labels[("Xanathar","Xanathar-Gilde")] = {"Rolle":"Anführer"}
add_item("Ahmaergo","persons")
G.add_edge("Ahmaergo","Xanathar-Gilde")
G.add_edge("Ahmaergo","Xanathar")
edge_labels[("Ahmaergo","Xanathar")] = {"Rolle":"Majordomus"}
#print(yapgd.G.in_edges("Xanathar-Gilde"))
add_edge("Ismark Koljanowitsch","persons","Irena Koljana","persons",{"Rolle":"Bruder"})
add_edge("Irena Koljana","persons","Ismark Koljanowitsch","persons",{"Rolle":"Schwester"})
add_edge("Koljan Indirowitsch","persons","Irena Koljana","persons",{"Rolle":"Vater"})
add_edge("Koljan Indirowitsch","persons","Ismark Koljanowitsch","persons",{"Rolle":"Vater"})
add_edge("Ismark Koljanowitsch","persons","Koljan Indirowitsch","persons",{"Rolle":"Sohn"})
add_edge("Irena Koljana","persons","Koljan Indirowitsch","persons",{"Rolle":"Adoptivtochter"})
add_inhabitants("Dorf Barovia",["Bildrath Cantemir","Parriwimple","Koljan Indirowitsch",
"Ismark Koljanowitsch", "Irena Koljana", "Arik Lorensk","Alenka","Mirabel","Sorvia",
"Marie", "Gertruda", "Donawitsch", "Doru"])
add_inhabitants("Schloss Ravenloft",["Quengelbauch","Esmeralda D'Avenir","Rahadin",
"Strahd von Zarowitsch","Lief Lipsiege","Helga Ruwak","Waruschka","Escher","Pidelwick",
"Pidelwick II","Cyrus Belview","Emil Toranescu", "Sascha Ivliskova",
"Patrina Ivliskova", "Patrina Welikowna","Klotz FielFielski","Beucephalus",
"Ludmilla Vilisewitsch","Anastrasya Karelova","Volenta Popofsky","König Barov", "Königin Ravenowia"])
add_connection("König Barov","Strahd von Zarowitsch",{"Rolle":"Vater"})
add_connection("Königin Ravenowia","Strahd von Zarowitsch",{"Rolle":"Mutter"})
add_connection("Sergej von Zarowitsch","Strahd von Zarowitsch",{"Rolle":"Bruder"})
add_multiple_edges_to("Nachtvetteln","races",["Morgantha","Bella Sonnenfluch","Offalia Wurmschwänzel"])
add_item("Erzfee","races")
G.add_edge("Ceithlenn mit den krummen Zähnen","Erzfee")
add_items("persons",["Friek","Mirtel"])
add_multiple_edges_to("Alter Knochenschleifer","places",["Morgantha","Bella Sonnenfluch","Offalia Wurmschwänzel","Friek","Mirtel"])
add_item("Wiedergänger","races")
add_items("Wiedergänger",["Wladimir Horngaard","Sir Godfrey Gwylyn"])
add_multiple_edges_to("Feste Argynvost","places",["Wladimir Horngaard","Savid","Sir Godfrey Gwylyn"])
add_inhabitants("Kresk",["Bürgermeister Dmitrij Kreskow","Anna"])
add_items("wichtige NPCs",["Irena Koljana","Ismark Koljanowitsch","Verna Goldbarren"])