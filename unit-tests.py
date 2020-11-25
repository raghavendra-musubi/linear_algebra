#-----------------------------------------------------------------------
# unit-tests.py
#-----------------------------------------------------------------------

# Imports --------------------------------------------------------------

from matrix import Matrix
import unittest

# Define Inputs --------------------------------------------------------

## static methods ------------------------------
# empty list
list_o = []

# vector list
list_a = [1,2,3,4]

# nested list for matrix 
list_b = [[1],[2],[3],[4]]

# nested list for matrix with empty list
list_c = [[1],[2],[],[4]]

# a non-entirely-numerical list
list_d = [2,3,[],4]

# a non-rectangular list
list_e = [[1,2],[3,4],[5],[6,7,8]]

## class methods ------------------------------
# 2x3 matrix for transpose 
list_f = [[1,2,3],[4,5,6]]

# 4x3 matrix for transpose 
list_g = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

# 3x3 matrix for transpose 
list_h = [[1,2,3],[4,5,6],[7,8,9]]

# Unit Tests -----------------------------------------------------------

class TestStringMethods(unittest.TestCase):

    ## static-method tests ---------------------------------------------

    # empty-matrix test
    def test_empty(self):
        self.assertTrue(Matrix.is_empty(list_o))
        self.assertFalse(Matrix.is_empty(list_a))
        self.assertFalse(Matrix.is_empty(list_b))
        self.assertFalse(Matrix.is_empty(list_c))
        self.assertFalse(Matrix.is_empty(list_d))

    # vector test
    def test_vector(self):
        self.assertTrue(Matrix.is_numeric_list(list_a))
        self.assertFalse(Matrix.is_numeric_list(list_b))

    # nested-list test 
    def test_nested_list(self):
        self.assertTrue(Matrix.is_nested_list(list_b))
        self.assertTrue(Matrix.is_nested_list(list_c))
        self.assertFalse(Matrix.is_nested_list(list_a))

    # rectangular check test 
    def test_rectangular(self):
        self.assertTrue( Matrix.is_rectangular(list_b))
        self.assertFalse( Matrix.is_rectangular(list_e))

    # flatten to vector test
    def test_flatten_arr_to_vec(self):
        self.assertEqual( Matrix.flatten_arr_to_vec(list_b),list_a)

    # size function test
    def test_size(self):
        self.assertEqual( Matrix.size(list_b), (4,1))

    # dim check function test
    def test_dim_check(self):
        self.assertFalse( Matrix.dim_check_for_mult(Matrix(list_f),Matrix(list_g)) )
        self.assertTrue( Matrix.dim_check_for_mult(Matrix(list_f),Matrix(list_h)) )

    # test zero matrix generator
    def test_zero_matrix(self):
        self.assertEqual( Matrix((1,2)), Matrix( [0,0]                  ) )
        self.assertEqual( Matrix((2,1)), Matrix( [0,0]                  ) )
        self.assertEqual( Matrix((3,1)), Matrix( [0,0,0]                ) )
        self.assertEqual( Matrix((3,2)), Matrix( [[0,0],[0,0],[0,0]]    ) )
        self.assertEqual( Matrix((2,3)), Matrix( [[0,0,0],[0,0,0]]      ) )
        
    ## instance-method tests ---------------------------------------------

    # transpose tests ----------------------------------------------------
    # vector transpose test
    def test_transpose_list(self):
        self.assertEqual( Matrix(list_a).transpose(), Matrix(list_a) )

    # matrix transpose test
    def test_transpose_matrix(self):
        self.assertEqual( Matrix(list_f).transpose(), Matrix([[1,4],[2,5],[3,6]]) )

    # dot product --------------------------------------------------------
    def test_vec_vec_dot_product(self):
        self.assertEqual( Matrix([1,2,3]), Matrix([3,4,5]) )

# Make the test results print --------------------------------------------

if __name__ == '__main__':
    unittest.main()