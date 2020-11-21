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

        # if input list is not empty
        if len(input_list) > 0:
            self.is_empty = False
            
            # check if input list is vector
            # isinstance(input_list, list):

        else:
            # set empty flag
            self.is_empty = True
            self.final_matrix = input_list

        self.input_list = input_list

    # Dunder Functions -------------------------------------------------

    # Class Methods ----------------------------------------------------

    def transpose(self, input_matrix):
        """
        outputs a copy of the transpose of the input matrix
        """
        pass

    # Helper Functions -------------------------------------------------
    
    def is_numeric_list(input_list):
        """
        helper function to check if all list elements are numeric
        """
        return sum([ isinstance(ele, (int, float)) for ele in input_list]) == len(input_list)

    def is_empty(input_list):
        """
        checks if list is empty
        """
        pass

    def is_matrix(input_list):
        """
        check if input list is valid matrix
        """
        pass

    def is_two_dim(input_matrix):
        """
        check if input matrix is 2-D
        """
        pass

    def size(input_matrix_or_vector):
        """
        computes the size of a verified vector or 2D matrix
        """