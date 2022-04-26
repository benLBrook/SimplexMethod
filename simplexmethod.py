from __future__ import division
import numpy as np
import pandas as pd
from scipy.spatial import HalfspaceIntersection, ConvexHull
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

#new
def buildTableau():
        r_cost=[-10,-12,-12,0,0,0]
        n_cost = 0
        x=[0,0,0,20,20,20]
        x_B = [20,20,20]
        arr=(np.array([[1,2,2],[2,1,2],[2,2,1]])).astype(float)
        identity_matrix = (np.identity(3, dtype="int")).astype(float)
        b = (np.insert(x_B,0,n_cost,axis=0)).astype(float)
        arr_I = np.insert(arr,len(arr[0,:]),identity_matrix,axis=1)
        arr_r_cost = np.insert(arr_I,0,r_cost,axis=0)
        tableau = np.insert(arr_r_cost,0,b,axis=1)
        print("Tableau: ")
        print(tableau)
#buildTableau()       


def fullTableauIteration():
        r_cost=[-10,-12,-12,0,0,0]
        n_cost = 0
        x=[0,0,0,20,20,20]
        x_B = [20,20,20]
        arr=(np.array([[1,2,2],[2,1,2],[2,2,1]])).astype(float)
        identity_matrix = (np.identity(3, dtype="int")).astype(float)
        b = (np.insert(x_B,0,n_cost,axis=0)).astype(float)
        arr_I = np.insert(arr,len(arr[0,:]),identity_matrix,axis=1)
        arr_r_cost = np.insert(arr_I,0,r_cost,axis=0)
        tableau = np.insert(arr_r_cost,0,b,axis=1)
        print("Tableau: ")
        print(tableau) #tableau[owsr,columns]
        arrf = []
        arrj = []
        n, k, p, q, i, m = 1, 0, 1, 0, 1, 1
        while n<len(tableau[0,:]):
                if tableau[0,n]<0:
                        while m < len(tableau[1:,0])+1:
                                if tableau[m,n]<0:
                                        m=m+1
                                else:
                                        arrf.append(tableau[m,n])
                                        arrj.append(tableau[m,0])
                                        m=m+1      
                        ratio = np.divide(arrj,arrf) #you could share the functions (o-o-p) look at stackoverflow to see how to do this. 
                        min = ratio[k]
                        while k<len(ratio)-1:
                                if min < 0:
                                        min = ratio[k+1]
                                        q, k = k+1, k+1
                                elif ratio[k+1] >= 0 and min > ratio[k+1]: #you need to fix this -0, +0 problem. 
                                        min = ratio[k+1]
                                        q, k = k+1, k+1
                                else:
                                        k = k+1
                        pivot_row = tableau[q+1,:]
                        pivot_row_divide = np.divide(pivot_row,tableau[q+1,n])
                        tableau[q+1,:] = pivot_row_divide
                        while p<len(tableau[:,n]): 
                                if np.array_equal(tableau[p,:],pivot_row_divide):
                                        p = p+1
                                else:
                                        tableau[p,:] = tableau[p,:]-tableau[p,n]*pivot_row_divide
                                        p = p+1
                        tableau[0,:] = tableau[0,:]-tableau[0,n]*pivot_row_divide
                        n, k, p, q, m = 1, 0, 1, 0, 1
                        arrf = []
                        arrj = []
                        print("iteration ",i,":")
                        print(tableau)
                        i = i+1
                        
                else:
                        n = n+1
        print("Final Tableau: ")
        print(tableau)
        
        
fullTableauIteration()
























def standardForm(): #need to eventually add variables in parenthesis for matrix, cost etc...
        r_cost=[-10,-12,-12,0,0,0] #could create a class called Simplex, and you could make these instance variables, so they can be shared between this function and the next (it will get rid of yellow underlines). you don't have to it's an option.
        x=[0,0,0,20,20,20]
        x_B = [20,20,20]
        const=np.array([[1,2,1],[2,1,2],[2,2,1]])

        c_add = np.array([1,0,0]) # Array to be added as column
        tableau = np.hstack((const, np.atleast_2d(c_add).T)) # Adding column to numpy array
        
        # printing result
        #print ("resultant array", str(result),'', 'initial array')
        

        for x in range(len(c_add)-1): #need -1, otherwise without it, we try to perform a swap at (*), but the index [x+1] does not exist. 
                num =c_add[x]
                c_add[x] = c_add[x+1] # (*)
                c_add[x+1] = num
                tableau = np.hstack((tableau, np.atleast_2d(c_add).T))
                #print ("resultant array", str(result),'',x)   
        
        #print(tableau)
        #print (str(tableau)) #note: tableau[x,y] -> tableau[rows,columns]
        #print(tableau[2,:])
        #lst = np.array([[-10,-12,-12,0,0,0]])
        #tableau = np.append(tableau, lst, axis=0) #axis=0 adds horizontally, axis=1 adds vertically.
        print("Matrix in standard form: ")
        print(tableau)
#standardForm()







        
#maybe add a method such that you can look at each iteration individually?

#fullTableauIteration()

#<---need code to test to test if the vector x is a basic feasible solution--->#
#<---need code that will calculate the negative cost c^T*x c^T= cost found in obj func. x= feasible solution--->#
#keep in mind you might need to create functions if you have alot of for loops in the code. 
#also consider adding the basic vector, reduced cost, and negative of cost to the result matrix for the complete format of the tableau. might save on code. 
#print(result[:,0])
#result[:,0] = np.divide(result[:,0],2)#result[:,0] - 4*result[:,0]
#print(result[:,0])

        
        

	
            
            
        
        
            