@0xec3b2b10a5e23975;
using Go = import "go.capnp";
$Go.package("proto");
$Go.import("github.com/netsec-ethz/scion/go/proto");

struct CertChainReq {
    isdas @0 :UInt32;
    version @1 :UInt32;
}

struct CertChainRep {
    chain @0 :Data;
}

struct TRCReq {
    isdas @0 :UInt32;
    version @1 :UInt32;
}

struct TRCRep {
    trc @0 :Data;
}

struct TRCxSigReq {
    trc @0 :Data;
}

struct TRCxSigRep {
    trc @0 :Data;
}

struct CertMgmt {
    union {
        unset @0 :Void;
        certChainReq @1 :CertChainReq;
        certChainRep @2 :CertChainRep;
        trcReq @3 :TRCReq;
        trcRep @4 :TRCRep;
        trcXsigReq @5 :TRCxSigReq;
        trcXsigRep @6 :TRCxSigRep;
    }
}
