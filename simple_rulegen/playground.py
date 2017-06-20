from sklearn.datasets import load_iris
from sklearn import tree
import os
from inspect import getmembers

print( getmembers( clf.tree_ ) )

# helper 
def objMethod(object):
    return [method for method in dir(object) if callable(getattr(object, method))]

data_in = load_iris()

clf = tree.DecisionTreeClassifier()
clf = clf.fit(data_in.data, data_in.target)

clf.tree_.impurity
clf.tree_.value

#clf.get_params()
data_name = data_in.feature_names

n_nodes = clf.tree_.node_count
children_left = clf.tree_.children_left
children_right = clf.tree_.children_right
feature = clf.tree_.feature
threshold = clf.tree_.threshold



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

import sys
sys.setrecursionlimit(1500)

def rule_info(sign,id):
    return((sign,id))

def get_rule(id,val):
    if pl[id]==0:
        return(rule_info('l',pl[id]))
    if pr[id]==0:
        return(rule_info('r',pr[id]))
    if pl[id]:
        out.append(get_rule(pl[id],rule_info('r',pl[id])))
    if pr[id]:
        out.append(get_rule(pr[id],rule_info('r',pr[id])))
    return(out)


pr
pl
out = []
get_rule(15,[])

rules = []
for leaf in leaf_ids:
    
    out = list()
    rules.append(get_rule(leaf,[leaf]))


                
        a.append()



objMethod(clf.tree_)
clf.tree_


# The tree structure can be traversed to compute various properties such
# as the depth of each node and whether or not it is a leaf.

node_depth = np.zeros(shape=n_nodes)
is_leaves = np.zeros(shape=n_nodes, dtype=bool)
stack = [(0, -1)]  # seed is the root node id and its parent depth
while len(stack) > 0:
    node_id, parent_depth = stack.pop()
    node_depth[node_id] = parent_depth + 1

    # If we have a test node
    if (children_left[node_id] != children_right[node_id]):
        stack.append((children_left[node_id], parent_depth + 1))
        stack.append((children_right[node_id], parent_depth + 1))
    else:
        is_leaves[node_id] = True

print("The binary tree structure has %s nodes and has "
      "the following tree structure:"
      % n_nodes)
for i in range(n_nodes):
    if is_leaves[i]:
        print("%snode=%s leaf node." % (node_depth[i] * "\t", i))
    else:
        print("%snode=%s test node: go to node %s if X[:, %s] <= %ss else to "
              "node %s."
              % (node_depth[i] * "\t",
                 i,
                 children_left[i],
                 feature[i],
                 threshold[i],
                 children_right[i],
                 ))
print()


