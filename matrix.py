#-----------------------------------------------------------------------
# matrix.py
#-----------------------------------------------------------------------

## Imports --------------------------------------------------------------

## Class Definition -----------------------------------------------------

class Matrix:
    '''
    Custom Data-Type for numerical vectors and numerical 2D matrices

    Note: 
    - lists are rows 
    - input vectors for matrix generation:
        - row vector: [[1,2,3,4]]
        - col vector: [[1],[2],[3],[4]]
        - 2X3 matrix: [[1,2,3],[4,5,6]]
    '''

    ## static-methods/helper functions ----------------------------------
    
    # check empty matrix ------------------------------------------------
    @staticmethod
    def is_empty(input_list):
        """
        checks if input is empty matrix candidate
        """
        return len(input_list) == 1 and len(input_list[0]) == 0
    
    # check if list elements are all lists ------------------------------
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
        checks if entered nested list is rectangular
        """
        lens = [ len(ele) for ele in input_list]
        if max(lens) == min(lens):
            return True
        else:
            return False

    # checks if list is entirely numeric -------------------------------
    @staticmethod
    def is_numeric_list(input_list):
        """
        helper function to check if all list elements are numeric
        """
        return sum([ isinstance(ele, (int, float)) for ele in input_list]) == len(input_list)
        
    # calculate size ----------------------------------------------------
    @staticmethod
    def get_size(input_list):
        """
        computes the size of a verified vector or 2D matrix
        """
        if Matrix.is_empty(input_list):
            num_of_rows = 0
            num_of_cols = 0
        else:   
            num_of_rows = len(input_list)
            num_of_cols = len(input_list[0])
        
        return (num_of_rows, num_of_cols)

    # check multiplication compatibility -------------------------------
    @staticmethod
    def dim_check_for_mult(input_matrix_a, input_matrix_b):

        try:
            size_a = input_matrix_a.size
            size_b = input_matrix_b.size

            print()

            if size_a[1] == size_b[0]:
                return True
            else: 
                return False
        except:
            raise Exception("Input type is not Matrix type")

    # generate zero matrix ----------------------------------------------
    @staticmethod
    def zero_matrix(size_tuple):
        """
        input a tuple with size of zero matrix to generate
        """
        return Matrix([ [0 for col in range(size_tuple[1]) ] for row in range(size_tuple[0]) ])

    ## instance-methods ------------------------------------------------

    def transpose(self):
        """
        outputs a copy of the transpose of the input matrix
        """

        if self.is_vector:
            return self

        elif self.is_matrix:
            transposed_list = []

            for col_n in range(self.size[1]):
                transposed_list.append([row[col_n] for row in self.final_matrix])

            return Matrix(transposed_list)

    def copy(self):
        """
        returns a copy of the Matrix object
        """
        return Matrix(self.final_matrix.copy())

    def dot(self, other):
        """
        computes dot product
            - vector * vector 
            - matrix * vector 
            - vector * matrix 
            - matrix * matrix
        """        
        pass

    ## dunder-methods --------------------------------------------------

    def __str__(self):
        """
        print out a Matrix data-type like a matrix in the CLI
        """
        try:

            string_to_print = '\n'
            
            if self.empty:

                string_to_print += '|  |\n'

                return string_to_print

            else:

                for row in self.final_matrix:

                    string_to_print += '| '

                    for ele in row:
                        string_to_print +=  str(ele) + ' '

                    string_to_print += '|\n'

                return string_to_print

        # throw error
        except:
            raise Exception('Cannot print Matrix!')
            
    def __eq__(self, other):
        """
        equality check for matrices 
        """
        
        # load the core lists stored in the data-type
        core_list_a = self.final_matrix
        core_list_b = self.final_matrix

        # check if the internally stored lists are equal
        if core_list_a == core_list_b:
            return True
        else: 
            return False
    
    ## constructor ------------------------------------------------------
    def __init__(self, input_list):
        '''
        constructor function for Matrix data-type
        '''    

        # check if nested list first ------------------------------------
        if self.is_nested_list(input_list):

            # if input list is empty ----------------------------------------
            if self.is_empty(input_list):

                # set empty flag
                self.empty = True

                # save core values of matrix
                self.final_matrix = input_list

                # set size of matrix
                self.size = (0,0)
        
            # if input list is not empty ------------------------------------
            else:
                
                try:

                    # check rectangular and numeric nested lists
                    if Matrix.is_rectangular(input_list) and all([ Matrix.is_numeric_list(nested_list) for nested_list in input_list  ]):

                        # set empty flag
                        self.empty = False

                        # save core values of matrix
                        self.final_matrix = input_list

                        # set size of matrix
                        self.size = Matrix.get_size(input_list)

                except:

                    raise Exception("Input list is either not rectangular like a Matrix or the nested lists are not all numeric!")
            
        # if input list is not nested
        else:
            raise Exception("Input list needs to be nested list where inner lists are rows of matrix")
