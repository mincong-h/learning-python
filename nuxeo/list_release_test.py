#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import list_release as lr

__author__ = "Mincong Huang"


class TestReleaseName(unittest.TestCase):
    def test_Artifact_split(self):
        self.assertEqual(('A-1.0.0', '.jar'), lr.Artifact.split('A-1.0.0.jar'))
        self.assertEqual(('A-1.0.0', '.jar.sha1'), lr.Artifact.split('A-1.0.0.jar.sha1'))
        self.assertEqual(('A-1.0.0', '.jar.md5'), lr.Artifact.split('A-1.0.0.jar.md5'))
        self.assertEqual(('A-1.0.0', '.version'), lr.Artifact.split('A-1.0.0.version'))
        self.assertEqual(('A-1.0.0', '.version.sha1'), lr.Artifact.split('A-1.0.0.version.sha1'))
        self.assertEqual(('A-1.0.0', '.version.md5'), lr.Artifact.split('A-1.0.0.version.md5'))
        self.assertEqual(('A-1.0.0', '.pom'), lr.Artifact.split('A-1.0.0.pom'))
        self.assertEqual(('A-1.0.0', '.pom.sha1'), lr.Artifact.split('A-1.0.0.pom.sha1'))
        self.assertEqual(('A-1.0.0', '.pom.md5'), lr.Artifact.split('A-1.0.0.pom.md5'))
