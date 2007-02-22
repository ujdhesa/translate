#!/usr/bin/env python
#
# -*- coding: utf-8 -*-
#
# These test classes should be used as super class of test classes for the
# classes that doesn't support the target property

from translate.storage import properties
from translate.storage import test_base
from translate.storage import base
from translate.misc import wStringIO
from py import test

class TestMonolingualUnit(test_base.TestTranslationUnit):
    UnitClass = base.TranslationUnit

    def test_target(self):
      pass

    def test_markreview(self):
        unit = self.UnitClass("Test Source String")
        assert test.raises(NotImplementedError, unit.markreviewneeded)

    def test_errors(self):
        """Assert the fact that geterrors() and adderror() is not (yet) implemented.
        This test needs to be removed when these methods get implemented."""
        assert test.raises(NotImplementedError, self.unit.geterrors)
        assert test.raises(NotImplementedError, self.unit.adderror, 'testname', 'Test error')

class TestMonolingualStore(test_base.TestTranslationStore):
    StoreClass = base.TranslationStore

    def test_translate(self):
      pass

    def test_markup(self):
      pass

    def test_nonascii(self):
      pass

