#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

__author__ = "Mincong Huang"


class Artifact:
    release_name = None
    type = None

    def __init__(self, filename):
        parts = Artifact.split(filename)
        self.release_name = parts[0]
        self.type = parts[1]

    @staticmethod
    def split(s):
        if s.endswith(('.jar', '.jar.md5', '.jar.sha1')):
            m = s.rindex('.jar')
            return s[:m], s[m:]

        if s.endswith(('.pom', '.pom.md5', '.pom.sha1')):
            m = s.rindex('.pom')
            return s[:m], s[m:]

        if s.endswith(('.version', '.version.md5', '.version.sha1')):
            m = s.rindex('.version')
            return s[:m], s[m:]


def main(projects_dir):
    release_count = 0
    miss_count = 0
    miss_types = {'.version': 0, '.version.md5': 0, '.version.sha1': 0,
                  '.jar': 0, '.jar.md5': 0, '.jar.sha1': 0,
                  '.pom': 0, '.pom.md5': 0, '.pom.sha1': 0}

    for curr, sub_dirs, files in os.walk(projects_dir):
        project = os.path.basename(curr)
        # Skip work-in-progress (WIP) and SNAPSHOT
        if project.startswith('wip--') or project.endswith('-SNAPSHOT'):
            continue

        releases = {}  # (K, V)=(ReleaseName, MissingTypes)
        for f in files:
            if f.startswith('.'):  # hidden file
                continue
            a = Artifact(f)
            k = "%s/%s" % (project, a.release_name)
            if k not in releases:
                releases[k] = ['.version', '.version.md5', '.version.sha1',
                               '.jar', '.jar.md5', '.jar.sha1',
                               '.pom', '.pom.md5', '.pom.sha1']
            releases[k].remove(a.type)

        release_count += len(releases)
        # Check integrity
        for name, types in releases.iteritems():
            if types:
                print '%s, missing: %s' % (name, types)
                miss_count += 1
                for t in types:
                    miss_types[t] += 1
            else:
                print '%s complete' % name
        sys.stdout.flush()

    print "%s releases found, %s are incomplete. Missing:" % (release_count, miss_count)
    for ext, count in miss_types.iteritems():
        print "'%s': %s" % (ext, count)
    print "Finished."


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print 'usage: ./list_releases.py /path/to/releases'
