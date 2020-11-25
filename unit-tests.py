#-----------------------------------------------------------------------
# unit-tests.py
#-----------------------------------------------------------------------

# Imports --------------------------------------------------------------

from matrix import Matrix
import unittest

# Define Inputs --------------------------------------------------------

## 00. invalid inputs -------------------------------

# invalid list
list_00 = []

# vector list
list_01 = [1,2,3,4]

# a non-entirely-numerical list
list_02 = [2,3,[],4]

# invalid list input
list_03 = [[1],[2],[],[4]]

# a non-rectangular list
list_04 = [[1,2],[3,4],[5],[6,7,8]]


## 01. valid inputs ---------------------------------

# empty vector
list_10 = [[]]

# 4x1 col vector
list_11 = [[1],[2],[3],[4]]

# 1x3 row vector
list_12 = [[1,2,3]]

# 2x3 matrix  
list_21 = [[1,2,3],[4,5,6]]

# 4x3 matrix  
list_22 = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

# 3x3 matrix  
list_23 = [[1,2,3],[4,5,6],[7,8,9]]


## Unit Tests -----------------------------------------------------------

class TestStringMethods(unittest.TestCase):

    ## static-method tests ---------------------------------------------

    # empty-matrix test
    def test_empty(self):
        self.assertTrue(Matrix.is_empty(list_o))
        self.assertFalse(Matrix.is_empty(list_a))
        self.assertFalse(Matrix.is_empty(list_b))
        self.assertFalse(Matrix.is_empty(list_c))
        self.assertFalse(Matrix.is_empty(list_d))

    # nested-list test 
    def test_nested_list(self):
        self.assertTrue(Matrix.is_nested_list(list_b))
        self.assertTrue(Matrix.is_nested_list(list_c))
        self.assertFalse(Matrix.is_nested_list(list_a))

    # rectangular check test 
    def test_rectangular(self):
        self.assertTrue( Matrix.is_rectangular(list_b))
        self.assertFalse( Matrix.is_rectangular(list_e))

    # numeric list check test 
    def test_rectangular(self):
        self.assertTrue( Matrix.is_rectangular(list_b))
        self.assertFalse( Matrix.is_rectangular(list_e))

    # size function test
    def test_size(self):
        self.assertEqual( Matrix.size(list_b), (4,1))

    # numeric-only-list test
    def test_numeric_only(self):
        self.assertTrue( Matrix.size(list_b))

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