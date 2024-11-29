package vrf

import (
	"github.com/decred/dcrd/dcrec/secp256k1/v4"
	"github.com/vechain/go-ecvrf"
)

type Proof struct {
	Beta []byte
	Pi []byte
}

func Prove(sk, alpha []byte) (*Proof, error) {
	privKey := secp256k1.PrivKeyFromBytes(sk)
	beta, pi, err := ecvrf.Secp256k1Sha256Tai.Prove(privKey.ToECDSA(), alpha)
	proof := &Proof{
		Beta: beta,
		Pi: pi,
	}
	return proof, err
}

func Verify(pk, pi, alpha []byte) ([]byte, error) {
	pubKey, err := secp256k1.ParsePubKey(pk)
	if err != nil {
		return nil, err
	}
	beta, err := ecvrf.Secp256k1Sha256Tai.Verify(pubKey.ToECDSA(), alpha, pi)
	return beta, err
}
