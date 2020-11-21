#-----------------------------------------------------------------------
# matrix.py
#-----------------------------------------------------------------------

# Imports --------------------------------------------------------------

# Class Definition -----------------------------------------------------

class Matrix:
    '''
    Custom Data-Type for vectors and 2D matrices 
    '''

    # Constructor ------------------------------------------------------
    def __init__(self, input_list):
        '''
        constructor function for Matrix data-type
        '''    

        # if input list is empty
        if self.is_empty(input_list):

            # set empty flag
            self.is_empty = True
            self.final_matrix = input_list
        
        # if input list is not empty 
        else:
            self.is_empty = False
            
            # check if vector
            if self.is_numeric_list(input_list):
                self.is_vector = True
                self.is_matrix = True
            elif self.is_nested_list(input_list):
                # check if matrix if 2D 
                if self.is_numeric_two_dim(input_list):
                    self.is_vector = False
                    self.is_matrix = True
            else:
                raise Exception('Input is not a valid vector or 2D matrix!')

        self.input_list = input_list

    # Class Methods ----------------------------------------------------

    def transpose(self, input_matrix):
        """
        outputs a copy of the transpose of the input matrix
        """
        pass


    # Helper Functions -------------------------------------------------
    @staticmethod
    def is_numeric_list(input_list):
        """
        helper function to check if all list elements are numeric
        """
        return sum([ isinstance(ele, (int, float)) for ele in input_list]) == len(input_list)
    
    @staticmethod
    def is_empty(input_list):
        """
        checks if list is empty
        """
        return len(input_list) == 0
        
    @staticmethod
    def is_nested_list(input_list):
        """
        check if input list is valid matrix
        """
        # check for all list elements
        return sum([ isinstance(ele, (list)) for ele in input_list]) == len(input_list)
        
    @staticmethod
    def is_numeric_two_dim(input_matrix):
        """
        check if input nested list is 2-D
        """
        
            
    @staticmethod
    def size(input_matrix_or_vector):
        """
        computes the size of a verified vector or 2D matrix
        """
        pass


    # Dunder Functions -------------------------------------------------