class Solution:
  def destCity(self, paths: List[List[str]]) -> str: 
      city = set() 

      for start, end in paths : 
          city.add(start) 

      for start, end in paths : 
          if end not in city : 
              return end 


         

         

    
      


    






    

    