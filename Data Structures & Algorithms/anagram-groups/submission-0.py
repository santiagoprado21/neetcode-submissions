class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {} #anagramas . array de esas palabras
        for i in strs: #O(n)
            key = tuple(sorted(i))#Reconocer cuales palarbas son anagramas, se crea una clave para que todas las anagramas sean iguales
            if key not in hashmap:
                hashmap[key] = [i] #Si la palabra ordenada, no esta en el hash, se agrega la palabra normal como lista
            else:
                hashmap[key].append(i) #Agrupar los que son anagramas 
        return list(hashmap.values())
        
        #O(n) x O(k log k) = O(n x k log k)