import networkx

G = networkx.MultiDiGraph()
indexes = dict()


def add_item(item:str,item_meaning:str):
    if item_meaning not in indexes.keys():
        G.add_node(item_meaning)
        add_index(item_meaning,indexes)
    add_node_and_register(item,item_meaning,G,indexes)

def add_index(index_name:str,index_register:dict):
    index_register[index_name] = set()

def add_node_and_register(node_name:str,index_name:str,graph:networkx.Graph,index_register:dict):
    graph.add_edge(node_name,index_name)
    index_register[index_name].add(node_name)

for i in ["groups","classes","persons","places","descriptions"]:
    add_index(i,indexes)

add_item("Vajra Safahr","persons")
add_item("Magier","classes")
G.add_edge("Vajra Safahr","Magier")
add_item("Xanathar-Gilde","groups")
add_item("Xanathar","persons")
G.add_edge("Xanathar","Xanathar-Gilde")