# BE Programmation fonctionnel
# Pierre Lalanne & Clement Poirier

import functools

"""
Definition de la fonction loop qui s'arretera au point fixe 
"""
def loop(p,f,x):
    return(x) if(p(x)) else loop(p,f,f(x))


"""
fonction exists
"""
def exists(p,l):
    liste = map(p,l)
    filter(liste==True,liste)
