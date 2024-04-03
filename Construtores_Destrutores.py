class ConstructAndDestruct:
    def __init__(self):
     pass
    def __del__(self):
        print('destructor')
    
      
obj = ConstructAndDestruct()
del obj