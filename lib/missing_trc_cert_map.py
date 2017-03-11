# Copyright 2017 ETH Zurich
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
:mod:`missing_trc_cert_map` --- SCION map for missing trcs and certchains
===============================================
"""
from collections import defaultdict


class MissingTrcCertMap(object):
    """
    The MissingTrcCertMap class holds missing trcs and certificates
    for a scion element instance.
    """

    def __init__(self):
        self.missing_trcs = defaultdict(set)
        self.missing_certs = defaultdict(set)

    def empty(self):
        return not self.missing_trcs and not self.missing_certs

    def trcs(self):
        return self.missing_trcs

    def certs(self):
        return self.missing_certs

    def add_missing(self, missing_trcs, missing_certs):
        """
        missing is a mapping from isd-as to versions
        """
        for isd_as, versions in missing_trcs.items():
            if isd_as in list(self.missing_trcs):
                for ver in versions:
                    self.missing_trcs[isd_as].add(ver)
            else:
                self.missing_trcs[isd_as] = versions
        for isd_as, versions in missing_certs.items():
            if isd_as in list(self.missing_certs):
                for ver in versions:
                    self.missing_certs[isd_as].add(ver)
            else:
                self.missing_certs[isd_as] = versions

    def remove_missing_trc(self, isd_as, ver):
        """
        trcs_to_rem is a map from isd-as to ver
        """
        if isd_as not in self.missing_trcs:
            return
        if not self.missing_trcs[isd_as]:
            del self.missing_trcs[isd_as]
            return
        if ver not in self.missing_trcs[isd_as]:
            return
        self.missing_trcs[isd_as].remove(ver)
        if not self.missing_trcs[isd_as]:
            del self.missing_trcs[isd_as]

    def remove_missing_cert(self, isd_as, ver):
        """
        trcs_to_rem is a map from isd-as to ver
        """
        if isd_as not in self.missing_certs:
            return
        if not self.missing_certs[isd_as]:
            del self.missing_certs[isd_as]
            return
        if ver not in self.missing_certs[isd_as]:
            return
        self.missing_certs[isd_as].remove(ver)
        if not self.missing_certs[isd_as]:
            del self.missing_certs[isd_as]

    def __str__(self):
        return "CERTS: %s \n TRCs %s" % (self.missing_certs, self.missing_trcs)
