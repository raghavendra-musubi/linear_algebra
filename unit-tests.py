#-----------------------------------------------------------------------
# unit-tests.py
#-----------------------------------------------------------------------

# Imports --------------------------------------------------------------

from matrix import Matrix
import unittest

# Define Inputs ---------------------------------------------------------

## 00. invalid inputs ---------------------------------------------------

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


## 01. valid inputs ------------------------------------------------------

# empty vector
list_10 = [[]]

# 4x1 col vector
list_11 = [[1],[2],[3],[4]]
list_11a = [[5],[6],[7],[8]]

# 1x3 row vector
list_12 = [[1,2,3]]

# 2x3 matrix  
list_21 = [[1,2,3],[4,5,6]]
list_21a = [[7,8,9],[10,11,12]]

# 4x3 matrix  
list_22 = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

# 3x3 matrix  
list_23 = [[1,2,3],[4,5,6],[7,8,9]]

## 02. symmetric matrices -----------------------------------------------

# 2x2
list_31 = [[9,7],[7,6]]

# 3x3
list_32 = [[2,0,6],[0,8,2],[6,2,9]]

# 4x4
list_33 = [[1,6,3,4],[6,1,1,1],[3,1,3,2],[4,1,2,6]]

## anti-symmetric matrix 
list_34 = [[0,-1],[1,0]]

## 03. other generic matrices -------------------------------------------

# 3x3 matrix 
list_33a = [[10,60,30],[50,20,70],[40,80,90]]

# 4x4 matrix 
list_44 = [[1,6,3,4],[6,9,1,1],[3,0,3,2],[4,1,2,6]]


## 04. matrices whose determinants are known ---------------------------

# 1x1 matrix whose determinant is (-4) -------------------------------
list_51 = [[-4]]

# 2x2 matrix whose determinant is (10) -------------------------------
list_52 = [[4,1],[2,3]]

# 3x3 matrix whose determinant is (-6) -------------------------------
list_53 = [[-2,3,-1],[5,-1,4],[4,-8,2]]

# 4x4 matrix whose determinant is (-279) -------------------------------
list_54 = [[7,4,2,0],[6,3,-1,2],[4,6,2,5],[8,2,-7,1]]

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

    # test identity matrix generator 
    def test_id_matrix(self):
        self.assertEqual( Matrix.id_matrix(1), Matrix([[1]]) )
        self.assertEqual( Matrix.id_matrix(3), Matrix([[1,0,0],[0,1,0],[0,0,1]]) )
        self.assertEqual( Matrix.id_matrix(5), Matrix([[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]]) )

    # test determinanat computation
    def test_det_computation(self):
        self.assertEqual( Matrix.det(Matrix(list_51)) , -4 )
        self.assertEqual( Matrix.det(Matrix(list_52)) , 10 )
        self.assertEqual( Matrix.det(Matrix(list_53)) , -6 )
        self.assertEqual( Matrix.det(Matrix(list_54)) , -279 )

    # test adjoint computation
    def test_adj_computation(self):
        self.assertEqual( Matrix.adj(Matrix(list_51)) , Matrix([[1]]) )
        self.assertEqual( Matrix.adj(Matrix(list_52)) , Matrix([[3,-2],[-1,4]]) )
        self.assertEqual( Matrix.adj(Matrix(list_53)) , Matrix([[30,6,-36],[2,0,-4],[11,3,-13]]) )
        self.assertEqual( Matrix.adj(Matrix(list_54)) , Matrix([[15,-98,4,104],[-156,331,-116,-226],[54,-111,33,21],[42,-107,67,68]]) )

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
        self.assertEqual( Matrix(list_21).dot(Matrix(list_23)), Matrix([[30,36,42],[66,81,96]]))
        self.assertEqual( Matrix([[1]]).dot(Matrix([[3]])), Matrix([[3]]))

    # is_symmetric method test -------------------------------------------
    def test_is_symmetric(self):
        self.assertTrue( Matrix(list_31).is_symmetric() )
        self.assertTrue( Matrix(list_32).is_symmetric() )
        self.assertTrue( Matrix(list_33).is_symmetric() )
        self.assertFalse( Matrix(list_23).is_symmetric() )

    # matrix scaling tests ------------------------------------------------
    def test_matrix_scale(self):
        self.assertEqual( Matrix(list_22).scale(0), Matrix([[0,0,0],[0,0,0],[0,0,0],[0,0,0]]) )
        self.assertEqual( Matrix(list_22).scale(1), Matrix(list_22))
        self.assertEqual( Matrix(list_22).scale(2), Matrix([[2,4,6],[8,10,12],[14,16,18],[20,22,24]]))
        self.assertEqual( Matrix(list_22).scale(10), Matrix([[10,20,30],[40,50,60],[70,80,90],[100,110,120]]))

    # is_antisymmetric method test ----------------------------------------
    def test_is_antisymmetric(self):
        self.assertTrue( Matrix(list_34).is_antisymmetric() )
        self.assertFalse( Matrix(list_31).is_antisymmetric() )

    # trace test ----------------------------------------------------------
    def test_trace_val(self):
        self.assertEqual( Matrix(list_23).trace(), 15)
        self.assertEqual( Matrix(list_33).trace(), 11)

    # test vector norm ----------------------------------------------------
    def test_vec_norm(self):
        self.assertEqual( Matrix(list_11).vec_norm(1), 10.0 )
        self.assertEqual( Matrix(list_11).vec_norm(), 5.477225575051661 )
        self.assertEqual( Matrix(list_11).vec_norm(3), 4.641588833612778 )

        self.assertEqual( Matrix(list_12).vec_norm(1), 6.0 )
        self.assertEqual( Matrix(list_12).vec_norm(), 3.7416573867739413 )
        self.assertEqual( Matrix(list_12).vec_norm(3), 3.3019272488946263 )

    # test drop row and col -----------------------------------------------
    def test_drop(self):
        self.assertEqual(   Matrix(list_33a).drop(1,2), Matrix([[10,60],[40,80]])  )
        self.assertEqual(   Matrix(list_44).drop(3,0),  Matrix([[6,3,4],[9,1,1],[0,3,2]]) )

    ## operator-overloading tests -----------------------------------------
    
    # add matrices 
    def test_add_matrices(self):
        self.assertEqual(   ( Matrix(list_11) + Matrix(list_11a) ) , Matrix([[6],[8],[10],[12]]) ) 
        self.assertEqual(   ( Matrix(list_21) + Matrix(list_21a) ) , Matrix([[8, 10, 12], [14, 16, 18]]) ) 

    # subtract matrices 
    def test_sub_matrices(self):
        self.assertEqual(   ( Matrix(list_11a) - Matrix(list_11) ) , Matrix([[4],[4],[4],[4]]) ) 
        self.assertEqual(   ( Matrix(list_21a) - Matrix(list_21) ) , Matrix([[6, 6, 6], [6, 6, 6]]) ) 
  
    # multiply matrices 
    def test_mul_matrices(self):
        self.assertEqual( (Matrix(list_22) * Matrix(list_23)), Matrix([[30,36,42],[66,81,96],[102,126,150],[138,171,204]]))
        self.assertEqual( (Matrix(list_21) * Matrix(list_23)), Matrix([[30,36,42],[66,81,96]]))
        self.assertEqual( (Matrix([[1]]) * Matrix([[3]])), Matrix([[3]]))

    # element access 
    def test_element_access(self):

        # ele row - ele col
        self.assertEqual( Matrix(list_33a)[1,2], 70 )
        self.assertEqual( Matrix(list_33a)[0,1], 60 )

        # slice row - slice col
        self.assertEqual( Matrix(list_44)[1:3,1:4], Matrix([[9,1,1],[0,3,2]]) )
        self.assertEqual( Matrix(list_44)[1:3,1:2], Matrix([[9],[0]]) )
        self.assertEqual( Matrix(list_44)[3:1:-1,1:3], Matrix([[1,2],[0,3]]) )
        self.assertEqual( Matrix(list_44)[1:3,3:1:-1], Matrix([[1,1],[2,3]]) )

        # ele row - slice col
        self.assertEqual( Matrix(list_44)[2,1:3], Matrix([[0,3]]) )
        self.assertEqual( Matrix(list_44)[1,0:3], Matrix([[6,9,1]]) )

        # slice row - ele col
        self.assertEqual( Matrix(list_44)[1:3,1], Matrix([[9],[0]]) )
        self.assertEqual( Matrix(list_44)[2:4,0], Matrix([[3],[4]]) )
        
# Make the test results print --------------------------------------------

if __name__ == '__main__':
    unittest.main()