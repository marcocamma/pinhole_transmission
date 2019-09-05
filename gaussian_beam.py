#! /usr/bin/env python3
""" 
Demonstrate that for a gaussian beam, we get 50% transmission when pinhole size 
is equal to beam FWHM

It is also a nice little example of sympy

TODO: repeat calculation when beam is offcenter
"""
import sympy

answers = {True: "Yes", False: "No"}


def find_half(function):
    return sympy.solve(sympy.Eq(function, sympy.Rational(1, 2)))[0]


# Gaussian sigma of intensity distribution
sig = sympy.Symbol("sig", positive=True)

# variable to integrate over
r = sympy.Symbol("r", positive=True)

# pinhole opening
D = sympy.Symbol("D", positive=True)

beam = sympy.exp(-r ** 2 / 2 / sig ** 2)

# calculate beam FWHM
HWHM = find_half(beam)[r]
FWHM = 2 * HWHM


# transmitted power through pinhole
transmitted = sympy.integrate(2 * sympy.pi * r * beam, (r, 0, D / 2))

# calculate full beam for R → infinity
full_beam = sympy.limit(transmitted, D, sympy.oo)

transmitted_normalized = transmitted / full_beam
transmitted_normalized = sympy.simplify(transmitted_normalized)

solution = find_half(transmitted_normalized)[D]

print("Pinhole diameter to have 50% intensity transmission", solution)
print("Beam FWHM", FWHM)
print(
    "Do you get 50% transmission when pinhole is open to beam FWHM ? ",
    answers[sympy.Eq(solution, FWHM)],
)
