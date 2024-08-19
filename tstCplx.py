import math

import lbCplx as lc
import unittest

class test_LBcplx(unittest.TestCase):
    def test_sum_cplx(self):
        suma = lc.sum_cplx((1,-3),(2,0))
        self.assertAlmostEqual(suma[0],3)
        self.assertAlmostEqual(suma[1], -3)
        suma = lc.sum_cplx((3,5), (-2.6,6.8))
        self.assertAlmostEqual(suma[0],0.4)
        self.assertAlmostEqual(suma[1], 11.8)
    def test_diff_cplx(self):
        diff = lc.diff_cplx((2,-2),(1,-1.5))
        self.assertAlmostEqual(diff[0], 1)
        self.assertAlmostEqual(diff[1], -0.5)
        diff = lc.diff_cplx((1,-3),(2,0))
        self.assertAlmostEqual(diff[0], -1)
        self.assertAlmostEqual(diff[1], -3)
    def test_prod_cplx(self):
        prod = lc.prod_cplx((1,-3),(5,4))
        self.assertAlmostEqual(prod[0], 17)
        self.assertAlmostEqual(prod[1], -11)
        prod = lc.prod_cplx((5, 4), (2, 0))
        self.assertAlmostEqual(prod[0], 10)
        self.assertAlmostEqual(prod[1], 8)
    def test_div_cplx(self):
        div = lc.div_cplx((1,-3),(5,2))
        self.assertAlmostEqual(div[0],-1/29)
        self.assertAlmostEqual(div[1],-17/29)
        div = lc.div_cplx((5, 4), (2, 0))
        self.assertAlmostEqual(div[0],10/4)
        self.assertAlmostEqual(div[1], 8/4)
    def test_modulo(self):
        modulo = lc.modulo((1,-3))
        self.assertAlmostEqual(modulo,math.sqrt(10))
        modulo = lc.modulo((5,4))
        self.assertAlmostEqual(modulo,math.sqrt(41))
    def test_conju(self):
        conju = lc.conju((4,-3))
        self.assertAlmostEqual(conju[1],3)
        conju = lc.conju((1, -1))
        self.assertAlmostEqual(conju[1], 1)
    def test_crt_plr(self):
        result = lc.crt_plr((5,-3))
        self.assertAlmostEqual(result[0],math.sqrt(34))
        self.assertAlmostEqual(result[1],5.742765807)
        result = lc.crt_plr((1,2))
        self.assertAlmostEqual(result[0], math.sqrt(5))
        self.assertAlmostEqual(result[1], 1.107148718)
    def test_plr_crt(self):
        result = lc.plr_crt((5,-math.pi/3))
        self.assertAlmostEqual(result[0], 2.5)
        self.assertAlmostEqual(result[1],-4.330127019)
        result = lc.plr_crt((5, math.pi / 3))
        self.assertAlmostEqual(result[0], 2.5)
        self.assertAlmostEqual(result[1], 4.330127019)
