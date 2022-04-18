#!/usr/bin/env python

from __future__ import print_function
from hr_tddschn.hr import hr
from functools import partial

hr_ending_sep = partial(hr, ' ', '#')