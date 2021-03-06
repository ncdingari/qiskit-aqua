# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2018, 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""
Inverse Quantum Fourier Transforms (:mod:`qiskit.aqua.components.iqfts`)
========================================================================
Inverse Quantum Fourier Transforms...

.. currentmodule:: qiskit.aqua.components.iqfts

Inverse Quantum Fourier Transform Base Class
============================================

.. autosummary::
   :toctree: ../stubs/
   :nosignatures:

   IQFT

Inverse Quantum Fourier Transforms
==================================

.. autosummary::
   :toctree: ../stubs/
   :nosignatures:

   Standard
   Approximate

"""
# pylint: disable=cyclic-import

from .iqft import IQFT
from .standard import Standard
from .approximate import Approximate

__all__ = ['Standard', 'Approximate', 'IQFT']
