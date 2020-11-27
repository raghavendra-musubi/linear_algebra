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
        self.assertTrue(    Matrix.is_empty(list_10)    )
        self.assertFalse(   Matrix.is_empty(list_00)    )
        self.assertFalse(   Matrix.is_empty(list_01)    )

    # nested-list test 
    def test_nested_list(self):
        self.assertTrue(    Matrix.is_nested_list(list_11)  )
        self.assertTrue(    Matrix.is_nested_list(list_21)  )
        self.assertFalse(   Matrix.is_nested_list(list_01)  )
        self.assertFalse(   Matrix.is_nested_list(list_02)  )

    # rectangular check test 
    def test_rectangular(self):
        self.assertTrue(    Matrix.is_rectangular(list_22) )
        self.assertFalse(   Matrix.is_rectangular(list_04) )

    # numeric list check test 
    def test_numeric_only(self):
        self.assertTrue(    Matrix.is_numeric_list(list_01)    )
        self.assertFalse(   Matrix.is_numeric_list(list_02)    )

    # size function test
    def test_size(self):
        self.assertEqual(   Matrix.get_size(list_10), (0,0)   )
        self.assertEqual(   Matrix.get_size(list_11), (4,1)   )
        self.assertEqual(   Matrix.get_size(list_12), (1,3)   )
        self.assertEqual(   Matrix.get_size(list_21), (2,3)   )

    # dim check function test
    def test_dim_check(self):
        self.assertFalse( Matrix.dim_check_for_mult( Matrix(list_21), Matrix(list_22)) )
        self.assertFalse( Matrix.dim_check_for_mult( Matrix(list_23), Matrix(list_22)) )
        self.assertTrue( Matrix.dim_check_for_mult( Matrix(list_22), Matrix(list_23)) )
        self.assertTrue( Matrix.dim_check_for_mult( Matrix(list_11), Matrix(list_12)) )
        
    # test zero matrix generator
    def test_zero_matrix(self):
        self.assertEqual( Matrix.zero_matrix((1,2)), Matrix( [[0,0]]                ) )
        self.assertEqual( Matrix.zero_matrix((2,1)), Matrix( [[0],[0]]              ) )
        self.assertEqual( Matrix.zero_matrix((3,1)), Matrix( [[0],[0],[0]]          ) )
        self.assertEqual( Matrix.zero_matrix((3,2)), Matrix( [[0,0],[0,0],[0,0]]    ) )
        self.assertEqual( Matrix.zero_matrix((2,3)), Matrix( [[0,0,0],[0,0,0]]      ) )

    # # test dim check for multiplication
    # def test_

    ## instance-method tests ---------------------------------------------

    # transpose tests ----------------------------------------------------
    def test_transpose(self):
        self.assertEqual(       Matrix(list_10).transpose(), Matrix([[]])                              )
        self.assertEqual(       Matrix(list_11).transpose(), Matrix([[1,2,3,4]])                       )
        self.assertEqual(       Matrix(list_12).transpose(), Matrix([[1],[2],[3]])                     )
        self.assertEqual(       Matrix(list_21).transpose(), Matrix([[1,4],[2,5],[3,6]])               )
        self.assertEqual(       Matrix(list_22).transpose(), Matrix([[1,4,7,10],[2,5,8,11],[3,6,9,12]]))
        self.assertNotEqual(    Matrix(list_22).transpose(), Matrix([[1,2,3,4]])                       )
        self.assertNotEqual(    Matrix(list_21).transpose(), Matrix([[1,2,3,4]])                       )

    # dot product --------------------------------------------------------
    def test_dot_product(self):
        self.assertEqual( Matrix(list_22).dot(Matrix(list_23)), Matrix([[30,36,42],[66,81,96],[102,126,150],[138,171,204]]))

# Make the test results print --------------------------------------------

if __name__ == '__main__':
    unittest.main()