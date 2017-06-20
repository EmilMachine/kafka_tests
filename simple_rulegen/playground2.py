from sklearn.datasets import load_iris
from sklearn import tree
from numpy import np
data_in = load_iris()

### TODO - 


### helper 
#from inspect import getmembers
#print( getmembers( clf.tree_ ) )
#
#def objMethod(object):
#    return [method for method in dir(object) if callable(getattr(object, method))]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(data_in.data, data_in.target)

data_name = data_in.feature_names

feature = clf.tree_.feature
threshold = clf.tree_.threshold
leaf_vals = clf.tree_.value


children_left = clf.tree_.children_left
children_right = clf.tree_.children_right


def parents_from_children(children):
    # return a list of parents from a list of children
    parents = [None]*len(children)
    for id,i in enumerate(children):
        if i>=0:
            parents[i] = id
    return parents

# get parents lists    
pl = parents_from_children(children_left)
pr = parents_from_children(children_right)

leaf_ids = [id for id,i in enumerate(feature) if i==-2]

def rule_info(sign,id):
    feature_name = data_name[feature[id]]
    sign_map = {'r':'>','l':'<='}
    val = round(threshold[id],3)
    return(feature_name + sign_map[sign]+ str(val))
        
    
def get_rule(id):
    out = []
    while not id==0:
        if pl[id] is not None:
            out.append(rule_info('l',pl[id]))
            id = pl[id]
        if pr[id] is not None:
            out.append(rule_info('r',pr[id]))
            id = pr[id]
    return(out)


def get_hitrate(id):
    return leaf_vals[id]/leaf_vals[id].sum()
    
def get_catchrate(id):    
    return leaf_vals[id]/leaf_vals[0]


rules = []
for leaf in leaf_ids:
   rules.append({'id':leaf,'rule':get_rule(leaf),'hitrate':get_hitrate(leaf),'catchrate':get_catchrate(leaf)})

for r in rules:
    print(r)

