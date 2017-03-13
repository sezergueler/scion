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

struct CertChainsReq {
    chains @0 :List(CertChainReq);
}

struct CertChainsRep {
    chains @0 :List(Data);
}

struct TRCReq {
    isdas @0 :UInt32;
    version @1 :UInt32;
}

struct TRCRep {
    trc @0 :Data;
}

struct CertMgmt {
    union {
        unset @0 :Void;
        certChainReq @1 :CertChainReq;
        certChainRep @2 :CertChainRep;
        trcReq @3 :TRCReq;
        trcRep @4 :TRCRep;
        certChainsReq @5 :CertChainsReq;
        certChainsRep @6 :CertChainsRep;
    }
}
