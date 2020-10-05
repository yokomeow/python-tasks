class DerivativeNum:
    
    def __init__(self, f, h, coeffs, hCoeffs):
        self.f = f
        self.h = h
        self.coeffs = coeffs
        self.hCoeffs = hCoeffs
    
    def getCoefficients(self):
        return self.coeffs
    
    def getHCoefficients(self):
        return self.hCoeffs
    
    def setCoefficients(self, coeffs):
        self.coeffs = coeffs
    
    def setHCoefficients(self, hCoeffs):
        self.hCoeffs = hCoeffs

    def __call__(self, x):
        f, h, coeffs, hCoeffs = self.f, self.h, self.coeffs, self.hCoeffs
        res = 0
        for i in range(len(coeffs)):
            res += 1 / h * coeffs[i] * f(x + hCoeffs[i] * h)
        return res

class DerivativeNum4(DerivativeNum):
    
    def __init__(self, f, h):
        DerivativeNum.__init__(self, f, h, \
                               [1 / 2, -1 / 2], \
                               [1, -1])