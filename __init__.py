from . import vrf, go

from typing import Tuple

__all__ = ["prove", "verify"]

def prove(sk: bytes, alpha: bytes) -> Tuple[bytes, bytes]:
    proof = vrf.prove(go.Slice_byte.from_bytes(sk), go.Slice_byte.from_bytes(alpha))
    return bytes(proof.beta), bytes(proof.pi)


def verify(pk: bytes, pi: bytes, alpha: bytes) -> bytes:
    beta = vrf.verify(
        go.Slice_byte.from_bytes(pk),
        go.Slice_byte.from_bytes(pi),
        go.Slice_byte.from_bytes(alpha),
    )
    return bytes(beta)
