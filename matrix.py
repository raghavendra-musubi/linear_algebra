#-----------------------------------------------------------------------
# matrix.py
#-----------------------------------------------------------------------

# Imports --------------------------------------------------------------

# Class Definition -----------------------------------------------------

class Matrix:
    '''
    Custom Data-Type for numerical vectors and numerical 2D matrices

    Note: 
        - all vectors are treated as column vectors 
        - consequently, no transpose exists for a matrix

    Note:
        - when inputting matrices, each list is a row 
    '''

    ## Static Helper Functions -----------------------------------------

    # check empty list -------------------------------------------------
    @staticmethod
    def is_empty(input_list):
        """
        checks if list is empty
        """
        return len(input_list) == 0
        # check inner list is also empty i.e. [[]]

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
        lens = [ len(ele) for ele in input_list]
        if max(lens) == min(lens):
            return True
        else:
            return False

    # flatten 1 col array to vector ------------------------------------
    @staticmethod
    def flatten_arr_to_vec(input_list):
        from functools import reduce
        tmp = reduce(lambda x,y: x + y, input_list)
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

    # check multiplication compatibility -------------------------------
    @staticmethod
    def dim_check_for_mult(input_matrix_type_a, input_matrix_type_b):
        size_a = input_matrix_type_a.size
        size_b = input_matrix_type_b.size

        if size_a[1] == size_b[0]:
            return True
        else: 
            return False

    # check multiplication compatibility -------------------------------
    @staticmethod
    def zero_matrix(size_tuple):
        return Matrix([ [0 for col in range(size_tuple[1]) ] for row in range(size_tuple[0]) ])
        
    ## Constructor ------------------------------------------------------
    def __init__(self, input_list):
        '''
        constructor function for Matrix data-type
        '''    

        # if input list is empty ----------------------------------------
        if self.is_empty(input_list):

            # set empty flag
            self.empty = True

            # set other flags 
            self.is_vector = True
            self.is_matrix = True

            # save core values of matrix
            self.final_matrix = []

            # set size of matrix
            self.size = (0,0)
        
        # if input list is not empty ------------------------------------
        else:

            # set empty flag
            self.empty = False
            
            # check if vector
            if self.is_numeric_list(input_list):

                # set other flags 
                self.is_vector = True
                self.is_matrix = False
                
                # save core values of matrix
                self.final_matrix = input_list

                # set size of matrix
                self.size = (len(input_list),1)
            
            # check if matrix if 2D -------------------------------------
            elif self.is_nested_list(input_list):

                try:
                    
                    # check rectangular AND all numerical rows 
                    if self.is_rectangular(input_list) and sum( [ self.is_numeric_list(list_ele) for list_ele in input_list ] ) == len(input_list):
                        
                        # one column nested vector input
                        if len(input_list[0]) == 1:

                            # set other flags 
                            self.is_vector = True
                            self.is_matrix = False

                            # save core values of matrix
                            self.final_matrix = flatten_arr_to_vec(input_list)

                        # multi column matrix
                        else: 

                            # set other flags 
                            self.is_vector = False
                            self.is_matrix = True
                            
                            # save core values of matrix
                            self.final_matrix = input_list

                        # set size of matrix
                        self.size = self.size(input_list)
                except:
                    raise ValueError('Input list may have empty lists as rows of intended matrix!')

            # raise error for wrong matrix -------------------------------
            else:
                raise Exception('Input is not a valid vector or 2D matrix!')

        

    ## Instance Methods -----------------------------------------------------

    def transpose(self):
        """
        outputs a copy of the transpose of the input matrix
        """
        # print(self.__dict__)
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
        
        # try matrix multiplication
        try:
            # vector-vector case
            if self.is_vector and other.is_vector:
                return sum( ele[0]*ele[1] for ele in zip(self.final_matrix, other.final_matrix) )

            else:

                try:
                    # vector-matrix case
                    if self.is_vector and self.is_matrix:
                        

                    # matrix-vector case

                    # matrix-matrix case

                except:
                    # throw dimension mismatch error
                    raise Exception('Matrix dimension mis-match!')


        # throw error for data type error 
        except:
            raise TypeError('Dot product applicable only to Matrix data-types')
            



    ## Dunder Functions --------------------------------------------------

    def __str__(self):
        """
        print out a Matrix data-type like a matrix in the CLI
        """

        string_to_print = '\n'
        
        if self.empty:

            string_to_print += '|  |\n'

            return string_to_print

        # print vector 
        elif self.is_vector:

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
    
    def __add__(self, other):
        """
        matrix addition operator overload
        """
        pass

    def __sub__(self, other):
        """
        matrix subtraction operator overload
        """
        pass

    def __mul__(self, other):
        """
        matrix multiplication operator overload
        """
        pass