#-----------------------------------------------------------------------
# matrix.py
#-----------------------------------------------------------------------

# Imports --------------------------------------------------------------

# Class Definition -----------------------------------------------------

class Matrix:
    '''
    Custom Data-Type for numerical vectors and numerical 2D matrices
    - note: all vectors are treated as column vectors 
    '''

    ## Static Helper Functions -----------------------------------------

    # check empty list -------------------------------------------------
    @staticmethod
    def is_empty(input_list):
        """
        checks if list is empty
        """
        return len(input_list) == 0

    # checks if list is entirely numeric -------------------------------
    @staticmethod
    def is_numeric_list(input_list):
        """
        helper function to check if all list elements are numeric
        """
        return sum([ isinstance(ele, (int, float)) for ele in input_list]) == len(input_list)
        
    # check if list elements are all lists -----------------------------
    @staticmethod
    def is_nested_list(input_list):
        """
        check if input list is valid matrix
        """
        # check for all list elements
        return sum([ isinstance(ele, (list)) for ele in input_list]) == len(input_list)
            
    # rectangular check -------------------------------------------------
    @staticmethod
    def is_rectangular(input_list):
        """
        checks if entered list is rectangular
        """

        for ele in input_list:
            if len(ele) != len(input_list[0]):
                return False
            else: 
                continue
        
        return True

    # flatten 1 col array to vector ------------------------------------
    def flatten_arr_to_vec(input_list):
        tmp = []
        for ele in input_list:
            tmp.extend(ele)
        return tmp

    # calculate size ---------------------------------------------------
    @staticmethod
    def size(input_list):
        """
        computes the size of a verified vector or 2D matrix
        """
        num_of_rows = len(input_list)
        num_of_cols = len(input_list[0])
        return (num_of_rows,num_of_cols)


    ## Constructor ------------------------------------------------------
    def __init__(self, input_list):
        '''
        constructor function for Matrix data-type
        '''    

        # if input list is empty ----------------------------------------
        if self.is_empty(input_list):

            # set empty flag
            self.is_empty = True
            self.is_vector = True
            self.is_matrix = True
            self.final_matrix = input_list
            self.size = (0,0)
        
        # if input list is not empty ------------------------------------
        else:
            self.is_empty = False
            
            # check if vector
            if self.is_numeric_list(input_list):
                self.is_vector = True
                self.is_matrix = False
                self.final_matrix = input_list
                self.size = (len(input_list),1)
            
            # check if matrix if 2D -------------------------------------
            elif self.is_nested_list(input_list):

                try:
                    
                    # check rectangular AND all numerical rows 
                    if self.is_rectangular(input_list) and sum( [ self.is_numeric_list(list_ele) for list_ele in input_list ] ) == len(input_list):
                        
                        # one column nested vector input
                        if len(input_list[0]) == 1:
                            self.is_vector = True
                            self.is_matrix = False
                            self.final_matrix = flatten_arr_to_vec(input_list)

                        # multi column matrix
                        else: 
                            self.is_vector = False
                            self.is_matrix = True
                            self.final_matrix = input_list
                        self.size = self.size(input_list)
                except:
                    raise ValueError('Input list may have empty lists as rows of intended matrix!')

            # raise error for wrong matrix -------------------------------
            else:
                raise Exception('Input is not a valid vector or 2D matrix!')

        

    ## Class Methods -----------------------------------------------------

    def transpose(self, input_matrix):
        """
        outputs a copy of the transpose of the input matrix
        """
        pass


    ## Dunder Functions --------------------------------------------------

    def __str__(self):
        string_to_print = '\n'
        
        # print vector 
        if self.is_vector:

            for ele in self.final_matrix:
                string_to_print += '| ' + str(ele) + ' |\n'

            return string_to_print
        
        # print matrix
        elif self.is_matrix:

            for row in self.final_matrix:

                string_to_print += '| '

                for ele in row:
                    string_to_print +=  str(ele) + ' '

                string_to_print += '|\n'

            return string_to_print

        
        # throw error
        else:
            raise Exception('Cannot print Matrix!')
            
