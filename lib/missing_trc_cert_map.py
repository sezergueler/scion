from collections import defaultdict


class MissingTrcCertMap(object):
    """
    ...
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
