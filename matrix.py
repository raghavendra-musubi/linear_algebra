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
        - empty matrix: [[]]
    '''

    ## static-methods/helper functions ----------------------------------
    
    # check if empty list ------------------------------------------------
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
         
    # rectangular nested list check -------------------------------------------------
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
        
    # calculate Matrix size ----------------------------------------------------
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

    # check Matrix multiplication compatibility -------------------------------
    @staticmethod
    def dim_check_for_mult(input_matrix_a, input_matrix_b):

        try:
            size_a = input_matrix_a.size
            size_b = input_matrix_b.size

            if size_a[1] == size_b[0]:
                return True
            else: 
                return False
        except:
            raise Exception("Input type is not Matrix type")

    # generate zero Matrix ----------------------------------------------
    @staticmethod
    def zero_matrix(size_tuple):
        """
        input a tuple with size of zero matrix to generate
        """
        if isinstance(size_tuple, tuple):
            return Matrix([ [0 for col in range(size_tuple[1]) ] for row in range(size_tuple[0]) ])

        else: raise Exception("Zero-Matrix size must be specified in a tuple type!")

    # generate identity Matrix ------------------------------------------
    @staticmethod
    def id_matrix(size_int):
        """
        input an identity matrix of given size
        """

        if isinstance(size_int, int):

            return_list = Matrix.zero_matrix((size_int,size_int)).final_matrix

            for index in range(size_int):
                return_list[index][index] = 1
            
            # print(return_list)
            return Matrix(return_list)

        else: raise Exception("Identity-Matrix size must be specified in int type!")
        

    ## instance-methods ------------------------------------------------

    # generate a new transpose Matrix from existing Matrix
    def transpose(self):
        """
        outputs a copy of the transpose of the input matrix
        """

        if not self.empty:

            transposed_list = []  
            
            for col_n in range(self.size[1]):
                transposed_list.append( [row[col_n] for row in self.final_matrix] )

        else:
            transposed_list = self.final_matrix
            
        return Matrix(transposed_list)

    # copy a Matrix 
    def copy(self):
        """
        returns a copy of the Matrix object
        """
        return Matrix(self.final_matrix.copy())

    # dot product of current Matrix with another
    def dot(self, other):
        """
        computes dot product
            - vector * vector 
            - matrix * vector 
            - vector * matrix 
            - matrix * matrix
        """

        if Matrix.dim_check_for_mult(self, other):
            
            # preparing both matrices for multiplication
            m1 = self.final_matrix
            m2 = other.transpose().final_matrix
            
            product_list = []

            for row_num, row in enumerate(m1):

                product_list.append([])

                for col_num, col in enumerate(m2): 

                    ele = [ x * y for x,y in zip(row,col) ]

                    sum_ele = sum(ele)

                    product_list[row_num].append(sum_ele)

            return Matrix(product_list) 
        
        else:
            raise Exception(" Matrix multiplication is not possible because of dimension mismatch! ")
    
    # check if a Matrix is symmetric
    def is_symmetric(self):
        '''
        check if matrix is symmetric i.e. Matrix = Matrix.transpose()
        '''

        if self.is_square:
            return self.transpose() == self
        else: raise Exception('Only square matrices can be symmetric!')

    # compute the multiplication of a scalar with Matrix
    def scale(self, int_scalar):
        '''
        scale all matrix elements with the input scalar
        '''

        return Matrix([ list(map(lambda x:x * int_scalar,row)) for row in self.final_matrix ])


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

        return self.final_matrix == other.final_matrix

    def __add__(self, other):
        '''
        sum two matrices of the same size
        '''

        if self.size == other.size:
            
            summed_list = Matrix.zero_matrix(self.size).final_matrix

            for row_num, row_val in enumerate(self.final_matrix):
                for col_num, col_val in enumerate(row_val):
                    summed_list[row_num][col_num] = self.final_matrix[row_num][col_num] + other.final_matrix[row_num][col_num]

            return Matrix(summed_list)

        else:
            raise Exception("Matrix dimension must match for matrix addition!")
        

    def __sub__(self, other):
        '''
        compute difference between matrices of the same size
        '''

        if self.size == other.size:
            
            difference_list = Matrix.zero_matrix(self.size).final_matrix

            for row_num, row_val in enumerate(self.final_matrix):
                for col_num, col_val in enumerate(row_val):
                    difference_list[row_num][col_num] = self.final_matrix[row_num][col_num] - other.final_matrix[row_num][col_num]

            return Matrix(difference_list)

        else:
            raise Exception("Matrix dimension must match for matrix subtraction!")
    
    def __mul__(self, other):
        '''
        compute product of dimensionally compatible matrices
        '''
        return self.dot(other)

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

                # set square matrix flag 
                self.is_square = True
        
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

                        # set square matrix flag 
                        if self.size[0] == self.size[1]: self.is_square = True
                        else: self.is_square = False

                except:

                    raise Exception("Input list is either not rectangular like a Matrix or the nested lists are not all numeric!")
            
        # if input list is not nested
        else:
            raise Exception("Input list needs to be nested list where inner lists are rows of matrix")
